from typing import Optional

from song_backend.base.exception.exception_type import ExceptionType


class BaseGenericException(Exception):
    """Categorised error, by default it is considered undefined-internal error"""

    type: ExceptionType = ExceptionType.INTERNAL
    message = "Internal Exception - no message"

    def __init__(self, message: Optional[str] = None, details: Optional[str] = None):
        """
        Args:
            message (str): Error message. This will replace the defined class message.
            details (str): Details about the error.
        """
        self.message = self._compose_message(message=message, details=details)
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

    def _compose_message(self, message: Optional[str] = None, details: Optional[str] = None) -> str:
        """Composition of the error message

        Args:
            message (str): Error message. This will replace the defined class message.
            details (str): Details about the error.

        Returns:
            message (str): A message  error with the following format:
                self.message: message - details
        """
        return " - ".join([msg for msg in [message or self.message, details] if msg])


class InternalRuntimeException(BaseGenericException):
    pass

class ElementNotFoundException(BaseGenericException):
    type = ExceptionType.NOT_FOUND
    message = "Element not found"


class ForbiddenAccessException(BaseGenericException):
    type = ExceptionType.FORBIDDEN
    message = "Do not have permission"


class UnauthorizedException(BaseGenericException):
    type = ExceptionType.UNAUTHORIZED
    message = "Not authorized"


class InvalidParameterException(BaseGenericException):
    type = ExceptionType.INVALID_PARAMS
    message = "Invalid parameters"


class UnprocessableEntityException(BaseGenericException):
    type = ExceptionType.UNPROCESSABLE
    message = "Cannot process the entity"


class ElementAlreadyExistsException(BaseGenericException):
    type = ExceptionType.CONFLICT
    message = "Element already exists"
