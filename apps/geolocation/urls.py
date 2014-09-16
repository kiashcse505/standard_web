import django.views.defaults
from apps.geolocation.models import Country,Division,District,Region
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views

urlpatterns = patterns('',

    url(r'api/countries/$', views.CountryListView.as_view(), name='country-list-api'),
    url(r'api/districts/$', views.DistrictListView.as_view(), name='district-list-api'),
    url(r'api/divisions/$', views.DivisionListView.as_view(), name='division-list-api'),
    url(r'api/regions/$', views.RegionListView.as_view(), name='region-list-api'),

    # url(r'api/cities/$', views.CityListView.as_view(), name='city-list-api'),
    # url(r'api/upazilas/$', views.UpazilaListView.as_view(), name='upazila-list-api'),
    # url(r'api/unions/$', views.UnionListView.as_view(), name='union-list-api'),
    # url(r'api/wards/$', views.WardListView.as_view(), name='ward-list-api'),
    # url(r'api/municipalities/$', views.MunicipalityListView.as_view(), name='municipality-list-api'),
    # url(r'api/villages/$', views.VillageListView.as_view(), name='village-list-api'),
    # url(r'api/metropolitan_cities/$', views.MetropolitanCityListView.as_view(), name='metropolitan-city-list-api'),
    # url(r'api/city_corporations/$', views.CityCorporationListView.as_view(), name='city-corporation-list-api'),


)

urlpatterns = format_suffix_patterns(urlpatterns)



