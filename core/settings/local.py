from .base import *

ALLOWED_HOSTS = ["teste-server-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = [
    "http://teste-server-production.up.railway.app/",
    "https://teste-server-production.up.railway.app/",
]

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

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
