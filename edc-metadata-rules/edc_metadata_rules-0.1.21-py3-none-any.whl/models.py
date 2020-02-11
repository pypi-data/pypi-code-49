from django.conf import settings

if settings.APP_NAME == "edc_metadata_rules":
    from .tests import models
