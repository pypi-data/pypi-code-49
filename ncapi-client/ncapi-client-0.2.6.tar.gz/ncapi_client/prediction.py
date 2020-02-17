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
from ncapi_client.utils import map_response, handle_response, AttrDict
import numpy as np
from tqdm import tqdm


class Prediction:
    """Prediction"""

    def __init__(self, client, uuid):
        """__init__

        Args:
            client: API client object
            uuid (str): uuid or name of the dataset
        """
        self._session = client._session
        self.url = client.url
        self.uuid = uuid

    @staticmethod
    def submit(client, trained_model_id, dataset_id):
        """Submit a new batch prediction job

        Args:
            client: API client
            trained_model_id: trained model id to use
            dataset_id: dataset id to use

        Returns:
            Prediction
        """
        payload = dict(trained_model=trained_model_id, dataset=dataset_id)
        info = handle_response(
            client._session.post(f"{client.url}/api/prediction/submit", json=payload)
        )
        return Prediction(client, info["uuid"])

    @property
    @map_response
    def info(self):
        """Prediction job info"""
        return self._session.get(f"{self.url}/api/prediction/{self.uuid}")

    @map_response
    def stop(self):
        """Stop this prediction job"""
        return self._session.post(f"{self.url}/api/prediction/{self.uuid}/stop")

    @map_response
    def restart(self):
        """Restart this prediction job"""
        return self._session.post(f"{self.url}/api/prediction/{self.uuid}/restart")

    @map_response
    def delete(self):
        """Delete this prediction job"""
        return self._session.delete(f"{self.url}/api/prediction/{self.uuid}")

    @property
    def current_results(self):
        """ids of current results"""
        resp = handle_response(
            self._session.get(f"{self.url}/api/prediction/{self.uuid}/results")
        )
        return resp

    def get_results(self, sample_ids):
        """get_results

        Args:
            sample_ids (list): id(s) of the sample(s) to retrieve

        Returns:
            AttrDict of numpy array: sample (including ground truth if present), and prediction
        """
        return [self._get_single_result(sid) for sid in tqdm(sample_ids)]

    def _get_single_result(self, sid):
        resp = handle_response(
            self._session.get(f"{self.url}/api/prediction/{self.uuid}/results/{sid}")
        )

        def _conv_to_npy(d):
            if isinstance(d, dict):
                res = d.copy()
                for k, v in res.items():
                    res[k] = _conv_to_npy(v)
                return res
            elif isinstance(d, list):
                return np.array(d)
            else:
                return d

        return AttrDict.convert(_conv_to_npy(resp))
