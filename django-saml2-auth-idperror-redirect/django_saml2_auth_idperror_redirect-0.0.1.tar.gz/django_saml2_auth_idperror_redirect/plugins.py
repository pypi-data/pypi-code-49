from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_saml2_auth.plugins import IdpErrorPlugin


class SingleLogOutSignoutHandler(IdpErrorPlugin):
    KEY = 'IDP_ERROR'

    @classmethod
    def idp_error(cls, request):
        """Logs the user out of the local system and redirects them to the REDIRECT URL in the SAML Metadata"""
        url = None
        view = settings.SAML2_AUTH.get('IDP_ERROR_REDIRECT_VIEW')
        if view is not None:
            url = reverse(view)
        if url is None:
            url = settings.SAML2_AUTH.get('IDP_ERROR_REDIRECT_URL')
        if url is None:
            raise ValueError("Must provide IDP_ERROR_REDIRECT_VIEW or IDP_ERROR_REDIRECT_URL")
        return HttpResponseRedirect(url)
