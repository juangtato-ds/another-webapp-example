from fastapi import APIRouter, FastAPI
import pkgutil
import importlib
from song_backend_rest import endpoints
from song_backend_rest.exception.exception_handler import default_exception_handler


def _retrieve_sub_modules(root_module: object) -> dict:
    modules = {}
    for _, name, _ in pkgutil.iter_modules(root_module.__path__):
        module_name = f"{root_module.__package__}.{name}"
        modules[module_name] = importlib.import_module(module_name)
    return modules


def _load_modules(app: FastAPI, root_module: object):
    for name, mod in _retrieve_sub_modules(root_module=root_module).items():
        router = getattr(mod, "router", None)
        if isinstance(router, APIRouter):
            app.include_router(router)


def _app_factory() -> FastAPI:
    # TODO add excepcion handler
    result = FastAPI(
        title="Song Lyrics Analyser",
        description="Another POC",
        version="0.0.0",
        exception_handlers=default_exception_handler
    )
    _load_modules(app=result, root_module=endpoints)
    return result


app = _app_factory()
