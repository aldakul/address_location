from rest_framework.exceptions import APIException


class NotAuthorized(APIException):
    status_code = 401
    default_detail = 'Authorization required.'
    default_code = 'forbidden'


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
