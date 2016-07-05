"""
Django settings for bcpp_interview project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
APP_LABEL = 'example'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4w#xs+=lrx4$mmqv+vzy^9i!(sni2eh=q_-9(#w4r20sv($2af'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TASTYPIE_FULL_DEBUG = True
ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_crypto_fields.apps.DjangoCryptoFieldsAppConfig',
    'edc_base',
    'edc_content_type_map.apps.EdcContentTypeAppConfig',
    'edc_visit_schedule',
    'example.apps.EdcMetaDataAppConfig',
    'example.apps.EdcAppointmentAppConfig',
    'example.apps.ExampleAppConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
SQLITE3_DBNAME = 'db.sqlite3'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, SQLITE3_DBNAME),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.child('static')
MEDIA_ROOT = BASE_DIR.child('media')
MEDIA_URL = '/media/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


GIT_DIR = BASE_DIR.ancestor(1)
KEY_PATH = os.path.join(BASE_DIR.ancestor(1), 'crypto_fields')
SHOW_CRYPTO_FORM_DATA = True
LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'),
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'
