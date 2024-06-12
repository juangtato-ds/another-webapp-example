from fastapi import Request, status
from starlette.responses import JSONResponse, Response
from typing import Any, Callable, Coroutine, Type, Union

from song_backend.base.exception.exception_type import ExceptionType
from song_backend.base.exception.exceptions import BaseGenericException


class FastapiExceptionHandler:
    _exception_map: dict[ExceptionType, int] = {
        ExceptionType.NOT_FOUND: status.HTTP_404_NOT_FOUND,
        ExceptionType.FORBIDDEN: status.HTTP_403_FORBIDDEN,
        ExceptionType.INVALID_PARAMS: status.HTTP_400_BAD_REQUEST,
        ExceptionType.CONFLICT: status.HTTP_409_CONFLICT,
        ExceptionType.INTERNAL: status.HTTP_500_INTERNAL_SERVER_ERROR,
        ExceptionType.UNAUTHORIZED: status.HTTP_401_UNAUTHORIZED,
        ExceptionType.UNPROCESSABLE: status.HTTP_422_UNPROCESSABLE_ENTITY,
    }

    @staticmethod
    async def exception_handler(request: Request, exc: BaseGenericException) -> Response:
        return JSONResponse(
            {"detail": str(exc)},
            status_code=FastapiExceptionHandler._exception_map.get(
                exc.type, status.HTTP_500_INTERNAL_SERVER_ERROR
            ),
            headers={},
        )


default_exception_handler: dict[
    Union[int, Type[Exception]], Callable[[Request, Any], Coroutine[Any, Any, Response]]
] = {BaseGenericException: FastapiExceptionHandler.exception_handler}
