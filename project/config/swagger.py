from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
            openapi.Info(
                title="ADDRESS API",
                default_version='v1',
                description="Written by MyCar.pro",
                terms_of_service="https://www.google.com/policies/terms/",
                contact=openapi.Contact(email="admin@mycar.kz"),
            ),
            public=True,
            permission_classes=(permissions.AllowAny,),
)


swagger_patterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='api.docs.swagger'),
    path(r'<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
