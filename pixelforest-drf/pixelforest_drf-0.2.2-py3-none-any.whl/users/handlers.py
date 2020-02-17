# Imports ##############################################################################################################
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in


# Signals handling #####################################################################################################

@receiver(user_logged_in, dispatch_uid='update_last_login')
def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
