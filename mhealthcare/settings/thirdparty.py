
################################ SESSION SECURITY ################################################

# SESSION_SECURITY_EXPIRE_AFTER = 600
# SESSION_SECURITY_WARN_AFTER = 300

SESSION_SECURITY_EXPIRE_AFTER=600
SESSION_SECURITY_WARN_AFTER=300

################################## DEBUG_TOOLBAR  ################################################

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

###################################### AXES ################################################

AXES_LOGIN_FAILURE_LIMIT = 10;
AXES_LOCKOUT_TEMPLATE = "users/lockout.html";

###################################### SWAGGER ################################################


SWAGGER_SETTINGS = {
    "exclude_namespaces": [], # List URL namespaces to ignore
    "api_version": '0.1', # Specify your API's version
    "api_path": "/", # Specify the path to your API not a root level
    "enabled_methods": [# Specify which methods to enable in Swagger UI
                        'get',
                        'post',
                        'put',
                        'patch',
                        'delete'
    ],
    "api_key": '', # An API key
    "is_authenticated": False, # Set to True to enforce user authentication,
    "is_superuser": True, # Set to True to enforce admin only access
}

######################################## BOWER ################################################

from mhealthcare.settings import PROJECT_ROOT

BOWER_COMPONENTS_ROOT = PROJECT_ROOT
BOWER_INSTALLED_APPS = (
    'bootstrap#2.3.2',
    'jquery#1.9.1',
    'bootstrap-datetimepicker',
    'datatables',
    'noty',
    'zoomooz',
    'highcharts',
    'bootstrap-tagsinput',
    'select2',
    'jasny-bootstrap',
    'jquery.cookie',
    'Avgrund',
    'multiple-select',
    'jquery.validation',
    'https://github.com/davetayls/jquery.kinetic.git',
    'https://github.com/ibrahim12/jquery-powertip.git#release',
    #'https://github.com/ibrahim12/Messi.git',
    'https://github.com/milu-buet/Messi.git',
    'https://github.com/atkinson/jquery-django-messages.git',
    'https://github.com/vitalets/x-editable.git#1.5.0',
    'https://github.com/nostalgiaz/bootstrap-switch.git#2.0.1',
    'https://github.com/pivotal-energy-solutions/django-datatable-view.git',

)


######################################## REST FRAMEWORK ################################################

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',

    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ),

    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    'DEFAULT_FILTER_BACKENDS':
        ('rest_framework.filters.DjangoFilterBackend',),



    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],

    'PAGINATE_BY': 5, # Default to 10
    'PAGINATE_BY_PARAM': 'page_size', # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100 # Maximum limit allowed when using `?page_size=xxx`.
}

######################################## DAJAXICE ########################################################

DAJAXICE_MEDIA_PREFIX = "dajaxice"


######################################## PUSH NOTIFICATION ################################################

PUSH_NOTIFICATIONS_SETTINGS = {
        "GCM_API_KEY": "AIzaSyBU1SZMfCMa8bgSXKdpGp0O4fmcLgnVFl0",
        # "APNS_CERTIFICATE": "/path/to/your/certificate.pem",
        # "GCM_POST_URL": "https://android.googleapis.com/gcm/send",
}

######################################## TRANSMETA ################################################

TRANSMETA_DEFAULT_LANGUAGE = 'en'



####################################### Django Celery ##############################################

######################   HAYSTACT    ###################################
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}




############################################################################

# import djcelery
# djcelery.setup_loader()


# #TIME_ZONE = 'UTC'
# #USE_TZ = True
# CELERY_ENABLE_UTC = False
# #CELERY_TIMEZONE = 'Australia/Sydney'
# CELERYD_TASK_TIME_LIMIT = 300


#BROKER_HOST = "localhost"
#BROKER_PORT = 5672
#BROKER_USER = "root"
#BROKER_PASSWORD = "root"
#BROKER_VHOST = "myhost"



#BROKER_URL = 'amqp://root:root@mhealth_host:5672//'
#BROKER_URL = 'amqp://root:root@localhost:5672//'

#BROKER_URL = 'amqp://mhealth:mhealth123@localhost:5672//'
#BROKER_URL = 'amqp://guest:guest@localhost:5672//'


#CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"


########################################## Django Simple Audit ######################################

DJANGO_SIMPLE_AUDIT_ACTIVATED = True
