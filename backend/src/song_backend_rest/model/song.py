from pydantic import BaseModel, Field


class SongAddRequest(BaseModel):
    artist: str = Field(description="Artist name", examples=["Lemmy"])
    title: str = Field(description="Title of the song", examples=["Ace of spades"])


class SongResponse(BaseModel):
    id: str = Field(description="ID of the song in the service", examples=["xx-xx-xx-xx"])
    artist: str = Field(description="Artist name", examples=["Lemmy"])
    title: str = Field(description="Title of the song", examples=["Ace of spades"])


class SongLyricsResponse(BaseModel):
    id: str = Field(description="ID of the song in the service", examples=["xx-xx-xx-xx"])
    artist: str = Field(description="Artist name", examples=["Lemmy"])
    title: str = Field(description="Title of the song", examples=["Ace of spades"])
    lyrics: str = Field(description="Lorem ipsum dolor")
