from django.conf import settings
from rest_framework import serializers


class IRBaseModelSerializer(serializers.ModelSerializer):

    friendly_fields = ()
    _default_friendly_fields = ( 'status' )

    def __init__(self, *args, **kwargs ):
        parent = super( IRBaseModelSerializer, self )
        parent.__init__(*args, **kwargs);




