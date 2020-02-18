import json
import time
import logging
import grpc
from zeebe_grpc import gateway_pb2 as zeebe

class ZeebeWorker:

    def __init__(self, stub,
                 type_, worker_name, timeout=5*60*1000, request_timeout=1*60*1000, max_jobs_to_activate=1,
                 target=None):
        self.stub = stub
        self.type = type_
        self.worker_name = worker_name
        self.timeout = timeout
        self.request_timeout = request_timeout
        self.max_jobs_to_activate = max_jobs_to_activate
        self.target = target

    def subscribe(self):
        while True:
            logging.debug(f'Polling for {self.type}')
            try:
                req = zeebe.ActivateJobsRequest(
                        type=self.type,
                        worker=self.worker_name,
                        timeout=self.timeout,
                        requestTimeout=self.request_timeout,
                        maxJobsToActivate=self.max_jobs_to_activate)
                # ActivateJobsResponse returns as a stream, therefore a loop is used
                for resp in self.stub.ActivateJobs(req):
                    for job in resp.jobs:
                        logging.info(f'Handling job: {job.key} in instance: {job.workflowInstanceKey}')
                        try:
                            resp_variables = self.target(job)
                            if not isinstance(resp_variables, dict):
                                resp_variables = {}
                            complete_job_req = zeebe.CompleteJobRequest(
                                    jobKey=job.key, variables=json.dumps(resp_variables))
                            self.stub.CompleteJob(complete_job_req)
                            logging.info(f'Job handled: {job.key} in instance: {job.workflowInstanceKey}')
                        except BaseException as e:  # Catches every exception (https://docs.python.org/3.6/library/exceptions.html#exception-hierarchy)
                            logging.error(repr(e), exc_info=True)
                            fail_job_req = zeebe.FailJobRequest(
                                    jobKey=job.key, errorMessage=repr(e))
                            self.stub.FailJob(fail_job_req)
                            logging.info(f'Job failed: {job.key} in instance: {job.workflowInstanceKey}')
            except grpc.RpcError as e:
                logging.error(f'Cannot subscribe to {self.type}')
                time.sleep(10)

