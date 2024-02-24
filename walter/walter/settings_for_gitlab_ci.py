from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_walter_prod',
        'USER': 'root',
        'PASSWORD': 'temp_root_pw',
        'HOST': 'mysql',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
