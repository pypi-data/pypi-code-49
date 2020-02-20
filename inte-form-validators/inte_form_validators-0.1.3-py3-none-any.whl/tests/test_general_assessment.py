from unittest import skip

from dateutil.relativedelta import relativedelta
from django import forms
from django.test import TestCase, tag
from edc_constants.constants import NO, YES, NOT_APPLICABLE
from edc_utils.date import get_utcnow
from inte_form_validators.form_validators import SubjectConsentFormValidator
from inte_screening.tests.inte_test_case_mixin import InteTestCaseMixin
from pytz import timezone

from ..form_validators import GeneralAssessmentInitialFormValidator


@skip
class TestGeneralAssessmentFormValidators(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.eligibility_datetime = get_utcnow() - relativedelta(days=1)  # yesterday
        self.subject_screening = self.get_subject_screening(
            report_datetime=get_utcnow(), eligibility_datetime=self.eligibility_datetime
        )
        self.screening_identifier = self.subject_screening.screening_identifier

    def get_now(self):
        return get_utcnow().astimezone(timezone("Africa/Kampala"))

    def test_ok(self):
        user_input = {
            "hiv": YES,
            "attending_hiv_clinic": YES,
            "use_hiv_clinic_nearby": YES,
            "hiv_next_appt_date": None,
            "diabetic": NO,
            "hypertensive": NO,
            "use_ncd_clinic_nearby": NOT_APPLICABLE,
            "attending_ncd_clinic": NOT_APPLICABLE,
            "ncd_next_appt_date": None,
        }

        form_validator = GeneralAssessmentInitialFormValidator(cleaned_data=user_input)
        self.assertRaises(forms.ValidationError, form_validator.validate)
        self.assertIn("f2", form_validator._errors)
