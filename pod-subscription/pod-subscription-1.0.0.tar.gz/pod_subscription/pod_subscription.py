# coding=utf-8
from os import path
from pod_base import PodBase, calc_offset, ConfigException, InvalidDataException
from .consts import SubscriptionPlanPaymentType


class PodSubscription(PodBase):
    __slots__ = ("export", "payment", "__common")

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services.json")
        super(PodSubscription, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                              sc_voucher_hash, path.join(here, "json_schema.json"))

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

    def add_subscription_plan(self, product_id, name, price, period_type, period_type_count, subscription_payment_type,
                              guild_code, **kwargs):
        """
        تعریف طرح اشتراک

        :param int product_id: شناسه محصول طرح
        :param str name: نام طرح
        :param float price: هزینه طرح
        :param str period_type: بازه زمانی طرح
        :param int period_type_count: تعداد مورد نظر از بازه زمانی
        :param str subscription_payment_type: نوع طرح - مسدودی، نقدی و یا پس پرداخت
        :param str guild_code: صنف طرح
        :return: dict
        """
        kwargs["productId"] = product_id
        kwargs["name"] = name
        kwargs["price"] = price
        kwargs["guildCode"] = guild_code
        kwargs["periodTypeCode"] = period_type
        kwargs["periodTypeCount"] = period_type_count
        kwargs["type"] = subscription_payment_type

        self.__check_post_paid_condition(kwargs)

        self._validate(kwargs, "addSubscriptionPlan")

        if "permittedGuildCode" in kwargs:
            kwargs["permittedGuildCode[]"] = kwargs["permittedGuildCode"]
            del kwargs["permittedGuildCode"]

        if "permittedBusinessId" in kwargs:
            kwargs["permittedBusinessId[]"] = kwargs["permittedBusinessId"]
            del kwargs["permittedBusinessId"]

        if "permittedProductId" in kwargs:
            kwargs["permittedProductId[]"] = kwargs["permittedProductId"]
            del kwargs["permittedProductId"]

        return self._request.call(
            super(PodSubscription, self)._get_sc_product_settings("/nzh/biz/addSubscriptionPlan", method_type="post"),
            params=kwargs, headers=self._get_headers(), **kwargs)

    @staticmethod
    def __check_post_paid_condition(params):
        """
        بررسی شرایط حالت پس پرداخت
        :param dict params: پارامترها
        :return:
        """
        if params["type"] != SubscriptionPlanPaymentType.POST_PAID:
            return

        if params["price"] != 0:
            params = {
                "message": "در حالت پس پرداخت مبلغ طرح باید صفر وارد شود",
                "error_code": 887
            }
            raise InvalidDataException(**params)

        if "maxDebtorAmount" not in params:
            params = {
                "message": "در حالت پس پرداخت حداکثر مبلغ بدهی الزامی است",
                "error_code": 887
            }
            raise InvalidDataException(**params)

        if "settlementPeriodTypeCode" not in params:
            params = {
                "message": "در حالت پس پرداخت دوره‌ی تصفیه الزامی است",
                "error_code": 887
            }
            raise InvalidDataException(**params)

    def subscription_plan_list(self, page=1, size=50, **kwargs):
        """
        دریافت لیست طرح های اشتراک ثبت شده

        :param int page: شماره صفحه
        :param int size: تعداد رکورد در هر صفحه
        :return: list
        """
        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size

        self._validate(kwargs, "subscriptionPlanList")
        return self._request.call(
            super(PodSubscription, self)._get_sc_product_settings("/nzh/biz/subscriptionPlanList"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    def update_subscription_plan(self, subscription_plan_id, **kwargs):
        """
        ویرایش طرح اشتراک

        :param int subscription_plan_id: شناسه طرح اشتراک
        :return: dict
        """
        kwargs["id"] = subscription_plan_id

        self._validate(kwargs, "updateSubscriptionPlan")
        return self._request.call(super(PodSubscription, self)
                                  ._get_sc_product_settings("/nzh/biz/updateSubscriptionPlan", method_type="post"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def request_subscription(self, subscription_plan_id, user_id, **kwargs):
        """
        فعال‌سازی طرح اشتراک

        :param int subscription_plan_id: شناسه طرح اشتراک
        :param int user_id: شناسه کاربر
        :return: dict
        """
        kwargs["subscriptionPlanId"] = subscription_plan_id
        kwargs["userId"] = user_id

        self._validate(kwargs, "requestSubscription")
        return self._request.call(super(PodSubscription, self)
                                  ._get_sc_product_settings("/nzh/biz/requestSubscription", method_type="post"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def confirm_subscription(self, subscription_id, code, **kwargs):
        """
        تایید فعال‌سازی طرح اشتراک

        :param int subscription_id: شناسه عضویت کاربر در طرح
        :param str code: کد فعال سازی
        :return: dict
        """
        kwargs["subscriptionId"] = subscription_id
        kwargs["code"] = code

        self._validate(kwargs, "confirmSubscription")
        return self._request.call(super(PodSubscription, self)
                                  ._get_sc_product_settings("/nzh/biz/confirmSubscription", method_type="post"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def revoke_subscription(self, subscription_id, **kwargs):
        """
        لغو طرح اشتراک

        :param int subscription_id: شناسه عضویت کاربر در طرح
        :return: dict
        """
        kwargs["subscriptionId"] = subscription_id

        self._validate(kwargs, "revokeSubscription")
        return self._request.call(super(PodSubscription, self)
                                  ._get_sc_product_settings("/nzh/biz/revokeSubscription", method_type="post"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def subscription_list(self, subscription_plan_id, page=1, size=50, **kwargs):
        """
        لیست اشتراک‌ها (مشترک)

        :param int subscription_plan_id: شناسه طرح مورد نظر
        :param int page: شماره صفحه
        :param int size: تعداد رکورد در خروجی
        :return: list
        """
        kwargs["subscriptionPlanId"] = subscription_plan_id
        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size

        self._validate(kwargs, "subscriptionList")
        return self._request.call(super(PodSubscription, self)._get_sc_product_settings("/nzh/biz/subscriptionList"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def user_subscription_list(self, access_token, subscription_plan_id=None, page=1, size=50, **kwargs):
        """
        لیست طرح های کاربر

        :param str access_token: اکسس توکن کاربر
        :param int subscription_plan_id: شناسه طرح مورد نظر
        :param int page: شماره صفحه
        :param int size: تعداد رکورد در خروجی
        :return: list
        """
        if subscription_plan_id is not None:
            kwargs["subscriptionPlanId"] = subscription_plan_id

        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size

        self._validate(kwargs, "userSubscriptionList")
        headers = self._get_headers()
        headers["_token_"] = access_token
        return self._request.call(super(PodSubscription, self)._get_sc_product_settings("/nzh/subscriptionList"),
                                  params=kwargs, headers=headers, **kwargs)

    def consume_subscription(self, subscription_id, used_amount=None, **kwargs):
        """
        مصرف اشتراک

        :param int subscription_id: شناسه طرح
        :param float used_amount: میزان استفاده از اشتراک
        :return: dict
        """
        kwargs["id"] = subscription_id
        if used_amount is not None:
            kwargs["usedAmount"] = used_amount

        self._validate(kwargs, "consumeSubscription")
        return self._request.call(super(PodSubscription, self)._get_sc_product_settings("/nzh/biz/consumeSubscription"),
                                  params=kwargs, headers=self._get_headers(), **kwargs)

    def pay_subscription_debt(self, subscription_id, access_token, **kwargs):
        """
        پرداخت بدهی طرح پس پرداخت

        :param int subscription_id: شناسه عضویت کاربر در طرح اشتراک
        :param str access_token: اکسس توکن کاربر
        :return: dict
        """
        kwargs["id"] = subscription_id
        headers = self._get_headers()
        headers["_token_"] = access_token

        self._validate(kwargs, "paySubscriptionDebt")
        return self._request.call(
            super(PodSubscription, self)._get_sc_product_settings("/nzh/paySubscriptionDebt", method_type="post"),
            params=kwargs, headers=headers, **kwargs)
