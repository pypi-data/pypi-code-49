import json
import logging
import threading
import time
from queue import Queue

from biz_monitor.biz_tracing.tracer import TREE_LEVEL_KEY, HTTP_URI
from jaeger_client.span import Span
from kafka import KafkaProducer
from opentracing.ext import tags

logger = logging.getLogger(__name__)

queue = Queue(maxsize=100)
METRICS_TOPIC = "uploadMetric"


class KafkaMetricsCollector:
    def __init__(self, kafka_uri, service_name, idc_name, set_name, instance_id):
        self.service_name = service_name
        self.idc_name = idc_name
        self.set_name = set_name
        self.instance_id = instance_id

        self.kafka_producer = KafkaProducer(bootstrap_servers=kafka_uri,
                                            value_serializer=lambda v: json.dumps(v).encode())
        self.running = False
        if not self.running:
            t = threading.Thread(target=self._consume_queue, daemon=True)
            t.start()

    def _consume_queue(self):
        self.running = True
        while True:
            data = queue.get()
            self._metrics(data)

    def report_span(self, span: Span, biz_code: str):
        try:
            self._report_span(span, biz_code)
        except Exception as e:
            logger.exception(f"Got an error while reporting span:{e}")

    def _report_span(self, span: Span, biz_code: str):
        span_tags = {tag.key: tag.vStr or tag.vDouble or tag.vBool or tag.vLong or tag.vBinary for tag in span.tags}
        timestamp = time.time()
        metrics_data = {
            "idcName": self.idc_name,
            "setName": self.set_name,
            "serviceName": self.service_name,
            "instanceId": self.instance_id,
            "traceId": str(span.trace_id),
            "uri": span_tags.get(HTTP_URI),
            "method": span_tags.get(tags.HTTP_METHOD),
            "httpCode": str(span_tags.get(tags.HTTP_STATUS_CODE)),
            "timeStamp": str(int(timestamp * 1000)),
            "timeCost": str(int((timestamp - span.start_time) * 1000)),
            "businessCode": str(biz_code) if biz_code else None,
            "treeLevel": str(span.get_baggage_item(TREE_LEVEL_KEY) or span.get_baggage_item(TREE_LEVEL_KEY.lower()))
        }
        queue.put_nowait(metrics_data)

    def _metrics(self, data: dict):
        try:
            self.kafka_producer.send(METRICS_TOPIC, data)
        except Exception as e:
            logger.exception(f"Got an error while sending metrics info:{e}")
