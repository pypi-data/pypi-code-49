from django.conf import settings

NOTIFICATION_SERVICES = getattr(settings, "ORION_NOTIFICATION_SERVICES", {
    "firebase-push": "orionframework.notifications.services.firebase.FirebasePushNotificationService",
    "firebase-web-push": "orionframework.notifications.services.firebase.FirebaseWebPushNotificationService"
})

NOTIFICATION_ENABLED = getattr(settings, "ORION_NOTIFICATION_ENABLED", False)
NOTIFICATION_DEBUG = getattr(settings, "ORION_NOTIFICATION_DEBUG", False)
