from .base import *

ALLOWED_HOSTS = ["teste-server-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://teste-server-production.up.railway.app"]

# Secure Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SSL
SECURE_SSL_REDIRECT = True

SECURE_REFERRER_POLICY = "strict-origin"

SECURE_BROWSER_XSS_FILTER = True

ENGINE = env("ENGINE")
NAME = env("NAME")
USER = env("USER")
PASSWORD = env("PASSWORD")
HOST = env("HOST")
PORT = env("PORT")

DATABASES = {
    "default": {
        "ENGINE": ENGINE,
        "NAME": NAME,
        "USER": USER,
        "PASSWORD": PASSWORD,
        "HOST": HOST,
        "PORT": PORT,
    }
}
