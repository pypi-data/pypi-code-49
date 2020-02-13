from django import forms
from edc_constants.constants import YES, NO, NOT_APPLICABLE
from edc_form_validators.form_validator import FormValidator

from .crf_form_validator_mixin import CrfFormValidatorMixin


class GeneralAssessmentInitialFormValidator(CrfFormValidatorMixin, FormValidator):
    def clean(self):
        # hiv

        if self.cleaned_data.get("hiv") == NO and self.hiv_clinic:
            raise forms.ValidationError(
                {"hiv": "Expected YES. Subject was enrolled from an HIV Clinic."}
            )

        self.applicable_if(YES, field="hiv", field_applicable="attending_hiv_clinic")

        self.applicable_if(
            YES, field="attending_hiv_clinic", field_applicable="use_hiv_clinic_nearby"
        )

        if (
            self.cleaned_data.get("diabetic") == NO
            and self.cleaned_data.get("hypertensive") == NO
            and self.ncd_clinic
        ):
            raise forms.ValidationError(
                {
                    "Expected subject to be diabetic or hypertensive. "
                    "Subject was enrolled from an NCD Clinic."
                }
            )

        # NCD CLINIC
        if (
            self.cleaned_data.get("diabetic") == YES
            or self.cleaned_data.get("hypertensive") == YES
        ):
            if self.cleaned_data.get("attending_ncd_clinic") == NOT_APPLICABLE:
                raise forms.ValidationError(
                    {"attending_ncd_clinic": "This field is applicable"}
                )

        if (
            self.cleaned_data.get("diabetic") == NO
            and self.cleaned_data.get("hypertensive") == NO
            and self.cleaned_data.get("attending_ncd_clinic") != NOT_APPLICABLE
        ):
            raise forms.ValidationError(
                {"attending_ncd_clinic": "This field is not applicable"}
            )

        self.applicable_if(
            YES, field="attending_ncd_clinic", field_applicable="use_ncd_clinic_nearby"
        )
