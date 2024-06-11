from pydantic import Field
from pydantic_settings import BaseSettings


class AppRestConfig(BaseSettings):
    app_rest_host: str = Field(description="Host")
    app_rest_port: int = Field(description="Port")
    app_rest_reload: bool = Field(
        False, description="Reload the app when a file changes, useful for develop"
    )
    app_log_level: str = Field("error", description="Logger level for rest")
