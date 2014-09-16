from django.contrib import admin
from apps.geolocation.models import Country,District,Region,Division

# class CityAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(City, CityAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)

class DivisionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Division, DivisionAdmin)

class DistrictAdmin(admin.ModelAdmin):
    pass

admin.site.register(District, DistrictAdmin)


class RegionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Region, RegionAdmin)