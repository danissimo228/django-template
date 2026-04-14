from typing import Optional
from http import HTTPStatus

from django.http import JsonResponse


class JsonResponseFactory:
    """A factory for creating standardized HTTP responses in JSON format."""

    @classmethod
    def _make_response(
        cls,
        body: Optional[dict] = None,
        status_code: int = HTTPStatus.OK.value,
        message: str = HTTPStatus.OK.name,
    ) -> JsonResponse:
        """Internal method for creating a JSON response with a uniform structure."""
        return JsonResponse(
            data={
                "body": body or {},
                "status": {"code": status_code, "message": message},
            },
            status=status_code,
        )

    @classmethod
    def success_response(
        cls,
        body: Optional[dict] = None,
        status_code: int = HTTPStatus.OK.value,
        message: str = HTTPStatus.OK.name,
    ) -> JsonResponse:
        """Creates a successful HTTP response in a standardized format."""
        return cls._make_response(body, status_code, message)

    @classmethod
    def error_response(
        cls,
        body: Optional[dict] = None,
        status_code: int = HTTPStatus.BAD_REQUEST.value,
        message: str = HTTPStatus.BAD_REQUEST.name,
    ) -> JsonResponse:
        """Creates an HTTP error response in a standardized format."""
        return cls._make_response(body, status_code, message)
