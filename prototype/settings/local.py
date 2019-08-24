from .base import *
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = '7456898oiuvbi876ir8tgbliygoubpiblk0987'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}