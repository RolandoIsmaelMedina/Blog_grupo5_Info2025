from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6qn40^&hd!63g3a8y(^mzy3ou$0wj$q%$j_+7=fkspa4ux8yg@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': 
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog_dbok',
            'USER': 'root',
            'PASSWORD': 'rmedina',
            'HOST': 'localhost',
            'PORT': '3306',
        }
}