from prometheus_client import Gauge, Histogram

# Create a metric to track time spent and requests made.
REQUEST_TIME = Histogram('request_processing_seconds', 'Time spent processing request', ['app', 'method', 'endpoint'])
CURRENT_USER = Gauge('current_users', 'Total number of current users', ['channel'], multiprocess_mode='livesum')
CHAT_LATENCY = Histogram('chat_latency_seconds_histogram', 'Latency of a chat response', ['channel', 'endpoint'])