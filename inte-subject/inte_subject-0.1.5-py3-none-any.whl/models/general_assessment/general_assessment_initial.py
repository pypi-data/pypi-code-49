from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO_UNKNOWN, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model.models.base_uuid_model import BaseUuidModel

from ..crf_model_mixin import CrfModelMixin


class GeneralAssessmentInitial(CrfModelMixin, BaseUuidModel):

    hiv = models.CharField(
        verbose_name=mark_safe("Have you previously tested <u>positive</u> for HIV"),
        max_length=15,
        choices=YES_NO_UNKNOWN,
    )

    attending_hiv_clinic = models.CharField(
        verbose_name="Are you receiving care at an HIV clinic",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    use_hiv_clinic_nearby = models.CharField(
        verbose_name="Do you attend the HIV clinic within this facility",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    hiv_next_appt_date = models.DateField(
        verbose_name="When is your next HIV appointment", null=True, blank=True
    )

    diabetic = models.CharField(
        verbose_name=mark_safe(
            "Have you previously been diagnosed with <u>diabetes</u> "
            "(high blood sugar)?"
        ),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe(
            "Have you previously been diagnosed with <u>hypertension</u> "
            "(high blood pressure)?"
        ),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    attending_ncd_clinic = models.CharField(
        verbose_name="Are you receiving care at an NCD clinic",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    use_ncd_clinic_nearby = models.CharField(
        verbose_name="Do you attend the NCD clinic within this facility",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    ncd_next_appt_date = models.DateField(
        verbose_name="When is your next NCD appointment", null=True, blank=True
    )

    class Meta(CrfModelMixin.Meta):
        verbose_name = "General Assessment (Baseline)"
        verbose_name_plural = "General Assessment (Baseline)"
