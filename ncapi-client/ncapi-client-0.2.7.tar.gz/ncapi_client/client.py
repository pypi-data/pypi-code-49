# Copyright (C) 2019  Neural Concept SA

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ========================================================================
import os
from functools import wraps
import requests
from ncapi_client.dataset import Dataset
from ncapi_client.job import Job
from ncapi_client.prediction import Prediction
from ncapi_client.session import Session
from ncapi_client.trained_model import TrainedModel
from ncapi_client.training import Training
from ncapi_client.utils import map_response, ResourceList, handle_response


# Requests timeout
TIMEOUT = 60

MAX_RETRY = 3


def timeout(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return f(*args, **kwargs)
    return wrapper


class SessionAdapter(requests.Session):

    def __init__(self):
        super().__init__()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRY)
        self.mount('http://', adapter)
        self.mount('https://', adapter)

    get = timeout(requests.Session.get)
    post = timeout(requests.Session.post)
    delete = timeout(requests.Session.delete)
    put = timeout(requests.Session.put)
    patch = timeout(requests.Session.patch)


class Client:
    """All-in-one client for NCAPI"""

    def __init__(self, url=None, username=None, password=None, access_token=None):
        """__init__

        Args:
            url (str): url where the API is served
            username (str): username for authentication
            password (str): password for authentication
            access_token (str): JWT access token
        """

        url = url or os.environ.get("NCAPI_URL")
        username = username or os.environ.get("NCAPI_USERNAME")
        password = password or os.environ.get("NCAPI_PASSWORD")
        access_token = access_token or os.environ.get("NCAPI_ACCESS_TOKEN")
        ssl_cert = os.environ.get("NCAPI_CERT")

        self._session = SessionAdapter()

        self._session.verify = ssl_cert or True

        if username and password and url:
            self.url = url
            resp = self._login(username, password)
            self.access_token = resp.access_token
        elif access_token and url:
            self.url = url
            self.access_token = access_token
        else:
            raise ValueError(
                "You should specify username-password-url or access_token-url: "
                "either explicitly or through environment variables"
            )

    def __repr__(self):
        return f"Client({self.url})"

    @map_response
    def _login(self, username, password):
        payload = dict(username=username, password=password)
        return self._session.post(f"{self.url}/api/user/login", json=payload)

    @property
    def datasets(self):
        """List of datasets"""
        dataset_list = handle_response(self._session.get(f"{self.url}/api/dataset"))
        return ResourceList([Dataset(self, info["uuid"]) for info in dataset_list])

    @property
    def trainings(self):
        """List of trainings"""
        trainings = handle_response(self._session.get(f"{self.url}/api/training"))
        return ResourceList([Training(self, info["uuid"]) for info in trainings])

    @property
    def trained_models(self):
        """List of trained models"""
        trained_models = handle_response(
            self._session.get(f"{self.url}/api/trained_model")
        )
        return ResourceList(
            [TrainedModel(self, info["uuid"]) for info in trained_models]
        )

    @property
    def jobs(self):
        """List of jobs"""
        jobs = handle_response(self._session.get(f"{self.url}/api/jobs"))
        return ResourceList([Job(self, info["uuid"]) for info in jobs])

    @property
    def predictions(self):
        """List of predictions"""
        predictions = handle_response(self._session.get(f"{self.url}/api/prediction"))
        return ResourceList([Prediction(self, info["uuid"]) for info in predictions])

    @property
    def sessions(self):
        """List of sessions"""
        sessions = handle_response(self._session.get(f"{self.url}/api/session/list"))
        return ResourceList([Session(self, info["id"]) for info in sessions])
