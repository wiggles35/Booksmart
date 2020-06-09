from .base import *
INSTALLED_APPS += ("gunicorn",)
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#os.environ['HTTPS'] = "on"

