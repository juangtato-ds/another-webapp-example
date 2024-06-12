import abc

from song_backend.business.song.lyrics.lyrics_command import SongSearchAclCommand
from song_backend.business.song.lyrics.lyrics_search_result import SongWithLyricsSearchResult


class LyricsSearchAclAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def find_song_and_lyrics(
        self, command: SongSearchAclCommand
    ) -> SongWithLyricsSearchResult:
        raise NotImplementedError()
