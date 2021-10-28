import datetime
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from locations.models import Country

logger = logging.getLogger(__name__)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            '__all__'
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }
