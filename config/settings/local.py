"""
Local settings for local development and testing
"""

from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "level": "WARNING",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / f"{PROJECT_NAME}.log",
            "formatter": "verbose",
            "encoding": "utf-8",
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 10,
            "level": "INFO",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["file", "console"],
            "level": "WARNING",
        },
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["file", "console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },
        "apps": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
