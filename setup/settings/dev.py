from .base import *

DEBUG = False
ALLOWED_HOSTS = ['192.168.0.25', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_main',
        'USER': 'root',
        'PASSWORD': 'ti@118',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
STATIC_ROOT = BASE_DIR / 'staticfiles'