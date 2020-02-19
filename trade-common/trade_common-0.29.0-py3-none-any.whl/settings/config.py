import abc

from dataclasses import dataclass


@dataclass
class Config(abc.ABC):
    base_url: str
    api_key: str
    api_secret: str
