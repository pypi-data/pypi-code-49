import re
import os
import six
import subprocess
from localstack import config as localstack_config
from localstack import constants as localstack_constants

# api server config
API_PATH = '/v1'
API_PORT_LOCAL = 8183
API_URL = localstack_constants.API_ENDPOINT

# api endpoints
API_PATH_USER = '%s/user' % API_PATH
API_PATH_ORGANIZATIONS = '%s/organizations' % API_PATH
API_PATH_SIGNIN = '%s/signin' % API_PATH_USER
API_PATH_SIGNUP = '%s/signup' % API_PATH_USER
API_PATH_RECOVER = '%s/recover' % API_PATH_USER
API_PATH_ACTIVATE = '%s/activate' % API_PATH_USER
API_PATH_KEY_ACTIVATE = '%s/activate' % API_PATH
API_PATH_CARDS = '%s/cards' % API_PATH_USER
API_PATH_PLANS = '%s/plans' % API_PATH
API_PATH_SUBSCRIPTIONS = '%s/subscriptions' % API_PATH_PLANS
API_PATH_EVENTS = '%s/events' % API_PATH
API_PATH_STATS = '%s/stats' % API_PATH_EVENTS
API_PATH_GITHUB = '%s/github' % API_PATH
API_PATH_CONFIG = '%s/config' % API_PATH
API_PATH_CI = '%s/ci' % API_PATH
API_PATH_ADMIN = '%s/admin' % API_PATH
API_PATH_STRIPE_WEBHOOK = '%s/webhooks/stripe' % API_PATH

ROOT_FOLDER = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

PROTECTED_FOLDERS = ('services', 'utils')

# database connection settings
DB_NAME = 'localstack'
DB_USER = os.environ.get('DB_USER') or 'localstack'
DB_PASS = os.environ.get('DB_PASS')

# localhost IP address
LOCALHOST_IP = '127.0.0.1'

# bind address of local DNS server
DNS_ADDRESS = os.environ.get('DNS_ADDRESS') or '0.0.0.0'

# IP address that AWS endpoints should resolve to in our local DNS server. By default,
# hostnames resolve to 127.0.0.1, which allows to use the LocalStack APIs transparently
# from the host machine. If your code is running in Docker, this should be configured
# to resolve to the Docker bridge network address, e.g., DNS_RESOLVE_IP=172.17.0.1
DNS_RESOLVE_IP = os.environ.get('DNS_RESOLVE_IP') or LOCALHOST_IP

# fallback port for non-SSL HTTP edge service (in case HTTPS edge service cannot be used)
PORT_EDGE_HTTP = int(os.environ.get('PORT_EDGE_HTTP') or 0)

# SMTP settings (required, e.g., for Cognito)
SMTP_HOST = os.environ.get('SMTP_HOST', '')
SMTP_USER = os.environ.get('SMTP_USER', '')
SMTP_PASS = os.environ.get('SMTP_PASS', '')
SMTP_EMAIL = os.environ.get('SMTP_EMAIL', '')

# backend service ports
DEFAULT_PORT_RDS_BACKEND = 4547
DEFAULT_PORT_COGNITO_IDP_BACKEND = 4546
DEFAULT_PORT_COGNITO_IDENTITY_BACKEND = 4545
DEFAULT_PORT_IOT_BACKEND = 4544
DEFAULT_PORT_IOT_DATA_BACKEND = 4543
DEFAULT_PORT_KMS_BACKEND = 4542
DEFAULT_PORT_ECS_BACKEND = 4541
DEFAULT_PORT_XRAY_BACKEND = 4540
DEFAULT_PORT_ATHENA_BACKEND = 4539
DEFAULT_PORT_GLUE_BACKEND = 4538
DEFAULT_PORT_REDSHIFT_BACKEND = 4537
DEFAULT_PORT_EMR_BACKEND = 4536
DEFAULT_PORT_LOCAL_DAEMON = 4535
DEFAULT_PORT_LOCAL_DAEMON_ROOT = 4534

# port ranges for service instances (e.g., Postgres DBs, ElastiCache clusters, ...)
SERVICE_INSTANCES_PORTS_START = 4510
SERVICE_INSTANCES_PORTS_END = SERVICE_INSTANCES_PORTS_START + 20

# add default service ports
localstack_constants.DEFAULT_SERVICE_PORTS['cognito-idp'] = 4590
localstack_constants.DEFAULT_SERVICE_PORTS['cognito-identity'] = 4591
localstack_constants.DEFAULT_SERVICE_PORTS['sts'] = 4592
localstack_constants.DEFAULT_SERVICE_PORTS['iam'] = 4593
localstack_constants.DEFAULT_SERVICE_PORTS['edge'] = 443

# Docker host name resolvable from containers
DOCKER_HOST_NAME = 'host.docker.internal'

if localstack_config.DOCKER_HOST_FROM_CONTAINER == DOCKER_HOST_NAME:
    # special case when we're running tests outside of Docker
    if not localstack_config.in_docker():
        image_name = localstack_constants.DOCKER_IMAGE_NAME
        cmd = "docker run --rm --entrypoint= -it %s bash -c 'ping -c 1 %s'" % (image_name, DOCKER_HOST_NAME)
        out = subprocess.check_output(cmd, shell=True)
        out = out.decode('utf-8') if isinstance(out, six.binary_type) else out
        ip = re.match(r'PING[^\(]+\(([^\)]+)\).*', out, re.MULTILINE | re.DOTALL)
        ip = ip and ip.group(1)
        if ip:
            localstack_config.DOCKER_HOST_FROM_CONTAINER = ip

# update variable names that need to be passed as arguments to Docker
localstack_config.CONFIG_ENV_VARS += [
    'SMTP_HOST', 'SMTP_USER', 'SMTP_PASS', 'SMTP_EMAIL', 'PORT_EDGE_HTTP',
    'DNS_RESOLVE_IP'
]

# re-initialize configs in localstack
localstack_config.populate_configs()
