from dajaxice.core import dajaxice_config

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView



# Uncomment the next two lines to enable the admin:
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^js/', include('djangojs.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'session_security/', include('session_security.urls')),
    #url(r'^docs/', include('sphinxdoc.urls')),

    # url(r'^%s%s/' % (settings.SITE_URL_BASE, settings.DAJAXICE_MEDIA_PREFIX) , include('dajaxice.urls')),

    url(  dajaxice_config.dajaxice_url , include('dajaxice.urls')),

    url(r'^$', RedirectView.as_view(url='/users/list', permanent=False), name='home' ),

    url(r'^users/', include('apps.wisys.urls')), # Check This
    url(r'^users/', include('apps.users.urls')),

    url(r'^geolocation/', include('apps.geolocation.urls')),
    url(r'^api/$', 'mhealthcare.views.api_root'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-api/', include('rest_framework_docs.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



