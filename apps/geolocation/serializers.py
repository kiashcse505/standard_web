from django.conf import settings
from rest_framework import serializers, pagination
from apps.geolocation.models import District,Division,Region, Country

#
# class CitySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = City


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District


# class UnionSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Union
# untry,
#
# class UpazilaSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Upazila
#
#
# class MunicipalitySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Municipality
#
#
# class MetropolitanCitySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MetropolitanCity
#
# class WardSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Ward
#
#
# class VillageSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Village
#
# class CityCorporationSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CityCorporation