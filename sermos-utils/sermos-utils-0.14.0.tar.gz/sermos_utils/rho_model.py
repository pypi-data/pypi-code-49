import os
import pprint

import boto3
import logging
import requests
from rho_ml.stored_model import StoredModel
from typing import Dict, Type, Optional

from rho_ml.rho_model import RhoModel
from rho_ml.serialization import LocalModelStorage
from sermos_utils.constants import DEFAULT_STORE_MODEL_URL, S3_MODEL_BUCKET, \
    DEFAULT_GET_MODEL_URL

logger = logging.getLogger(__name__)


def get_storage_key(model: Type[RhoModel], prefix: str) -> str:
    return "{0}/{1}_{2}".format(prefix, model.name, model.version)


def get_headers(api_key: str) -> Dict[str, str]:
    return {
        'Content-Type': 'application/json',
        'apikey': api_key
    }


def get_s3_client_from_api_response(response_data: Dict[str, str]):
    try:
        access_key = response_data['aws_access_key']
        secret_key = response_data['aws_secret_key']
        session_token = response_data['aws_session_token']
        region = response_data['aws_region']
    except KeyError as e:
        logger.warning("Missing IAM keys in response:\n{0}"
                       .format(pprint.pformat(response_data)))
        raise e
    else:
        client = boto3.client('s3',
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key,
                              aws_session_token=session_token,
                              region_name=region)
        return client


def store_rho_model(model: Type[RhoModel],
                    deploy_key: Optional[str] = None,
                    store_model_endpoint: Optional[str] = None):
    """ Get S3 credentials from the sermos-admin API, then use the credentials
     to store the model and metadata in the appropriate bucket / subfolder"""
    if not deploy_key:
        deploy_key = os.environ['SERMOS_DEPLOY_KEY']
    headers = get_headers(api_key=deploy_key)
    if not store_model_endpoint:
        store_model_endpoint = DEFAULT_STORE_MODEL_URL
    post_data = {'model_key': model.name + '_' + str(model.version)}
    r = requests.post(url=store_model_endpoint, headers=headers, json=post_data)
    response_data = r.json()
    client = get_s3_client_from_api_response(response_data=response_data)
    storage_key = response_data['model_key']
    logger.debug("Attempting to serialize {0}".format(model.name))
    stored_model = StoredModel.from_model(model=model)
    store_json = stored_model.to_json()
    logger.info("Uploading serialized {0}"
                .format('_'.join([model.name, str(model.version)])))
    client.put_object(Body=store_json, Bucket=S3_MODEL_BUCKET, Key=storage_key)


class ModelNotFoundError(Exception):
    pass


def get_stored_model_json(model_name: str,
                          version_pattern: str,
                          deploy_key: str,
                          get_model_endpoint: Optional[str] = None) -> str:
    headers = get_headers(api_key=deploy_key)
    if not get_model_endpoint:
        get_model_endpoint = DEFAULT_GET_MODEL_URL
    query_params = {
        'model_name': model_name,
        'version_pattern': version_pattern
    }
    logger.debug("Requesting storage info from Admin API...")
    r = requests.post(
        url=get_model_endpoint, headers=headers, json=query_params)
    response_data = r.json()
    client = get_s3_client_from_api_response(response_data=response_data)
    model_key = response_data['model_key']
    if not model_key:
        raise ModelNotFoundError("Couldn't find model matching name {0} and"
                                 "version pattern {1}"
                                 .format(model_name, version_pattern))
    logger.debug("Retrieving {0} from storage...".format(model_key))
    s3_response = client.get_object(Bucket=S3_MODEL_BUCKET, Key=model_key)
    model_json = s3_response['Body'].read()
    return model_json


def get_local_storage(base_path: Optional[str]) -> LocalModelStorage:
    if base_path:
        result = LocalModelStorage(base_path=base_path)
    else:
        result = LocalModelStorage()
    return result


def get_local_model(model_name: str,
                    version_pattern: str,
                    local_base_path: str) -> Optional[RhoModel]:
    """ Search for a local model by name and version and instantiate it
    if found. """
    local_storage = get_local_storage(base_path=local_base_path)
    local_key = local_storage.get_key_from_pattern(
        model_name=model_name, version_pattern=version_pattern)
    if local_key:
        logger.info("Local model found with filename: {0}".format(local_key))
        result = local_storage.retrieve(local_key)
        return result


def rho_model_loader(model_name: str,
                     version_pattern: str,
                     deploy_key: Optional[str] = None,
                     local_base_path: Optional[str] = None,
                     save_to_local_disk: bool = True,
                     get_model_endpoint: Optional[str] = None) -> Type[RhoModel]:
    """ Retrieve models stored using the Sermos Admin API by name and
    version.

    Optionally cache the result locally for later use (caching on by
    default). """
    model = get_local_model(model_name=model_name,
                            version_pattern=version_pattern,
                            local_base_path=local_base_path)
    if not model:
        if not deploy_key:
            deploy_key = os.environ['SERMOS_DEPLOY_KEY']
        stored_bytes = get_stored_model_json(
            model_name=model_name,
            version_pattern=version_pattern,
            deploy_key=deploy_key,
            get_model_endpoint=get_model_endpoint)
        stored_model = StoredModel.from_json(storage_json=stored_bytes)
        model = stored_model.load_model()
        if save_to_local_disk:
            logger.info("Caching retrieved model {0} locally..."
                        .format(model.name))
            local_storage = get_local_storage(base_path=local_base_path)
            local_storage.store(model=model)
    return model
