"""
Django settings for news365 project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""


import os
import django_heroku




SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'pzdi35uz17b5@ns7!65%#4r3c3$gs@9sra57!n_et-erf0@d^u')


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}





## Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

# Base url to serve media files
MEDIA_URL = '/media/'


# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'pzdi35uz17b5@ns7!65%#4r3c3$gs@9sra57!n_et-erf0@d^u'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True



DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     
     #Main Apps
    'homepage',
    'video',
    'politics',
    'education',
    'bangladesh',
    'international',
    'sport',
    'travel',
    'health',
    'technology',
    'funny',
    'fashion',
    
    #Thirdparty apps
    'django_summernote',
    'crispy_forms',
    
    
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'news365.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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





WSGI_APPLICATION = 'news365.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pportal',
        'USER': 'nasim',
        'PASSWORD': 'Nimudryflower2018',
        'HOST': 'localhost',
        'PORT': '2000',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

MESSAGE_LEVEL = 25


#summernote settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_THEME = 'bs4'

# Activate Django-Heroku.
django_heroku.settings(locals())

