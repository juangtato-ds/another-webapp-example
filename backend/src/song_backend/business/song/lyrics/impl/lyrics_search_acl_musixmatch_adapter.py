from dataclasses import dataclass
import json
from typing import Any
import aiohttp
from song_backend.business.song.lyrics.lyrics_command import SongSearchAclCommand
from song_backend.business.song.lyrics.lyrics_search_acl_adapter import LyricsSearchAclAdapter
from song_backend.business.song.lyrics.lyrics_search_result import SongWithLyricsSearchResult

_QueryParams = dict[str, str | int]


@dataclass
class MusixmatchTrack:
    track_id: int
    track_name: str
    artist_name: str


class LyricsSearchAclMusixmatchAdapter(LyricsSearchAclAdapter):
    _apikey: str
    _base_url: str = "http://api.musixmatch.com/ws/1.1/"

    def __init__(self, apikey: str) -> None:
        self._apikey = apikey

    @staticmethod
    def _traverse_dict(path: list[str | int], data: dict[str | int, Any]) -> Any:
        try:
            current: Any = data
            for item in path:
                if isinstance(current, dict):
                    current = current.get(item)
                elif isinstance(current, list) and isinstance(item, int):
                    current = current[item]
                else:
                    current = None
                    break
            return current
        except:
            return None

    @staticmethod
    def _secure_get(data: dict[str, str], key: str) -> Any:
        result = data.get(key)
        if result is None:
            raise RuntimeError("another fake exception")  # TODO add custom exception
        return result

    def _domain_url(self, domain: str) -> str:
        return f"{self._base_url}{domain}"

    def _params(self, params: _QueryParams) -> _QueryParams:
        result: _QueryParams = {"apikey": self._apikey}
        result.update(params)
        return result

    def _identify_first_track(self, response: dict[str | int, Any]) -> MusixmatchTrack | None:
        track = self._traverse_dict(["message", "body", "track_list", 0, "track"], response)
        return (
            MusixmatchTrack(
                track_id=self._secure_get(track, "track_id"),
                track_name=self._secure_get(track, "track_name"),
                artist_name=self._secure_get(track, "artist_name"),
            )
            if track is not None
            else None
        )

    def _identify_lyrics(self, response: dict[str | int, Any]) -> str | None:
        return self._traverse_dict(["message", "body", "lyrics", "lyrics_body"], response)

    async def find_song_and_lyrics(
        self, command: SongSearchAclCommand
    ) -> SongWithLyricsSearchResult:
        async with aiohttp.ClientSession() as session:
            params: _QueryParams = self._params(
                {
                    "q_artist": command.author,
                    "q_track": command.song_title,
                    "page_size": 10,
                    "page": 1,
                    "s_track_rating": "desc",
                }
            )
            async with session.get(self._domain_url("track.search"), params=params) as response:
                track = self._identify_first_track(json.loads(await response.text()))
            if track is None:
                raise RuntimeError()  # TODO place a proper exception
            params = self._params({"track_id": track.track_id})
            async with session.get(self._domain_url("track.lyrics.get"), params=params) as response:
                lyrics = self._identify_lyrics(json.loads(await response.text()))
            if lyrics is None or lyrics.strip() == "":
                raise RuntimeError()  # TODO place a proper exception

        return SongWithLyricsSearchResult(
            author=track.artist_name, title=track.track_name, lyrics=lyrics
        )
