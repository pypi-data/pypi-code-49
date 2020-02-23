from __future__ import annotations
import typing as tp

from logexp.utils.jsondict import JsonDict


class Params(JsonDict):
    """parameter dict"""

    @classmethod
    def from_json(cls, params_dict: tp.Dict[str, tp.Any]) -> Params:
        # pylint: disable=arguments-differ
        return Params(params_dict)
