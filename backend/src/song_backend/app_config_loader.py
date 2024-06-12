from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# TODO - move individual config classes to config module inside backend module
class AppLyricConfig(BaseSettings):
    source: Literal["dummy"] | Literal["musixmatch"] = Field(
        "dummy", description="Source for the lyrics"
    )
    apikey: str | None = Field(None, description="API key for accessing lyrics services")

    model_config = SettingsConfigDict(env_prefix="APP_LYRICS_")


class AppLyricsAnalyserConfig(BaseSettings):
    source: Literal["dummy"] | Literal["openai"] = Field("dummy", description="Analysis source")
    apikey: str | None = Field(None, description="API key for analysis external service")

    model_config = SettingsConfigDict(env_prefix="APP_LYRICS_ANALYSER_")


class AppSqlConfig(BaseSettings):
    dialect: str = Field("postgresql", description="SQL dialect")
    username: str = Field(description="SQL username")
    password: str = Field(description="SQL user password")
    host: str = Field(description="SQL host")
    database: str = Field(description="SQL database name")

    model_config = SettingsConfigDict(env_prefix="APP_SQL_")


class AppConfigLoader:
    # General
    _sql_config: AppSqlConfig

    # Domain - song
    _lyrics_config: AppLyricConfig
    _lyrics_analyser_config: AppLyricsAnalyserConfig

    def __init__(self) -> None:
        self._sql_config = AppSqlConfig()  # type: ignore - missing constructor params that are fetched at runtime from env variables
        self._lyrics_config = AppLyricConfig()  # type: ignore - missing constructor params that are fetched at runtime from env variables
        self._lyrics_analyser_config = AppLyricsAnalyserConfig()  # type: ignore - missing constructor params that are fetched at runtime from env variables

    @property
    def sql(self) -> AppSqlConfig:
        return self._sql_config

    @property
    def lyrics(self) -> AppLyricConfig:
        return self._lyrics_config

    @property
    def lyrics_analyser(self) -> AppLyricsAnalyserConfig:
        return self._lyrics_analyser_config
