from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from django_press.models import BaseInquiry, Contact


class InquiryChildAdmin(PolymorphicChildModelAdmin):
    base_model = BaseInquiry


class ContactAdmin(InquiryChildAdmin):
    base_model = Contact
    list_display = (
        'category',
        'name',
        'email',
        'body',
        'created_at',
    )


class InquiryAdmin(PolymorphicParentModelAdmin):
    base_model = BaseInquiry  # Optional, explicitly set here.
    child_models = (Contact,)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.
