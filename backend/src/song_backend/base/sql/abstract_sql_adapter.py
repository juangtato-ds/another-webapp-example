from typing import Generic, TypeVar

from sqlalchemy import Engine
from sqlalchemy.orm import Session
from song_backend.base.sql.base_sql_entity import BaseEntityVar

ID = TypeVar("ID")


class AbstractSqlAdapter(Generic[BaseEntityVar, ID]):
    _clazz: type[BaseEntityVar]
    _engine: Engine

    def __init__(self, clazz: type[BaseEntityVar], engine: Engine) -> None:
        self._clazz = clazz
        self._engine = engine

    def _session(self) -> Session:
        return Session(self._engine)

    def _find_by_id(self, id_value: int) -> BaseEntityVar | None:
        with self._session() as session:
            return session.get(self._clazz, id_value)

    def _get_all(self) -> list[BaseEntityVar]:
        with self._session() as session:
            query = session.query(self._clazz)
            return query.all()

    def _get(self, id_: ID) -> BaseEntityVar | None:
        with self._session() as session:
            return session.get(self._clazz, id_)
