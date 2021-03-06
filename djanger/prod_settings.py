# import environ

from .settings import *

env = environ.Env(
    DEBUG=(bool, False))  # false default
environ.Env.read_env(env_file='./.env')


ALLOWED_HOSTS += [
    'kromm.info',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGGING['handlers']['file']['level'] = 'WARNING'
LOGGING['handlers']['file']['filename'] = '/home/abi83/kromm.info/logging/log.log'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'admin@kromm.info'
EMAIL_HOST_PASSWORD = env('EMAIL_PSWD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
