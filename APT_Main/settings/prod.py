from .base import *

DEBUG = False
ALLOWED_HOSTS = ['192.168.0.25', 'agtimaxi.local', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'