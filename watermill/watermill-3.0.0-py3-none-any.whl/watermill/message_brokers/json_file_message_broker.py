import json
from logging import getLogger
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Mapping
from typing import Type

from watermill.message_brokers.message_broker import EndOfStreamError
from watermill.message_brokers.message_broker import MessageBroker
from watermill.message_brokers.message_broker import RightJoinedStreamRanAhead
from watermill.message_brokers.message_broker import StreamsShift
from watermill.stream_types import StreamType


logger = getLogger(__name__)


class JsonFileMessageBroker(MessageBroker):
    def __init__(self, stream_paths: Mapping[Type[StreamType], Path]):
        self._stream_paths = stream_paths
        self._stream_file_data: Dict[str, List[dict]] = {}
        self._stream_file_pos: Dict[str, int] = {}
        self._stream_out_data = {}

    def send(self, element_type: Type[StreamType], item: dict):
        self._stream_out_data.setdefault(element_type, []).append(item)

    def send_eos(self, element_type: Type[StreamType]):
        path = self._stream_paths[element_type]
        with path.open('w') as out_file:
            json.dump(self._stream_out_data[element_type], out_file)

    def get_elements(
            self,
            element_type: Type[StreamType],
            comparator: Callable[[Any, Any], StreamsShift] = None
    ) -> dict:
        if not comparator:
            yield self._get_next_element(element_type)
            return

        element = self._get_next_element(element_type)
        while comparator(element) == StreamsShift.Greater:
            logger.warning(f'Skipped stream {element_type} element')
            element = self._get_next_element(element_type)

        if comparator(element) == StreamsShift.Less:
            self._step_back(element_type)
            raise RightJoinedStreamRanAhead(element_type)

        while comparator(element) == StreamsShift.Equal:
            yield element
            element = self._get_next_element(element_type)
        self._step_back(element_type)

    def _get_stream_qualified_name(self, stream_type: Type[StreamType]) -> str:
        return stream_type.__name__

    def _step_back(
            self,
            stream_type: Type[StreamType],
    ):
        stream_name = self._get_stream_qualified_name(stream_type)
        position = self._stream_file_pos[stream_name]
        if position < 1:
            logger.warning(f'Skipping stream {stream_type} element')
            return

        self._stream_file_pos[stream_name] -= 1

    def _get_next_element(
            self,
            stream_type: Type[StreamType],
    ) -> dict:
        stream_name = self._get_stream_qualified_name(stream_type)
        if stream_name not in self._stream_file_data:
            with self._stream_paths[stream_type].open() as f:
                self._stream_file_data[stream_name] = json.load(f)
                self._stream_file_pos[stream_name] = 0

        position = self._stream_file_pos[stream_name]
        if position >= len(self._stream_file_data[stream_name]):
            raise EndOfStreamError(stream_type)
        element = self._stream_file_data[stream_name][position]
        self._stream_file_pos[stream_name] += 1
        return element
