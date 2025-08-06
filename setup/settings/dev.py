# setup/settings/dev.py

from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-9m45fd(vzw0i+5v&&uk3b7-2pfy^^bxh64ario%2+f_9pg-gmz'

ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.2']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
