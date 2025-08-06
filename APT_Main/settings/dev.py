from .base import *

DEBUG = True
ALLOWED_HOSTS = ['192.168.0.25', 'agtimaxi.local','127.0.0.1']

# Banco SQLite local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}