from django.core.urlresolvers import reverse_lazy

PROJECT_NAME = 'mhealthcare'
PROJECT_APP_NAME = 'mhealthcare'

PROJECT_NAMES = {
    'SDWP': 'Standard Djano Web Portal',
    'PRMS': 'Patient Record Management System'
}

ADMINS = (
    ('kiash', 'kiash.wisys@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Asia/Dhaka'

######################################## LANGUAGE ################################################

LANGUAGE_CODE = 'en-us'

USE_I18N = False

USE_L10N = False

USE_TZ = False


SECRET_KEY = '=xjr+70(^1l71^%5lyf*#l0g!mb@^q(9gtk-*0lg@@_7z+5p+q'

WSGI_APPLICATION = 'mhealthcare.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

TEST_RUNNER = 'apps.wisys.testing.DatabaselessTestRunner'

LANGUAGES = (
    ('en', 'English'),
    ('bn', 'Bangla')
)


DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d', '%m-%d-%Y')

AUTH_PROFILE_MODULE = 'users.Profile'
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

#DEBUG

INTERNAL_IPS = ('127.0.0.1',)


ADMINS = (
    ('Yourname', 'kiash.wisys@gmail.com'),
)

MANAGERS = ADMINS

# For Custom url after registration.
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('edit-profile'),
}
