import time
from typing import Dict, List

from cognite.client.data_classes._base import CogniteResource, CogniteResourceList
from cognite.datastudio.exceptions import ModelFailedException


def request(client, path, request_type, data=None):
    project = client._config.project
    url = f"/api/playground/projects/{project}/context/entity_matching{path}"
    if request_type == "GET":
        response = client._api_client._get(url)
    else:
        response = client._api_client._post(url, json=data, headers={"Content-Type": "application/json"})

    return response


class EntityMatchingModel(CogniteResource):
    def __init__(self, model_id=None, status=None, error_message=None, cognite_client=None):
        self.model_id = model_id
        self.status = status
        self.error_message = error_message
        self._cognite_client = cognite_client

    def __repr__(self):
        return "Model(id: %d,status: %s)" % (self.model_id, self.status)

    def predict(self, y: List[str]):
        y = list(y)
        response = request(self._cognite_client, f"/{self.model_id}/predict", "POST", data={"items": y})
        data = response.json()
        job_id = data["jobId"]
        while data["status"] != "Completed":
            response = request(self._cognite_client, f"/{self.model_id}/predict/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {self.model_id} error: {data.get('error_message')}")
            time.sleep(1)
        return data["items"]


class EntityMatchingModelList(CogniteResourceList):
    _RESOURCE = EntityMatchingModel
    _ASSERT_CLASSES = False


class EntityMatcher:
    def __init__(self, client):
        self.client = client

    def fit(self, X: List[str]):
        X = list(X)
        response = request(self.client, "/fit", "POST", data={"items": X})

        data = response.json()
        model_id = data["modelId"]
        while data["status"] != "Completed":
            response = request(self.client, f"/{model_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {model_id} error: {data.get('error_message')}")
            time.sleep(1)
        return EntityMatchingModel(
            model_id=model_id,
            status=data["status"],
            error_message=data.get("error_message"),
            cognite_client=self.client,
        )

    def create_rules(self, matches: List[Dict]):
        matches = list(matches)
        response = request(self.client, "/rules", "POST", data={"items": matches})
        data = response.json()
        job_id = data["jobId"]

        while data["status"] != "Completed":
            response = request(self.client, f"/rules/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {job_id} error: {data.get('error_message')}")
            time.sleep(1)
        return data["items"]

    def retrieve(self, model_id: int) -> EntityMatchingModel:
        response = request(self.client, f"/{model_id}", "GET")
        return EntityMatchingModel._load(response.json())

    def list(self) -> EntityMatchingModelList:
        response = request(self.client, "/", "GET")
        return EntityMatchingModelList._load(response.json()["items"])
