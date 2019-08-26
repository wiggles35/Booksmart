from .base import *
INSTALLED_APPS += ("gunicorn",)
SECRET_KEY = os.environ['SECRET_KEY']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
os.environ['HTTPS'] = "on"
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd20si1a0vmjaov',
        'USER': 'kfakoszmkchopf',
        'PASSWORD': '80be5b694b4b4f2d1fbed91caddceee788026a487a92f6b5b13ba872803af7ca',
        'HOST': 'ec2-107-22-238-217.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
'''
