from typing import List, Iterable
from requests import Response, Session


class BaseConsolidator:
    """Base consolidator class"""

    base = ""
    dataset = ""
    scope = ""
    folder = ""

    def __init__(self, session: Session):
        self.session = session

    def merge(self, id: str, reverse=False) -> Response:
        hostname = self.session.headers.get("origin")
        url = f"{hostname}/manage/database/dedupe?cmd=compare&id={id}"
        payload = {
            "m": id,
            "reverse": 1 if reverse else 0,
            "dataset": 0 if self.dataset == "" else self.dataset,
            "scope": self.scope,
            "folder": self.folder,
            "cmd": "merge",
        }
        r = self.session.post(url, payload)
        r.raise_for_status()
        return r

    def merge_bulk(self, ids: Iterable[str]) -> Response:
        hostname = self.session.headers.get("origin")
        url = f"{hostname}/manage/database/dedupe?cmd=results&q={self.folder}&dataset=&scope={self.scope}"
        payload = {
            "base": self.base,
            "dataset": 0 if self.dataset == "" else self.dataset,
            "scope": self.scope,
            "folder": self.folder,
            "m": ids,
            "cmd": "merge",
        }
        r = self.session.post(url, payload)
        r.raise_for_status()
        return r

    def exclude(self, ids: Iterable[str]) -> Response:
        if isinstance(ids, str):
            ids = [ids]
        hostname = self.session.headers.get('origin')
        url = f"{hostname}/manage/database/dedupe?cmd=results&q={self.folder}&dataset=&scope={self.scope}"
        payload = {
            'base': self.base,
            'dataset': 0 if self.dataset == '' else self.dataset,
            'scope': self.scope,
            'folder': self.folder,
            'm': ids,
            'cmd': 'exclude'
        }
        r = self.session.post(url, payload)
        r.raise_for_status()
        return r


class SchoolConsolidator(BaseConsolidator):
    base = "58a8d2ff-09c9-4fd9-a272-029a43729c93"
    scope = "school"
    folder = "Key"


class SchoolKeyConsolidator(BaseConsolidator):
    base = "58a8d2ff-09c9-4fd9-a272-029a43729c93"
    scope = "school_key"
    folder = "Name"

    def merge(self, id: str, update=False) -> Response:
        """Merge the indicated duplicate

        Parameters
        ----------
        id : str
            The id of the duplicate record ([duplicate].[id])
        update : bool
            When True, record will be linked & updated with the matched organization record
        """
        hostname = self.session.headers.get("origin")
        url = f"{hostname}/manage/database/dedupe?cmd=compare&id={id}"
        payload = {
            "m": id,
            "reverse": 0,
            "dataset": 0 if self.dataset == "" else self.dataset,
            "scope": self.scope,
            "folder": self.folder,
            "cmd": "merge_update" if update else "merge",
        }
        r = self.session.post(url, payload)
        r.raise_for_status()
        return r

    def merge_bulk(self, ids: List[str]) -> Response:
        hostname = self.session.headers.get("origin")
        url = f"{hostname}/manage/database/dedupe?cmd=results&q={self.folder}&dataset=&scope={self.scope}"
        payload = {
            "base": self.base,
            "dataset": 0 if self.dataset == "" else self.dataset,
            "scope": self.scope,
            "folder": self.folder,
            "m": ids,
            "cmd": "merge",
        }
        r = self.session.post(url, payload)
        r.raise_for_status()
        return r
