import abc

from song_backend.business.song.model.song import Song


class SongStorageAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_song(self, song: Song) -> Song:
        raise NotImplementedError()

    # Warning - only for first approach
    @abc.abstractmethod
    def find_all(self) -> list[Song]:
        raise NotImplementedError()
