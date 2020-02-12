# coding=utf-8
import json
from os import path
from pod_base import PodBase, calc_offset, ConfigException
from .response import Response
from .exception import AvandException


class Avand(PodBase):
    __slots__ = "response"

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(Avand, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key, sc_voucher_hash,
                                         path.join(here, "json_schema.json"))
        self.response = Response()

    def __parse_response(self, result):
        try:
            result = json.loads(result)
        except ValueError:
            raise AvandException(message="اطلاعات دریافتی از سرور نامعتبر است")

        self.response = Response(**result)
        self.__check_response(result)
        return result["result"]

    @staticmethod
    def __check_response(result):
        if "errorCode" not in result:
            raise AvandException(message="اطلاعات دریافتی از سرور نامعتبر است")

        if result["errorCode"] != 0:
            raise AvandException(**result)

    def __get_private_call_address(self):
        """
        دریافت آدرس سرور پرداخت از فایل کانفیگ

        :return: str
        :raises: :class:`ConfigException`
        """
        private_call_address = self.config.get("private_call_address", self._server_type)
        if private_call_address:
            return private_call_address

        raise ConfigException("config `private_call_address` in {} not found".format(self._server_type))

    def issue_invoice(self, user_id, business_id, price, redirect_uri, **kwargs):
        """
        صدور فاکتور

        :param int user_id: شناسه کاربری خریدار
        :param int business_id: شناسه کسب و کار
        :param float price:  جمع کل فاکتور
        :param str redirect_uri: آدرس بازگشت
        :return: dict
        """
        kwargs["userId"] = user_id
        kwargs["businessId"] = business_id
        kwargs["price"] = price
        kwargs["redirectUri"] = redirect_uri

        self._validate(kwargs, "issueInvoice")

        return self.__parse_response(self._request.call(
            super(Avand, self)._get_sc_product_settings("/nzh/biz/issueInvoice", method_type="post"),
            params=kwargs, headers=self._get_headers(), internal=False, **kwargs))

    def get_invoice_list(self, from_date="", to_date="", **kwargs):
        """
        لیست فاکتورها

        :param str from_date: از تاریخ صدور به صورت شمسی
        فرمت تاریخ شروع باید به صورت yyyy/mm/dd hh:ii:ss باشد به طور مثال
        :param str to_date: تا تاریخ صدور به صورت شمسی
        فرمت تاریخ پایان باید به صورت yyyy/mm/dd hh:ii:ss باشد به طور مثال

        :return: list
        """

        if "firstId" not in kwargs and "lastId" not in kwargs and "page" not in kwargs:
            kwargs.setdefault("page", 1)

        kwargs.setdefault("size", 50)
        if "page" in kwargs:
            kwargs["offset"] = calc_offset(kwargs["page"], kwargs["size"])
            del kwargs["page"]

        if from_date:
            kwargs["fromDate"] = from_date
        if to_date:
            kwargs["toDate"] = to_date

        self._validate(kwargs, "getInvoiceList")

        return self._request.call(super(Avand, self)._get_sc_product_settings("/nzh/biz/getInvoiceList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def verify_invoice(self, invoice_id, **kwargs):
        """
        تایید پرداخت فاکتور بر اساس شماره فاکتور

        :param int invoice_id:
        :return: boolean
        """
        params = {
            "invoiceId": invoice_id
        }

        self._validate(params, "verifyInvoice")

        self.__parse_response(self._request.call(
            super(Avand, self)._get_sc_product_settings("/nzh/biz/verifyInvoice", method_type="post"),
            params=params, headers=self._get_headers(), internal=False, **kwargs))

        return True

    def cancel_invoice(self, invoice_id, **kwargs):
        """
        ابطال فاکتور

        :param int invoice_id: شماره فاکتور
        :return: boolean
        """

        params = {
            "invoiceId": invoice_id
        }

        self._validate(params, "cancelInvoice")

        self.__parse_response(self._request.call(
            super(Avand, self)._get_sc_product_settings("/nzh/biz/cancelInvoice", method_type="post"),
            params=params, headers=self._get_headers(), internal=False, **kwargs))

        return True
