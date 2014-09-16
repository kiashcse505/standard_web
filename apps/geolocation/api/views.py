from apps.geolocation.models import (
    Country,Division,District,Region,
    )
from apps.geolocation.serializers import (
    CountrySerializer,DistrictSerializer,DivisionSerializer,RegionSerializer
)
from rest_framework import generics, filters
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.wisys.api.views import IrBaseAPIView


class CountryListView(generics.ListCreateAPIView, IrBaseAPIView):
    """All Country List"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    paginate_by = 100
    filter_fields = ('code', )




# class CityListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """"All City List"""
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#     paginate_by = 100
#     filter_fields = ('district','code','slug', )
#
#


class DivisionListView(generics.ListCreateAPIView, IrBaseAPIView ):
    """All Division List"""
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    paginate_by = 100
    filter_fields = ('country','code','slug', )



class DistrictListView(generics.ListCreateAPIView, IrBaseAPIView ):
    """All District List"""
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    paginate_by = 100
    filter_fields = ('division','code','slug', )




class RegionListView(generics.ListCreateAPIView, IrBaseAPIView ):
    """All Region List"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    paginate_by = 100
    filter_fields = ('district','name','slug', )



# class UnionListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """All Union List"""
#     queryset = Union.objects.all()
#     serializer_class = UnionSerializer
#     paginate_by = 100
#     filter_fields = ('upazila','name','slug', )




# class UpazilaListView(generics.ListCreateAPIView, IrBaseAPIView):
#     """All Upazila List"""
#     queryset = Upazila.objects.all()
#     serializer_class = UpazilaSerializer
#     paginate_by = 100
#     filter_fields = ('district','name','slug', )



# class MunicipalityListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """All Municipality List"""
#     queryset = Municipality.objects.all()
#     serializer_class = MunicipalitySerializer
#     paginate_by = 100
#     filter_fields = ('ward','name','slug', )
#
#
# class MetropolitanCityListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """All MetropolitanCity List"""
#     queryset = MetropolitanCity.objects.all()
#     serializer_class = MetropolitanCitySerializer
#     paginate_by = 100
#     filter_fields = ('district','name','slug', )
#
#
#
# class WardListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """All WARD List"""
#     queryset = Ward.objects.all()
#     serializer_class = WardSerializer
#     paginate_by = 100
#     filter_fields = ('union','name','slug', )
#
#
#
#
# class VillageListView(generics.ListCreateAPIView, IrBaseAPIView ):
#     """
#     Retrieve  Village List
#     """
#     queryset = Village.objects.all()
#     serializer_class = VillageSerializer
#     paginate_by = 100
#     filter_fields = ('municipality','name','slug', )
#
#
#
#
# class CityCorporationListView(generics.ListCreateAPIView, IrBaseAPIView):
#     """All CityCorporation List"""
#     queryset = CityCorporation.objects.all()
#     serializer_class = CityCorporationSerializer
#     paginate_by = 100
#     filter_fields = ('metropolitan_city','name','slug', )
#
