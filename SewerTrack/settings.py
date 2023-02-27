"""
Django settings for SewerTrack project.

Generated by 'django-admin startproject' using Django 4.2.dev20220930042619.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



#ENABLE GDAL AND GEOS LIBRARIES
GDAL_LIBRARY_PATH = r"C:\Users\Admin\New\Sewer_Project\venv\Lib\site-packages\osgeo\gdal304.dll"
GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1okvx5i79=utogm)&pxtr8hgycc7b)*xr4y(#+(u7z)g%hso)c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Repo',
    'SewerTrack',
    'geopy',
    'folium',
    'django.contrib.gis',
    "phonenumber_field",
    'django_bootstrap5',
    'bootstrap5',
    'mapwidgets',
    'location_field.apps.DefaultConfig',
    'rest_framework',
    'mapbox_location_field',
    'googlemaps',
    'psycopg2',
    'geojson'
    

]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SewerTrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'SewerTrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Sewer_Repo_Track_2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_MAP_API_KEY = 'AIzaSyDbkL14BUIdpTXGCqhYQxWlyk_JvFLLlgw'
MAPBOX_KEY = 'pk.eyJ1IjoiY2hlZ2VyZSIsImEiOiJjbGR6a2dhazYwdHJ1M29wNnBxbHJ1bm5rIn0.qIMl6ZY2s7PlUi5J2icKvQ'

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 12),
        ("mapCenterLocationName", "nairobi"),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'kenya'}}),
        ("markerFitZoom", 12),
        ("scrollWheel", False),
        ("streetViewControl", True),
    ),
    "GOOGLE_MAP_API_KEY": 'AIzaSyDbkL14BUIdpTXGCqhYQxWlyk_JvFLLlgw'
    
}