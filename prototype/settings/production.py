from .base import *
INSTALLED_APPS += ("gunicorn",)
SECRET_KEY = os.environ['SECRET_KEY']