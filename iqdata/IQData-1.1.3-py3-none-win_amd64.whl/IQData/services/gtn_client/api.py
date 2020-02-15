# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：api.py
# 摘    要：IQData数据库对外暴露接口
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2019-05-06
# 备    注：
###############################################################################
from . import settings
from .gtn_client import create_gtn_client as base_create_gtn_client

__all__ = ['create_gtn_client']


def create_gtn_client(app_key=None, app_secret=None, base_url=None):
    if app_key is not None:
        app_key_tmp = app_key
    else:
        app_key_tmp = settings.gtn.app_key
    if app_secret is not None:
        app_secret_tmp = app_secret
    else:
        app_secret_tmp = settings.gtn.secret
    if base_url is not None:
        base_url_tmp = base_url
    else:
        base_url_tmp = settings.gtn.url

    return base_create_gtn_client(
        app_key_tmp,
        app_secret_tmp,
        base_url_tmp,
    )
