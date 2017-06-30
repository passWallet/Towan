# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from getenv import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', 'a_secret_key')

# Blocktrail API config
MY_APIKEY = env('MY_APIKEY')
MY_APISECRET = env('MY_APISECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG= env('DEBUG')

ADMIN_ENABLED = env('DEBUG')


ALLOWED_HOSTS = [env('ALLOWED_HOSTS', '')]

# Application definition

INSTALLED_APPS = (
    # Default
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Added tools
    'easy_pjax',
    'tastypie',
    'tastycrust',
    'channels',
    # Self made
    'address',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'towan.urls'

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

WSGI_APPLICATION = 'towan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME','postgres'),
        'USER': env('DB_USER','postgres'),
        'PASSWORD': env('DB_PASSWORD','postgres'),
        'HOST': env('DB_HOST','localhost'),
        'PORT': 5432,

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

# tastypie
TASTYPIE_DEFAULT_FORMATS = ['json']

# channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "towan.routing.routing",
    },
}
