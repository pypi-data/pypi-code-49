from pydantic.main import BaseModel

from escarpolette.player import State


class PlayerSchema(BaseModel):
    state: State
