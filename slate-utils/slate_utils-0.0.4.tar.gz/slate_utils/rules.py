import requests


class ForceExecutor:
    def __init__(self, session: requests.Session):
        self.session = session
        self.hostname = session.headers.get("origin")

    def force_execute(self, guid: str, scope: str = "person") -> requests.Response:
        """Force the given record to execute.

        Parameters
        ----------
        guid : str
            The guid of the record to execute.
        """
        uri = f"/manage/lookup/record?id={guid}"
        if scope == "dataset":
            uri = f"/manage/lookup/record?id={guid}"
        url = f"{self.hostname}/{uri}"
        data = {"cmd": "defer"}
        response = self.session.post(url, data=data)
        response.raise_for_status()
        return response
