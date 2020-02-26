from cognite.client import CogniteClient as _Client
from cognite.datastudio import utils


class Client(_Client):
    def __init__(self, **kwargs):
        kwargs["api_key"] = kwargs.get("api_key", utils.get_api_key())
        super().__init__(**kwargs)
