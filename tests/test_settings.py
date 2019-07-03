# coding: utf-8

from __future__ import unicode_literals

import os

DIRNAME = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

SECRET_KEY = 'foo'

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'hipo_drf_exceptions',
    'test_app',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'hipo_drf_exceptions.handler',
}

ROOT_URLCONF = 'test_app.urls'
