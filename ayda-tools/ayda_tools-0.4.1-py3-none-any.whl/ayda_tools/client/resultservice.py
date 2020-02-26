import requests

from .connection import ServerConnection
import sys
import multiprocessing as mp
import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class ResultService:
    def __init__(self, connection: ServerConnection):
        self.connection = connection

    def upload_model(self, job_ref: str, file_name: str, binary_data):
        try:
            response = self.connection.send_server_request(
                "get_model_upload_url/" + job_ref + "/" + file_name, method="GET"
            )
            requests.put(response["url"], data=binary_data)
        except ConnectionError:
            logger.warning("Could not get upload URL")

    def download_model(self, job_ref: str, filename: str) -> Optional[bytes]:
        try:
            response = self.connection.send_server_request(
                "get_pretrained_model_download_url/{}/{}".format(filename, job_ref),
                method="GET",
            )
            model = requests.get(response["url"])
            return model.content

        except ConnectionError:
            logger.warning("Could not download model")
            return None


class AydaLogger:
    """
    stream to REST-sender
    """

    def __init__(self, job_ref: str, connection: ServerConnection):
        self.job_ref = job_ref
        self.connection = connection
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.lines = mp.Queue()
        self.running = mp.Value("b", False)
        self.process = mp.Process(target=self._upload_loop)

    def write(self, buf: str):
        for line in buf.rstrip().splitlines():
            self.lines.put(line)
        self.stdout.write(buf)

    def __enter__(self):
        sys.stdout = self
        sys.stderr = self
        self.process.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.running.value = False
        if self.process.is_alive():
            self.process.join()

    def _upload_loop(self):
        self.running.value = True
        while self.running.value:
            time.sleep(5)
            lines = []
            while not self.lines.empty():
                lines.append(self.lines.get())
            if not lines:
                continue
            out = "\n".join(lines)
            try:
                self.connection.send_server_request(
                    "send_log/" + self.job_ref, data={"log": out}
                )
            except ConnectionError:
                pass

    def flush(self):
        pass
