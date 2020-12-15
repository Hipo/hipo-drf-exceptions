from django.conf import settings

HIPO_DRF_EXCEPTIONS_SETTINGS = getattr(settings, "HIPO_DRF_EXCEPTIONS_SETTINGS", {})

# Defaults
HIPO_DRF_EXCEPTIONS_SETTINGS.setdefault("DJANGO_NON_FIELD_ERRORS_KEY", "non_field_errors")
