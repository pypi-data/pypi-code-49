# coding=utf-8
class SubscriptionPlanPeriodType:
    """بازه های زمانی طرح اشتراک"""
    def __init__(self):
        pass
    """بازه زمانی سالانه"""
    YEARLY = "SUBSCRIPTION_PLAN_PERIOD_TYPE_YEARLY"
    """بازه زمانی ماهانه"""
    MONTHLY = "SUBSCRIPTION_PLAN_PERIOD_TYPE_MONTHLY"
    """بازه زمانی روزانه"""
    DAILY = "SUBSCRIPTION_PLAN_PERIOD_TYPE_DAILY"


class SubscriptionPlanPaymentType:
    """انواع روش های پرداخت، طرح اشتراک"""
    def __init__(self):
        pass
    """طرح مسدودی"""
    BLOCK = "SUBSCRIPTION_PLAN_TYPE_BLOCK"
    """طرح نقدی"""
    CASH = "SUBSCRIPTION_PLAN_TYPE_CASH"
    """طرح پس پرداخت"""
    POST_PAID = "SUBSCRIPTION_PLAN_TYPE_POST_PAID"


class SubscriptionPlanSettlementPeriodType:
    """انواع دوره‌های تصفیه طرح اشتراک"""
    def __init__(self):
        pass
    """دوره‌ی تصفیه سالانه"""
    YEARLY = "SUBSCRIPTION_PLAN_SETTLEMENT_PERIOD_TYPE_YEARLY"
    """دوره‌ی تصفیه ماهانه"""
    MONTHLY = "SUBSCRIPTION_PLAN_SETTLEMENT_PERIOD_TYPE_MONTHLY"
    """دوره‌ی تصفیه روزانه"""
    DAILY = "SUBSCRIPTION_PLAN_SETTLEMENT_PERIOD_TYPE_DAILY"
    """دوره‌ی تصفیه هفتگی"""
    WEEKLY = "SUBSCRIPTION_PLAN_SETTLEMENT_PERIOD_TYPE_WEEKLY"


class SubscriptionStatus:
    """وضعیت های اشتراک"""
    def __init__(self):
        pass

    CONFIRM = "SUBSCRIPTION_CONFIRM"
    NOT_VERIFY = "SUBSCRIPTION_NOT_VERIFY"
    REVOKED = "SUBSCRIPTION_REVOKED"
