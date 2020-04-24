from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from hipo_drf_exceptions import settings


class BaseAPIException(APIException):
    status_code = HTTP_400_BAD_REQUEST


class InternalServerError(APIException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = settings.INTERNAL_SERVER_ERROR_FALLBACK_MESSAGE
