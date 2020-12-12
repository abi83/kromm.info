# import environ

from .settings import *

env = environ.Env(
    DEBUG=(bool, False))  # false default
environ.Env.read_env(env_file='./.env')


ALLOWED_HOSTS += [
    'kromm.info',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'info@krommclub.ru'
# EMAIL_HOST_PASSWORD = env('EMAIL_PSWD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = 'info@krommclub.ru'

# LOGGING['handlers']['file']['filename'] = '/home/abi83/krommclub.ru/logging/log.log'
