from django.utils.safestring import mark_safe

from ..forms import screening_fields


def get_fieldset(collapse=None):

    dct = {
        "description": mark_safe(
            "To be completed by the <u>study clinician</u> or the "
            "<u>research nurse</u> in consultation with the study clinician"
        ),
        "fields": screening_fields,
    }
    if collapse:
        dct.update(classes=("collapse",))
    return ("Part 1", dct)


comments_fieldset = (
    "Additional Comments",
    {"fields": (*part_three_comment_fields,),},
)

calculated_values_fieldset = (
    "Calculated values",
    {
        "classes": ("collapse",),
        "fields": (
            "calculated_bmi",
            "converted_fasting_glucose",
            "converted_ogtt_two_hr",
            "converted_creatinine",
            "calculated_egfr",
            "inclusion_a",
            "inclusion_b",
            "inclusion_c",
            "inclusion_d",
        ),
    },
)
