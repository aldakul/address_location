from django.contrib.auth.models import Permission
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from locations.models import City
from locations.api.v1.serializers.city import CitySerializer


class CityViewSet(ListModelMixin, GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
