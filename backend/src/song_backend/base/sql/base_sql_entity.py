from typing import TypeVar
from sqlalchemy.orm import DeclarativeBase


class BaseEntity(DeclarativeBase):
    # TODO add general attributes
    pass


# TODO for future abstractions and common functionalities
BaseEntityVar = TypeVar("BaseEntityVar", bound=BaseEntity)
