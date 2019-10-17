from django.core.exceptions import ValidationError
from django.http import Http404
from django.utils.translation import ugettext as _

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import exception_handler


def get_fallback_message(exception):
    if isinstance(exception, str):
        return exception.capitalize()
    elif isinstance(exception, list):
        return get_fallback_message(exception[0])
    elif isinstance(exception, dict):
        # A dictionary can be empty. https://github.com/Hipo/hipo-drf-exceptions/issues/8
        if exception == {}:
            return get_fallback_message("")
        else:
            first_key = next(iter(exception))
        return get_fallback_message(exception[first_key])
    elif isinstance(exception, Exception):
        if hasattr(exception, "detail"):
            return get_fallback_message(exception.detail)

    return exception.__str__()


def handler(exc, context):
    # It's a django validation error?
    if isinstance(exc, ValidationError):
        try:
            detail = exc.message_dict
        except AttributeError:
            detail = {
                api_settings.NON_FIELD_ERRORS_KEY: exc.messages
            }

        data = {
            'type': exc.__class__.__name__,
            'detail': detail,
            'fallback_message': get_fallback_message(exc)
        }
        response = Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:  # API Exception.
        response = exception_handler(exc, context)

        if response is not None:
            if isinstance(exc, Http404):
                detail = _("Not Found.")
            else:
                detail = exc.detail

            if not isinstance(detail, dict):
                # It must be list of errors.
                if not isinstance(detail, list):
                    detail = [detail]

                detail = {
                    api_settings.NON_FIELD_ERRORS_KEY: detail
                }

            response.data = {
                'type': exc.__class__.__name__,
                'detail': detail,
                'fallback_message': get_fallback_message(exc)
            }

    return response
