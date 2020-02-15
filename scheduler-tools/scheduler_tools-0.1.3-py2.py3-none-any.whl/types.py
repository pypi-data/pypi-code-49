from typing import Union
from typing_extensions import TypedDict
from pathlib import Path


class PrefDict(TypedDict):
    GateWay = TypedDict('gateway', {'url': str, 'user': str, 'identityfile': Union[str, Path]})
    gateway: GateWay
    localfolder: str
    dask_port: int
    dashboard_port: int


Pathlike = Union[Path, str]
PathDict = Union[Pathlike, PrefDict, type(None)]
