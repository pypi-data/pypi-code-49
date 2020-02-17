# coding=utf-8
from __future__ import absolute_import
from os import path

from pod_base import PodBase, calc_offset, InvalidDataException


class PodVoucher(PodBase):

    """کد تخفیف یکبار مصرف برای یک آیتم"""
    DISCOUNT_TYPE_ONE_TIME_ITEM = 4
    """کد تخفیف یکبار مصرف برای یک فاکتور"""
    DISCOUNT_TYPE_ONE_TIME_INVOICE = 16
    """کد تخفیف نامحدود"""
    DISCOUNT_TYPE_UNLIMITED = 8

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services_voucher.json")
        super(PodVoucher, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key, sc_voucher_hash,
                                         path.join(here, "json_schema_voucher.json"))

    def define_credit_voucher(self, vouchers, guild_code, expire_date, limited_consumer_id=None, currency_code=None,
                              **kwargs):
        """
        ایجاد کدهای اعتباری

        :param list vouchers: لیست کد های اعتباری
        :param str guild_code: کد صنف
        :param str expire_date: تاریخ انقضا کدهای اعتباری
        :param int limited_consumer_id: شناسه کاربر
        :param str currency_code: کد ارز
        :return: list
        """

        return self.__define_vouchers(service="defineCreditVoucher", vouchers=vouchers, guild_code=guild_code,
                                      expire_date=expire_date, limited_consumer_id=limited_consumer_id,
                                      currency_code=currency_code, **kwargs)

    def define_discount_amount_voucher(self, vouchers, guild_code, expire_date, limited_consumer_id=None,
                                       currency_code=None, product_id=None, dealer_business_id=None, **kwargs):
        """
        ایجاد بن تخفیف مبلغی

        :param list vouchers: لیست کد های اعتباری
        :param str guild_code: کد صنف
        :param str expire_date: تاریخ انقضا کدهای اعتباری
        :param int limited_consumer_id: شناسه کاربر
        :param str currency_code: کد ارز
        :param list product_id: لیست شناسه محصولاتی که میخواهید این کدهای تخفیف بر روی آن اعمال شود
        :param list dealer_business_id: لیست شناسه کسب و کارهای همکاری که می توانند از این تخفیف ها استفاده نمایند
        :return: list
        """

        return self.__define_vouchers(service="defineDiscountAmountVoucher", vouchers=vouchers, guild_code=guild_code,
                                      expire_date=expire_date, limited_consumer_id=limited_consumer_id,
                                      currency_code=currency_code, product_id=product_id,
                                      dealer_business_id=dealer_business_id, **kwargs)

    def define_discount_percentage_voucher(self, vouchers, guild_code, expire_date, discount_type,
                                           limited_consumer_id=None, currency_code=None, product_id=None,
                                           dealer_business_id=None, **kwargs):
        """
        ایجاد بن تخفیف درصدی

        مقدار `discount_type` می تواند یکی از موارد زیر باشد \n
        `PodVoucher.DISCOUNT_TYPE_ONE_TIME_ITEM` - محدود به یک آیتم\n
        `PodVoucher.DISCOUNT_TYPE_ONE_TIME_INVOICE` - محدود به یک فاکتور\n
        `PodVoucher.DISCOUNT_TYPE_UNLIMITED` - نامحدود\n

        :param list vouchers: لیست کد های اعتباری
        :param str guild_code: کد صنف
        :param str expire_date: تاریخ انقضا کدهای اعتباری
        :param int discount_type: نوع کد تخفیف
        :param int limited_consumer_id: شناسه کاربر
        :param str currency_code: کد ارز
        :param list product_id: لیست شناسه محصولاتی که میخواهید این کدهای تخفیف بر روی آن اعمال شود
        :param list dealer_business_id: لیست شناسه کسب و کارهای همکاری که می توانند از این تخفیف ها استفاده نمایند
        :return: list
        """
        kwargs["type"] = discount_type
        kwargs["discountPercentage[]"] = [voucher["discountPercentage"] for voucher in vouchers]

        return self.__define_vouchers(service="defineDiscountPercentageVoucher", vouchers=vouchers,
                                      guild_code=guild_code, expire_date=expire_date, discount_type=discount_type,
                                      limited_consumer_id=limited_consumer_id, currency_code=currency_code,
                                      product_id=product_id, dealer_business_id=dealer_business_id, **kwargs)

    def __define_vouchers(self, service, vouchers, guild_code, expire_date, limited_consumer_id=None,
                          currency_code=None, product_id=None, dealer_business_id=None, **kwargs):
        kwargs["vouchers"] = vouchers
        kwargs["guildCode"] = guild_code
        kwargs["expireDate"] = expire_date
        if limited_consumer_id is not None:
            kwargs["limitedConsumerId"] = limited_consumer_id
        if currency_code is not None:
            kwargs["currencyCode"] = currency_code
        if product_id is not None:
            if isinstance(product_id, list):
                kwargs["productId[]"] = product_id
            else:
                kwargs["productId[]"] = [product_id]

        if dealer_business_id is not None:
            if isinstance(dealer_business_id, list):
                kwargs["dealerBusinessId[]"] = dealer_business_id
            else:
                kwargs["dealerBusinessId[]"] = [dealer_business_id]

        self._validate(kwargs, service)
        (kwargs["name[]"], kwargs["amount[]"], kwargs["count[]"], kwargs["description[]"], kwargs["hash[]"]) = \
            self.__split_to_list(kwargs["vouchers"])
        del kwargs["vouchers"]

        if len(kwargs["hash[]"]) == 0:
            del kwargs["hash[]"]
        else:
            self.__check_count_hash(kwargs["count[]"], kwargs["hash[]"])

        return self._request.call(
            super(PodVoucher, self)._get_sc_product_settings("/nzh/biz/" + str(service), method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __check_count_hash(cnt_vouchers, hash_list):
        if sum(cnt_vouchers) == len(hash_list):
            return
        raise InvalidDataException(message="تعداد کدهای هش باید برابر با تعداد کد ها باشد.", error_code=887)

    @staticmethod
    def __split_to_list(vouchers):
        count = []
        amount = []
        name = []
        description = []
        voucher_hash = []

        for v in vouchers:
            count.append(v["count"])
            amount.append(v["amount"])
            name.append(v["name"])
            description.append(v["description"])
            if "hash" in v:
                voucher_hash += v["hash"]

        return name, amount, count, description, voucher_hash

    def apply_voucher(self, invoice_id, voucher_hash, preview=False, **kwargs):
        """
        اعمال کد تخفیف بر روی فاکتور

        :param int invoice_id: شناسه سفارش
        :param list voucher_hash: لیستی از کدهای تخفیف
        :param boolean preview: پیش نمایش اعمال ووچر روی فاکتور (در سیستم ثبت نمی گردد)
        :return: dict
        """
        kwargs["preview"] = preview
        kwargs["invoiceId"] = invoice_id
        if type(voucher_hash) != list:
            voucher_hash = [voucher_hash]
        kwargs["voucherHash"] = voucher_hash

        self._validate(kwargs, "applyVoucher")
        return self._request.call(
            super(PodVoucher, self)._get_sc_product_settings("/nzh/biz/applyVoucher", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def get_voucher_list(self, page=1, size=50, **kwargs):
        """
        دریافت لیست کدهای تخفیف

        :param int page: شماره صفحه
        :param int size: تعداد در هر صفحه
        :return: list
        """
        kwargs["offset"] = calc_offset(page=page, size=size)
        kwargs["size"] = size
        if "guildCode" in kwargs:
            kwargs["guildCode[]"] = kwargs["guildCode"]
            del kwargs["guildCode"]

        if "productId" in kwargs:
            kwargs["productId[]"] = kwargs["productId"]
            del kwargs["productId"]

        self._validate(kwargs, "getVoucherList")
        return self._request.call(super(PodVoucher, self)._get_sc_product_settings("/nzh/biz/getVoucherList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def activate_voucher(self, voucher_id, **kwargs):
        """
        فعال کردن یک کد تخفیف

        :param int voucher_id: شناسه کد تخفیف
        :return: dict
        """
        kwargs["id"] = voucher_id

        self._validate(kwargs, "activateVoucher")
        return self._request.call(
            super(PodVoucher, self)._get_sc_product_settings("/nzh/biz/activateVoucher", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    def deactivate_voucher(self, voucher_id, **kwargs):
        """
        غیرفعال کردن یک کد تخفیف

        :param int voucher_id: شناسه کد تخفیف
        :return: dict
        """
        kwargs["id"] = voucher_id

        self._validate(kwargs, "deactivateVoucher")
        return self._request.call(
            super(PodVoucher, self)._get_sc_product_settings("/nzh/biz/deactivateVoucher", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)
