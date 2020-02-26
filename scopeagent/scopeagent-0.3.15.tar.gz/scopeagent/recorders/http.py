import gzip
import io
import logging
import uuid

import certifi
import msgpack

import urllib3

from .asyncrecorder import AsyncRecorder
from ..formatters.dict import DictFormatter
from ..tracer import tags
from .utils import UnrecoverableClientError, RecoverableClientError

logger = logging.getLogger(__name__)

INGEST_NUM_RETRIES = 10
INGEST_TIMEOUT = 10

MAXIMUM_NUMBER_OF_SPANS_TO_INGEST = 1000
MAXIMUM_NUMBER_OF_EVENTS_TO_INGEST = 1000


class HTTPRecorder(AsyncRecorder):
    def __init__(self, api_key, api_endpoint, metadata=None, dry_run=False, **kwargs):
        super(HTTPRecorder, self).__init__(**kwargs)
        self._api_key = api_key
        self._api_endpoint = api_endpoint
        self._ingest_endpoint = "%s/%s" % (self._api_endpoint, 'api/agent/ingest')
        self.metadata = metadata or {}
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        self.dry_run = dry_run
        self.spans_left_to_send = []
        self.events_left_to_send = []

    UNRECOVERABLE_HTTP_STATUSES = [401, 403, 404]
    RECOVERABLE_HTTP_STATUSES = [400]

    def _send_payload(self):
        payload = {
            "metadata": self.metadata,
            "agent.id": self.metadata[tags.AGENT_ID],
            "spans": [],
            "events": [],
        }
        payload['spans'] = self.spans_left_to_send[:MAXIMUM_NUMBER_OF_SPANS_TO_INGEST]
        payload['events'] = self.events_left_to_send[:MAXIMUM_NUMBER_OF_EVENTS_TO_INGEST]
        logger.debug('sending payload to server: %s', payload)
        self._send(payload)
        self.spans_left_to_send = self.spans_left_to_send[MAXIMUM_NUMBER_OF_SPANS_TO_INGEST:]
        self.events_left_to_send = self.events_left_to_send[MAXIMUM_NUMBER_OF_EVENTS_TO_INGEST:]

    def flush_final_payload(self):
        while len(self.spans_left_to_send) > 0 or len(self.events_left_to_send) > 0:
            self._send_payload()

    def flush(self, spans):
        for span in spans:
            span_dict = DictFormatter.dumps(span)
            events = span_dict.pop('logs')
            self.spans_left_to_send.append(span_dict)
            span_context = span_dict['context']
            for event in events:
                event['context'] = {
                    'trace_id': span_context['trace_id'],
                    'span_id': span_context['span_id'],
                    'event_id': str(uuid.uuid4()),
                }
                self.events_left_to_send.append(event)

        self._send_payload()

    def _send(self, body):
        from .. import version

        payload_msgpack = msgpack.dumps(body, default=lambda value: str(value))
        logger.debug("uncompressed msgpack payload size is %d bytes", len(payload_msgpack))
        out = io.BytesIO()
        with gzip.GzipFile(fileobj=out, mode="wb") as f:
            f.write(payload_msgpack)
        payload_gzip = out.getvalue()
        logger.debug("compressed gzip payload size is %d bytes", len(payload_gzip))

        headers = {
            "User-Agent": "scope-agent-python/%s" % version,
            "Content-Type": "application/msgpack",
            "X-Scope-ApiKey": self._api_key,
            "Content-Encoding": "gzip",
        }
        if not self.dry_run:
            resp = self.http.request(
                'POST',
                self._ingest_endpoint,
                headers=headers,
                body=payload_gzip,
                retries=INGEST_NUM_RETRIES,
                timeout=INGEST_TIMEOUT,
            )
            if resp.status in self.UNRECOVERABLE_HTTP_STATUSES:
                raise UnrecoverableClientError(
                    'Unrecoverable client error {status} in ingest'.format(status=resp.status)
                )
            if resp.status in self.RECOVERABLE_HTTP_STATUSES:
                raise RecoverableClientError('Recoverable client error {status} in ingest'.format(status=resp.status))

            logger.debug("response from server: %d %s", resp.status, resp.data)
        else:
            logger.debug("dry run active, payload not sent to server")
