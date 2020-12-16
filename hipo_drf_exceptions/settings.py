from django.conf import settings

from rest_framework.settings import api_settings

HIPO_DRF_EXCEPTIONS_SETTINGS = getattr(settings, "HIPO_DRF_EXCEPTIONS_SETTINGS", {})

# Defaults
HIPO_DRF_EXCEPTIONS_SETTINGS.setdefault("DJANGO_NON_FIELD_ERRORS_KEY", api_settings.NON_FIELD_ERRORS_KEY)
