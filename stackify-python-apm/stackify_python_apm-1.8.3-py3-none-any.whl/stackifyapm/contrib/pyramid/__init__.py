import os
import pkg_resources
import sys

from stackifyapm.base import Client
from stackifyapm.conf import constants
from stackifyapm.handlers.exceptions import get_exception_context
from stackifyapm.utils.helper import can_insert_script
from stackifyapm.utils.helper import get_stackify_header
from stackifyapm.instrumentation.control import instrument
from stackifyapm.traces import execution_context
from stackifyapm.traces import set_transaction_context
from stackifyapm.utils import get_url_data
from stackifyapm.utils.helper import get_rum_script_or_None


def includeme(config):
    config.add_tween('stackifyapm.contrib.pyramid.stackifyapm_tween_factory')
    config.scan('stackifyapm.contrib.pyramid')


def get_data_from_request(request):
    return {
        "headers": dict(**request.headers),
        "method": request.method,
        "url": get_url_data(request.url),
    }


def get_data_from_response(response=None):
    return {
        "status_code": response and response.status_int or 500,
    }


def make_client(registry, **defaults):
    config = {
        "FRAMEWORK_NAME": "pyramid",
        "FRAMEWORK_VERSION": pkg_resources.get_distribution("pyramid").version,
        "BASE_DIR": os.getcwd(),
    }
    defaults.update(registry.settings)

    return Client(config, **defaults)


class stackifyapm_tween_factory(object):
    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry
        self.client = make_client(registry)
        instrument(client=self.client)

    def __call__(self, request):
        response = None
        self.client.begin_transaction('request', client=self.client)
        try:
            transaction = execution_context.get_transaction()

            response = self.handler(request)
            response.headers["X-StackifyID"] = get_stackify_header(transaction)

            if self.client.config.rum_enabled:
                set_transaction_context(lambda: True, "rum")
                # adding RUM Cookie
                response.set_cookie(
                    constants.RUM_COOKIE_NAME,
                    str(transaction.get_trace_parent().trace_id),
                )

            if self.client.config.rum_auto_injection:
                rum_script = get_rum_script_or_None(transaction)
                data = response.text
                if rum_script and can_insert_script(data):
                    data = data.replace('</head>', '{}</head>'.format(rum_script))
                    response.text = data

            return response
        except Exception:
            exc_info = sys.exc_info()
            if exc_info:
                exception = exc_info[1]
                traceback = exc_info[2]
                self.client.capture_exception(
                    exception=get_exception_context(exception, traceback)
                )
            raise
        finally:
            transaction_name = request.matched_route.pattern if request.matched_route else request.view_name
            transaction_name = " ".join((request.method, transaction_name)) if transaction_name else ""
            set_transaction_context(lambda: get_data_from_request(request), "request")
            set_transaction_context(lambda: get_data_from_response(response), "response")
            self.client.end_transaction(transaction_name)
