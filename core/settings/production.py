from .base import *

HOST = "teste-server-production.up.railway.app"

ALLOWED_HOSTS += [HOST]

CSRF_TRUSTED_ORIGINS += [f"https://{HOST}"]

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
