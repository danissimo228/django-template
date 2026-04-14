"""
Local settings for local development and testing
"""

from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
