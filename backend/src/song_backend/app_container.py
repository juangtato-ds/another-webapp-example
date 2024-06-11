from song_backend.app_config_loader import AppConfigLoader
from song_backend.business.song.lyrics.impl.lyrics_search_acl_dummy_adapter import LyricsSearchAclDummyAdapter
from song_backend.business.song.lyrics.lyrics_search_acl_adapter import LyricsSearchAclAdapter
from song_backend.business.song.song_service import SongService, SongServiceFactory


class AppContainer:
    # App config
    _config: AppConfigLoader
    # Acl
    _lyrics_acl: LyricsSearchAclAdapter | None = None
    # Services
    _song_service: SongService

    def __init__(self) -> None:
        self._config = AppConfigLoader()  # type: ignore

        self._song_service = SongServiceFactory.create(self._get_lyrics_acl())

    def _get_lyrics_acl(self) -> LyricsSearchAclAdapter:
        if self._lyrics_acl is None:
            if self._config.lyrics.source == "musixmatch" and self._config.lyrics.apikey is not None:
                raise NotImplementedError()
            else:
                # fallback
                self._lyrics_acl = LyricsSearchAclDummyAdapter()
        return self._lyrics_acl

    def song_service(self) -> SongService:
        return self._song_service


class AppContainerFactory:
    @staticmethod
    def create() -> AppContainer:
        return AppContainer()


app_container = AppContainerFactory.create()
