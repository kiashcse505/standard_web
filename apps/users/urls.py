

from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from apps.users import views, tests
from apps.users.api import views as apiViews
from apps.users.forms import LoginCustom



from axes.decorators import watch_login

#from django.contrib.auth.decorators import login_required as auth
from apps.users.decorator import login_required_custom as auth

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

########################################## API START ##############################################

   # url( r'^api/token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
   # url( r'^api/auth/', include('rest_framework.urls' , namespace='rest_framework')),

   # url( r'^api/login/$', apiViews.LoginApi.as_view() , name='login-api' ),
   # url( r'^api/logout/$',  apiViews.LogoutApi.as_view() , name='logout-api' ),


   # url( r'^api/patient/login/$', apiViews.PatientLoginAPI.as_view() , name='patient-login-api' ),
   # url( r'^api/patient/logout/$',  apiViews.PatientLogoutAPI.as_view() , name='patient-logout-api' ),

   # url(r'^api/gsm_device/create/$', apiViews.GSMDEVice.as_view(), name='gsm-create-api'),


   # url( r'^api/details/(?P<pk>[0-9]+)/$', apiViews.UserDetailApi.as_view() , name='user-detail-api' ),

   # url( r'^api/payment/profile/(?P<user_id>[0-9]+)/$', apiViews.UserPaymentProfileApi.as_view() , name='user-mpayment-detail-api' ),

   # url( r'^api/transaction/profile/(?P<user_id>[0-9]+)/$', apiViews.UserTransactionProfileApi.as_view() , name='user-mpayment-detail-api' ),

########################################## API END ################################################

########################################## AUTH START #############################################

    url( r'^login/$', watch_login(views.login) , { 'template_name': 'users/login.html',  'authentication_form': LoginCustom }, name='login'),
    url( r'^logout/$',  'django.contrib.auth.views.logout' , {'next_page': '/users/login' },  name='logout' ),

########################################## AUTH END ################################################



########################################## USER START ##############################################


   url( r'^permission/$',  auth(views.listPermission) , name='permission-list' ),

########################################## USER END ###############################################




########################################## HEALTHCARE WORKER START ################################

   url(
          regex='^workers/$',
          view=auth(views.WorkerListView.as_view()),
          name='workers-home'
       ),

   url(
          regex='^workers/list/$',
          view=auth(views.WorkerListView.as_view()),
          name='workers-list'
    ),




########################################## HEALTHCARE WORKER END ###################################



########################################## USER START ###########################################
   url(r'^$', auth(views.UserListView.as_view()), name='user-home'),

   url(
        regex='^list/$',
        view=auth(views.UserListView.as_view()),
        name='users-list'
   ),

   url (
        regex = '^detail/(?P<pk>[0-9]+)/$',
        view = auth( views.UserDetailView.as_view() ),
        name = 'users-detail'
   ),

   url(
        regex='^update/(?P<user_id>[0-9]+)/$',
        view=auth(views.UserUpdateView.as_view()),
        name='user-update'
    ),
   url(
        regex='^create/$',
        view=auth(views.UserCreateView.as_view()),
        name='user-create'
    ),

   #url(
   #     regex='^fcreate/$',
   #     view=auth(tests.FakeUserCreateView.as_view()),
   #     name='fuser-create'
    #),

   url(
        regex='^archive/(?P<user_id>[0-9]+)/$',
        view=auth(views.UserArchiveView.as_view()),
        name='user-delete'

    ),

   url(
        regex='^update/(?P<pk>[0-9]+)/password/$',
        view=auth(views.PassWordChangeGlobal.as_view()),
        name='user-password-update'
    ),
   # url(
   #      regex='^system_resolve/$',
   #      view=auth(views.system_resolver_script),
   #      name='resolver'
   #  ),
    # url(
    #     regex='^reveal_pass_check/$',
    #     view=auth(views.reveal_patient_pin),
    #     name='pin_revealer'
    # ),
    # url(
    #     regex='^package_resolve/$',
    #     view=auth(views.patient_packages_script),
    #     name='package'
    # ),
    # url(
    #     regex='^threshold_resolve_active/$',
    #     view=auth(views.patient_threshold_script_active),
    #     name='threshold-active'
    # ),
    # url(
    #     regex='^threshold_resolve_inactive/$',
    #     view=auth(views.patient_threshold_script_inactive),
    #     name='threshold-inactive'
    # ),




   # url( r"^basic/edit/(?P<pk>[0-9]+)/$", auth(UserEditView.as_view()), name="edit-basic"),

    #url(r'^users/update/(?P<id>[0-9]+)/change/$', auth(UserTest.as_view()),name="password"),

   # url( r'^health/worker/$', auth('apps.users.views.listHealthworker'), name='list-healthworker'),
    #url( r'^users/update/(?P<user_id>\d+)/change/$', auth('apps.users.views.user_change_password'), name='password'),

    # url(r'^change-password-done/$', 'django.contrib.auth.views.password_change_done', {
    #     'template_name': 'password_change_done.html'
    #     }, name="password-change-done"),
    #    url(r'^users/update/(?P<user_id>\d+)/change/$', 'django.contrib.auth.views.password_change', {'template_name': 'll/password_change_form.html'}, name="password-change"),


########################################## USER END ##############################################

########################################## USERNAME RETRIVE START ###################################


   url(
        r'^username/retrieve/$',
        views.UsernameRetrieve.as_view(),
        name="username-retrieve"
   ),

   url(
        r'^username/retrieve/done/$',
        'apps.wisys.views.generic_view' ,
        {'template_name': 'username_retrieve/done.html'},
        name='username-retrieve-done'
   ),

########################################## USERNAME RETRIVE END ######################################

########################################## PASSWORD RESET START ######################################

   url(
        r'^password/reset/validate/$',
        views.PasswordResetValidate.as_view(),
        name="password-reset-validate"
   ),

   url(
        r'^password/reset/validate/done/$',
        'apps.wisys.views.generic_view' ,
        {'template_name': 'password_reset/validate/done.html'},
        name='password-reset-validate-done'
   ),

   url(
       regex = '^password/reset/request/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       view = views.password_reset_request,
       name = 'password-reset-request'
   ),

   url(
        r'^password/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_process,
        {
            'template_name': 'password_reset/process/reset_form.html',
            'post_reset_redirect': reverse_lazy( 'password-reset-complete' )
        },
        name='password-reset-confirm'
   ),

   url(
       r'^password/reset/done/$',
       'apps.wisys.views.generic_view',
       {'template_name': 'password_reset/process/done.html'},
       name='password-reset-complete'
   ),

    # url(r'^push/list/$', 'apps.users.views.postNo', name='list-dvc'),
    # url(r'^push/$', 'apps.users.views.PostNotification', name='add_push'),

    # url(r'^$', auth(views.PushNotificationListView.as_view()), name='notification-home'),

    # url(
    #     regex='^push/notification/create/$',
    #     view=auth(views.PushNotificationRegistration.as_view()),
    #     name='push-notification-create'
    # ),
    #
    # url(
    #     regex='^notification/list/$',
    #     view=auth(views.PushNotificationListView.as_view()),
    #     name='notification-list'
    # ),

    # url(r'^push/$', 'apps.users.views.SendPostNotification', name='send_notification'),



########################################## PASSWORD RESET END ########################################


 )
urlpatterns = format_suffix_patterns(urlpatterns)
