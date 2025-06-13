import os
from.settings import *
import dj_database_url
from settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'django-backend-code.onrender.com')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('WEBSITE_HOSTNAME', 'django-backend-code.onrender.com')]

DEBUG=False
SECRET_KEY = os.environ.get('MY_SECRET_KEY', 'fallback-secret-key')
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout'
]
CORS_ALLOWED_ORIGINS = [
    "https://employe-management-sysytem.onrender.com",
    "https://django-backend-code.onrender.com"
]

STORAGES={'default': 
          {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
          
           'staticfiles':
             {'BACKEND': "whitenoise.storage.CompressedStaticFilesStorage"},
               }
# DATABASES = {
#    'default': {
#        'ENGINE': dj_database_url.config(
#            default=os.environ['DATABASE_URL'],
#            conn_max_age=600

#        )
       
#    }
# } 
DATABASES = {
   'default': dj_database_url.config(
       default=os.environ.get('DATABASE_URL'),
       conn_max_age=600
   )
}
