from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # Your logging configuration only captures logs within the django namespace.
        # https://stackoverflow.com/questions/36571284/why-django-logging-is-not-working
        #'django': {
        #    'handlers': ['console'],
        #    'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        #},
        # So that we capture ANY namespace
        '': {
            'handlers': ['console'],
            #'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
