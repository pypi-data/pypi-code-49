# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""Custom logging handlers
"""
import os
import socket

from dealer.git import git
from google.cloud.logging._helpers import retrieve_metadata_server  # pylint: disable=protected-access
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging.resource import Resource


SKIP_LOGRECORD_ATTRS = [
    'args',
    'levelname',
    'levelno',
    'message',
    'msecs',
    'msg',
    'process',
    'processName',
    'relativeCreated',
    'thread',
    'threadName',
]


class StackdriverLoggingHandler(CloudLoggingHandler):
    """Log to stackdriver with additional labels.

    Logs to stackdriver with k8s resource related information in the ```resource.labels``` field,
    and other additional information in the root message labels field. To add any key-value pair to
    the log struct's labels field, add it as dictionary to the logger's ```extra``` kwarg.
    Due to the limitations of python logging and google.cloud.logging's implementation of
    stackdriver support, it is not possible to add extra json-structured info to the jsonPayLoad,
    nor to put source related info (file, lineno) to stackdriver's sourceLocation field. Therefore
    everything will be added as a flat k:v list in the ```labels``` field.

    Example:
        logger.info('Starting processing of new scene', extra={'sceneId': 'TheSceneID'})

        this will add a labels.sceneId = 'TheSceneID' to the log struct in stackdriver.
    """

    def __init__(self, *args, tier='', app='', **kwargs):
        """Init

        Args:
            args (tuple): arguments
            tier (str): environment tier
            app (str): app name
            kwargs (dict): keyword arguments
        """

        super(StackdriverLoggingHandler, self).__init__(*args, **kwargs)

        project_id = retrieve_metadata_server('project/project-id')
        cluster_name = retrieve_metadata_server('instance/attributes/cluster-name')
        location = retrieve_metadata_server('instance/attributes/cluster-location')
        namespace_name = os.environ.get('KUBERNETES_NAMESPACE', '')
        container_name = os.environ.get('KUBERNETES_CONTAINER_NAME', '')
        node_name = os.environ.get('KUBERNETES_NODE_NAME', '')
        pod_name = socket.gethostname()
        try:
            tag = str(git.tag)
        except TypeError:
            tag = os.environ.get('{}_VERSION'.format(app.upper()), '')

        self.resource = Resource(
            type='k8s_container',
            labels={
                'cluster_name': cluster_name if cluster_name else '',
                'project_id': project_id if project_id else '',
                'location': location if location else '',
                'pod_name': pod_name if pod_name else '',
                'namespace_name': namespace_name,
                'container_name': container_name,
                'node_name': node_name,
            }
        )

        if self.labels is None:
            self.labels = {}

        self.labels.update(
            app=app,
            tier=tier,
            tag=tag,
        )

    def emit(self, record):
        """Actually log the specified logging record.

        Args:
            record (logging.LogRecord): The record to be logged.
        """
        message = super(StackdriverLoggingHandler, self).format(record)

        labels = self.labels.copy()

        for key, value in vars(record).items():
            if key not in SKIP_LOGRECORD_ATTRS and value is not None:
                labels[key] = str(value)

        self.transport.send(
            record, message, resource=self.resource, labels=labels)
