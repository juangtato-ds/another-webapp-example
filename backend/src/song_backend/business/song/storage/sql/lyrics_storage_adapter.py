from sqlalchemy import Engine
from song_backend.base.sql.abstract_sql_adapter import AbstractSqlAdapter
from song_backend.business.song.storage.lyrics_storage_adapter import LyricsStorageAdapter
from song_backend.business.song.storage.sql.song_entity import SongLyricsEntity


class LyricsStorageSqlAdapter(AbstractSqlAdapter[SongLyricsEntity, str], LyricsStorageAdapter):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine=engine, clazz=SongLyricsEntity)

    def upsert_lyrics(self, song_id: str, lyrics: str) -> None:
        with self._session() as session:
            entity = session.get(self._clazz, song_id)
            if entity is None:
                entity = SongLyricsEntity(song_id=song_id, lyrics=lyrics)
                session.add(entity)
            else:
                entity.lyrics = lyrics
            session.commit()

    def get_lyrics(self, song_id: str) -> str | None:
        entity = self._get(song_id)
        return entity.lyrics if entity is not None else None
