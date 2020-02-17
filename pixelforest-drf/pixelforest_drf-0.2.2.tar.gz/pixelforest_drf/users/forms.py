# Imports ##############################################################################################################
from django import forms
from django.contrib.auth import get_user_model

from ..countries.models import Country, SubRegion, Region
from ..companies.models import Service
User = get_user_model()


# Forms mixins #########################################################################################################

class UserWithCountriesLinkCreationFormMixin(forms.ModelForm):
    country = forms.ModelChoiceField(label="Country", queryset=Country.objects.active(), required=False, help_text=
                                     "Leave empty if this user is global or linked to a Sub Region or Region")
    sub_region = forms.ModelChoiceField(label="Sub Region", queryset=SubRegion.objects.active(), required=False, help_text=
                                        "Leave empty if this user is global or linked to a Country or Region")
    region = forms.ModelChoiceField(label="Region", queryset=Region.objects.active(), required=False, help_text=
                                    "Leave empty if this user is global or linked to a Country or Sub Region")


class UserWithLinkServiceCreationFormMixin(forms.ModelForm):
    service = forms.ModelChoiceField(label="Service", queryset=Service.objects.all(), required=True, help_text=
                                     "Required field --> A User must be linked to a Service")
