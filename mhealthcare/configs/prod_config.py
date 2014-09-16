DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mhealthcarev2',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dev',
        'PASSWORD': 'g0ldyl0ck$',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# SITE_URL_BASE = '/mhealth'
# HOME_URL = SITE_URL_BASE + '/alerts/list'
#
# MEDIA_URL = SITE_URL_BASE + '/media/'
# STATIC_URL = SITE_URL_BASE + '/static/'
#
# LOGIN_REDIRECT_URL = HOME_URL
#
# DAJAXICE_MEDIA_PREFIX = "mhealth/dajaxice"
# DAJAXICE_DEBUG = True




#############  celery settings ###############

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

