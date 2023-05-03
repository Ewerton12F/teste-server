from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]

INTERNAL_IPS = ALLOWED_HOSTS

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
