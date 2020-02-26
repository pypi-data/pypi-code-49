import enum


class State(enum.Enum):
    Started = 1
    Finished = 2
    Failed = 3


class Message:
    def __init__(self, source, state, msg=None):
        self.source = source
        self.state = state
        self.msg = msg
