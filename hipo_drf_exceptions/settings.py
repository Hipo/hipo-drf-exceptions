from django.conf import settings

HIPO_DRF_SETTINGS = getattr(settings, "HIPO_DRF_SETTINGS", {})

SERVER_ERROR_FALLBACK_MESSAGE = HIPO_DRF_SETTINGS.get(
    "SERVER_ERROR_FALLBACK_MESSAGE",
    _('Our servers are unreachable at the moment. Please try again a few minutes later.')
)
