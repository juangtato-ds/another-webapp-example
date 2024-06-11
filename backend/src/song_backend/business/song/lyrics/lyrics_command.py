from dataclasses import dataclass


@dataclass
class SongSearchAclCommand:
    author: str
    song_title: str
