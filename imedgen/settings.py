"""
Django future_settings_system for imedgen project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/future_settings_system/

For the full list of future_settings_system and their values, see
https://docs.djangoproject.com/en/2.1/ref/future_settings_system/
"""
import os
import string

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

PROJECT_VERSION = os.getenv('PV_IMEDGEN', 'DEVELOPMENT')

# Quick-start development future_settings_system - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c-_n9y3)v=sdq3@4tnt)!$w5t_d1!vf%bb)@m#c^d)nc^%i5#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv('DEBUG_MODE', 0))

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
    '192.168.210.214',
    '192.168.135.38'
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

if os.getenv('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS.extend(
        [host.strip() for host in os.getenv('DJANGO_ALLOWED_HOSTS').split(',')]
    )


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imedgen',
    'projects',
    'django_extensions',
    'rest_framework',
    'django_cleanup',  # Always in the end! Order matters
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'imedgen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['imedgen', 'projects'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'imedgen.context_proccessors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'imedgen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'imedgen'),
        'USER': os.getenv('POSTGRES_USER', 'imedgen'),
        'HOST': os.getenv('PSQL_HOST', 'postgresql'),
        'PORT': os.getenv('PSQL_PORT', 5432),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
    },
}


# Cache
# https://docs.djangoproject.com/en/2.2/topics/cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": (
            "redis://"
            f"{os.getenv('REDIS_HOST', '127.0.0.1')}:"
            f"{os.getenv('REDIS_PORT', '6379')}/1"
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# I guess that's our only choice
TIME_ZONE = 'Europe/Moscow'

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

DATA_UPLOAD_MAX_MEMORY_SIZE = 262144000
FILE_UPLOAD_MAX_MEMORY_SIZE = 262144000

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('STATIC_FILES', '/static/')
# DEBUG ONLY

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

VALIDATOR_SYMBOLS = f'{string.ascii_letters}{string.digits}_-'

CRT_TTS_CONVERT_API_URL = '%YOUR_CRT_TTS_API_LINK%'

YSK_TTS_CONVERT_API_URL = (
    '%YOUR_YSK_TTS_API_LINK%'
)
YSK_TTS_FOLDER_ID = '%YOUR_YSK_FOLDERID%'

YSK_BEARER_PULL_SECRET = '%YOUR_YSK_BEARER_PULL_TOKEN%'
YSK_IAM_BEARER_PULL_URL = '%YOUR_YSK_BEARER_PULL_LINK%'


ROOT_URL = 'imedgen/'

LOGGING = {

    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {

        'main_file': {
            'class': 'logging.FileHandler',
            'filename': 'debug.log'
        },

        'audiorecord_file': {
            'class': 'logging.FileHandler',
            'filename': 'audiorecord_debug.log'
        },

        'project_api': {
            'class': 'logging.FileHandler',
            'filename': 'projects_api.log'
        },

        'tts_backend_file': {
            'class': 'logging.FileHandler',
            'filename': 'tts_backend.log'
        }

    },

    'loggers': {

        'django': {
            'handlers': ['main_file'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'mediarecord': {
            'handlers': ['audiorecord_file'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'tts_backend': {
            'handlers': ['tts_backend_file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}


YANDEX_VOICES = [
    'alyss',
    'jane',
    'oksana',
    'omazh',
    'zahar',
    'ermil',
    'alena',
    'filipp'
]

YANDEX_EMOTE = ['neutral', 'good', 'evil']


CRT_VOICES = [
    'Vladimir8000',
    'Julia8000',
    'Anna8000',
    'Alexander8000',
    'Maria8000',
    'Lydia8000',
    'Carol8000',
    'Asel8000',
]

MANUAL_EDIT_SLUG = 'drafts'

# Other Hz rate cannot be played by Buddy
DEFAULT_HRZ_RATE = 8000


CRT_TTS_OPENING_SHORTENING_RULES = {
    'Анна8000': 0.2,
    'Владимир8000': 0.4,
    'Юлия8000': 0.4,
    'Виктория8000': 0.3,
    'Александр8000': 0.35,
    'Мария8000': 0.28,
    'Лидия8000': 0,
}

ALLOWED_MIME_TYPES = (
    'text/plain',
    'text/csv',
    'text/x-csv',
    'application/csv',
    'application/msword',
    'application/vnd.ms-excel',
    'text/xml',
    'text/html',
    'application/xml'
)

EXTENSIONS_MAX_UNIQUE_QUERY_ATTEMPTS = 1000


CRT_TEMPLATE = {
    'uuid': '123456789',
    'key': 'imedgen',
    'ie': 'UTF-8',
    'lang': 'ru-RU',
    'voice': '',
    'text': '',
}

YSK_TEMPLATE = {
    'text': '',
    'lang': 'ru-RU',
    'voice': '',
    'emotion': '',
    'speed': 1,  # Since we're using SoX it's better to get regular val
    'format': 'lpcm',
    'sampleRateHertz': DEFAULT_HRZ_RATE,
    'folderId': ''
}