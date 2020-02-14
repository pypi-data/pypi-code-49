# -*- coding: utf-8 -*-
from django.http import Http404

from aparnik.utils.utils import is_app_installed

def send_to_bank(request, payment):
    try:
        if not is_app_installed('aparnik.packages.bankgateways.bmi'):
            raise Exception()
        from aparnik.packages.bankgateways.bmi.views import send_request as bmi_send_request
        return bmi_send_request(request=request, payment=payment)
    except:
        pass
    try:
        if not is_app_installed('aparnik.packages.bankgateways.zarinpals'):
            raise Exception()
        from aparnik.packages.bankgateways.zarinpals.views import send_request as zarinpal_send_request
        return zarinpal_send_request(request=request, payment=payment)
    except:
        pass

    raise Http404