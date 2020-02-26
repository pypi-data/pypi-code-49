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
from ncapi_client.utils import (
    map_response,
    handle_response,
    AttrDict,
    delete_dependent_jobs,
)
from io import BytesIO
import glob
import re
import yaml


class TrainedModel:
    """TrainedModel"""

    def __init__(self, client, uuid):
        """__init__

        Args:
            client: API client object
            uuid (str): uuid or name of the trained model
        """
        self._session = client._session
        self.url = client.url
        self.uuid = uuid
        # needed to force delete, not very nice though
        self._client = client

    @staticmethod
    def add(client, config, checkpoint, stamp=None):
        """Add a new trained model

        Args:
            config: trained model config
            checkpoint: compatible §model training checkpoint

        Returns:
            new TrainedModel
        """
        files = [
            ("checkpoint", open(path, "rb")) for path in glob.glob(f"{checkpoint}.*")
        ]
        if stamp is not None:
            with open(config) as f:
                cfg = yaml.safe_load(f)
            cfg["model"]["revision"] = stamp
            with open(config, "w") as f:
                yaml.dump(cfg, f)
        files += [("config", open(config, "rb"))]
        resp = handle_response(
            client._session.post(f"{client.url}/api/trained_model/add", files=files)
        )
        return TrainedModel(client, resp["uuid"])

    @map_response
    def delete(self, force=False):
        """delete
        Args:
            force (bool): force deletion of dependent resources (default False)
        """
        if force:
            delete_dependent_jobs(self._client, {"trained_model": self.info.uuid})
        return self._session.delete(f"{self.url}/api/trained_model/{self.uuid}")

    @property
    @map_response
    def info(self):
        """Trained model info"""
        return self._session.get(f"{self.url}/api/trained_model/{self.uuid}")

    @property
    def config(self):
        """Trained model config"""
        resp = handle_response(
            self._session.get(f"{self.url}/api/trained_model/{self.uuid}/config")
        )
        return AttrDict.convert(resp["model"])

    def download(self):
        """Download this trained model as a tar.gz archive
        
        Returns:
            BytesIO: tar.gz archive as bytes
        """
        resp = self._session.get(f"{self.url}/api/trained_model/{self.uuid}/download")
        resp.raise_for_status()
        buff = BytesIO(resp.content)
        buff.name = re.findall("filename=(.+)", resp.headers["content-disposition"])[0]
        return buff
