
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

)

THIRD_PARTY_APPS = (
    'django_admin_bootstrapped',

    'djangojs',
    'dajaxice',
    'dajax',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'rest_framework_docs',

    'djangobower',
    'django_filters',
    'json_field',
    'autofixture',
    'south',
    'mockups',


    'debug_toolbar',

    'django_like',

    'session_security',

    'datatableview',
    'bootstrap-pagination',

    'django_select2',
    'axes',

    # 'push_notifications',
    'smart_selects',


    "django_countries",
    #"postal",

    # "celery",
    # "djcelery",
    'bootstrap3_datetime',

    "simple_audit",
    #'import_export',
    #'haystack',


)

LOCAL_APPS = (

    'apps.wisys',
    'apps.geolocation',
    'apps.users',
    #'sphinxdoc',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS  + LOCAL_APPS