# coding=utf-8
import json
from os import path
from pod_base import PodBase, calc_offset, PodException, ConfigException, InvalidDataException
from pod_common import PodCommon
from pod_export import PodExport

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class PodBilling(PodBase):
    __slots__ = ("export", "payment", "__common")

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodBilling, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key, sc_voucher_hash,
                                         path.join(here, "json_schema.json"))
        self.__init_module(config_path)

    def __init_module(self, config_path):
        """
        ایجاد نمونه از ماژول مورد نیاز

        :param str config_path:
        """
        self.export = PodExport(api_token=self._api_token, token_issuer=self._token_issuer,
                                server_type=self._server_type, config_path=config_path,
                                sc_api_key=self._default_params["sc_api_key"],
                                sc_voucher_hash=self._default_params["sc_voucher_hash"])

        self.__common = PodCommon(api_token=self._api_token, token_issuer=self._token_issuer,
                                  server_type=self._server_type, config_path=config_path,
                                  sc_api_key=self._default_params["sc_api_key"],
                                  sc_voucher_hash=self._default_params["sc_voucher_hash"])

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

    def issue_invoice(self, products, guild_code, **kwargs):
        """
        صدور فاکتور

        :param list products: لیست محصولات
        :param str guild_code: کد صنف
        :return: dict
        """
        kwargs["productList"] = products
        kwargs["guildCode"] = guild_code
        kwargs["_ott_"] = kwargs.pop("ott", kwargs.pop("_ott_", None))
        if kwargs["_ott_"] is None:
            kwargs["_ott_"] = self.__common.get_ott()

        if "metadata" in kwargs:
            if type(kwargs["metadata"]) == dict:
                kwargs["metadata"] = json.dumps(kwargs["metadata"])
            else:
                del kwargs["metadata"]

        if "eventMetadata" in kwargs:
            if type(kwargs["eventMetadata"]) == dict:
                kwargs["eventMetadata"] = json.dumps(kwargs["eventMetadata"])
            else:
                del kwargs["eventMetadata"]

        if "eventReminders" in kwargs:
            kwargs["eventReminders"] = self.__convert_dict_to_str_in_list(kwargs["eventReminders"])

        self._validate(kwargs, "issueInvoice")
        del kwargs["productList"]
        (kwargs["productId[]"], kwargs["quantity[]"], kwargs["discount[]"], kwargs["productDescription[]"],
         kwargs["price[]"]) = self.__prepare_product(products)

        result = self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/issueInvoice", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)
        return result

    @staticmethod
    def __prepare_product(products):
        product_id = []
        quantity = []
        discount = []
        product_description = []
        price = []

        for product in products:
            product_id.append(product["productId"])
            quantity.append(product["quantity"])
            price.append(product["price"])
            product_description.append(product["productDescription"])
            if "discount" in product:
                discount.append(product["discount"])
            else:
                discount.append(0)

        return product_id, quantity, discount, product_description, price

    @staticmethod
    def __convert_dict_to_str_in_list(items):
        if type(items) == list:
            output = []
            for e in items:
                output.append(json.dumps(e))
            return output
        if type(items) == dict:
            return [json.dumps(items)]

        return []

    def reduce_invoice(self, invoice_id, items, preferred_tax_rate, **kwargs):
        params = {
            "id": invoice_id,
            "preferredTaxRate": preferred_tax_rate,
            "invoiceItemList": items
        }

        self._validate(params, "reduceInvoice")

        (params["invoiceItemId[]"], params["quantity[]"], params["itemDescription[]"], params["price[]"]) = \
            self.__prepare_items(params["invoiceItemList"])

        del params["invoiceItemList"]

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/reduceInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __prepare_items(products):
        invoice_item_id = []
        quantity = []
        item_description = []
        price = []

        for product in products:
            invoice_item_id.append(product["invoiceItemId"])
            quantity.append(product["quantity"])
            price.append(product["price"])
            item_description.append(product["itemDescription"])

        return invoice_item_id, quantity, item_description, price

    def get_invoice_list(self, bill_number="", from_date="", to_date="", **kwargs):
        """
        لیست فاکتورها

        :param str bill_number: شماره قبض یکتا
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

        if bill_number:
            kwargs["billNumber"] = bill_number
        if from_date:
            kwargs["fromDate"] = from_date
        if to_date:
            kwargs["toDate"] = to_date

        self._validate(kwargs, "getInvoiceList")

        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/getInvoiceList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def get_invoice(self, invoice_id, **kwargs):
        """
        دریافت جزئیات یک فاکتور

        :param int invoice_id: شماره فاکتور
        :raises: :class:`PodException`

        :return: dict
        """
        invoice = self.get_invoice_list(size=1, id=invoice_id, **kwargs)
        if len(invoice):
            return invoice[0]

        raise PodException(message="فاکتور {} یافت نشد".format(invoice_id))

    def get_invoice_list_by_metadata(self, meta_query, page=1, size=20, **kwargs):
        """
        جستجو در پارامتر metadata فاکتورها

        :param dict meta_query: عبارت جستجو در metadata
        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: list
        """
        if type(meta_query) != dict:
            info = {
                "message": "meta_data is not dict",
                "error_code": 887
            }
            raise InvalidDataException(**info)

        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size
        kwargs["metaQuery"] = meta_query

        self._validate(kwargs, "getInvoiceListByMetadata")

        kwargs["metaQuery"] = json.dumps(meta_query)

        result = self._request.call(super(PodBilling, self)._get_sc_product_settings("/getInvoiceListByMetadata"),
                                    params=kwargs, headers=self._get_headers(), **kwargs)
        return result

    def create_pre_invoice(self, user_id, products, guild_code, redirect_url, **kwargs):
        """
        ایجاد پیش فاکتور

        :param int user_id: شناسه کاربری مشتری
        :param list products: لیست محصولات
        :param str guild_code: کد صنف
        :param str redirect_url: آدرس بازگشت
        :return: dict
        """
        if self._server_type != PodBase.PRODUCTION_MODE:
            raise PodException(message="سرویس ایجاد پیش فاکتور تنها در حالت Production کار می کند.")

        kwargs.setdefault("token", self._api_token)

        kwargs["productList"] = products
        kwargs["guildCode"] = guild_code
        kwargs["redirectUri"] = redirect_url
        kwargs["userId"] = user_id

        self._validate(kwargs, "createPreInvoice")

        result = self._request.call(super(PodBilling, self)._get_sc_product_settings("/createPreInvoice"),
                                    params=kwargs, headers=self._get_headers(), internal=False, **kwargs)
        print(result)
        return {
            "hash": result["result"],
            "url": "{}/v1/pbc/preinvoice/{}".format(self.__get_private_call_address(), result["result"])
        }

    def verify_invoice(self, invoice_id, **kwargs):
        """
        تایید پرداخت فاکتور بر اساس شماره فاکتور

        :param int invoice_id:
        :return: boolean
        """
        return self._verify_invoice({"id": invoice_id}, **kwargs)

    def verify_invoice_by_bill_number(self, bill_number, **kwargs):
        """
        تایید پرداخت فاکتور براساس شماره قبض

        :param str bill_number:
        :return: boolean
        """
        return self._verify_invoice({"billNumber": bill_number}, **kwargs)

    def _verify_invoice(self, params, **kwargs):
        """
        تایید پرداخت فاکتور

        :param dict params: اطلاعات
        :return: boolean
        """

        self._validate(params, "verifyInvoice")

        result = self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/verifyInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

        return result

    def close_invoice(self, invoice_id, **kwargs):
        """
        بستن فاکتور

        :param int invoice_id: شماره فاکتور
        :return: boolean
        """

        params = {
            "id": invoice_id
        }

        self._validate(params, "closeInvoice")

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/closeInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    def verify_and_close_invoice(self, invoice_id, **kwargs):
        """
        تایید پرداخت و بستن فاکتور

        :param int invoice_id: شماره فاکتور
        :return: boolean
        """

        params = {
            "id": invoice_id
        }

        self._validate(params, "verifyAndCloseInvoice")

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/verifyAndCloseInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    def cancel_invoice(self, invoice_id, **kwargs):
        """
        ابطال فاکتور

        :param int invoice_id: شماره فاکتور
        :return: boolean
        """

        params = {
            "id": invoice_id
        }

        self._validate(params, "cancelInvoice")

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/cancelInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    def get_invoice_list_as_file(self, **kwargs):
        """
        درخواست ایجاد فایل خروجی از فاکتورها

        :param kwargs:
        :return: dict
        """
        self._validate(kwargs, "getInvoiceListAsFile")

        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/getInvoiceListAsFile"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def get_pay_invoice_by_wallet_link(self, invoice_id, redirect_url=None, call_url=None, token_issuer=1):
        """
        تولید لینک پرداخت هزینه فاکتور از طریق کیف پول کاربر

        :param int invoice_id: شناسه فاکتور
        :param str redirect_url: آدرس بازگشت به برنامه بعد از پرداخت
        :param str call_url: آدرس فراخوانی سرور بعد از پرداخت
        :param int token_issuer: مرجع صادر کننده توکن
        :return: str
        """
        params = {
            "invoiceId": invoice_id,
            "tokenIssuer": token_issuer
        }

        if redirect_url:
            params["redirectUri"] = redirect_url

        if call_url:
            params["callUri"] = call_url

        self._validate(params, "getPayInvoiceByWalletLink")

        return "{}/v1/pbc/payinvoice/?{}".format(self.__get_private_call_address(), urlencode(params))

    def pay_invoice_by_credit(self, invoice_id, **kwargs):
        """
        پرداخت فاکتور صادر شده برای شما از طریق اعتبارتان

        :param int invoice_id:     شناسه فاکتور
        :return: boolean
        """
        params = {
            "invoiceId": invoice_id,
            "_ott_": kwargs.pop("ott", kwargs.pop("_ott_", None))
        }

        if params["_ott_"] is None:
            params["_ott_"] = self.__common.get_ott()

        self._validate(params, "payInvoiceByCredit")
        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/payInvoiceByCredit", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    def pay_any_invoice_by_credit(self, invoice_id, wallet, **kwargs):
        """
        پرداخت فاکتور صادر شده از طریق اعتبارتان

        :param int invoice_id:     شناسه فاکتور
        :param str wallet: کد کیف پول
        :return: boolean
        """
        kwargs["invoiceId"] = invoice_id
        kwargs["_ott_"] = kwargs.pop("ott", kwargs.pop("_ott_", None))
        kwargs["wallet"] = wallet

        if kwargs["_ott_"] is None:
            kwargs["_ott_"] = self.__common.get_ott()

        self._validate(kwargs, "payAnyInvoiceByCredit")
        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/payAnyInvoiceByCredit", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def get_invoice_payment_link(self, invoice_id, redirect_url=None, call_url=None, gateway="PEP", **kwargs):
        """
        دریافت لینک پرداخت از طریق درگاه

        :param int invoice_id:     شناسه فاکتور
        :param str redirect_url: آدرس بازگشت به برنامه بعد از پرداخت
        :param str call_url: آدرس فراخوانی سرور بعد از پرداخت
        :param str gateway: کد درگاه
        :return: str
        """
        invoice = self.get_invoice(invoice_id, **kwargs)
        return self.get_pay_invoice_by_unique_number_link(unique_number=invoice["uniqueNumber"],
                                                          redirect_url=redirect_url, call_url=call_url, gateway=gateway)

    def get_pay_invoice_by_unique_number_link(self, unique_number, redirect_url=None, call_url=None, gateway="PEP"):
        """
        دریافت لینک پرداخت از طریق درگاه

        :param str unique_number: کد یکتا فاکتور
        :param str redirect_url: آدرس بازگشت به برنامه بعد از پرداخت
        :param str call_url: آدرس فراخوانی سرور بعد از پرداخت
        :param str gateway: کد درگاه
        :return: str
        """

        params = {
            "uniqueNumber": unique_number,
            "gateway": gateway
        }

        if redirect_url is not None:
            params["redirectUri"] = redirect_url

        if call_url is not None:
            params["callUri"] = call_url

        self._validate(params, "getPayInvoiceByUniqueNumberLink")
        return "{}/v1/pbc/payInvoiceByUniqueNumber/?{}".format(self.__get_private_call_address(), urlencode(params))

    def send_invoice_payment_sms(self, invoice_id, **kwargs):
        """
        ارسال پیامک پرداخت فاکتور

        :param int invoice_id:     شناسه فاکتور
        :return: boolean
        """
        params = kwargs
        params["invoiceId"] = invoice_id

        self._validate(params, "sendInvoicePaymentSMS")
        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/sendInvoicePaymentSMS"),
                                  params=params, headers=self._get_headers(), **kwargs)

    def pay_invoice(self, invoice_id, **kwargs):
        """
        پرداخت فاکتور از طریق شخص ثالث - خارج از پلتفرم پاد
        در این روش تنها فاکتور به صورت پرداخت شده ثبت می شود و هیچ پولی به حساب صنفی شما واریز نمی شود

        :param int invoice_id:     شناسه فاکتور
        :return: boolean
        """
        params = {
            "invoiceId": invoice_id
        }

        self._validate(params, "payInvoice")
        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/payInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    def pay_invoice_by_invoice(self, creditor_invoice_id, debtor_invoice_id, **kwargs):
        """
        پرداخت فاکتور با استفاده از فاکتور

        :param int creditor_invoice_id: شناسه فاکتور بستانکار
        :param int debtor_invoice_id: شناسه فاکتور بدهکار
        :return: boolean
        """

        params = {
            "creditorInvoiceId": creditor_invoice_id,
            "debtorInvoiceId": debtor_invoice_id
        }

        self._validate(params, "payInvoiceByInvoice")
        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/payInvoiceByInvoice"),
                                  params=params, headers=self._get_headers(), **kwargs)

    def pay_invoice_in_future(self, invoice_id, date, guild_code=None, wallet=None, **kwargs):
        """
        پرداخت فاکتور در آینده

        :param int invoice_id:     شناسه فاکتور
        :param str date:  تاریخ شمسی سررسید به فرمت yyyy/mm/dd
        :param str guild_code:  کد صنف
        :param str wallet: کد کیف پول
        :return: boolean
        """
        kwargs["invoiceId"] = invoice_id
        kwargs["date"] = date
        kwargs["_ott_"] = kwargs.pop("ott", kwargs.pop("_ott_", None))

        if kwargs["_ott_"] is None:
            kwargs["_ott_"] = self.__common.get_ott()

        if guild_code is not None:
            kwargs["guildCode"] = guild_code

        if wallet is not None:
            kwargs["wallet"] = wallet

        self._validate(kwargs, "payInvoiceInFuture")
        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/payInvoiceInFuture"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def pay_invoice_by_pos(self, invoice_id, terminal_number, merchant_code, reference_number, tracking_number,
                           transaction_date, wallet=None, **kwargs):
        """
        ثبت پرداخت فاکتور از طریق دستگاه کارتخوان (POS)

        :param int invoice_id:     شناسه فاکتور
        :param str terminal_number: شماره پایانه پرداخت
        :param str merchant_code: شناسه پذیرنده پایانه پرداخت
        :param str reference_number: شماره مرجع
        :param str tracking_number: شماره پیگیری
        :param str transaction_date: تاریخ تراکنش به فرمت yyyy/mm/dd HH:MM:ss
        :param str wallet: کد کیف پول
        :return: boolean
        """
        kwargs["invoiceId"] = invoice_id
        kwargs["terminalNumber"] = terminal_number
        kwargs["merchantCode"] = merchant_code
        kwargs["referenceNumber"] = reference_number
        kwargs["trackingNumber"] = tracking_number
        kwargs["transactionDate"] = transaction_date

        if wallet is not None:
            kwargs["wallet"] = wallet

        self._validate(kwargs, "payInvoiceByPos")
        return self._request.call(super(PodBilling, self)._get_sc_product_settings("/nzh/biz/payInvoiceByPos"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def issue_multi_invoice(self, main_invoice, customer_invoice, sub_invoices, **kwargs):
        """
        صدور فاکتور تسهیمی

        :param dict main_invoice: اطلاعات فاکتور اصلی
        :param list customer_invoice: اطلاعات فاکتور مشتری
        :param list sub_invoices: لیستی از فاکتورهای ذینفعان
        :return: dict
        """

        params = {"data": kwargs}
        params["data"]["mainInvoice"] = main_invoice
        params["data"]["subInvoices"] = sub_invoices
        params["data"]["customerInvoiceItemVOs"] = customer_invoice

        self._validate(params, "issueMultiInvoice")

        params["data"] = json.dumps(self.__convert_dict_to_str(params["data"]))

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/issueMultiInvoice", method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __convert_dict_to_str(data):
        if "metadata" in data["mainInvoice"]:
            data["mainInvoice"]["metadata"] = json.dumps(data["mainInvoice"]["metadata"])
        if "customerMetadata" in data:
            data["customerMetadata"] = json.dumps(data["customerMetadata"])

        for i, k in enumerate(data["subInvoices"]):
            if "metadata" in k:
                data["subInvoices"][i]["metadata"] = json.dumps(k["metadata"])

        return data

    def reduce_multi_invoice(self, preferred_tax_rate, main_invoice, customer_invoice, sub_invoices, **kwargs):
        """
        کاهش فاکتور تسهیمی

        :param float preferred_tax_rate: نرخ مالیات بین 0 تا 1
        :param dict main_invoice: اطلاعات فاکتور اصلی
        :param list customer_invoice: اطلاعات فاکتور مشتری
        :param list sub_invoices: اطلاعات ذینفعان
        :return: dict
        """

        return self.__reduce_invoice("reduceMultiInvoice", preferred_tax_rate=preferred_tax_rate,
                                     main_invoice=main_invoice, sub_invoices=sub_invoices,
                                     customer_invoice=customer_invoice, **kwargs)

    def reduce_multi_invoice_and_cash_out(self, preferred_tax_rate, main_invoice, customer_invoice, sub_invoices,
                                          tool_code=None, **kwargs):
        """
        کاهش فاکتور تسهیمی و برگشت بلافاصله مبلغ به حساب مشتری

        :param float preferred_tax_rate: نرخ مالیات بین 0 تا 1
        :param dict main_invoice: اطلاعات فاکتور اصلی
        :param list customer_invoice: اطلاعات فاکتور مشتری
        :param list sub_invoices: اطلاعات ذینفعان
        :param str tool_code: کد ابزار تسویه
        :return: dict
        """
        if tool_code is not None:
            kwargs["toolCode"] = tool_code

        return self.__reduce_invoice("reduceMultiInvoiceAndCashout", preferred_tax_rate=preferred_tax_rate,
                                     main_invoice=main_invoice, sub_invoices=sub_invoices,
                                     customer_invoice=customer_invoice, **kwargs)

    def __reduce_invoice(self, service, preferred_tax_rate, main_invoice, customer_invoice, sub_invoices, **kwargs):
        """
        :param str service: آدرس سرویس
        :param float preferred_tax_rate: نرخ مالیات بین 0 تا 1
        :param dict main_invoice: اطلاعات فاکتور اصلی
        :param list customer_invoice: اطلاعات فاکتور مشتری
        :param list sub_invoices: اطلاعات ذینفعان
        :return: dict
        """
        params = {"data": kwargs}
        params["data"]["preferredTaxRate"] = preferred_tax_rate
        params["data"]["mainInvoice"] = main_invoice
        params["data"]["subInvoices"] = sub_invoices
        params["data"]["customerInvoiceItemVOs"] = customer_invoice
        self._validate(params, service)

        params["data"] = json.dumps(self.__convert_dict_to_str(params["data"]))

        return self._request.call(
            super(PodBilling, self)._get_sc_product_settings("/nzh/biz/" + str(service), method_type="post"),
            params=params, headers=self._get_headers(), **kwargs)
