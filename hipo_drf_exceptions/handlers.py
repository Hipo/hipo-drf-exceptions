from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.http import Http404
from django.utils.translation import ugettext as _

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import exception_handler

from .settings import HIPO_DRF_EXCEPTIONS_SETTINGS


def get_human_readable_concatenation_of(key, value):
    # "first_name", "This is required." -> "First Name: This is required."
    human_readable_key = " ".join(key.split("_")).title()
    value = f"{human_readable_key}: {value.capitalize()}"
    return value


def get_fallback_message(exception):
    if isinstance(exception, str):
        return exception
    elif isinstance(exception, list):
        for item in exception:
            if item:
                # Return first non-empty value in the list. https://github.com/Hipo/hipo-drf-exceptions/issues/8
                return get_fallback_message(item)
    elif isinstance(exception, dict):
        first_key = next(iter(exception))
        message = exception[first_key]

        # message: {"field": ["error message"]}
        if isinstance(message, list) and len(message) > 0 and isinstance(message[0], str):
            message = get_human_readable_concatenation_of(first_key, message[0])
        # message: {"field": "error message"}
        elif isinstance(message, str):
            message = get_human_readable_concatenation_of(first_key, message)

        return get_fallback_message(message)
    elif isinstance(exception, Exception):
        if hasattr(exception, "detail"):
            return get_fallback_message(exception.detail)
        elif hasattr(exception, "message"):
            # Handle Django ValidationError message attribute
            return get_fallback_message(exception.message)
        elif hasattr(exception, "message_dict"):
            return get_fallback_message(exception.message_dict)

    return exception.__str__()


def handler(exc, context):
    # It's a django validation error?
    if isinstance(exc, ValidationError):
        try:
            # Convert Django's non field errors with "__all__" key
            # to DRF's non field errors with "non_field_errors" key.
            django_non_field_errors = exc.error_dict.pop(NON_FIELD_ERRORS, None)
            if django_non_field_errors:
                exc.error_dict[HIPO_DRF_EXCEPTIONS_SETTINGS["DJANGO_NON_FIELD_ERRORS_KEY"]] = django_non_field_errors

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
