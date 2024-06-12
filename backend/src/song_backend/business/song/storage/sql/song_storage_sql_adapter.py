from sqlalchemy import Engine
from song_backend.base.sql.abstract_sql_adapter import AbstractSqlAdapter
from song_backend.business.song.model.song import Song
from song_backend.business.song.storage.song_storage_adapter import SongStorageAdapter
from song_backend.business.song.storage.sql.song_entity import SongCountryEntity, SongEntity


class SongStorageSqlAdapter(AbstractSqlAdapter[SongEntity, str], SongStorageAdapter):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine=engine, clazz=SongEntity)

    @classmethod
    def _map_optional(cls, data: SongEntity | None) -> Song | None:
        return cls._map(data) if data is not None else None

    @staticmethod
    def _map(data: SongEntity) -> Song:
        return Song(
            id=data.id,
            author=data.author,
            title=data.title,
            country_list=[c.country for c in data.country_list],
        )

    def create_song(self, song: Song) -> Song:
        with self._session() as session:
            entity = SongEntity(
                id=song.id,
                author=song.author,
                title=song.title,
                country_list=[SongCountryEntity(country=c) for c in song.country_list],
            )
            session.add(entity)
            session.commit()
            return self._map(entity)

    def find_all(self) -> list[Song]:
        return [self._map(s) for s in self._get_all()]

    def find(self, song_id: str) -> Song | None:
        return self._map_optional(self._get(song_id))
