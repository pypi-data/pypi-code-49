import fnmatch
import enum
import uuid
import aiohttp
from django.db import models
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save


class EventTypes(enum.Enum):
    CONSUMER_REGISTRATION_SESSION_CREATED = 'consumer/registration/created'
    CONSUMER_REGISTRATION_SESSION_UPDATED = 'consumer/registration/updated'
    CONSUMER_REGISTRATION_SESSION_VALIDATED = 'consumer/registration/validated'
    CONSUMER_REGISTRATION_SESSION_VERIFYED = 'consumer/registration/verifyed'

    CONSUMER_UPDATE_PASSWORD_REQUEST_CREATED = 'consumer/password/update/created'
    CONSUMER_UPDATE_PASSWORD_REQUEST_VERIFYED = 'consumer/password/update/verifyed'

    CONSUMER_UPDATE_EMAIL_SESSION_CREATED = 'consumer/email/update/created'
    CONSUMER_UPDATE_EMAIL_SESSION_VALIDATED = 'consumer/email/update/validated'
    CONSUMER_UPDATE_EMAIL_SESSION_VERIFYED = 'consumer/email/update/verifyed'

    CONSUMER_UPLOAD_IDENTITY_CREATED = 'consumer/identity/created'

    MERCHANT_REGISTRATION_SESSION_CREATED = 'merchant/registration/created'
    MERCHANT_REGISTRATION_SESSION_UPDATED = 'merchant/registration/updated'
    MERCHANT_REGISTRATION_SESSION_VALIDATED = 'merchant/registration/validated'
    MERCHANT_REGISTRATION_SESSION_VERIFYED = 'merchant/registration/verifyed'

    MERCHANT_UPDATE_PASSWORD_REQUEST_CREATED = 'merchant/password/update/created'
    MERCHANT_UPDATE_PASSWORD_REQUEST_VERIFYED = 'merchant/password/update/verifyed'

    MERCHANT_CREATE_PUBLIC_PRIVATE_TOKENS = 'merchant/tokens/public_private/created'

    CHECKOUT_CREATED = 'checkout/created'
    CHECKOUT_CUSTOMER_CREATED = 'checkout/customer/created'
    CHECKOUT_ORDER_PREAPPROVED = 'checkout/order/preapproved'
    CHECKOUT_ORDER_CONFIRMED = 'checkout/order/confirmed'

    ORDER_CREATED = 'order/created'
    CUSTOMER_CREATED = 'customer/created'

    PAYMENT_METHODS_CREATED = 'payment_methods/created'
    PAYMENT_METHODS_UPDATED = 'payment_methods/updated'
    PAYMENT_METHODS_DELETED = 'payment_methods/deleted'

    INSTALLMENTS_ESTIMATION_CREATED = 'installments/estimation/created'
    INSTALLMENTS_CREATED = 'installments/created'

    BILLING_ADDRESS_CREATED = 'billing_address/created'
    BILLING_ADDRESS_UPDATED = 'billing_address/updated'
    BILLING_ADDRESS_DELETED = 'billing_address/deleted'

    ORDER_CAPTURED = 'order/captured'
    ORDER_REFUNDED = 'order/refunded'
    ORDER_REPORT_CREATED = 'order/report/created'
    ORDER_PAYED = 'order/payed'

    SETTLEMENTS_REPORT_CREATED = 'settlements/report/created'
    REFUNDS_REPORT_CREATED = 'refunds/report/created'

    BANK_ACCOUNT_CREATED = 'bank_accounts/created'
    BANK_ACCOUNT_UPDATED = 'bank_accounts/updated'
    BANK_ACCOUNT_DELETED = 'bank_accounts/deleted'

    USER_EMAIL_VERIFYED = 'user/email/verifyed'
    USER_SIGNIN_BY_TOKEN = 'user/signin/token'
    USER_SIGNIN_BY_USERNAME = 'user/signin/username'


class Event(models.Model):
    event_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    event_type = models.CharField(max_length=254)
    object_type = models.CharField(max_length=254, null=True, blank=True)
    object_id = models.CharField(max_length=255, null=True, blank=True)
    account_id = models.UUIDField(null=True, blank=True)
    meta_data = JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    registerd_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def data(self) -> dict:
        return {
            "event_id":  str(self.event_id),
            "event_type": self.event_type,
            "object_type": self.object_type if self.object_type else None,
            "object_id": str(self.object_id) if self.object_id else None,
            "account_id": str(self.account_id) if self.account_id else None,
            "meta_data": self.meta_data if self.meta_data else None,
        }

    def register(self):
        push_notifications = PushNotification.actual_objects.filter(
            created_at__lte=self.created_at
        ).all()

        for push_notification in push_notifications:
            if fnmatch.fnmatch(self.event_type, push_notification.pattern):
                PushNotificationEvent.objects.get_or_create(
                    event=self, push_notification=push_notification
                )


@receiver(post_save, sender=Event)
def event_registrator(sender, **kwargs):
    event = kwargs.get("instance", None)
    if event:
        event.register()


class PushNotificationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class PushNotification(models.Model):
    push_notification_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    callback_url = models.URLField()
    pattern = models.CharField(max_length=10000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = models.Manager()
    actual_objects = PushNotificationManager()

    class Meta:
        verbose_name = "push notification"
        verbose_name_plural = "push notifications"
        unique_together = [
            'callback_url', 'pattern',
        ]


class PushNotificationEventManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(processed_at__isnull=True)


class PushNotificationEvent(models.Model):
    push_notification = models.ForeignKey(
        PushNotification, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    retry = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True)
    last_retried_at = models.DateTimeField(null=True)

    objects = models.Manager()
    actual_objects = PushNotificationEventManager()

    class Meta:
        verbose_name = "push notification event"
        verbose_name_plural = "push notification events"
        unique_together = ["push_notification", "event"]
        indexes = [
            models.Index(fields=["processed_at", "retry", "last_retried_at"]),
        ]

    async def post(self, session: aiohttp.ClientSession) -> aiohttp.ClientResponse:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "SpotiiPush/1.0 (https://www.spotii.me/bot.html)",
        }
        async with session:
            res = await session.post(
                self.push_notification.callback_url, json=self.event.data(),
                headers=headers)
            return res
