from .base import *

ALLOWED_HOSTS += ["teste-server-production.up.railway.app"]

CSRF_TRUSTED_ORIGINS = [f"https://{ALLOWED_HOSTS}"]

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
