from alfa_sdk.common.base import BaseClient


class SecretsClient(BaseClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list_names(self):
        return self.session.request("get", "core", "/api/Secrets/list")

    def fetch_value(self, name):
        return self.session.request("get", "core", "/api/Secrets/?name={}".format(name))

    def fetch_values(self, names):
        body = {"names": names}
        return self.session.request("post", "core", "/api/Secrets/batch", json=body)

    def store_value(self, name, value, *, description=None):
        body = {"name": name, "value": value, "description": description}
        return self.session.request("post", "core", "/api/Secrets/", json=body)

    def remove_value(self, name):
        body = {"name": name}
        return self.session.request("post", "core", "/api/Secrets/remove", json=body)
