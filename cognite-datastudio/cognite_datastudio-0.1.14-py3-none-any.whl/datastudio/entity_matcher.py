import time
from typing import Dict, List

from cognite.datastudio.exceptions import ModelFailedException


def request(client, path, request_type, data=None):
    project = client._config.project
    url = f"/api/playground/projects/{project}/context/entity_matching{path}"
    if request_type == "GET":
        response = client._api_client._get(url)
    else:
        response = client._api_client._post(url, json=data, headers={"Content-Type": "application/json"})

    return response


class Model:
    def __init__(self, client, model_id):
        self.model_id = model_id
        self.client = client

    def __repr__(self):
        return "Model(id: %d)" % self.model_id

    def predict(self, y: List[str]):
        y = list(y)
        response = request(self.client, f"/{self.model_id}/predict", "POST", data={"items": y})
        data = response.json()
        job_id = data["jobId"]
        while data["status"] != "Completed":
            response = request(self.client, f"/{self.model_id}/predict/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"model_id: {self.model_id}")
            time.sleep(1)
        return data["items"]


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
                raise ModelFailedException(f"model_id: {model_id}")
            time.sleep(1)
        return Model(self.client, model_id)

    def create_rules(self, matches: List[Dict]):
        matches = list(matches)
        response = request(self.client, "/rules", "POST", data={"items": matches})
        data = response.json()
        job_id = data["jobId"]

        while data["status"] != "Completed":
            response = request(self.client, f"/rules/{job_id}", "GET")
            data = response.json()
            if data["status"] == "Failed":
                raise ModelFailedException(f"job_id: {job_id}")
            time.sleep(1)
        return data["items"]
