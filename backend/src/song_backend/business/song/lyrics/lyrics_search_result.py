from dataclasses import dataclass


@dataclass
class SongWithLyricsSearchResult:
    author: str
    title: str
    lyrics: str
