from typing import Final

from fastapi import APIRouter, status

from song_backend.business.song.model.command import SongAddCommand
from song_backend.business.song.model.lyrics import Lyrics
from song_backend_rest.dependencies.core_dependencies import SongServiceDep
from song_backend_rest.model.song import SongAddRequest, SongLyricsResponse, SongResponse


ROUTER_TAG: Final[str] = "Song"
ROUTER_PREFIX: Final[str] = "/song"

router = APIRouter(
    prefix=ROUTER_PREFIX,
    tags=[ROUTER_TAG],
)


def _map_song_lyrics_response(data: Lyrics) -> SongLyricsResponse:
    return SongLyricsResponse(
        id=data.song.id,
        artist=data.song.author,
        title=data.song.title,
        lyrics=data.lyrics,
        contry_list=data.song.country_list.copy(),
    )


@router.post(
    "/",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_201_CREATED,
    response_model=SongLyricsResponse,
)
async def add_song(
    song_service: SongServiceDep,
    request: SongAddRequest,
) -> SongLyricsResponse:
    return _map_song_lyrics_response(
        await song_service.add_song(SongAddCommand(author=request.artist, title=request.title))
    )


@router.get(
    "/",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_200_OK,
    response_model=list[SongResponse],
)
async def filter_songs(song_service: SongServiceDep) -> list[SongResponse]:
    return [SongResponse(id=s.id, artist=s.author, title=s.title) for s in song_service.find_all()]


@router.get(
    "/{song_id}",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_200_OK,
    response_model=SongLyricsResponse,
)
async def get_song_and_lyrics(song_id: str, song_service: SongServiceDep) -> SongLyricsResponse:
    return _map_song_lyrics_response(song_service.get_lyrics(song_id))
