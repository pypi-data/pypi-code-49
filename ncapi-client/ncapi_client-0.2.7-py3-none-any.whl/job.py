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
from ncapi_client.utils import map_response
from time import sleep


class Job:
    """Job"""

    def __init__(self, client, uuid):
        """__init__

        Args:
            client: API client object
            uuid (str): uuid or name of the dataset
        """
        self._session = client._session
        self.url = client.url
        self.uuid = uuid

    @map_response
    def delete(self):
        """Delete this job."""
        return self._session.delete(f"{self.url}/api/jobs/{self.uuid}")

    @property
    @map_response
    def info(self):
        """Get info on the conversion job."""
        return self._session.get(f"{self.url}/api/jobs/{self.uuid}")

    @map_response
    def stop(self):
        """Stop a job."""
        return self._session.post(f"{self.url}/api/jobs/{self.uuid}/stop")

    @map_response
    def restart(self):
        """Restart a job."""
        return self._session.post(f"{self.url}/api/jobs/{self.uuid}/restart")
