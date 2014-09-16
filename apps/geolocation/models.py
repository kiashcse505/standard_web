from django.db import models
from json_field import JSONField


########## Constants ##############

APP_NAME = 'geolocation'

########## Helpers ##############


########## Models ##############

###################### Country ######################


############## Base ##############


class BaseGeoModel(models.Model):

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=255,unique=True)

    extra = JSONField(default="{}",blank=True)

    def __unicode__(self):
        return " %s " % self.name

    class Meta:
        abstract = True

############## Country ##############

class Country(BaseGeoModel):
    lat = models.FloatField(blank=True,default=0.0)
    lang = models.FloatField(blank=True,default=0.0)

    ############## Division ##############

class Division(BaseGeoModel):
    country = models.ForeignKey('Country', related_name='division_countries')

        ############## District ##############
class District(BaseGeoModel):
    division = models.ForeignKey('Division', related_name='district_divisions')

#             ############## City ##############
# class City(BaseGeoModel):
#     district = models.ForeignKey('District', related_name='city_districts')

            ############## Region ##############
class Region(BaseGeoModel):
    district = models.ForeignKey('District', related_name='region_districts')


class Ethnicity(BaseGeoModel):
    country = models.ForeignKey('Country', related_name='ethnicity_country')

#             ############## Upazila ##############
# class Upazila(BaseGeoModel):
#     district = models.ForeignKey('District', related_name='upazila_districts')
#
#                 ############## Union ##############
# class Union(BaseGeoModel):
#     upazila = models.ForeignKey('District', related_name='union_upazilas')
#
#                     ############## Ward ##############
# class Ward(BaseGeoModel):
#     union = models.ForeignKey('District', related_name='ward_unions')
#
#                         ############## Municipality ##############
# class Municipality(BaseGeoModel):
#     ward = models.ForeignKey('Ward', related_name='municipality_wards')
#
#                             ############## Village ##############
# class Village(BaseGeoModel):
#     ward = models.ForeignKey('District', related_name='village_wards')
#
#
#         ############## MetropolitanCity ##############
# class MetropolitanCity(BaseGeoModel):
#     division = models.ForeignKey('Division', related_name='metropolitan_city_divisions')
#
#     class Meta:
#         db_table = '%s_%s' % ( APP_NAME, 'metropolitan_city')
#
#             ############## CityCorporation ##############
# class CityCorporation(BaseGeoModel):
#     metropolitan_city = models.ForeignKey('MetropolitanCity', related_name='city_corporation_metropolitan_cities')
#
#     class Meta:
#         db_table = '%s_%s' % ( APP_NAME, 'city_corporation')











