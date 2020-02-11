# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from zeep import Client
import datetime
import json
from Crypto.Cipher import DES3
import base64
import logging

from aparnik.packages.shops.payments.models import Payment
from aparnik.packages.shops.orders.models import Order
from aparnik.settings import aparnik_settings, Setting
from aparnik.packages.bankgateways.zarinpals.models import Bank
# from .models import Bank

logging.basicConfig()

def send_request(request, payment):
    order = payment.order_obj
    order_id = order.id
    total_cost = int(order.get_total_cost() * 10)
    # TODO: change the link
    API_URL_REQUEST = 'https://sadad.shaparak.ir/vpg/api/v0/Request/PaymentRequest'
    call_back_url = request.build_absolute_uri(reverse('aparnik:bank_gateways:bmi:verify', args=[payment.uuid]))
    merchent_code = Setting.objects.get(key='BANK_MELLI_MERCHENT_CODE').get_value()
    terminal_id = Setting.objects.get(key='BANK_MELLI_TERMINAL_CODE').get_value()
    time_now = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S %P')

    init_data = {
        'TerminalId': terminal_id,
        'MerchantId': merchent_code,
        'Amount': total_cost,
        'SignData': encrypt_des3('%s;%s;%s' % (terminal_id, order_id, total_cost)),
        'ReturnUrl': call_back_url,
        'LocalDateTime': time_now,
        'OrderId': order_id,
        'AdditionalData':  'oi:%s-ou:%s'%(order_id, order.user.username),
    }

    init_response = requests.post(API_URL_REQUEST, json=init_data)
    response_json = get_json(init_response)
    if response_json['ResCode'] == '0':
        token = response_json['Token']
        url = "https://sadad.shaparak.ir/VPG/Purchase?Token=%s"%token

        bank = Bank.objects.create(authority_id=response_json['Token'],
                                   status=0,
                                   payment=payment)

        return redirect(url)
    else:
        logging.log(logging.INFO, response_json)
        print(response_json)
        raise Http404  # HttpResponse('Error code: ' + str(result.Status))

def verify(request, uuid):
    from aparnik.packages.shops.payments.views import payment as payment_view
    # order = get_object_or_404(Order.objects.active(), pk=request.POST.get('OrderId'))
    payment = get_object_or_404(Payment, uuid=uuid)

    token = request.POST.get('token')
    result_code = request.POST.get("ResCode")
    API_URL_REQUEST = 'https://sadad.shaparak.ir/vpg/api/v0/Advice/Verify'

    if payment.status != Payment.STATUS_WAITING:
        return payment_view(request, uuid=payment.uuid)

    if int(result_code) == 0:
        bank = get_object_or_404(Bank, authority_id=token)

        if bank.payment != payment:
            raise Http404

        verify_data = {
            'Token': token,
            'SignData': encrypt_des3(token),
        }

        init_response = requests.post(API_URL_REQUEST, json=verify_data)
        response_json = get_json(init_response)

        if response_json['ResCode'] == '0':
            # شماره پیگیری
            bank.ref_id = response_json['SystemTraceNo']

            # شماره مرجع
            bank.authority_id = response_json['RetrivalRefNo']

            bank.status = Bank.TRANSACTION_SUCCESS
            bank.save()
            payment.success()
            return payment_view(request, uuid=payment.uuid)

    payment.cancel()

    # return response
    return payment_view(request, uuid=payment.uuid)

def get_json(resp):
    """
    :param response:returned response as json when sending a request
    using 'requests' module.

    :return:response's content with json format
    """

    return json.loads(resp.content.decode('utf-8'))


def pad(text,pad_size=16):
    text_length = len(text)
    last_block_size = text_length % pad_size
    remaining_space = pad_size - last_block_size

    text = text + (remaining_space*chr(remaining_space))

    return text

def encrypt_des3(text):
    secret_key_bytes = base64.b64decode(Setting.objects.get(key='BANK_MELLI_SECRET_KEY').get_value())
    text = pad(text, 8)
    cipher = DES3.new(secret_key_bytes, DES3.MODE_ECB)
    my_export = cipher.encrypt(str.encode(text))
    return base64.b64encode(my_export).decode("utf-8")