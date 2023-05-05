from .base import *

CSRF_TRUSTED_ORIGINS = [f"https://.{HOST}"]
CORS_ORIGIN_WHITELIST = (f"https://{HOST}", "https://test-website-ecru.vercel.app")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
