from django.utils.translation import ugettext as _

from hipo_drf_exceptions import BaseAPIException


class InvalidTitleError(BaseAPIException):
    default_detail = _('Invalid title')
