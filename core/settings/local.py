from .base import *

INTERNAL_IPS = ALLOWED_HOSTS

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "http")
