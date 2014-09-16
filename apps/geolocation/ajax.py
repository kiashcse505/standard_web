from apps.geolocation.models import Country,Division,District,Region, Ethnicity
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register



@dajaxice_register
def changeCountry( request, country_id ):
    if  country_id == 2 :
        return updateRegion(request, 201)
    elif country_id == 1:
        return updateDivision(request, country_id)
    elif country_id == 3:
        return updateRegion(request, 301)
    elif country_id == 3:
        return updateEthnicity(request)


@dajaxice_register
def updateEthnicity(request, country_id):
    dajax = Dajax()
    ethnicities = Ethnicity.objects.filter(country__id=country_id)

    ethnicityOptionHtmls = []
    for aEthnicity in ethnicities:
        ethnicityOptionHtmls.append("<option value='%s'>%s</option>" % (aEthnicity.id, aEthnicity.name ) );

    dajax.assign('#id_ethnicity','innerHTML', ''.join(ethnicityOptionHtmls) )

    return dajax.json()

@dajaxice_register
def updateDivision(request, country_id):
    dajax = Dajax()
    divisions = Division.objects.filter(country__id=country_id)

    divisionOptionHtmls = []
    for aDivision in divisions:
        divisionOptionHtmls.append("<option value='%s'>%s</option>" % (aDivision.id, aDivision.name ) );

    dajax.assign('#id_division','innerHTML', ''.join(divisionOptionHtmls) )

    return dajax.json()


@dajaxice_register
def updateDistrict(request, division_id):
    dajax = Dajax()
    districts = District.objects.filter(division__id=division_id)

    districtOptionHtmls = []
    for aDistrict in districts:
        districtOptionHtmls.append("<option value='%s'>%s</option>" % (aDistrict.id, aDistrict.name ) );

    dajax.assign('#id_district','innerHTML', ''.join(districtOptionHtmls) )

    return dajax.json()


@dajaxice_register
def updateRegion(request, district_id):
    dajax = Dajax()
    regions = Region.objects.filter(district__id=district_id)
    print district_id

    regionsOptionHtmls = []
    for aRegion in regions:
        regionsOptionHtmls.append("<option value='%s'>%s</option>" % (aRegion.id, aRegion.name) );

    dajax.assign('#id_region','innerHTML', ''.join(regionsOptionHtmls) )
    return dajax.json()

