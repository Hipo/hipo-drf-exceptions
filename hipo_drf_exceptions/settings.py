from django.conf import settings as django_settings
from django.utils.translation import gettext_lazy as _

HIPO_DRF_EXCEPTIONS_SETTINGS = getattr(django_settings, "HIPO_DRF_EXCEPTIONS_SETTINGS", {})

INTERNAL_SERVER_ERROR_FALLBACK_MESSAGE = HIPO_DRF_EXCEPTIONS_SETTINGS.get(
    "INTERNAL_SERVER_ERROR_FALLBACK_MESSAGE",
    _('Our servers are unreachable at the moment. Please try again a few minutes later.')
)
