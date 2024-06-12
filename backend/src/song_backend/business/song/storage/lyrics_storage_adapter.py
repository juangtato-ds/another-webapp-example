import abc


class LyricsStorageAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def upsert_lyrics(self, song_id: str, lyrics: str) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_lyrics(self, song_id: str) -> str | None:
        raise NotImplementedError()
