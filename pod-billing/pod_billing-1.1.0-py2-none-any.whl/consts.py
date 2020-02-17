# coding=utf-8


class ToolCodeSettlement:
    """
    کد ابزارهای تسویه
    """

    """کارت به کارت"""
    CARD = "SETTLEMENT_TOOL_CARD"

    """پایا"""
    PAYA = "SETTLEMENT_TOOL_PAYA"

    """ساتنا"""
    SATNA = "SETTLEMENT_TOOL_SATNA"

    def __init__(self):
        pass


class StatusSettlement:
    """
    وضعیت های درخواست های تسویه
    """

    """تسویه حساب انجام شده است"""
    DONE = "SETTLEMENT_DONE"

    """تسویه درخواست داده شده و تایید نشده است"""
    REQUESTED = "SETTLEMENT_REQUESTED"

    """تسویه تایید شده و ارسال شده است"""
    SENT = "SETTLEMENT_SENT"

    """تسویه توسط درخواست دهنده لغو شده یا تایید نشده است"""
    CANCELED = "SETTLEMENT_CANCELED"

    """در هنگام ارسال درخواست تسویه، خطا رخ داده است. در صورت دریافت وضعیت خود به خود به روز رسانی میگردد در غیر این 
    صورت نیاز به بررسی دارد تا در صورت عدم واریز به حساب مجازی برگردانده شود """
    EXCEPTION_IN_SENDING = "SETTLEMENT_EXCEPTION_IN_SENDING"

    """در مواقع بسیار نادری ممکن است در اثر خطای داخلی تسویه در این وضعیت بماند که نیاز به بررسی دارد"""
    CONFIRMING = "SETTLEMENT_CONFIRMING"

    """در صورت بروز خطا در عملیات انتقال وجه و لغو تراکنش یا رد شدن درخواست توسط بانک مقابل این وضعیت رخ می دهد."""
    REJECTED = "SETTLEMENT_REJECTED"

    def __init__(self):
        pass

