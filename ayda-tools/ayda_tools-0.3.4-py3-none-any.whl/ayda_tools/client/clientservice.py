import asyncio
import logging
from multiprocessing import Process
from typing import Optional

import jsonpickle

from .connection import ServerConnection
from .resultservice import ResultService, AydaLogger
from .trainingservice import TrainingService
from ..interfaces import JobInfo, ClientMode

logger = logging.getLogger(__name__)


class AnalyticToolClient:
    GRAB_JOB_INTERVAL = 30
    RESULT_SENDING_INTERVAL = 25
    HEARTBEAT_INTERVAL = 30

    def __init__(
        self, connection: ServerConnection, mode: ClientMode = ClientMode.MULTIPLE_JOB
    ):

        self.connection = connection
        self.result_service = ResultService(self.connection)
        self.training_service = TrainingService(self.connection, self.result_service)
        self.mode = mode

        self.train_process = None
        self.result_sending_task = None
        self.train_process = None
        self.active_job_ref = ""

    def process_job(self) -> Optional[JobInfo]:
        job = self.get_next_job_from_server()

        if job is None:
            return None
        self.active_job_ref = job.obj_ref
        self.train_process = Process(target=self.start_training, kwargs={"job": job})
        self.train_process.start()

        return job

    def get_next_job_from_server(self) -> Optional[JobInfo]:
        """
        get next available Job for this client
        """
        try:
            response = self.connection.send_server_request("get_next_job")
            if not response or "job" not in response or response["job"] == "null":
                return None
        except ConnectionError:
            return None
        next_job = jsonpickle.decode(response["job"])

        return next_job

    async def grab_job_job(self):
        while True:
            await asyncio.sleep(self.GRAB_JOB_INTERVAL)
            if self.train_process is not None and self.train_process.is_alive():
                logger.info("Job running")
                continue
            logger.info("Try to grab new Job")

            job_name = self.process_job()

            if (
                self.mode == ClientMode.ONE_JOB
                and self.train_process is not None
                and not self.train_process.is_alive()
            ):
                break
            if job_name is None:
                logger.info("No new Job available")
                continue

    async def heartbeat(self):
        while True:
            await asyncio.sleep(self.HEARTBEAT_INTERVAL)
            logger.info("Heartbeat with job " + self.active_job_ref)
            try:
                response = self.connection.send_server_request(
                    "heartbeat", {"job_ref": self.active_job_ref}
                )
                if response["cancelled"] and self.train_process.is_alive():
                    self.train_process.terminate()
            except ConnectionError:
                continue

    def start(self):
        asyncio.get_event_loop().create_task(self.heartbeat())
        grab_job_job = asyncio.get_event_loop().create_task(self.grab_job_job())
        asyncio.get_event_loop().run_until_complete(grab_job_job)

    def start_training(self, job: JobInfo):
        """
        starts training in a process
        Args:
            job: the trainingsparameter are taken from this job
            model: for resumed jobs the path to an existing model

        """
        logger.info("Start Training")

        with AydaLogger(job_ref=job.obj_ref, connection=self.connection):

            pretrained_model = self.training_service.download_pretrained_model(job)
            self.training_service.train_job(job, pretrained_model)

        logger.info("Finish training and upload model")
        self.active_job_ref = ""

        self.connection.send_server_request("finish_job", {"job_ref": job.obj_ref})
