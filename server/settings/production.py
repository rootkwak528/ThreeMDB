from .base import *
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

<<<<<<< HEAD
ALLOWED_HOSTS = ['ssafy5-seoul5-group5-final-pjt.herokuapp.com']

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}
=======
ALLOWED_HOSTS = ['ssafy5-seoul5-group5-final-pjt.herokuapp.com']
>>>>>>> 09688a53ca7bcc66f2488b418584a49bdf94d4c6
