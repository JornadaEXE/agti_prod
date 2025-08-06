# setup/settings/prod.py

from decouple import config # O decouple puxa as configurações do config.env para usar as senhas sem revelar elas no git por exemplo
from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-9m45fd(vzw0i+5v&&uk3b7-2pfy^^bxh64ario%2+f_9pg-gmz'

ALLOWED_HOSTS = ['192.168.0.25', 'agtimaxi.local', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DB_NAME'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASSWORD'),
        'HOST': config('MYSQL_HOST', default='localhost'),
        'PORT': config('MYSQL_PORT', default='3306'),
    }
}
