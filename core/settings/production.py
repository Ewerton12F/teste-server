from .base import *

ALLOWED_HOSTS += [HOST, "http://localhost:3000/"]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS += [f"https://.{HOST}", "http://localhost:3000/"]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
