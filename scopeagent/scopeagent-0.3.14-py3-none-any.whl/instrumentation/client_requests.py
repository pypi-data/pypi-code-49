import json
import logging
import io

import opentracing
import wrapt
from opentracing.ext import tags
from six.moves.urllib_parse import urlparse
import six

from ..tracer import tags as scope_tags
from . import run_once
from .http_utils import MAXIMUM_HTTP_PAYLOAD_SIZE, filter_http_headers

logger = logging.getLogger(__name__)


def is_file(possible_file):
    if six.PY3:
        return isinstance(possible_file, io.IOBase)
    return hasattr(possible_file, 'close') and hasattr(possible_file, 'write')


@run_once
def patch(tracer):
    def wrapper(wrapped, instance, args, kwargs):
        logger.debug('intercepting request: instance=%s args=%s kwargs=%s', instance, args, kwargs)
        request = args[0] if len(args) > 0 else kwargs['requests']
        parsed_url = urlparse(request.url)

        agent_metadata = tracer.recorder.metadata
        active_http_payloads = agent_metadata[scope_tags.HTTP_PAYLOADS]
        extra_http_headers = agent_metadata[scope_tags.HTTP_HEADERS]

        try:
            serialized_request_headers = json.dumps(filter_http_headers(request.headers, extra_http_headers))
        except Exception:
            serialized_request_headers = '{}'

        if active_http_payloads:
            sliced_request_payload = request.body
            if sliced_request_payload:
                # If it is a file, we don't want to affect it in any way
                if is_file(sliced_request_payload):
                    sliced_request_payload = 'not_accessible'
                else:
                    # For generators we can't a list index
                    try:
                        sliced_request_payload = sliced_request_payload[:MAXIMUM_HTTP_PAYLOAD_SIZE]
                    except TypeError:
                        sliced_request_payload = 'not_accessible'
        else:
            sliced_request_payload = 'disabled'

        with tracer.start_active_span(
            operation_name='HTTP %s' % request.method,
            tags={
                tags.SPAN_KIND: tags.SPAN_KIND_RPC_CLIENT,
                tags.HTTP_URL: request.url,
                tags.HTTP_METHOD: request.method,
                tags.PEER_ADDRESS: parsed_url.netloc,
                tags.PEER_PORT: parsed_url.port,
                scope_tags.HTTP_REQUEST_HEADERS: serialized_request_headers,
                scope_tags.HTTP_REQUEST_PAYLOAD: sliced_request_payload,
            },
        ) as scope:
            tracer.inject(scope.span.context, format=opentracing.Format.HTTP_HEADERS, carrier=request.headers)
            resp = wrapped(*args, **kwargs)
            try:
                serialized_response_headers = json.dumps(filter_http_headers(resp.headers, extra_http_headers))
            except Exception:
                serialized_response_headers = '{}'

            scope.span.set_tag(tags.HTTP_STATUS_CODE, resp.status_code)
            scope.span.set_tag(scope_tags.HTTP_RESPONSE_HEADERS, serialized_response_headers)

            # We only intercept if it is not a stream, if it is, we don't want to read the content
            # because it will fire the request. More info in
            # https://requests.readthedocs.io/en/master/user/advanced/#body-content-workflow
            if active_http_payloads:
                if not kwargs.get('stream', False):
                    sliced_response_payload = resp.content
                    if sliced_response_payload:
                        # For generators we can't a list index
                        try:
                            sliced_response_payload = sliced_response_payload[:MAXIMUM_HTTP_PAYLOAD_SIZE]
                        except TypeError:
                            sliced_response_payload = 'not_accessible'
                else:
                    sliced_response_payload = 'not_accessible'

            else:
                sliced_response_payload = 'disabled'

            scope.span.set_tag(
                scope_tags.HTTP_RESPONSE_PAYLOAD, sliced_response_payload,
            )

            if resp.status_code >= 400:
                scope.span.set_tag(tags.ERROR, True)
        return resp

    try:
        logger.debug('patching module=requests.adapters name=HTTPAdapter.send')
        wrapt.wrap_function_wrapper('requests.adapters', 'HTTPAdapter.send', wrapper)
    except ImportError:
        logger.debug('module not found module=requests.adapters')
