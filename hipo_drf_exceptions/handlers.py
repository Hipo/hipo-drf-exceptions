from django.core.exceptions import ValidationError
from django.http import Http404
from django.utils.translation import ugettext as _

from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import exception_handler


def handler(exc, context):
    def get_automated_fallback_message(name_of_field, error_message):
        return "'{field_name}' has an error. {error_message}".format(
            field_name=name_of_field.capitalize(),
            error_message=error_message,
        )

    # It's a django validation error?
    if isinstance(exc, ValidationError):
        try:
            detail = exc.message_dict
            field_name = next(iter(detail))
            fallback_message = get_automated_fallback_message(field_name, detail[field_name][0])
        except AttributeError:
            detail = {
                api_settings.NON_FIELD_ERRORS_KEY: exc.messages
            }
            fallback_message = exc.messages[0]

        data = {
            'type': exc.__class__.__name__,
            'detail': detail,
            'fallback_message': fallback_message
        }
        response = Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:  # API Exception.
        response = exception_handler(exc, context)

        if response is not None:
            if isinstance(exc, Http404):
                detail = _("Not Found.")
                fallback_message = detail
            else:
                detail = exc.detail
                try:
                    field_name = next(iter(detail))
                    fallback_message = get_automated_fallback_message(field_name, detail[field_name][0])
                except TypeError:
                    fallback_message = detail.capitalize()

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
                'fallback_message': fallback_message
            }

    return response
