from song_backend.base.sql.base_sql_entity import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


class SongEntity(BaseEntity):
    __tablename__ = "song"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    author: Mapped[str] = mapped_column(String(100))
    title: Mapped[str] = mapped_column(String(100))

    country_list: Mapped[list["SongCountryEntity"]] = relationship(
        lazy="joined", cascade="save-update"
    )

    lyrics: Mapped["SongLyricsEntity"] = relationship()  # lazy


class SongCountryEntity(BaseEntity):
    __tablename__ = "song_country"

    song_id: Mapped[str] = mapped_column(ForeignKey("song.id"), primary_key=True)
    country: Mapped[str] = mapped_column(String(100), primary_key=True)


class SongLyricsEntity(BaseEntity):
    __tablename__ = "song_lyrics"

    song_id: Mapped[str] = mapped_column(ForeignKey("song.id"), primary_key=True)
    lyrics: Mapped[str] = mapped_column()
