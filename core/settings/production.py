from .base import *

DEBUG = False

ALLOWED_HOSTS = ["teste-server-production.py.up.railway.app/", "127.0.0.1"]

DATABASES = {
    "default": {
        #'ENGINE': 'django.db.backends.sqlite3',
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "N0xDAZu2MT19tYhFMcEK",
        "HOST": "containers-us-west-5.railway.app",
        "PORT": "6164",
    }
}
