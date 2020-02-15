# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c)2018, 恒生电子股份有限公司
# All rights reserved.
#
# 文件名称：i18n.py
# 摘    要：i18n
#
# 当前版本：V1.0.0
# 作    者：qianmx21829
# 完成日期：2018-10-20
# 备    注：本地化模块
###############################################################################


import os.path
from gettext import NullTranslations, translation

from IQCommon.logger import system_log
from IQCommon.pycompatibility import to_utf8


class Localization(object):

    def __init__(self, trans=None):
        self.trans = NullTranslations() if trans is None else trans

    def set_locale(self, locales, trans_dir=None):
        if locales[0] is None or "en" in locales[0].lower():
            self.trans = NullTranslations()
            return
        if "cn" in locales[0].lower():
            locales = ["zh_Hans_CN"]
        try:
            if trans_dir is None:
                trans_dir = os.path.join(
                    os.path.dirname(
                        os.path.abspath(
                            __file__,
                        ),
                    ),
                    "translations"
                )
            self.trans = translation(
                domain="messages",
                localedir=trans_dir,
                languages=locales,
            )
        except Exception as e:
            system_log.debug(e)
            self.trans = NullTranslations()


localization = Localization()


def get_local_text(message):
    """
    用于本地化多国语言函数
    :param message:
    :return:
    """
    trans_txt = localization.trans.gettext(message)
    return to_utf8(trans_txt)
