
from TMS_Pro.base_settings import *

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ALLOWED_HOSTS = [os.getenv("MY_HOST")]
CSRF_TRUSTED_ORIGINS = ["https://" + os.getenv("MY_HOST")]

# Production sqlite database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod_db.sqlite3',
    }
}

# Log any errors and warnings to a rolling file in /var/log/django/tms_log.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s, %(levelname)s, %(name)s, %(message)s'
        },
    },
    'handlers': {
        'rolling_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/django/tms.log',
            'maxBytes': 1024 * 1024 * 5, # i.e. 5 MB
            'backupCount': '3',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['rolling_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}