import typing as t
import requests
from requests import Response
from uuid import UUID
from urllib.parse import urljoin
from datetime import datetime, timezone
from json import dumps

from logging import Logger
from .encoders import CustomJSONEncoder


class Writer:
    def __init__(
        self, url: str,
        workspace_name: str,
        params: t.Dict[str, t.Any] = {},
        logger: t.Optional[Logger] = None,
    ) -> None:
        self.url = url
        self._trace_id_map: t.Dict[str, UUID] = {}
        self._workspace_id = self.register_workspace(
            name=workspace_name,
            params=params,
        )
        self.workspace_name = workspace_name
        self._logger = logger

    def _post(self, url: str, data: t.Any) -> Response:
        return requests.post(
            url,
            data=dumps(data, cls=CustomJSONEncoder),
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'}
        )

    def register_workspace(self, name: str, params: t.Dict[str, t.Any]) -> UUID:
        res = self._post(
            urljoin(self.url, 'workspace/register'),
            data={
                "name": name,
                "params": params,
            }
        )
        res.raise_for_status()
        return res.json()

    def register_trace(self, name: str) -> UUID:
        if name in self._trace_id_map:
            return self._trace_id_map[name]
        res = self._post(
            urljoin(self.url, 'trace/register'),
            data={
                "name": name,
                'workspace_id': self._workspace_id,
            }
        )
        res.raise_for_status()
        self._trace_id_map[name] = res.json()
        return res.json()

    def add_scalars(self, values: t.Dict[str, float], ts: t.Optional[datetime] = None) -> int:
        _values = {self.register_trace(k): v for k, v in values.items()}
        _ts = ts if ts is not None else datetime.now(timezone.utc)
        res = self._post(
            urljoin(self.url, 'point/add-scalars'),
            data={
                "values": _values,
                "ts": _ts,
            }
        )
        res.raise_for_status()
        if self._logger is not None:
            self._logger.info(f'{self.workspace_name} - add_scalars: {values}')
        return res.json()
