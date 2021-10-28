from rest_framework.routers import DefaultRouter

from locations.api.v1.views.country import CountryViewSet

router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = []

urlpatterns += router.urls
