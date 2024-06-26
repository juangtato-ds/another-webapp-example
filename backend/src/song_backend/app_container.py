from sqlalchemy import URL, Engine, create_engine
from song_backend.app_config_loader import AppConfigLoader
from song_backend.business.song.lyrics.impl.lyrics_search_acl_dummy_adapter import (
    LyricsSearchAclDummyAdapter,
)
from song_backend.business.song.lyrics.impl.lyrics_search_acl_musixmatch_adapter import (
    LyricsSearchAclMusixmatchAdapter,
)
from song_backend.business.song.lyrics.lyrics_search_acl_adapter import LyricsSearchAclAdapter
from song_backend.business.song.lyrics_analyser.impl.lyrics_analyser_acl_dummy_adapter import (
    LyricsAnalyserAclDummyAdapter,
)
from song_backend.business.song.lyrics_analyser.impl.openai.lyrics_analyser_acl_openai_adapter import (
    LyricsAnalyserAclOpenaiAdapter,
)
from song_backend.business.song.lyrics_analyser.lyrics_analyser_acl_adapter import (
    LyricsAnalyserAclAdapter,
)
from song_backend.business.song.song_service import SongService, SongServiceFactory


class AppContainer:
    # App config
    _config: AppConfigLoader
    # DB
    _db_engine: Engine
    # Acl
    _lyrics_acl: LyricsSearchAclAdapter | None = None
    _lyrics_analyser_acl: LyricsAnalyserAclAdapter | None = None
    # Services
    _song_service: SongService

    def __init__(self) -> None:
        self._config = AppConfigLoader()  # type: ignore

        sql_db_url: URL = URL.create(
            self._config.sql.dialect,
            username=self._config.sql.username,
            password=self._config.sql.password,  # plain (unescaped) text
            host=self._config.sql.host,
            database=self._config.sql.database,
        )

        self._db_engine = create_engine(sql_db_url, echo=True)

        self._song_service = SongServiceFactory.create(
            self._db_engine, self._get_lyrics_acl(), self._get_lyrics_analyser_acl()
        )

    def _get_lyrics_acl(self) -> LyricsSearchAclAdapter:
        if self._lyrics_acl is None:
            if (
                self._config.lyrics.source == "musixmatch"
                and self._config.lyrics.apikey is not None
            ):
                self._lyrics_acl = LyricsSearchAclMusixmatchAdapter(self._config.lyrics.apikey)
            else:
                # fallback
                self._lyrics_acl = LyricsSearchAclDummyAdapter()
        return self._lyrics_acl

    def _get_lyrics_analyser_acl(self) -> LyricsAnalyserAclAdapter:
        if self._lyrics_analyser_acl is None:
            if (
                self._config.lyrics_analyser.source == "openai"
                and self._config.lyrics_analyser.apikey is not None
            ):
                self._lyrics_analyser_acl = LyricsAnalyserAclOpenaiAdapter(
                    self._config.lyrics_analyser.apikey
                )
            else:
                # fallback
                self._lyrics_analyser_acl = LyricsAnalyserAclDummyAdapter()
        return self._lyrics_analyser_acl

    def song_service(self) -> SongService:
        return self._song_service


class AppContainerFactory:
    @staticmethod
    def create() -> AppContainer:
        return AppContainer()


app_container = AppContainerFactory.create()
