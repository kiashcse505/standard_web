
from django.conf.urls import patterns, url
from apps.wisys import views

#from django.contrib.auth.decorators import login_required as auth
from apps.users.decorator import login_required_custom as auth

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(
        regex='^settings/$',
        view=auth(views.SettingsView.as_view()),
        name='system-settings'
    ),
    url(
        regex='^settings/site-name/(?P<pk>[0-9]+)/$',
        view=auth(views.SitenameView.as_view()),
        name='settings-site'
    ),
   url(r'^settings/list/$', auth(views.DomainListView.as_view()), name='domain-list'),

   url(
        regex='^setting/list/$',
        view=auth(views.DomainListView.as_view()),
        name='domain-list'
   ),

 )