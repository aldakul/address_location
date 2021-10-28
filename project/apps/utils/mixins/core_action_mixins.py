import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from utils.utils import send_get


logger = logging.getLogger(__name__)


class CoreActionMatchingViewMixin:
    core_action = None

    def get(self, request, *args, **kwargs):
        try:
            url = settings.CORE_BASE_URL + self.core_action.value
            headers = {'Authorization': f'Bearer {request.META.get("HTTP_AUTHORIZATION", None).split().pop()}'}
            if hasattr(self, 'lookup_field') and self.lookup_field:
                url += f'{kwargs.get(self.lookup_field)}/'
            response = send_get(url, headers=headers)
            return Response(response.json())
        except Exception as e:
            error_info = f'{e.__class__.__name__}: {str(e)}'
            logger.error(error_info)
            return Response({'error': error_info}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
