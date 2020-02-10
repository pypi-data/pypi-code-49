import logging

from logging import CRITICAL, WARNING

from hologger.middleware import HoLoggingMiddleware
from django.core.handlers.wsgi import WSGIRequest
from django.core.signals import got_request_exception, request_finished
from django.dispatch import receiver

from logging import INFO


def get_current_environ():
    thread_local = HoLoggingMiddleware.thread_local

    if hasattr(thread_local, 'status'):
        status = thread_local.status
        delattr(thread_local, 'status')
    else:
        status = None

    if hasattr(thread_local, 'request'):
        request = thread_local.request
        delattr(thread_local, 'request')
    else:
        request = None

    if hasattr(thread_local, 'response'):
        response = thread_local.response
        delattr(thread_local, 'response')
    else:
        response = None

    if hasattr(thread_local, 'body'):
        body = thread_local.body
        delattr(thread_local, 'body')
    else:
        body = None

    if hasattr(thread_local, 'pid'):
        pid = thread_local.pid
        delattr(thread_local, 'pid')
    else:
        pid = None

    if hasattr(thread_local, 'query'):
        query = thread_local.query
        delattr(thread_local, 'query')
    else:
        query = None

    return status, response, request, body, pid, query


@receiver(request_finished, weak=False)
def request_finished_callback(sender, **kwargs):
    logger = logging.getLogger(__name__)
    level = INFO

    status, response, request, body, pid, query = get_current_environ()

    logger.log(level, "", extra={
        'action': 'request',
        'data': {
            'status': status,
            'response': response,
            'request': request,
            'body': body,
            'pid': pid,
            'query': query
        }
    })


@receiver(got_request_exception, weak=False)
def request_exception(sender, request, **kwargs):
    if not isinstance(request, WSGIRequest):
        logger = logging.getLogger(__name__)
        level = CRITICAL if request.status_code <= 500 else WARNING

        logger.log(level, '%s exception occured (%s)',
                   request.status_code, request.reason_phrase)

    else:
        logger = logging.getLogger(__name__)
        logger.log(WARNING, 'WSGIResponse exception occured')
