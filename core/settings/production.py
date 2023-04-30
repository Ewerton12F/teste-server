from .base import *

import os

env = os.environ.get

ALLOWED_HOSTS = ["teste-server-production.py.up.railway.app/", "127.0.0.1"]

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
    }
}

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
