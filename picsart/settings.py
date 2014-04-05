"""
Django settings for picsart_twitter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('Joris Andrade', 'contact@nafiris.com'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au0pz+bo@+382*@dhc&tp2o9np)ie)x9dq(*!q94sge**kq87p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'picsart',
    'django_cas',
    'jfu'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.backends.ModelBackend',
    'django_cas.middleware.CASMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_cas.backends.CASBackend',
)

ROOT_URLCONF = 'picsart.urls'

WSGI_APPLICATION = 'picsart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sql',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr-FR'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True  # Ajoute un slash en fin d'URL

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'picsart/static/'

USE_PROXY = False

CAS_SERVER_URL = 'https://cas.utc.fr/casUTConly/'
CAS_AUTO_CREATE_USERS = True

PROXY_SETTINGS = {'http': 'http://proxyweb.utc.fr:3128/',
                  'https': 'http://proxyweb.utc.fr:3128/',
                  'ftp': 'http://proxyftp.utc.fr:3128/'}

FLICKR_API_KEY = '36773a70eb6db13b4fb1dc780948f0b6'
FLICKR_SECRET_KEY = '26186d98447f14ec'