from rest_framework.routers import DefaultRouter

from locations.api.v1.views.country import CountryViewSet
from locations.api.v1.views.city import CityViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)

urlpatterns = []

urlpatterns += router.urls
