from django.core.urlresolvers import reverse
from django.template.defaulttags import register
from apps.wisys.models import SettingsLogo


@register.simple_tag
def active(request, urlName):
    url = reverse(urlName)
    if url == request.path:
        return 'active'
    return ''

@register.simple_tag
def logo_url():

    LOGO_IMAGE_URL = 'images/default/logo.png'
    try:
        logoData = SettingsLogo.objects.get(pk=1)
        LOGO_IMAGE_URL = logoData.logo_image

    except Exception,ex:
        pass

    return LOGO_IMAGE_URL

@register.filter(name='split')
def split(value, seperator):
    return value.split(seperator)


from random import randint

@register.simple_tag()
def random_number(start, end ):
    """
    Create a random integer with given length.
    For a length of 3 it will be between 100 and 999.
    For a length of 4 it will be between 1000 and 9999.
    """
    return randint(start, end)