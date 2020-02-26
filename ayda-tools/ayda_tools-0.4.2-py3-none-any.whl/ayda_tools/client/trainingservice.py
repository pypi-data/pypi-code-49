from .connection import ServerConnection
from .callbacks import create_all_result_callbacks
from .resultservice import ResultService

from ..interfaces import JobInfo
from ..parsing import create_object

import logging
import os

logger = logging.getLogger(__name__)


class TrainingService:
    def __init__(self, connection: ServerConnection, result_service: ResultService):
        self.result_service = result_service
        self.connection = connection

    def download_pretrained_model(self, job: JobInfo):
        temp_model_folder = ""
        if job.pretrained_model:
            pre_job, filename = job.pretrained_model.split("#")
            model = self.result_service.download_model(pre_job, filename)
            if model is None:
                return None
            temp_model_folder = "/media"
            if not os.path.isdir(temp_model_folder):
                logger.error(
                    "Could not save pretrained model: "
                    + temp_model_folder
                    + " is not present."
                )
                return None, ""
            temp_model_folder = temp_model_folder + "/start_model"
            open(temp_model_folder, "wb").write(model)
        return temp_model_folder

    def train_job(self, job: JobInfo, pretrained_model_path: str = ""):

        model = create_object(job.model_parameter)
        training_data = create_object(job.training_data)

        train_options = job.train_options
        model.train(
            training_data,
            model_dir="/media",
            callbacks=create_all_result_callbacks(
                "/media/model{}.h5",
                job,
                connection=self.connection,
                result_service=self.result_service,
            ),
            pretrained_model_name=pretrained_model_path,
            epochs=train_options.epochs,
            epoch_size=train_options.epoch_size,
            timeout_secs=train_options.timeout_secs,
            validation_size=train_options.validation_size,
        )
