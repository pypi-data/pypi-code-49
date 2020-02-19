import os
from io import StringIO


class Metric:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MetricBuilder:
    def __init__(self):
        self.buffer = StringIO()

    def append(self, metric):
        self.buffer\
            .write('{key}, {value}\n'.format(key=metric.key, value=metric.value))

    def write(self, s3_interface, s3_metrics_path):
        s3_metrics_key = os.path.join(s3_metrics_path, 'mb-metrics.csv')
        s3_interface\
            .upload_object(s3_metrics_key, self.buffer.getvalue())
