
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