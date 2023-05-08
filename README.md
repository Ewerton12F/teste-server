# Hello

This is the basis of a Django+Postgres+Next.js private project. You can use for building you own app. Give a look above for more details.

## Railway + Vercel

I deployed the Django+Postgres on a Railway server. You can access the API [here][railway].

I deployed the Next.js website on a Vercel server. You can access [here][vercel]. The Github repository can be found [here][next-repo].

## Index

🚧 = Documentation under construction

* [Get Started](#run)
  * [Configuring enviorement variables](#configuring-enviorement-variables) 
  * [Secret key generation](#secret-key-generation) 
  * [Run](#run)
* [Django](#django)
  * [Configuring Multiple Settings Files](#configuring-multiple-settings-files)
  * [WSGI🚧](#wsgi)
    * [Gunicorn🚧](#gunicorn)
* [Django Rest Framework 🚧](#django-rest-framework)
  * [Routers 🚧](#routers)
  * [Serializers 🚧](#serializers)
  * [API endpoints🚧](#api-endpoints)
* [Best practices🚧](#best-practices)
  * [black🚧](#black)
  * [isort🚧](#isort)
  * [flake8🚧](#flake8)
* [Security🚧](#security)
  * [SSL🚧](#ssl)
* [Tests🚧](#tests)
  * [Coverage🚧](#coverage)
* [PostgreSQL🚧](#postgresql) 
  * [psycopg2🚧](#psycopg2) 
  * [dj-database-url🚧](#dj-database-url) 
* [CI/CD🚧](#ci-cd)
  * [Github Actions🚧](#github-actions)
  * [Railway deployment🚧](#railway-deployment)

## Get Started

First things comes first, download the repository to your machine and enter the folder:

```bash
git clone git@github.com:Ewerton12F/teste-server.git
cd teste-server
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

Now you have to install the the dependencies in `requirements.txt` and `requirements-dev.txt` files:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Configuring environment variables

We're gona use environment variables to set up our Django project.

Now that we have done the Run step we must configure the environment variables. Those are:

```bash
DEBUG=DEBUG
HOST=HOST
SECRET_KEY=SECRET_KEY
DATABASE_URL=DATABASE_URL
```

You can use the example file [`.env_example`](.env_example) in the root and change the variables values. Don't forget to rename the file to `.env`.

We're gona use `dotenv` and `decouple` package to manage our environment variables.

In `base.py` file I will set this configuration:

```python
from decouple import config
from dotenv import load_dotenv

import os

load_dotenv()

env = os.environ.get

DEBUG = config("DEBUG", default=False, cast=bool)
HOST = env("HOST")
SECRET_KEY = env("SECRET_KEY")
DATABASE_URL = env("DATABASE_URL")
```

* In `DEBUG` we must set the variable to `True` if we're working locally - it's gona trigger some features to help on debuging. To production we must set it to `False`. 
* The `HOST` can set to `127.0.0.1` if we're working locally. To production we must set it to `changethisdomain.com`.
* The `DATABASE_URL` must follow this patern `postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}`.
* Use some tool to generate your own `SECRET_KEY`, like the one above here.

### Secret key generation

We are gona add our own secret key. Python brings a built-in tool which enables us to generate a secret key.

In [Django's Github repository][django-repo] we can find a function that`s going to provide a way of generating a random key.

To create a secret key we need to access the python shell using the command:

```bash
$ python3 manage.py shell
```

And then:

```bash
$ from django.core.management.utils import get_random_secret_key
$ print(get_random_secret_key())
```

And we're a gona get something like this:

```bash
0v7#=qc!&0^yhqyzc2)atop#at_foelv6g4*6=)if#r=@5=6mb
```
### Run

That's it, we're finish the setup and now we can run some Django commands:

```bash
./manage.py migrate api
./manage.py migrate 
```

Now we can finally make our Django project run:

```bash
./manage.py runserver
```

## Django

In this section I'm going to describe how I setup this Django application.

### Configuring Multiple Settings Files

The settings will be divided in other files because this application will be runing in ours machines and a server when deployed.

We have different environments with different configurations so we have to be prepared for that.

We can create a modular approuch and have different settings files for different environments for our Django application to work within. For example, we can use `DEBUG = True` when we work locally.

So we want to tell Django to find settings as shows:

```bash
.
├── settings
│   ├── base.py
│   ├── local.py
│   └── production.py.py 
.
```

In `manage.py` we determinate which configuration will be used for each environment:

```python
from core.settings import base

def main():
    if base.DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
```

In `core.urls` we determine which configuration use for each environment.

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

🚧 Under construction 🚧


[django-repo]: https://github.com/django/django
[next-repo]: https://github.com/Ewerton12F/test-website
[railway]: https://teste-server-production.up.railway.app/api/services-list
[vercel]: https://test-website-rho-three.vercel.app/