from carlogger.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'carlogger_db',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '',
        'PORT': '',
    }
}

