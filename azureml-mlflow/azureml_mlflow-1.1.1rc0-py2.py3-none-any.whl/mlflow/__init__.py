# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""
Contains functionality integrating Azure Machine Learning with MLFlow.

MLflow (https://mlflow.org/) is an open-source platform for tracking machine learning experiments and managing models.
You can use MLFlow logging APIs with Azure Machine Learning so that the metrics and artifacts are logged to your Azure
machine learning workspace.

Within an Azure Machine Learning :class:`azureml.core.workspace`, add the lines below to your MLflow code:

    import mlflow
    from azureml.core import Workspace
    workspace = Workspace.from_config()
    mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

More examples can be found at https://aka.ms/azureml-mlflow-examples.
"""

import os
import logging
import re
from six.moves.urllib import parse

import mlflow
from mlflow.exceptions import MlflowException

import azureml
from azureml.exceptions import RunEnvironmentException
from azureml.core import Workspace, Experiment, Run
from azureml.core.authentication import ArmTokenAuthentication
from azureml.mlflow._version import VERSION

from ._internal import store
from ._internal.store import _VERSION_WARNING
from ._internal.utils import (get_service_context_from_tracking_url,
                              get_aml_experiment_name, _IS_REMOTE,
                              _TRUE_QUERY_VALUE, _TOKEN_PREFIX,
                              _AUTH_HEAD, _AUTH_TYPE)

_SUBSCRIPTIONS_PREFIX = "/subscriptions/"

logger = logging.getLogger(__name__)

__version__ = VERSION

__all__ = ["get_portal_url", "register_model", "azureml_store_builder", "azureml_artifacts_builder"]


class _AzureMLStoreLoader(object):
    """
    _AzureMLStoreLoader loads an AzureMLStore from 3 supported scenarios.

    1, new tracking_uri without is remote set to True. A store is created from the uri
    2, is remote set to true in a workspace tracking uri. Loads the
       store information from the current Run context and sets the experiment and ActiveRun.
    3, a cached result of option 1 or 2, this cache is relative to the netloc + path of the tracking_uri
    """

    _azure_uri_to_store = {}

    @classmethod
    def _load_azureml_store(cls, store_uri):
        parsed_url = parse.urlparse(store_uri)
        queries = dict(parse.parse_qsl(parsed_url.query))

        # cache the Azure workspace object
        cache_key = store_uri.split("?")[0]
        if cache_key in cls._azure_uri_to_store:
            logger.debug("Loading an existing AzureMLRestStore from the _AzureMLStoreLoader cache")
            return cls._azure_uri_to_store[cache_key]
        elif _IS_REMOTE in queries and queries[_IS_REMOTE] == _TRUE_QUERY_VALUE:
            try:
                run = Run.get_context()
            except RunEnvironmentException:
                raise MlflowException(
                    "AzureMlflow tracking URI was set to remote but there was a failure in loading the run.")
            else:
                logger.debug("Creating a new AzureMLRestStore for a remote run")
                amlflow_store = store.AzureMLRestStore(
                    service_context=run.experiment.workspace.service_context)

                cls._azure_uri_to_store[cache_key] = amlflow_store
                logger.debug("Setting Mlflow experiment with {}".format(run.experiment.name))
                mlflow.set_experiment(run.experiment.name)
        else:
            service_context = get_service_context_from_tracking_url(parsed_url)
            logger.debug("Creating a new AzureMLRestStore for a local run")
            cls._azure_uri_to_store[cache_key] = store.AzureMLRestStore(service_context=service_context)

        return cls._azure_uri_to_store[cache_key]


def azureml_store_builder(store_uri=None, artifact_uri=None):
    """Create or return a store to read and record metrics and artifacts in Azure via MLflow.

    :param store_uri: A URI to the store.
    :type store_uri: str
    :param artifact_uri: A URI where artifacts are stored.
    :type artifact_uri: str
    """
    try:
        from mlflow import get_tracking_uri
    except ImportError:
        logger.warning(_VERSION_WARNING.format("mlflow.get_tracking_uri"))
        from mlflow.tracking.utils import get_tracking_uri
    tracking_uri = store_uri if store_uri is not None else get_tracking_uri()
    return _AzureMLStoreLoader._load_azureml_store(tracking_uri)


def adb_azureml_store_builder(store_uri=None, artifact_uri=None):
    """Create or return a store to read and record metrics and artifacts in Azure via MLflow when using Databricks.

    :param store_uri: A URI to the store.
    :type store_uri: str
    :param artifact_uri: A URI where artifacts are stored.
    :type artifact_uri: str
    """
    try:
        from mlflow import get_tracking_uri
    except ImportError:
        logger.warning(_VERSION_WARNING.format("mlflow.get_tracking_uri"))
        from mlflow.tracking.utils import get_tracking_uri
    tracking_uri = store_uri if store_uri is not None else get_tracking_uri()
    return store.AdbAzuremlRestStore(tracking_uri)


def azureml_artifacts_builder(artifact_uri=None):
    """Create an artifact repository for AzureMLflow.

    :param artifact_uri: A URI where artifacts are stored.
    :type artifact_uri: str
    """
    from ._internal.artifact_repo import AzureMLflowArtifactRepository
    return AzureMLflowArtifactRepository(artifact_uri)


def adb_azureml_artifacts_builder(artifact_uri=None):
    """Create an artifact repository for AzureMLflow when using Databricks.

    :param artifact_uri: A URI where artifacts are stored.
    :type artifact_uri: str
    """
    from ._internal.artifact_repo import AdbAzuremlArtifactRepository
    return AdbAzuremlArtifactRepository(artifact_uri)


def _get_mlflow_tracking_uri(self, with_auth=True):
    """
    Retrieve the tracking URI from Workspace for use in AzureMLflow.

    Return a URI identifying the workspace, with optionally the auth header
    embedded as a query string within the URI. The authentication header does not include the "Bearer " prefix.

    :return: Returns the URI pointing to this workspace, with the auth query paramter if with_auth is True.
    :rtype: str
    """
    queries = []
    if with_auth:
        auth = self._auth_object
        logger.debug("Creating a tracking uri with an {} auth token".format(auth.__class__.__name__))
        header = auth.get_authentication_header()
        token = header["Authorization"][len(_TOKEN_PREFIX):]
        queries.append(_AUTH_TYPE + "=" + auth.__class__.__name__)
        queries.append(_AUTH_HEAD + "=" + token)

    service_location = parse.urlparse(self.service_context._get_run_history_url()).netloc
    workspace_scope = self.service_context._get_workspace_scope()
    logger.debug("Creating a tracking uri in {} for workspace {}".format(service_location, workspace_scope))

    return "azureml://{}/history/v1.0{}{}".format(
        service_location,
        workspace_scope,
        "?" + "&".join(queries) if queries else "")


def _setup_remote(azureml_run):
    logger.debug("Setting up a Remote MLflow run")
    tracking_uri = azureml_run.experiment.workspace.get_mlflow_tracking_uri() + "&is-remote=True"
    mlflow.set_tracking_uri(tracking_uri)
    try:
        from mlflow.tracking._tracking_service.utils import _TRACKING_URI_ENV_VAR
    except ImportError:
        logger.warning(_VERSION_WARNING.format("_TRACKING_URI_ENV_VAR from " +
                                               "mlflow.tracking._tracking_service.utils"))
        from mlflow.tracking.utils import _TRACKING_URI_ENV_VAR
    from mlflow.tracking.fluent import _RUN_ID_ENV_VAR
    logger.debug("Setting MLflow tracking uri env var")
    os.environ[_TRACKING_URI_ENV_VAR] = tracking_uri
    logger.debug("Setting MLflow run id env var with {}".format(azureml_run.id))
    os.environ[_RUN_ID_ENV_VAR] = azureml_run.id
    logger.debug("Setting Mlflow experiment with {}".format(azureml_run.experiment.name))
    mlflow.set_experiment(azureml_run.experiment.name)
    from mlflow.entities import SourceType

    mlflow_tags = {}
    mlflow_source_type_key = 'mlflow.source.type'
    if mlflow_source_type_key not in azureml_run.tags:
        logger.debug("Setting the mlflow tag {}".format(mlflow_source_type_key))
        mlflow_tags[mlflow_source_type_key] = SourceType.to_string(SourceType.JOB)
    mlflow_source_name_key = 'mlflow.source.name'
    if mlflow_source_name_key not in azureml_run.tags:
        logger.debug("Setting the mlflow tag {}".format(mlflow_source_name_key))
        mlflow_tags[mlflow_source_name_key] = azureml_run.get_details()['runDefinition']['script']
    azureml_run.set_tags(mlflow_tags)


def get_portal_url(run):
    """Get the URL to the Azure Machine Learning studio page for viewing run details.

    :param run: The run for which to view details.
    :type run: azureml.core.Run
    :return: A URL to the Azure Machine Learning studio which can be used to view
        run details, including run artifacts.
    :rtype: str
    """
    if isinstance(run, Run):
        return run.get_portal_url()
    else:
        from mlflow.tracking.client import MlflowClient
        experiment_name = MlflowClient().get_experiment(run.info.experiment_id).name
        run_id = run.info.run_uuid
        try:
            def_store = MlflowClient()._tracking_client.store
        except:
            logger.warning(_VERSION_WARNING.format("MlflowClient()._tracking_client.store"))
            def_store = MlflowClient().store
        aml_store = def_store if isinstance(def_store, store.AzureMLRestStore) else def_store.aml_store
        host = aml_store.get_host_creds().host
        netloc = "https://mlworkspace.azure.ai/portal"
        uri = "{}{}".format(_SUBSCRIPTIONS_PREFIX, host.split(_SUBSCRIPTIONS_PREFIX, 2)[1])
        experiment_name = get_aml_experiment_name(experiment_name)
        experiment_run_uri = "/experiments/{}/runs/{}".format(experiment_name, run_id)
        return netloc + uri + experiment_run_uri


def _azureml_run_from_mlflow_run(mlflow_run):
    from mlflow.tracking.client import MlflowClient
    experiment_name = MlflowClient().get_experiment(mlflow_run.info.experiment_id).name
    try:
        def_store = MlflowClient()._tracking_client.store
    except:
        logger.warning(_VERSION_WARNING.format("MlflowClient()._tracking_client.store"))
        def_store = MlflowClient().store
    aml_store = def_store if isinstance(def_store, store.AzureMLRestStore) else def_store.aml_store
    host = aml_store.get_host_creds().host
    auth_token = aml_store.get_host_creds().token

    cluster_url = host.split(_SUBSCRIPTIONS_PREFIX, 2)[0].split("/history/")[0]
    scope = "{}{}".format(_SUBSCRIPTIONS_PREFIX, host.split(_SUBSCRIPTIONS_PREFIX, 2)[1])
    auth = ArmTokenAuthentication(auth_token)
    run_id = mlflow_run.info.run_uuid

    subscription_id = re.search(r'/subscriptions/([^/]+)', scope).group(1)
    resource_group_name = re.search(r'/resourceGroups/([^/]+)', scope).group(1)
    workspace_name = re.search(r'/workspaces/([^/]+)', scope).group(1)
    workspace = Workspace(subscription_id,
                          resource_group_name,
                          workspace_name,
                          auth=auth,
                          _disable_service_check=True)

    experiment = Experiment(workspace, experiment_name)
    changed_env_var = False
    prev_env_var = None
    from azureml._base_sdk_common.service_discovery import HISTORY_SERVICE_ENDPOINT_KEY
    try:
        if HISTORY_SERVICE_ENDPOINT_KEY in os.environ:
            prev_env_var = os.environ[HISTORY_SERVICE_ENDPOINT_KEY]
        os.environ[HISTORY_SERVICE_ENDPOINT_KEY] = cluster_url
        changed_env_var = True
        azureml_run = Run(experiment, run_id)
        return azureml_run
    finally:
        if changed_env_var:
            if prev_env_var is not None:
                os.environ[HISTORY_SERVICE_ENDPOINT_KEY] = prev_env_var
            else:
                del os.environ[HISTORY_SERVICE_ENDPOINT_KEY]


def register_model(run, name, path, tags=None, **kwargs):
    """
    Register a model with the specified name and artifact path.

    .. remarks::

        .. code-block:: python

            model = register_model(run, 'best_model', 'outputs/model.pkl', tags={'my': 'tag'})

    :param name: The name to give the registered model.
    :type name: str
    :param path: The relative cloud path to the model, for example, "outputs/modelname".
    :type path: str
    :param tags: An optional dictionary of key value tags to pass to the model.
    :type tags: dict[str, str]
    :param kwargs: Optional parameters.
    :type kwargs: dict
    :return: A registered model.
    :rtype: azureml.core.model.Model
    """
    azureml_run = run if isinstance(run, Run) else _azureml_run_from_mlflow_run(run)
    return azureml_run.register_model(model_name=name, model_path=path, **kwargs)


azureml.core.workspace.Workspace.get_mlflow_tracking_uri = _get_mlflow_tracking_uri
