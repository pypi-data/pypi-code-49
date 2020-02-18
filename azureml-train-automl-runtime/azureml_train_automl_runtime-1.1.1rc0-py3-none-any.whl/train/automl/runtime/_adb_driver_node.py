# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import threading
import time

from azureml.core import Run
from azureml.core.authentication import AzureMLTokenAuthentication
from azureml.core.experiment import Experiment
from azureml.core.workspace import Workspace
from ._adb_run_experiment import adb_run_experiment


class _AdbDriverNode(threading.Thread):
    """This code initiates the experiments to be run on worker nodes by calling adb map and collect."""

    def __init__(self, name, input_data, spark_context, partition_count, run_id):
        """
        Initialize the _AdbDriverNode class.

        :param name: Name of the experiment run.
        :type name: string
        :param input_data: Input context data for the worker node run.
        :type input_data: Array of tuple [(worker_id, context_dictionary),(worker_id, context_dictionary)]
        :param spark_context: Spark context.
        :type spark_context: spark context.
        :param partition_count: Partition count.
        :type partition_count: int
        :param run_id: Run id.
        :type run_id: string
        """
        super(_AdbDriverNode, self).__init__()
        self.name = name
        self.input_data = input_data
        self.spark_context = spark_context
        self.partition_count = partition_count
        self.run_id = run_id

    def run(self):
        self.spark_context.setJobGroup(
            self.run_id, "AutoML Run on spark", True)
        automlRDD = self.spark_context.parallelize(
            self.input_data, self.partition_count)
        automlRDD.map(adb_run_experiment).collect()

    def cancel(self):
        try:
            self.spark_context.cancelJobGroup(self.run_id)
        except Exception:
            raise Exception(
                "Failed to cancel spark job with id: {}".format(self.run_id))

    def _rehydrate_experiment(self, run_context):
        subscription_id = run_context.get('subscription_id', None)
        resource_group = run_context.get('resource_group', None)
        workspace_name = run_context.get('workspace_name', None)
        location = run_context.get('location', None)
        aml_token = run_context.get('aml_token', None)
        aml_token_expiry = run_context.get('aml_token_expiry', None)
        experiment_name = run_context.get('experiment_name', None)
        parent_run_id = run_context.get('parent_run_id', None)
        service_url = run_context.get('service_url', None)
        auth = AzureMLTokenAuthentication.create(aml_token,
                                                 AzureMLTokenAuthentication._convert_to_datetime(aml_token_expiry),
                                                 service_url,
                                                 subscription_id,
                                                 resource_group,
                                                 workspace_name,
                                                 experiment_name,
                                                 parent_run_id)
        workspace = Workspace(subscription_id,
                              resource_group, workspace_name,
                              auth=auth,
                              _location=location,
                              _disable_service_check=True)
        experiment = Experiment(workspace, experiment_name)
        return experiment

    def _rehydrate_parent_run(self, run_context):
        parent_run_id = run_context.get('parent_run_id', None)
        return Run(self._rehydrate_experiment(run_context), parent_run_id)
