import time
from typing import List

from cognite.datastudio.exceptions import ModelFailedException


def request(client, path, request_type, data=None):
    project = client._config.project
    api_key = client._config.api_key
    url = f"/api/playground/projects/{project}/context/entity_extraction{path}"
    if request_type == "GET":
        response = client._api_client._get(url)
    else:
        response = client._api_client._post(
            url, json=data, headers={"Content-Type": "application/json", "API-Key": api_key}
        )

    return response


class EntityExtraction:
    def __init__(self, client):
        self.client = client

    def extract_entities(self, fileIds: List[int], entities: List[str]):
        entities = list(entities)
        response = request(self.client, "/extract_new", "POST", data={"fileIds": fileIds, "entities": entities})

        data = response.json()
        job_id = data["jobId"]
        while data["status"] != "Completed":
            response = request(self.client, f"/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {job_id} error: {data.get('error_message')}")
            time.sleep(1)
        return data
