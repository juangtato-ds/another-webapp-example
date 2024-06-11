import uvicorn

from song_backend_rest.config.app_rest_config import AppRestConfig


if __name__ == "__main__":
    config = AppRestConfig()  # type: ignore

    uvicorn.run(
        "song_backend_rest.main:app",
        host=config.app_rest_host,
        port=config.app_rest_port,
        reload=config.app_rest_reload,
        log_level=config.app_rest_reload,
    )
