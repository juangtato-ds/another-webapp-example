from typing import Final

from fastapi import APIRouter, Depends, status

from song_backend.business.song.model.command import SongAddCommand
from song_backend_rest.dependencies.core_dependencies import SongServiceDep
from song_backend_rest.model.song import SongAddRequest, SongLyricsResponse, SongResponse


ROUTER_TAG: Final[str] = "Song"
ROUTER_PREFIX: Final[str] = "/song"

router = APIRouter(
    prefix=ROUTER_PREFIX,
    tags=[ROUTER_TAG],
)


@router.post(
    "/",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_200_OK,
    response_model=SongLyricsResponse,
)
async def add_song(
    song_service: SongServiceDep,
    request: SongAddRequest,
) -> SongLyricsResponse:
    result = await song_service.add_song(SongAddCommand(author=request.artist, title=request.title))
    return SongLyricsResponse(
        id=result.song.id, artist=result.song.author, title=result.song.title, lyrics=result.lyrics
    )


@router.get(
    "/",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_200_OK,
    response_model=list[SongResponse],
)
async def filter_songs(song_service: SongServiceDep) -> list[SongResponse]:
    return [SongResponse(id=s.id, artist=s.author, title=s.title) for s in song_service.find_all()]
