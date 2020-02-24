""" Constants used throughout utils.
"""
from urllib.parse import urljoin

ENV_VAR_DEPLOY_KEY = "SERMOS_DEPLOY_KEY"
ENV_VAR_PKG_NAME = "SERMOS_CLIENT_PKG_NAME"
DEFAULT_BASE_URL = "https://admin.sermos.ai/api/v1/"
DEFAULT_DEPLOY_URL = urljoin(DEFAULT_BASE_URL, 'deploy')
DEFAULT_GET_MODEL_URL = urljoin(DEFAULT_BASE_URL, 'models/get-model/')
DEFAULT_STORE_MODEL_URL = urljoin(DEFAULT_BASE_URL, 'models/store-model/')
DEFAULT_YAML_NAME = "sermos.yaml"
S3_MODEL_BUCKET = 'sermos-client-models'

# Used to define the 'name' of the default, base image that is used for
# every customer build unless they define imageConfig.customImages in their
# sermos.yaml and then specify the customImageName key on either the API
# or custom workers.
DEFAULT_BASE_IMAGE_NAME = 'base'
