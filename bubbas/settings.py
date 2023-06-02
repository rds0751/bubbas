"""
Django settings for bubbas project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%=*+3ohnfapm8mz)ma-gt(xzckuawdof%7w5i9gcp!$v5ctm*z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    "debug_toolbar",
    'webp_converter',
    'ckeditor',
    "sorl.thumbnail",
    "compressor",

    # Custom Made
    'ads',
    'home',
    'escorts',
    'call_girls',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'bubbas.urls'

INTERNAL_IPS = [
    "127.0.0.1",
    "test.bubbas.in"
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'webp_converter.context_processors.webp_support',
            ],
        },
    },
]

WSGI_APPLICATION = 'bubbas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://dbmasteruser:smarty24@ls-da7a92b0797c88d3459343bcb1d7c69ce6cd65ab.cfcmo0to43fn.ap-south-1.rds.amazonaws.com:5432/postgres',
        conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
COMPRESS_REBUILD_TIMEOUT = 5400


CKEDITOR_UPLOAD_PATH=os.path.join(BASE_DIR, "rich")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
COMPRESS_OUTPUT_DIR = "CACHE"
COMPRESS_URL = STATIC_URL
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ("text/less", "lessc {infile} {outfile}"),
    ("text/x-sass", "sass {infile} {outfile}"),
    ("text/x-scss", "sass {infile} {outfile}"),
)

COMPRESS_OFFLINE_CONTEXT = {
    "STATIC_URL": "STATIC_URL",
}

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "compressor.finders.CompressorFinder",
)

CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'gv_cache',
        'TIMEOUT': 150,
    }
}