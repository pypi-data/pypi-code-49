import os
from google.cloud import logging_v2
from google.cloud import dataproc_v1
from google.protobuf.struct_pb2 import Struct
from logging import StreamHandler, Formatter


def get_execution_id_from_request(request):
    return request.headers.get("Function-Execution-Id")

def get_execution_id_from_context(context):
    return context.event_id

class GcpHandler(StreamHandler):

    known_types = ['cloud_dataproc_job', 'cloud_function']

    def __init__(self, type, labels, format=None):
        super().__init__()

        if type not in self.known_types:
            raise ValueError("'type' must be one of %s but was %s" % (self.known_types,type))

        if format is None:
            format = '%(name)s:%(message)s'

        # For unknown reason, logging to Stackdriver doesnt work if cluster_name or resource_name not in labels
        if type == 'cloud_dataproc_job':
            labels["dataproc.googleapis.com/cluster_name"] = os.environ['DATAPROC_CLUSTER_NAME']
            labels["dataproc.googleapis.com/cluster_uuid"] = os.environ['DATAPROC_CLUSTER_UUID']

        self.type = type
        self.client = logging_v2.LoggingServiceV2Client()
        self.labels = labels
        self.log_name, self.resource = self._get_name_and_resource()
        self.setFormatter(self.NoExcFromatter(format))

    def emit(self, record):
        msg = self.format(record)
        self.log(record.levelname, message=msg, traceback=record.exc_text)


    def log(self, severity, **kwargs):
        json_payload = Struct()
        for k,v in kwargs.items():
            if v is not None:
                json_payload[k] = v
        self.client.write_log_entries(
            [{'json_payload': json_payload, 'severity': severity}],
            log_name=self.log_name, resource=self.resource, labels=self.labels
        )

    def _get_name_and_resource(self):
        if self.type == 'cloud_dataproc_job':

            # Get step_id and job_id
            job_id = os.environ['PWD'].split('/')[-1]
            step_id = job_id.rsplit('-',1)[0]

            # Get job_uuid
            client = dataproc_v1.JobControllerClient(
                client_options={'api_endpoint': 'europe-west1-dataproc.googleapis.com:443'})
            job = client.get_job(os.environ['GCP_PROJECT'], os.environ['DATAPROC_REGION'], job_id)
            job_uuid =  job.job_uuid

            self.labels['step_id'] = step_id

            # Name and resource
            name =  "projects/{}/logs/dataproc.job.driver".format(os.environ['GCP_PROJECT'])
            resource = {
               'labels': {
                  'job_id': job_id,
                  'job_uuid': job_uuid,
                  'region': os.environ['DATAPROC_REGION'],
               },
               'type': 'cloud_dataproc_job'
            }

        elif self.type == 'cloud_function':
            name = "projects/{}/logs/cloudfunctions.googleapis.com%2Fcloud-functions".format(os.environ['GCP_PROJECT'])
            resource = {
                'labels': {
                    'function_name': os.environ['FUNCTION_NAME'],
                    'region': os.environ['FUNCTION_REGION']
                },
                'type': 'cloud_function'
            }
        else:
            raise ValueError("'type' %s is not known'" % self.type)
        return name, resource

    class NoExcFromatter(Formatter):
        """
        Same as Formatter, only format method doesnt add stack or traceback information to message.
        The traceback as text is still cached in record.exc_text
        """

        def format(self, record):
            record.message = record.getMessage()
            if self.usesTime():
                record.asctime = self.formatTime(record, self.datefmt)
            s = self.formatMessage(record)
            if record.exc_info:
                if not record.exc_text:
                    record.exc_text = self.formatException(record.exc_info)

            return s



def add_labels(logger, labels):
    logger.gcp_handler.labels.update(labels)

def add_gcp_handler(logger,type,labels):
    if getattr(logger,'has_gcp_handler',False):
        RuntimeError('logger already has a GcpHandler')

    # Create handler
    if logger.name is None:
        gcp_handler = GcpHandler(type, labels,'%(message)s')
    else:
        gcp_handler = GcpHandler(type,labels)

    # Add handler
    logger.addHandler(gcp_handler)
    logger.gcp_handler = gcp_handler
    logger.has_gcp_handler = True
    return logger




