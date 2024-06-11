from dataclasses import dataclass

from song_backend.business.song.model.song import Song


@dataclass
class Lyrics:
    lyrics: str
    song: Song
