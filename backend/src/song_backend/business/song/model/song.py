from dataclasses import dataclass


@dataclass
class Song:
    id: str
    # TODO author id + other information
    author: str
    title: str
