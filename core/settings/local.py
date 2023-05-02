from .base import *

import dj_database_url

ALLOWED_HOSTS = ["teste-server-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = [
    "http://teste-server-production.up.railway.app/",
    "https://teste-server-production.up.railway.app",
]

DATABASE_URL = env("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
