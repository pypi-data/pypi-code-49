"""
Wraps urllib.request (f.k.a. urllib2).
"""
import logging
import json

import opentracing
import six
import wrapt
from opentracing.ext import tags
from six.moves.urllib_parse import urlparse

from . import run_once
from .http_utils import MAXIMUM_HTTP_PAYLOAD_SIZE, filter_http_headers
from ..tracer import tags as scope_tags

logger = logging.getLogger(__name__)


@run_once
def patch(tracer):
    def wrapper(wrapped, instance, args, kwargs):
        logger.debug('intercepting request: instance=%s args=%s kwargs=%s', instance, args, kwargs)

        request = args[1] if len(args) > 1 else kwargs['req']
        # Is there any better way to get this?
        if hasattr(request, 'full_url'):
            url = request.full_url  # py3
        else:
            url = request._Request__original  # py2
        parsed_url = urlparse(url)
        method = request.get_method()

        agent_metadata = tracer.recorder.metadata
        active_http_payloads = agent_metadata[scope_tags.HTTP_PAYLOADS]
        extra_http_headers = agent_metadata[scope_tags.HTTP_HEADERS]

        try:
            serialized_request_headers = json.dumps(filter_http_headers(request.headers, extra_http_headers))
        except (TypeError, ValueError):
            serialized_request_headers = '{}'

        if active_http_payloads:
            sliced_request_payload = request.data
            if sliced_request_payload:
                # For generators we can't a list index
                try:
                    sliced_request_payload = sliced_request_payload[:MAXIMUM_HTTP_PAYLOAD_SIZE]
                except TypeError:
                    sliced_request_payload = 'not_accessible'
        else:
            sliced_request_payload = 'disabled'

        with tracer.start_active_span(
            operation_name='HTTP %s' % method,
            tags={
                tags.SPAN_KIND: tags.SPAN_KIND_RPC_CLIENT,
                tags.HTTP_URL: url,
                tags.HTTP_METHOD: method,
                tags.PEER_ADDRESS: parsed_url.netloc,
                tags.PEER_PORT: parsed_url.port,
                scope_tags.HTTP_REQUEST_HEADERS: serialized_request_headers,
                scope_tags.HTTP_REQUEST_PAYLOAD: sliced_request_payload,
            },
        ) as scope:
            tracer.inject(scope.span.context, format=opentracing.Format.HTTP_HEADERS, carrier=request.headers)
            resp = wrapped(*args, **kwargs)
            scope.span.set_tag(tags.HTTP_STATUS_CODE, resp.code)
            if six.PY2:
                headers = dict(resp.headers.items())
                # payload can't be read in py2 because there is no peek method, so
                # the queue is consumed, which we don't want
                scope.span.set_tag(scope_tags.HTTP_RESPONSE_PAYLOAD, 'not_accessible')
            else:
                headers = dict(resp.getheaders())
                if active_http_payloads:
                    # This does not consume the stream so it shouldn't affect it
                    sliced_response_payload = resp.peek()
                    if sliced_response_payload:
                        # For generators we can't a list index
                        try:
                            sliced_response_payload = sliced_response_payload[:MAXIMUM_HTTP_PAYLOAD_SIZE]
                        except TypeError:
                            sliced_response_payload = 'not_accessible'
                else:
                    sliced_response_payload = 'disabled'
                scope.span.set_tag(
                    scope_tags.HTTP_RESPONSE_PAYLOAD, sliced_response_payload,
                )
            try:
                serialized_response_headers = json.dumps(filter_http_headers(headers, extra_http_headers))
            except (TypeError, ValueError):
                serialized_response_headers = '{}'

            scope.span.set_tag(scope_tags.HTTP_RESPONSE_HEADERS, serialized_response_headers)
            if resp.code >= 400:
                scope.span.set_tag(tags.ERROR, True)
        return resp

    if six.PY2:
        module = 'urllib2'
    else:
        module = 'urllib.request'
    name = 'AbstractHTTPHandler.do_open'
    logger.debug('patching module=%s name=%s', module, name)
    try:
        wrapt.wrap_function_wrapper(module, name, wrapper)
    except ImportError:
        logger.debug('module not found module=%s', module)
