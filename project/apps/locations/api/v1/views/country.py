from django.contrib.auth.models import Permission
from rest_framework import filters
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from locations.api.v1.serializers.country import CountrySerializer


class CountryViewSet(ListModelMixin, GenericViewSet):
    queryset = Permission.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$id', '$name_ru', 'name_kz']
