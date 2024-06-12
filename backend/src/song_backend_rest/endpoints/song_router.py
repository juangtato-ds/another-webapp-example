from typing import Annotated, Final

from fastapi import APIRouter, Body, status

from song_backend.business.song.model.command import SongAddCommand
from song_backend.business.song.model.lyrics import Lyrics
from song_backend_rest.dependencies.core_dependencies import SongServiceDep
from song_backend_rest.model.song import SongAddRequest, SongFullResponse, SongResponse


ROUTER_TAG: Final[str] = "Song"
ROUTER_PREFIX: Final[str] = "/song"

router = APIRouter(
    prefix=ROUTER_PREFIX,
    tags=[ROUTER_TAG],
)

_add_song_examples = [
    SongAddRequest(artist="Gente de zona", title="La gozadera"),  # a bunch of countries
    SongAddRequest(title="I'm coming home", artist="Alex Band"),  # song not found
    SongAddRequest(artist="Alestorm", title="Mexico"),  # one country
    SongAddRequest(artist="Rainbow", title="The Temple of the King"),  # no countries
]


def _map_song_full_response(data: Lyrics) -> SongFullResponse:
    return SongFullResponse(
        id=data.song.id,
        artist=data.song.author,
        title=data.song.title,
        lyrics=data.lyrics,
        country_list=data.song.country_list.copy(),
    )


@router.post(
    "/",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_201_CREATED,
    response_model=SongFullResponse,
)
async def add_song(
    song_service: SongServiceDep,
    request: Annotated[SongAddRequest, Body(examples=_add_song_examples)],
) -> SongFullResponse:
    return _map_song_full_response(
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
    response_model=SongFullResponse,
)
async def get_song_full_information(song_id: str, song_service: SongServiceDep) -> SongFullResponse:
    return _map_song_full_response(song_service.get_lyrics(song_id))
