from song_backend.business.song.storage.lyrics_storage_adapter import LyricsStorageAdapter


class LyricsStorageDummyAdapter(LyricsStorageAdapter):
    _storage: dict[str, str]

    def __init__(self) -> None:
        self._storage = {}

    def upsert_lyrics(self, song_id: str, lyrics: str) -> None:
        self._storage[song_id] = lyrics

    def get_lyrics(self, song_id: str) -> str | None:
        return self._storage.get(song_id)
