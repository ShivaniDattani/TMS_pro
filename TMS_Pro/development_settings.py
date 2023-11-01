
from TMS_Pro.base_settings import *

DEBUG = True

#development database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev_db.sqlite3',
    }
}