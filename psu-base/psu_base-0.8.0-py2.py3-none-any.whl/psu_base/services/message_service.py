from psu_base.classes.Log import Log
from psu_base.services import utility_service
from django.contrib import messages
log = Log()


def post_info(msg):
    return post_message(msg, "info")


def post_success(msg):
    return post_message(msg, "success")


def post_warning(msg):
    return post_message(msg, "warning")


def post_error(msg):
    return post_message(msg, "error")


def post_message(msg, msg_type):
    request = utility_service.get_request()
    message = str(msg)

    if request is None:
        log.error(f"Request does not exist. Could not post message: {message}")
    else:
        if msg_type == "info":
            messages.info(request, message)
            log.info(message)
        elif msg_type == "success":
            messages.success(request, message)
            log.info(message)
        elif msg_type == "warning":
            messages.warning(request, message)
            log.warning(message)
        elif msg_type == "error":
            messages.error(request, message)
            log.error(message, trace_error=False)

    return None
