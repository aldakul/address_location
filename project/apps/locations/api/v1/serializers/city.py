import datetime
import logging

from rest_framework import serializers

from locations.models import City

logger = logging.getLogger(__name__)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            '__all__'
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }
