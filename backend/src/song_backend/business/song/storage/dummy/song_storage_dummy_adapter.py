from song_backend.business.song.model.song import Song
from song_backend.business.song.storage.song_storage_adapter import SongStorageAdapter


class SongStorageDummyAdapter(SongStorageAdapter):
    _storage: dict[str, Song]

    def __init__(self) -> None:
        self._storage = {}

    def create_song(self, song: Song) -> Song:
        self._storage[song.id] = song
        return song

    def find_all(self) -> list[Song]:
        return list(self._storage.values())

    def find(self, song_id: str) -> Song | None:
        return self._storage.get(song_id)
