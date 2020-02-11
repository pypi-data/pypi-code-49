import sys

from django.apps.config import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style

from .site import site_metadata_rules


style = color_style()


class AppConfig(DjangoAppConfig):
    name = "edc_metadata_rules"
    metadata_rules_enabled = True

    def ready(self):
        sys.stdout.write(f"Loading {self.name} ...\n")
        site_metadata_rules.autodiscover()
        if not site_metadata_rules.registry:
            sys.stdout.write(style.ERROR(" Warning. No metadata rules have loaded.\n"))
        if not self.metadata_rules_enabled:
            sys.stdout.write(style.NOTICE(" * metadata rules disabled!\n"))
        sys.stdout.write(f" Done loading {self.name}.\n")


if settings.APP_NAME == "edc_metadata_rules":
    from dateutil.relativedelta import SU, MO, TU, WE, TH, FR, SA
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {"edc_metadata_rules.subjectvisit": "reason"}

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            "edc_metadata_rules": ("subject_visit", "edc_metadata_rules.subjectvisit")
        }

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        definitions = {
            "default": dict(
                days=[MO, TU, WE, TH, FR, SA, SU], slots=[100, 100, 100, 100, 100]
            )
        }
