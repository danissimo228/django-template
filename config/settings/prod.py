"""
Production settings
"""

from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
