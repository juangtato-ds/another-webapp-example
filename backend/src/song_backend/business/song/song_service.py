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

from song_backend.business.song.storage.dummy.lyrics_storage_dummy_adapter import (
    LyricsStorageDummyAdapter,
)
from song_backend.business.song.storage.dummy.song_storage_dummy_adapter import (
    SongStorageDummyAdapter,
)
from song_backend.business.song.storage.lyrics_storage_adapter import LyricsStorageAdapter
from song_backend.business.song.storage.song_storage_adapter import SongStorageAdapter

logger = logging.getLogger("uvicorn.error")


class SongService:
    _lyrics_adapter: LyricsSearchAclAdapter
    _lyrics_analyser_adapter: LyricsAnalyserAclAdapter
    _song_storage: SongStorageAdapter
    _lyrics_storage: LyricsStorageAdapter

    def __init__(
        self,
        lyrics_adapter: LyricsSearchAclAdapter,
        lyrics_analyser_adapter: LyricsAnalyserAclAdapter,
        song_storage: SongStorageAdapter,
        lyrics_storage: LyricsStorageAdapter,
    ) -> None:
        self._lyrics_adapter = lyrics_adapter
        self._lyrics_analyser_adapter = lyrics_analyser_adapter
        self._song_storage = song_storage
        self._lyrics_storage = lyrics_storage

    async def add_song(self, command: SongAddCommand) -> Lyrics:
        """Add a song to the catalog.

        Only songs with lyrics can be included in the catalog."""
        lyrics_search = await self._lyrics_adapter.find_song_and_lyrics(
            SongSearchAclCommand(author=command.author, song_title=command.title)
        )

        if not lyrics_search.lyrics.strip():
            raise RuntimeError("Song cannot be added: empty lyrics")

        # TODO do something with the analysis
        analysis = await self._lyrics_analyser_adapter.analyse(
            LyricsAnalyserCommand(lyrics=lyrics_search.lyrics)
        )

        # At this point everything is fine
        song = Song(
            id=str(uuid4()),
            title=lyrics_search.title,
            author=lyrics_search.author,
            country_list=analysis.country_list,
        )

        self._song_storage.create_song(song)
        self._lyrics_storage.upsert_lyrics(song.id, lyrics_search.lyrics)

        return Lyrics(
            lyrics=lyrics_search.lyrics,
            song=song,
        )

    def find_all(self) -> list[Song]:  # only for first approach
        return self._song_storage.find_all()


class SongServiceFactory:
    @staticmethod
    def create(
        lyrics_adapter: LyricsSearchAclAdapter,  # this acl is selected by final application
        lyrics_analyser_adapter: LyricsAnalyserAclAdapter,  # this acl is selected by final application
    ) -> SongService:
        return SongService(
            lyrics_adapter=lyrics_adapter,
            lyrics_analyser_adapter=lyrics_analyser_adapter,
            song_storage=SongStorageDummyAdapter(),
            lyrics_storage=LyricsStorageDummyAdapter(),
        )
