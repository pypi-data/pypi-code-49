import os

DEBUG = True
CONTAINER_CARRIER = "docker"
CLIENT_URL = "unix://var/run/docker.sock"
NETWORK_NAME = os.environ.get("CALCCORE_NETWORK_NAME")  # "threedi_backend"
IMAGE_NAME = os.environ.get("CALCCORE_DOCKER_IMAGE")
CONTAINER_LOG_LEVEL = os.environ.get("CALCCORE_LOG_LEVEL", "INFO")

# harbor.lizard.net/threedi/threedicore:1.4.15.devtest_3"
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")  # "redis"
BASE_MODEL_PATH = os.environ.get("CALCORE_MODEL_PATH", "/models")
# # Location where to write the results of the calccore.
BASE_RESULT_PATH = os.environ.get("CALCCORE_RESULTS_PATH", "/results")

THREEDI_OUTPUT_DIR = ""

DOCKER_MOUNT_POINTS = {}

# Provision docker mount points from all CALCCORE_MOUNT_XXXX
# environment variables
# format:
#    CALCCORE_MOUNT_XX=LOCAL_PATH:DOCKER_PATH
for key in os.environ.keys():
    if key.startswith('CALCCORE_MOUNT'):
        local_path, docker_path, read_only = os.environ[key].split(':')
        DOCKER_MOUNT_POINTS.update(
            {
                local_path: {
                    'bind': docker_path,
                    'ro': read_only == 'ro'}
            }
        )


START_ACTION_SUBCHANNEL_NAME = "start_action"
SENTRY_DSN = ""
