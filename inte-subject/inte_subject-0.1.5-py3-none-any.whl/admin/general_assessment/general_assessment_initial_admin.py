from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin


from ...admin_site import inte_subject_admin
from ...forms import GeneralAssessmentInitialForm
from ...models import GeneralAssessmentInitial
from ..modeladmin import CrfModelAdminMixin


@admin.register(GeneralAssessmentInitial, site=inte_subject_admin)
class GeneralAssessmentInitialAdmin(
    CrfModelAdminMixin, FormLabelModelAdminMixin, SimpleHistoryAdmin
):

    form = GeneralAssessmentInitialForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Baseline Conditions and Care",
            {
                "fields": (
                    "hiv",
                    "attending_hiv_clinic",
                    "use_hiv_clinic_nearby",
                    "hiv_next_appt_date",
                    "diabetic",
                    "hypertensive",
                    "attending_ncd_clinic",
                    "use_ncd_clinic_nearby",
                    "ncd_next_appt_date",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "hiv": admin.VERTICAL,
        "attending_hiv_clinic": admin.VERTICAL,
        "use_hiv_clinic_nearby": admin.VERTICAL,
        "diabetic": admin.VERTICAL,
        "hypertensive": admin.VERTICAL,
        "attending_ncd_clinic": admin.VERTICAL,
        "use_ncd_clinic_nearby": admin.VERTICAL,
    }
