import typing

from shioaji.base import BaseModel


class Tick(BaseModel):
    ts: int
    close: typing.Union[float, int]
    volume: int


class Ticks(BaseModel):
    ticks: typing.List[Tick]
