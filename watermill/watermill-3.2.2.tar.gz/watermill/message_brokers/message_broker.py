import enum
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import Type
from typing import TypeVar


StreamType = TypeVar('StreamType')
JoinedStreamType = TypeVar('JoinedStreamType')


class EndOfStreamError(Exception):
    def __init__(
            self,
            stream_type: Type[StreamType],
    ):
        super().__init__()
        self._stream_type = stream_type


class StreamTimeoutError(Exception):
    def __init__(
            self,
            stream_type: Type[StreamType],
    ):
        super().__init__()
        self._stream_type = stream_type


class RightJoinedStreamRanAhead(Exception):
    def __init__(self, stream_type: Type[JoinedStreamType]):
        super().__init__()
        self.stream_type = stream_type


@dataclass
class EndOfStream:
    eos__: bool = True


class StreamsShift(enum.Enum):
    Less = 'Less'
    Equal = 'Equal'
    Greater = 'Greater'


class MessageBroker:
    def send(self, item_type: Type[StreamType], item: dict):
        raise NotImplementedError()

    def send_eos(self, item_type: Type[StreamType]):
        raise NotImplementedError()

    def get_elements(
            self,
            element_type: Type[StreamType],
            comparator: Callable[[Any, Any], StreamsShift] = None
    ) -> dict:
        raise NotImplementedError()

    def commit(self):
        pass
