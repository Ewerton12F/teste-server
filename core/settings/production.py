from .base import *

CORS_ORIGIN_WHITELIST = (f"https://{HOST}", "https://test-website-ecru.vercel.app/")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [f"https://.{HOST}"]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
