from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.utils import timezone
from ipware.ip import get_real_ip
import logging


logger = logging.getLogger(__name__)


def build_auth_log_string(message: str, username: str, email: str, request):
    """
    Build a string with user and auth info for logging
    """
    msg = "{message} username:[{username}] email:[{email}] ip:[{ipaddr}] datetime:[{now}]".format(
        message=message,
        username=username or '',
        email=email or '',
        ipaddr=get_real_ip(request) if request else '',
        now=timezone.now())
    return msg


def handle_user_logged_in(sender, user=None, request=None, **kwargs):
    username, email = (None, None) if user is None else (user.username, user.email)
    log_string = build_auth_log_string("User Login Successful", username, email, request)
    logger.info(log_string)


def handle_user_login_failed(sender, credentials, request=None, **kwargs):
    username = credentials.get('username', None)
    email = credentials.get('email', None)
    log_string = build_auth_log_string("User Login Failed", username, email, request)
    logger.info(log_string)


user_logged_in.connect(handle_user_logged_in)
user_login_failed.connect(handle_user_login_failed)
