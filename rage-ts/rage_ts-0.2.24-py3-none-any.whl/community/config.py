import ctypes
import time
from multiprocessing.sharedctypes import Array
import json
import os
import uuid

from ragex.community.constants import EVENT_CONSUMER_SEPARATION_ENV

LOCAL_MODE = os.environ.get("LOCAL_MODE", "true").lower() == "true"
OPEN_WEB_BROWSER = os.environ.get("OPEN_WEB_BROWSER", "true").lower() == "true"
PROCESS_START = time.time()

SYSTEM_USER = "system_user"

# Platform-wide variables
rasa_x_password = os.environ.get("RASA_X_PASSWORD")
rasa_x_token = os.environ.get("RASA_X_TOKEN") or uuid.uuid4().hex
password_salt = os.environ.get("PASSWORD_SALT", "salt")
project_name = os.environ.get("PROJECT_ID", "default")
self_port = int(os.environ.get("SELF_PORT", "5002"))
jwt_public_key_path = os.environ.get("JWT_PUBLIC_KEY_PATH", "/app/public_key")
jwt_private_key_path = os.environ.get("JWT_PRIVATE_KEY_PATH", "/app/private_key")
jwt_public_key = None  # placeholder, will be set on startup
jwt_private_key = None  # placeholder, will be set on startup
jwt_expiration_time = int(
    os.environ.get("JWT_EXPIRATION_TIME") or (60 * 60 * 8)  # 8 hours
)
debug_mode = os.environ.get("DEBUG_MODE", "false") == "true"
log_level = "DEBUG" if debug_mode else os.environ.get("LOG_LEVEL", "INFO")
team_name = os.environ.get("TEAM_ID", "rasa")
saml_path = os.environ.get("SAML_PATH", "/app/auth/saml")
saml_default_role = os.environ.get("SAML_DEFAULT_ROLE", "tester")
rasa_model_dir = os.environ.get("RASA_MODEL_DIR", "/models")
data_dir = os.environ.get("DATA_DIR", "data")
default_environments_config_path = os.environ.get(
    "DEFAULT_ENVIRONMENT_CONFIG_PATH", "environments.yml"
)
default_nlu_filename = os.environ.get("DEFAULT_NLU_FILENAME", "nlu.md")
default_stories_filename = os.environ.get("DEFAULT_STORIES_FILENAME", "stories.md")
default_domain_path = os.environ.get("DEFAULT_DOMAIN_PATH", "domain.yml")
default_config_path = os.environ.get("DEFAULT_CONFIG_PATH", "config.yml")
default_username = os.environ.get("DEFAULT_USERNAME", "me")
development_mode = os.environ.get("DEVELOPMENT_MODE", "false").lower() == "true"
credentials_path = os.environ.get("CREDENTIALS_PATH", "/app/credentials.yml")
endpoints_path = os.environ.get("ENDPOINTS_PATH", "/app/endpoints.yml")

# user metrics collection
metrics_collection_config = {}
# Interval at which to send "Status" event, in seconds
metrics_status_event_interval = int(
    os.environ.get("TELEMETRY_STATUS_INTERVAL") or (60 * 60)  # 1 hour
)
# Metrics events can be sent to another Segment source by using the TELEMETRY_WRITE_KEY
# environment variable. The default is to send all events to the dev team's Rasa X
# Python source.
metrics_write_key = os.environ.get(
    "TELEMETRY_WRITE_KEY", "ioI9ijcgQNp6wB9jMyIIk1ceyFdX5w04"
)

# by default data based on platform users will be excluded from the analytics
# set to "1" if you wish to include them
rasa_x_user_analytics = bool(int(os.environ.get("RASA_X_USER_ANALYTICS", "0")))

# the number of bins in the analytics results if `window` is not specified
# in the query
default_analytics_bins = int(os.environ.get("DEFAULT_ANALYTICS_BINS", "10"))

# APscheduler config defining the update behaviour of the analytics cache. See
# https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html
# the default value of {"hour": "*"} will run the caching once per hour
analytics_update_kwargs = json.loads(
    os.environ.get("ANALYTICS_UPDATE_KWARGS", '{"hour": "*"}')
)

# Stack variables
rasa_token = os.environ.get("RASA_TOKEN", "")

# RabbitMQ variables
rabbitmq_username = os.environ.get("RABBITMQ_USERNAME", "user")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD", "bitnami")
rabbitmq_host = os.environ.get("RABBITMQ_HOST", "localhost")
rabbitmq_port = os.environ.get("RABBITMQ_PORT", "5672")
rabbitmq_queue = os.environ.get("RABBITMQ_QUEUE", "rasa_production_events")

# whether the Pika event consumer should be run from within rasa X or as a
# separate service
should_run_event_consumer_separately = (
    os.environ.get(EVENT_CONSUMER_SEPARATION_ENV, "false") == "true"
)

# SSL configuration
ssl_certificate = os.environ.get("RASA_X_SSL_CERTIFICATE")
ssl_keyfile = os.environ.get("RASA_X_SSL_KEYFILE")
ssl_ca_file = os.environ.get("RASA_X_SSL_CA_FILE")
ssl_password = os.environ.get("RASA_X_SSL_PASSWORD")


GIT_FEATURE_FLAG = {"name": "Integrated Version Control", "enabled": False}

# Feature Flags which only apply to local mode
DEFAULT_LOCAL_FEATURE_FLAGS = []
# Feature Flags which only apply to server mode
DEFAULT_SERVER_FEATURE_FLAGS = [GIT_FEATURE_FLAG]

# Path to the current project directory which contains domain, training data and so on
# Use a `multiprocessing.Array` to ensure that changes are reflected across
# multiple Sanic workers.
PROJECT_DIRECTORY = Array(ctypes.c_char, 300)

SANIC_RESPONSE_TIMEOUT_IN_SECONDS = int(
    os.environ.get("SANIC_RESPONSE_TIMEOUT", "3600")
)
SANIC_ACCESS_CONTROL_MAX_AGE = int(
    os.environ.get("SANIC_ACCESS_CONTROL_MAX_AGE") or (60 * 30)  # 30 minutes
)

#Response Image Directory
rasa_image_dir = os.environ.get("RASA_IMAGE_DIR", "public_images")
