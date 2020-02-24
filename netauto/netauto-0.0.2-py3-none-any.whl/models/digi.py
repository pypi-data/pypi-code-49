from typing import List

from pydantic import BaseModel


class Digi(BaseModel):
    device: str
    ip: str
    status: str


class DigiList(BaseModel):
    result: List[Digi]


class DigiRebooted(BaseModel):
    ip: str
    status: str
