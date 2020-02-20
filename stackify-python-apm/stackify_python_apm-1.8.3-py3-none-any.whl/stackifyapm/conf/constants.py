import os


TRACEPARENT_HEADER_NAME = "stackify-apm-traceparent"
TRACE_CONTEXT_VERSION = '2.0'

KEYWORD_MAX_LENGTH = 1024

HTTP_WITH_BODY = {"POST", "PUT", "PATCH", "DELETE"}

ERROR = "error"
TRANSACTION = "transaction"
SPAN = "span"

if os.name == 'nt':
    BASE_PATH = "c:\\ProgramData\\Stackify\\Python\\"
    LOG_PATH = "{}Log\\".format(BASE_PATH)
else:
    BASE_PATH = "/usr/local/stackify/stackify-python-apm/"
    LOG_PATH = "{}log/".format(BASE_PATH)

QUEUE_TIME_INTERVAL_IN_MS = 500
QUEUE_MAX_SIZE = 1000

ASYNC_WAITING_TIME_IN_SEC = 10
ASYNC_MAX_WAITING_TIME_IN_SEC = 40

RUM_SCRIPT_SRC = "https://stckjs.azureedge.net/stckjs.js"
RUM_COOKIE_NAME = ".Stackify.Rum"

AGENT_TRACES_MAX_SIZE = 50
AGENT_SEND_INTERVAL_IN_SEC = 10
AGENT_TRACES_PATH = '/traces'

TRANSPORT_AGENT_HTTP = "agent_http"
TRANSPORT_AGENT_SOCKET = "agent_socket"
TRANSPORT_DEFAULT = "default"
TRANSPORT_LOGGING = "logging"

DEFAULT_ENVIRONMENT = "Production"
DEFAULT_APPLICATION_NAME = "Python Application"
DEFAULT_CONFIG_FILE = "stackify.json"
DEFAULT_MULTIPROCESSING = False
DEFAULT_RUM_ENABLED = False
DEFAULT_RUM_AUTO_INJECTION = False
DEFAULT_TRANSPORT = TRANSPORT_DEFAULT
DEFAULT_TRANSPORT_SOCKET_FILE = "http+unix://%2Fusr%2Flocal%2Fstackify%2Fstackify.sock"
DEFAULT_HTTP_ENDPOINT = "https://localhost:10601"
DEFAULT_DEBUG = False
DEFAULT_QUEUE = True
