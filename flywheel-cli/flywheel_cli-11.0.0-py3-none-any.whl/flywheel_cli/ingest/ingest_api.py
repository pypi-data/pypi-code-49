"""Provides IngestApi class"""

import json
import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from . import schemas

log = logging.getLogger(__name__)


class IngestApi:
    """Ingest api"""

    def __init__(self, ingest_id, config):
        self.ingest_id = ingest_id
        self.config = config
        self.session = Session(self.config.cluster, headers=self.get_auth_header(config))

    @classmethod
    def create(cls, config):
        """Create a new ingest operation and instantiate an ingest manager with
        the newly created ingest opreation.
        """
        headers = cls.get_auth_header(config)
        ingest = schemas.IngestInAPI(
            src_fs=config.src_fs_url,
            config=config.dict(exclude_none=True),
        )
        session = Session(config.cluster, headers=headers)
        resp = session.post("/ingests", json=ingest.dict())
        resp.raise_for_status()
        return cls(resp.json()["id"], config)

    def get_ingest(self):
        """Get ingest operation."""
        resp = self.session.get(f"/ingests/{self.ingest_id}")
        return schemas.IngestOutAPI(**resp.json())

    def start_ingest(self):
        """Start the ingest and create an initial scan task."""
        resp = self.session.post(f"/ingests/{self.ingest_id}/start")
        return schemas.IngestOutAPI(**resp.json())

    def review_ingest(self, changes=None):
        """Add any review adjustments and create a prepare task."""
        resp = self.session.post(f"/ingests/{self.ingest_id}/review", json=changes)
        return schemas.IngestOutAPI(**resp.json())

    def abort_ingest(self):
        """Abort ingest operation."""
        resp = self.session.post(f"/ingests/{self.ingest_id}/abort")
        return schemas.IngestOutAPI(**resp.json())

    def get_ingest_progress(self):
        """Get ingest summary including status, hierarchy and progress info."""
        resp = self.session.get(f"/ingests/{self.ingest_id}/progress")
        return schemas.Progress(**resp.json())

    def get_ingest_summary(self):
        """Get ingest summary including status, hierarchy and progress info."""
        resp = self.session.get(f"/ingests/{self.ingest_id}/summary")
        return schemas.Summary(**resp.json())

    def get_ingest_report(self):
        """Get ingest status, elapsed time per status and list of failed tasks"""
        resp = self.session.get(f"/ingests/{self.ingest_id}/report")
        return schemas.Report(**resp.json())

    def get_ingest_tree(self):
        """Yield hierarchy nodes (containers and files)."""
        resp = self.session.get(f"/ingests/{self.ingest_id}/tree", stream=True)
        for line in resp.iter_lines():
            if line:  # filter out keep-alive new lines
                yield schemas.ContainerOut(**json.loads(line.decode("utf-8")))

    def load_subject_csv(self, subject_csv):
        """Load subjects from file"""
        resp = self.session.post(f"/ingests/{self.ingest_id}/subjects", files={
            "subject_csv": subject_csv,
        })
        return resp.json()  # TODO add some useful response

    def get_subjects_csv(self):
        """Get subjects"""
        resp = self.session.get(f"/ingests/{self.ingest_id}/subjects", stream=True)
        for line in resp.iter_lines():
            if line:  # filter out keep-alive new lines
                yield line.decode("utf-8") + "\n"

    def get_audit_logs(self):
        """Get audit logs of ingest operation"""
        resp = self.session.get(f"/ingests/{self.ingest_id}/audit", stream=True)
        for line in resp.iter_lines():
            if line:  # filter out keep-alive new lines
                yield line.decode("utf-8") + "\n"

    def get_deid_logs(self):
        """Get deid logs of ingest"""
        resp = self.session.get(f"/ingests/{self.ingest_id}/deid", stream=True)
        for line in resp.iter_lines():
            if line:  # filter out keep-alive new lines
                yield line.decode("utf-8") + "\n"

    @staticmethod
    def get_auth_header(config):
        """Get auth header"""
        api_key = config.get_api_key()
        return {"Authorization": f"scitran-user {api_key}"}


class Session(requests.Session):
    """Session class with predefined host name."""

    def __init__(self, host, headers=None, timeout=10, retries=3, backoff_factor=0.3, status_forcelist=None):
        super().__init__()
        self.host = host.rstrip("/") + "/"
        self.headers.update(headers or {})
        self.timeout = timeout
        self.retries = retries
        # sleep time: {backoff factor} * (2 ^ ({number of total retries} - 1))
        self.backoff_factor = backoff_factor
        self.status_forcelist = status_forcelist or (500, 502, 504)
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.mount('http://', adapter)
        self.mount('https://', adapter)

    def request(self, method, url, **kwargs):  # pylint: disable=arguments-differ
        url = self.host + url.lstrip("/")
        kwargs.setdefault("timeout", self.timeout)
        resp = super().request(method, url, **kwargs)
        resp.raise_for_status()
        return resp
