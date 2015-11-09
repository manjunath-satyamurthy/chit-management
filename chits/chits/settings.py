"""
Django settings for chits project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "@&$$$#f)l(%^-d+nym0fneofmxhk6_6u%xw96ma#+$tp9lo+9e"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chits',
    'base',
    'management',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chits.urls'

WSGI_APPLICATION = 'chits.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


TEMPLATES = [
    {
        'context_processors': 'django.template.context_processors.media',
    }
]


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

try:
    from local_settings import STATICFILES_DIRS
except ImportError:
    STATICFILES_DIRS = None

try:
    from local_settings import MEDIA_ROOT
except ImportError:
    MEDIA_ROOT = None

AUTH_USER_MODEL = 'base.ChitUser'

MEDIA_URL = 'http://127.0.0.1:8000/static/media/member_photos/'

AWS_STORAGE_BUCKET_NAME = 'reports-pdfs'
AWS_ACCESS_KEY_ID = 'AKIAJXQU7GUI4LQIUKIA'
AWS_SECRET_ACCESS_KEY = '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'

from boto.s3.connection import S3Connection

conn = S3Connection(
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY
)
bucket = conn.create_bucket(AWS_STORAGE_BUCKET_NAME)