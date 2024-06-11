from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppLyricConfig(BaseSettings):
    source: Literal["dummy"] | Literal["musixmatch"] = Field("dummy", description="Source for the lyrics")
    apikey: str | None = Field(None, description="API key for accessing lyrics services")

    model_config = SettingsConfigDict(env_prefix="APP_LYRICS_")


class AppConfigLoader:
    _lyrics_config: AppLyricConfig

    def __init__(self) -> None:
        self._lyrics_config = AppLyricConfig()  # type: ignore

    @property
    def lyrics(self) -> AppLyricConfig:
        return self._lyrics_config
