from django.template.defaulttags import register


@register.filter
def getitem ( item, key ):
    if key in item:
        return item[key]
    return False
