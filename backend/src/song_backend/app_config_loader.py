from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppLyricConfig(BaseSettings):
    source: Literal["dummy"] | Literal["musixmatch"] = Field("dummy", description="Source for the lyrics")
    apikey: str | None = Field(None, description="API key for accessing lyrics services")

    model_config = SettingsConfigDict(env_prefix="APP_LYRICS_")


class AppLyricsAnalyserConfig(BaseSettings):
    source: Literal["dummy"] | Literal["openai"] = Field("dummy", description="Analysis source")
    apikey: str | None = Field(None, description="API key for analysis external service")

    model_config = SettingsConfigDict(env_prefix="APP_LYRICS_ANALYSER_")


class AppConfigLoader:
    _lyrics_config: AppLyricConfig
    _lyrics_analyser_config: AppLyricsAnalyserConfig

    def __init__(self) -> None:
        self._lyrics_config = AppLyricConfig()  # type: ignore - missing constructor params that are fetched at runtime from env variables
        self._lyrics_analyser_config = AppLyricsAnalyserConfig()  # type: ignore - missing constructor params that are fetched at runtime from env variables

    @property
    def lyrics(self) -> AppLyricConfig:
        return self._lyrics_config

    @property
    def lyrics_analyser(self) -> AppLyricsAnalyserConfig:
        return self._lyrics_analyser_config
