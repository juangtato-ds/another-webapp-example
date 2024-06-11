from typing import Annotated
from fastapi import Depends

from song_backend.app_container import app_container
from song_backend.business.song.song_service import SongService

SongServiceDep = Annotated[SongService, Depends(app_container.song_service)]
