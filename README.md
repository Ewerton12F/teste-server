# <p align="center">🚧 Under construction 🚧</p>

<p align="center">I will be updating this page during the week.</p>

--- 

# Hello!

I deployed this website on a Vercel server. You can access [here][vercel].

I deployed this website on a Vercel server. You can access [here][vercel].

The back-end is developed using Django Rest Framework to provide an API which will be consumed by the Next.JS front-end application.

---

# Django

@ Phase 1 - Design, Implement and iterate over a complex database schema

@ Phase 2 - Implement Routers Vieewsets and Serializers to create API endpoints for clients interactions

@ Phase 3 - Implement serializer custumizations to customize data output

@ Phase 4 - Buid unit and end-to-end tests to ensure the application works as intended

@ Phase 5 - Document the API endpoints to support frontend interactions 

## Modularizing Django Settings

The settings will be divided in other files because this application will be runing in ours machines and a server when deployed.

We have different environments with different configurations so we have to be prepared for that.

We can create a modular approuch and have different settings files for different environments for our Django application to work within. For example, we can use `DEBUG = True` when we work locally.

So we want to tell Django to find settings as shows:

```bash
.
├── settings
│   ├── base.py
│   ├── local.py
│   └── production.py 
.
```

In `manage.py` we determinate which configuration will be used for each environment:

```python
def main():
    if base.DEBUG:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
```

### `local.py`

Settings related to local development

### `production.py`

Settings related to deployed application

## Secret Key Generation

We are gona add our own secret key. Python brings a built-in tool which enables us to generate a secret key.

In [Django Github repository][django-repo] we can find a function that`s going to provide a way of generating a random key.

To create we nedd to access the python shell using the comman:

```bash
$ python manage.py shell
```

and then:

```bash
$ from django.core.management.utils import get_random_secret_key
$ print(get_random_secret_key())
```

## Configuring Environment Variables

We gona use `python-dotenv` package to manage our environment variables.

In `base.py` file we will set this configuration:

```python
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
```

The key will that we generated will be placed in our `.env` file.

## Tests

- pytest
- pytest_django

---

# Design

If you access the link above you'll see that it's a mobile version of the layout 
below. This happened because in the middle of the development I understood the
concept of "Mobile First". 

I'm using Figma to design the layout of this website.

![Desktop Layout](repo_imgages/Frame-Website.png "Desktop Layout")



[django-repo]: https://github.com/django/django
[vercel]: https://test-website-rho-three.vercel.app/