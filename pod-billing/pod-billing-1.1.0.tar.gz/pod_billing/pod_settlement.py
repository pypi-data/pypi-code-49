# coding=utf-8
from __future__ import absolute_import
from os import path

from pod_base import PodBase, calc_offset, InvalidDataException
from pod_common import PodCommon
from .consts import ToolCodeSettlement


class PodSettlement(PodBase):
    __slots__ = "__common"

    def __init__(self, api_token, token_issuer="1", server_type="sandbox", config_path=None,
                 sc_api_key="", sc_voucher_hash=None):
        here = path.abspath(path.dirname(__file__))
        self._services_file_path = path.join(here, "services_settlement.json")
        super(PodSettlement, self).__init__(api_token, token_issuer, server_type, config_path, sc_api_key,
                                            sc_voucher_hash, path.join(here, "json_schema_settlement.json"))

        self.__common = PodCommon(api_token=self._api_token, token_issuer=self._token_issuer,
                                  server_type=self._server_type, config_path=config_path,
                                  sc_api_key=self._default_params["sc_api_key"],
                                  sc_voucher_hash=self._default_params["sc_voucher_hash"])

    def request_wallet_settlement(self, amount, **kwargs):
        """
        درخواست تسویه کیف پول

        :param float amount: مبلغ برداشت
        :return: dict
        """
        kwargs["amount"] = amount
        kwargs = self.__prepare_request_settlement(**kwargs)

        self._validate(kwargs, "requestWalletSettlement")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/requestSettlement"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    def request_guild_settlement(self, amount, guild_code, **kwargs):
        """
        درخواست تسویه از حساب صنفی

        :param float amount: مبلغ برداشت
        :param str guild_code: کد صنف
        :return: dict
        """
        kwargs["amount"] = amount
        kwargs["guildCode"] = guild_code
        kwargs = self.__prepare_request_settlement(**kwargs)
        self._validate(kwargs, "requestGuildSettlement")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/biz/requestSettlement"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    def __prepare_request_settlement(self, **kwargs):
        kwargs["_ott_"] = kwargs.pop("ott", kwargs.pop("_ott_", None))
        if kwargs["_ott_"] is None:
            kwargs["_ott_"] = self.__common.get_ott()

        if "sheba" in kwargs:
            kwargs["sheba"] = kwargs["sheba"][-24:]

        return kwargs

    def request_settlement_by_tool(self, amount, guild_code, tool_code, tool_id, **kwargs):
        """
        درخواست تسویه از حساب صنفی به حساب بانکی با استفاده از ابزار

        :param float amount: مبلغ برداشت
        :param str guild_code: کد صنف
        :param str tool_code: کد ابزار
        :param str tool_id: شماره ابزار
        :return: dict
        """
        if tool_code != ToolCodeSettlement.CARD:
            tool_id = tool_id[-24:]

        kwargs["toolCode"] = tool_code
        kwargs["toolId"] = tool_id
        kwargs["amount"] = amount
        kwargs["guildCode"] = guild_code
        self.__check_tool_id(kwargs["toolCode"], kwargs["toolId"])

        self._validate(kwargs, "requestSettlementByTool")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/biz/requestSettlementByTool"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    @staticmethod
    def __check_tool_id(tool_code, tool_id):
        if tool_code == ToolCodeSettlement.CARD:
            if len(tool_id) == 16:
                return

        if len(tool_id) == 24:
            return

        raise InvalidDataException(message="طول شماره کارت/شبا نامعتبر است", error_code=887)

    def list_settlements(self, page=1, size=50, **kwargs):
        """
        لیست درخواست های تسویه

        :param int page: شماره صفحه
        :param int size: اندازه صفحه
        :return: list dict
        """
        kwargs["offset"] = calc_offset(page, size)
        kwargs["size"] = size

        self._validate(kwargs, "listSettlements")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/listSettlements"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    def add_auto_settlement(self, guild_code, **kwargs):
        """
        فعالسازی تسویه خودکار

        :param str guild_code: کد صنف
        :return: bool
        """
        kwargs["guildCode"] = guild_code

        self._validate(kwargs, "addAutoSettlement")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/biz/addAutoSettlement"), params=kwargs,
            headers=self._get_headers(), **kwargs)

    def remove_auto_settlement(self, guild_code, **kwargs):
        """
        حذف تسویه خودکار

        :param str guild_code: کد صنف
        :return: bool
        """
        kwargs["guildCode"] = guild_code

        self._validate(kwargs, "removeAutoSettlement")

        return self._request.call(
            super(PodSettlement, self)._get_sc_product_settings("/nzh/biz/removeAutoSettlement"), params=kwargs,
            headers=self._get_headers(), **kwargs)

