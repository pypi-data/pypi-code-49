# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django import forms
from django.utils.translation import ugettext_lazy as _
from fobi.base import (
    BasePluginForm,
    FormHandlerPlugin,
    form_handler_plugin_registry,
)  # noqa: E501


from .shortcuts import get_sendgrid_client, get_sendgrid_lists


class SendgridListRegistrationForm(forms.Form, BasePluginForm):
    plugin_data_fields = [
        ("sendgrid_list_id", ""),
        ("email_field", ""),
        ("optin_field", ""),
        ("first_name_field", ""),
        ("last_name_field", ""),
    ]

    # Sendgrid list id to register user to
    sendgrid_list_id = forms.ChoiceField(
        label=_("Sendgrid list"), required=True, choices=[]
    )
    first_name_field = forms.CharField(label=_("First name field"), required=False)
    last_name_field = forms.CharField(label=_("Last name field"), required=False)
    email_field = forms.CharField(label=_("E-mail field"), required=True)
    optin_field = forms.CharField(label=_("Opt-in field"), required=True)

    def __init__(self, *args, **kwargs):
        super(SendgridListRegistrationForm, self).__init__(*args, **kwargs)

        sendgrid_lists = get_sendgrid_lists()
        self.fields["sendgrid_list_id"].choices = [
            (sendgrid_list["id"], sendgrid_list["name"])
            for sendgrid_list in sendgrid_lists
        ]


class SendgridListRegistrationHandlerPlugin(FormHandlerPlugin):
    """ Sendgrid handler plugin."""

    uid = "sendgrid_list_registration"
    name = _("Sendgrid list registration")
    form = SendgridListRegistrationForm

    def run(self, form_entry, request, form, form_element_entries=None):
        # Prevent circular import
        from .models import CTAPluginSettings

        # Extract contact details
        email = form.cleaned_data.get(self.data.email_field)

        cta_plugin_id = getattr(form_entry, "cta_plugin_id", None)
        if cta_plugin_id is not None:
            cta_plugin = CTAPluginSettings.objects.filter(id=cta_plugin_id).first()

            if (
                email is not None
                and form.cleaned_data.get(self.data.optin_field)
                and cta_plugin
            ):
                contact_details = {"email": email}

                first_name = last_name = None
                if self.data.first_name_field is not None:
                    first_name = form.cleaned_data.get(self.data.first_name_field)
                    contact_details["first_name"] = first_name
                if self.data.last_name_field is not None:
                    last_name = form.cleaned_data.get(self.data.last_name_field)
                    contact_details["last_name"] = last_name

                # Build sendgrid client
                sg = get_sendgrid_client()

                # Create/update contact and retrieve contact id
                data = [contact_details]
                response = sg.client.contactdb.recipients.post(
                    request_body=[contact_details]
                )
                data = json.loads(response.body)
                contact_id = data["persisted_recipients"][0]

                # Register contact to mailling list
                sg.client.contactdb.lists._(self.data.sendgrid_list_id).recipients._(
                    contact_id
                ).post()


form_handler_plugin_registry.register(SendgridListRegistrationHandlerPlugin)
