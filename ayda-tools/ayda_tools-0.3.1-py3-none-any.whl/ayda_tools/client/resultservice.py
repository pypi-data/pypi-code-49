import requests

from .connection import ServerConnection


class ResultService:
    def __init__(self, connection: ServerConnection):
        self.connection = connection

    def upload_model(self, job_ref: str, file_name: str, binary_data):
        response = self.connection.send_server_request(
            "get_model_upload_url/" + job_ref + "/" + file_name, method="GET"
        )
        requests.put(response["url"], data=binary_data)

    def download_model(self, job_ref: str, filename: str) -> bytes:
        response = self.connection.send_server_request(
            "get_pretrained_model_download_url/{}/{}".format(filename, job_ref),
            method="GET",
        )
        model = requests.get(response["url"])
        return model.content


class StreamToREST:
    """
    stream to REST-sender
    """

    def __init__(self, job_ref: str, connection: ServerConnection):
        self.job_ref = job_ref
        self.connection = connection

    def write(self, buf: str):
        for line in buf.rstrip().splitlines():
            self.connection.send_server_request(
                "send_log/" + self.job_ref, data={"log": line}
            )

    def flush(self):
        pass
