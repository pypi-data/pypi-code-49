from edc_dashboard.views import AdministrationView
from django.urls.conf import path, include

urlpatterns = [
    path("accounts/", include("edc_auth.urls")),
    path("edc_adverse_event/", include("edc_adverse_event.urls")),
    path("edc_dashboard/", include("edc_dashboard.urls")),
    path("edc_export/", include("edc_export.urls")),
    path("edc_lab/", include("edc_lab.urls")),
    path("edc_lab_dashboard/", include("edc_lab_dashboard.urls")),
    path("edc_auth/", include("edc_auth.urls")),
    path("edc_pharmacy/", include("edc_pharmacy.urls")),
    path("edc_reference/", include("edc_reference.urls")),
    path("inte_ae/", include("inte_ae.urls")),
    path("inte_lists/", include("inte_lists.urls")),
    path("inte_prn/", include("inte_prn.urls")),
    path("edc_randomization/", include("edc_randomization.urls")),
    path("inte_screening/", include("inte_screening.urls")),
    path("inte_consent/", include("inte_consent.urls")),
    path("inte_subject/", include("inte_subject.urls")),
    path("administration/", AdministrationView.as_view(),
         name="administration_url"),
]
