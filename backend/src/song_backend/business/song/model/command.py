from dataclasses import dataclass


@dataclass
class SongCommand:
    pass


@dataclass
class SongAddCommand(SongCommand):
    author: str
    title: str
