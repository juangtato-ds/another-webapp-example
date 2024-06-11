from uuid import uuid4
from song_backend.business.song.lyrics.lyrics_command import SongSearchAclCommand
from song_backend.business.song.lyrics.lyrics_search_acl_adapter import LyricsSearchAclAdapter
from song_backend.business.song.lyrics_analyser.lyrics_analyser_acl_adapter import (
    LyricsAnalyserAclAdapter,
)
from song_backend.business.song.lyrics_analyser.lyrics_analyser_command import LyricsAnalyserCommand
from song_backend.business.song.model.command import SongAddCommand
from song_backend.business.song.model.lyrics import Lyrics
from song_backend.business.song.model.song import Song

import logging

logger = logging.getLogger("uvicorn.error")


class SongService:
    _lyrics_adapter: LyricsSearchAclAdapter
    _lyrics_analyser_adapter: LyricsAnalyserAclAdapter

    def __init__(
        self,
        lyrics_adapter: LyricsSearchAclAdapter,
        lyrics_analyser_adapter: LyricsAnalyserAclAdapter,
    ) -> None:
        self._lyrics_adapter = lyrics_adapter
        self._lyrics_analyser_adapter = lyrics_analyser_adapter

    async def add_song(self, command: SongAddCommand) -> Lyrics:
        lyrics_search = await self._lyrics_adapter.find_song_and_lyrics(
            SongSearchAclCommand(author=command.author, song_title=command.title)
        )
        # TODO do something with the analysis
        analysis = await self._lyrics_analyser_adapter.analyse(
            LyricsAnalyserCommand(lyrics=lyrics_search.lyrics)
        )

        return Lyrics(
            lyrics=lyrics_search.lyrics,
            song=Song(id=str(uuid4()), author=lyrics_search.author, title=lyrics_search.title),
        )


class SongServiceFactory:
    @staticmethod
    def create(
        lyrics_adapter: LyricsSearchAclAdapter,  # this acl is selected by final application
        lyrics_analyser_adapter: LyricsAnalyserAclAdapter,  # this acl is selected by final application
    ) -> SongService:
        return SongService(
            lyrics_adapter=lyrics_adapter, lyrics_analyser_adapter=lyrics_analyser_adapter
        )
