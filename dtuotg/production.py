from .settings import *
import os
import pyodbc

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = True

# WhiteNoise configuration
MIDDLEWARE = [                                                                   
    'django.middleware.security.SecurityMiddleware',
# Add whitenoise middleware after the security middleware                             
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',                      
    'django.middleware.common.CommonMiddleware',                                 
    'django.middleware.csrf.CsrfViewMiddleware',                                 
    'django.contrib.auth.middleware.AuthenticationMiddleware',                   
    'django.contrib.messages.middleware.MessageMiddleware',                      
    'django.middleware.clickjacking.XFrameOptionsMiddleware',                    
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# DBHOST is only the server name, not the full URL
hostname = os.environ['DBHOST']

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + '.database.windows.net',
        'USER': os.environ['DBUSER'] + '@' + hostname,
        'PASSWORD': os.environ['DBPASS'],
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        }
    }
}

LOGGING = {
 'version': 1,
 'disable_existing_loggers': False,
 'filters': {
 'require_debug_false': {
 '()': 'django.utils.log.RequireDebugFalse'
 }
 },
 'handlers': {
 'logfile': {
 'class': 'logging.handlers.WatchedFileHandler',
 'filename': 'D:\home\site\wwwroot\myapp.log'
 }
 },
 'loggers': {
 'django': {
 'handlers': ['logfile'],
 'level': 'ERROR',
 'propagate': False,
 }
 }
 }
