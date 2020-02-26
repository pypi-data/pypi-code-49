from opentracing.ext.tags import *  # noqa

# General tags
HOSTNAME = 'hostname'
SERVICE = 'service'
COMMAND = 'command'
PLATFORM_NAME = 'platform.name'
PLATFORM_VERSION = 'platform.version'
ARCHITECTURE = 'architecture'
REPOSITORY = 'repository'
COMMIT = 'commit'
BRANCH = 'branch'
SPAN_KIND_PUBLISH = 'publish'
SPAN_KIND_RECEIVE = 'receive'
SOURCE_ROOT = 'source.root'
AGENT_ID = 'agent.id'
AGENT_VERSION = 'agent.version'
AGENT_TYPE = 'agent.type'
HTTP_PAYLOADS = 'instrumentation.http.payload'
DB_STATEMENTS_INSTRUMENTATION = 'instrumentation.db.statements'
HTTP_HEADERS = 'instrumentation.http.headers'
TESTING = 'testing'
DEPENDENCIES = 'dependencies'
PEER_SERVICE = 'peer.service'

# Python specific tags
PYTHON_IMPLEMENTATION = 'python.implementation'
PYTHON_VERSION = 'python.version'

# CI specific tags
CI = 'ci.in_ci'
CI_PROVIDER = 'ci.provider'
CI_BUILD_ID = 'ci.build_id'
CI_BUILD_NUMBER = 'ci.build_number'
CI_BUILD_URL = 'ci.build_url'

# Test related tags
TEST = 'test'
TEST_SUITE = 'test.suite'
TEST_NAME = 'test.name'
TEST_CODE = 'test.code'
TEST_FRAMEWORK = 'test.framework'

TEST_STATUS = 'test.status'
TEST_STATUS_PASS = 'PASS'
TEST_STATUS_FAIL = 'FAIL'
TEST_STATUS_SKIP = 'SKIP'
TEST_TYPE = 'test.type'

# RPC related tags
RPC_OPERATION_ID = 'rpc.id'

# Log fields
ERROR_KIND = 'error.kind'
ERROR_OBJECT = 'error.object'
EVENT = 'event'
MESSAGE = 'message'
STACK = 'stack'
EXCEPTION = 'exception'
EVENT_LOG = 'log'
LOG_LOGGER = 'log.logger'
LOG_LEVEL = 'log.level'
SOURCE = 'source'

# Baggage tags
TRACE_KIND = 'trace.kind'

# HTTP
HTTP_REQUEST_HEADERS = 'http.request_headers'
HTTP_REQUEST_PAYLOAD = 'http.request_payload'
HTTP_RESPONSE_HEADERS = 'http.response_headers'
HTTP_RESPONSE_PAYLOAD = 'http.response_payload'

# Benchmark
BENCHMARK_TYPE = 'benchmark'
BENCHMARK_RUNS = 'benchmark.runs'
BENCHMARK_DURATION_MEAN = 'benchmark.duration.mean'
BENCHMARK_DURATION_MIN = 'benchmark.duration.min'
BENCHMARK_DURATION_MAX = 'benchmark.duration.max'
BENCHMARK_DURATION_STDDEV = 'benchmark.duration.std_dev'
BENCHMARK_DURATION_MEDIAN = 'benchmark.duration.median'
BENCHMARK_DURATION_Q1 = 'benchmark.duration.q1'
BENCHMARK_DURATION_Q3 = 'benchmark.duration.q3'

# Database
DB_STATEMENT = 'db.statement'
DB_PREPARE_STATEMENT = 'db.prepare_statement'
DB_PRODUCT_NAME = 'db.product_name'
DB_PRODUCT_VERSION = 'db.product_version'
DB_DRIVER_NAME = 'db.driver_name'
DB_DRIVER_VERSION = 'db.driver_version'
DB_PARAMS = 'db.params'
DB_CONNECTION_STRING = 'db.conn'
DB_CURSOR = 'db.cursor'
