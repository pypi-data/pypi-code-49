from pylaunch.roku.server import Roku


class Application:
    def __init__(
        self, name: str, id: str, type: str, subtype: str, version: str, roku: Roku
    ):
        self.name = name
        self.id = id
        self.type = type
        self.subtype = subtype
        self.version = version
        self.roku = roku

    def __repr__(self):
        return "{cn}(name='{name}', id='{id}', type='{type}', subtype='{subtype}', version='{version}')".format(
            cn=self.__class__.__name__,
            name=self.name,
            id=self.id,
            type=self.type,
            subtype=self.subtype,
            version=self.version,
        )

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    @property
    def icon(self):
        request_url = f"{self.roku.address}/query/icon/{self.id}"
        response = self.request.get(request_url, stream=True)
        if str(response.headers["Content-Length"]) != "0":
            filetype = response.headers["Content-Type"].split("/")[-1]
            return {"content": response.content, "filetype": filetype}

    def launch(self, callback: Callable[[None], dict] = None, **kwargs) -> None:
        request_url = f"{self.roku.address}/launch/{self.id}"
        response = self.request.post(
            request_url, params=kwargs, headers={"Content-Length": "0"}
        )
        if callback:
            results = {"request_url": request_url, "status_code": response.status_code}
            callback(results)
