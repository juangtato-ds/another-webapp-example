from pydantic import BaseModel, Field


class SongAddRequest(BaseModel):
    artist: str = Field(description="Artist name", examples=["Rainbow"])
    title: str = Field(description="Title of the song", examples=["The Temple of the King"])


class SongResponse(BaseModel):
    id: str = Field(description="ID of the song in the service", examples=["xx-xx-xx-xx"])
    artist: str = Field(description="Artist name", examples=["Rainbow"])
    title: str = Field(description="Title of the song", examples=["The Temple of the King"])


class SongFullResponse(BaseModel):
    id: str = Field(description="ID of the song in the service", examples=["xx-xx-xx-xx"])
    artist: str = Field(description="Artist name", examples=["Rainbow"])
    title: str = Field(description="Title of the song", examples=["The Temple of the King"])
    lyrics: str = Field(description="Song lyrics", examples=["Lorem ipsum dolor"])
    contry_list: list[str] = Field(
        description="List of countries in the song", examples=[["Narnia", "Mordor"]]
    )
