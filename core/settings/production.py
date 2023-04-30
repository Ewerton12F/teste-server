from .base import *

ALLOWED_HOSTS = ["teste-server-production.up.railway.app"]

ENGINE = env("ENGINE")
NAME = env("NAME")
USER = "postgres"
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
        "TEST": {
            "NAME": "mytestdatabase",
        },
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
