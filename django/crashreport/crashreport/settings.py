"""
Django settings for crashreport project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'at_4nc!x(m=v2dxwzr*kdsvzz_()r+jt^5usmzexh^jvaaj9iz')

DEBUG = bool(os.environ.get('DEBUG', False))

TEMP_UPLOAD_DIR = os.environ.get('TEMP_UPLOAD_DIR', '/tmp/upload_dir')

SYMBOL_LOCATION = os.environ.get('SYMBOL_LOCATION', '/tmp/symbols/')

SYMBOL_UPLOAD_DIR = os.environ.get('SYMBOL_UPLOAD_DIR', '/tmp/symbol_upload/')

MINIDUMP_STACKWALK = os.environ.get('MINIDUMP_STACKWALK', 'minidump_stackwalk')

SYMBOL_PROCESSING = os.environ.get('SYMBOL_PROCESSING', os.path.join(BASE_DIR, "../../tools/process-symbols/process-symbols.py"))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', [])

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'crashsubmit.apps.CrashsubmitConfig',
    'processor.apps.ProcessorConfig',
    'symbols.apps.SymbolsConfig',
    'stats.apps.StatsConfig',
    'base.apps.BaseConfig',
    'management.apps.ManagementConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crashreport.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'crashreport.wsgi.application'

COMPRESS_PRECOMPILERS = (
        ('text/less', 'lesscpy {infile}'),
)


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ.get('DB_NAME', 'crashreport'),

        'USER': os.environ.get('DB_USER', 'moggi'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('DB_PORT', ''),                      # Set to empty string for default.
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING_DIR = os.environ.get('LOGGING_DIR', '/home/moggi/django_logs/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'crashsubmit': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'crashsubmit.log'),
            },
        'processor': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'processor.log'),
            },
        'stats': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'stats.log'),
            },
        'symbols': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'symbols.log'),
            },
        },
    'loggers': {
        'crashsubmit': {
            'handlers': ['crashsubmit'],
            'level': 'WARNING',
            'propagate': True,
            },
        'processor': {
            'handlers': ['processor'],
            'level': 'WARNING',
            'propagate': True,
            },
        'stats': {
            'handlers': ['stats'],
            'level': 'WARNING',
            'propagate': True,
            },
        'symbols': {
            'handlers': ['symbols'],
            'level': 'INFO',
            'propagate': True,
            },
        },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/srv/www/static')
