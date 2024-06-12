from enum import Enum


class ExceptionType(str, Enum):
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    INVALID_PARAMS = "invalid_params"
    CONFLICT = "conflict"
    INTERNAL = "internal"
    UNPROCESSABLE = "unprocessable"
