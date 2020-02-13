from django import forms
from edc_sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from inte_form_validators import GeneralAssessmentInitialFormValidator

from ..models import GeneralAssessmentInitial


class GeneralAssessmentInitialForm(
    SiteModelFormMixin, FormValidatorMixin, forms.ModelForm
):

    form_validator_cls = GeneralAssessmentInitialFormValidator

    class Meta:
        model = GeneralAssessmentInitial
        fields = "__all__"
