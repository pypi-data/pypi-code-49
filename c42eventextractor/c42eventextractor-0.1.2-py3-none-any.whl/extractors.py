import json
from datetime import datetime, timedelta

from py42.sdk import SDK
from py42.sdk.file_event_query import ExposureType, FileEventQuery, InsertionTimestamp

from c42eventextractor.common import FileEventHandlers, convert_datetime_to_timestamp

_DEFAULT_LOOK_BACK_DAYS = 60
_MAX_PAGE_SIZE = 10000
INSERTION_TIMESTAMP_FIELD_NAME = u"insertionTimestamp"


class AEDEventExtractor(object):
    _previous_query_total_count = _MAX_PAGE_SIZE
    _previous_insertion_time = None

    def __init__(self, sdk, handlers):
        # type: (SDK, FileEventHandlers) -> None
        self._sdk = sdk
        self._handlers = handlers

    @property
    def previous_query_total_count(self):
        return self._previous_query_total_count

    def extract(self, initial_min_timestamp=None, max_timestamp=None, exposure_types=None):
        # type: (float, float, iter) -> None
        """Queries for recent security exposure events.
           Passes the raw response from the py42 call to `handlers.handle_response`.
           The default implementation of `handlers.handle_response` prints `response.text` to the console.
           Provide your own implementation for `handlers.handle_response` to do something else.
           Makes subsequent calls to py42 and `handlers.handle_response`
                if the total event count is greater than 10,000.

        Args:
            initial_min_timestamp: An initial timestamp to use if you don't want to start from 60 days back.
                Subsequent calls use a recorded min_timestamp, if they exist.
                Using a recorded timestamp requires providing your own custom implementation of
                    `handlers.record_cursor_position` and `handlers.get_cursor_position` methods.

            max_timestamp: A max insertion timestamp for which events to extract.
            exposure_types: A list of exposure types to extract. Options: SharedViaLink, SharedToDomain,
                ApplicationRead, CloudStorage, RemovableMedia, IsPublic.
        """

        min_timestamp = self._calculate_min_timestamp(initial_min_timestamp)
        max_timestamp = max_timestamp if max_timestamp else self._get_default_max_timestamp()
        self._extract_in_range(min_timestamp, max_timestamp, exposure_types)

    def extract_raw(self, raw_query):
        try:
            response = self._search_file_events(raw_query)
            if response:
                self._handlers.handle_response(response)
        except Exception as ex:
            self._handlers.handle_error(ex)

    def _extract_in_range(self, min_timestamp, max_timestamp, exposure_types=None):
        if self.previous_query_total_count < _MAX_PAGE_SIZE:
            # We know we got all the events if the last query returned a count less than max
            return

        query = self._create_file_event_query(min_timestamp, max_timestamp, exposure_types)
        response = self._search_file_events(query)
        if response:
            self._handlers.handle_response(response)
            self._extract_in_range(
                min_timestamp=self._previous_insertion_time,
                max_timestamp=max_timestamp,
                exposure_types=exposure_types,
            )

    @staticmethod
    def _create_file_event_query(min_timestamp, max_timestamp, exposure_types=None):
        min_timestamp += 0.001  # Prevent duplicates from previous runs
        insertion_filter = InsertionTimestamp.in_range(min_timestamp, max_timestamp)
        exposure_filter = (
            ExposureType.is_in(exposure_types) if exposure_types else ExposureType.exists()
        )
        query = FileEventQuery(insertion_filter, exposure_filter)
        query.sort_direction = u"desc"
        query.sort_key = INSERTION_TIMESTAMP_FIELD_NAME
        query.page_size = _MAX_PAGE_SIZE
        return query

    def _search_file_events(self, query):
        try:
            response = self._sdk.security.search_file_events(query)
            if response.text:
                response_dict = json.loads(response.text)
                self._set_count_from_dict(response_dict)
                self._record_cursor_position_from_dict(response_dict)

            return response
        except Exception as ex:
            self._handlers.handle_error(ex)

    def _record_cursor_position_from_dict(self, response_dict):
        insertion_time = self._get_insertion_timestamp_from_dict(response_dict)
        self._previous_insertion_time = insertion_time
        if insertion_time is not None:
            self._handlers.record_cursor_position(insertion_time)

    def _get_insertion_timestamp_from_dict(self, response_dict):
        events = self._get_events_from_dict(response_dict)
        if events and INSERTION_TIMESTAMP_FIELD_NAME in events[0]:
            return self._get_insertion_timestamp_from_event(events[0])

    @staticmethod
    def _get_events_from_dict(response_dict):
        file_events_key = u"fileEvents"
        if file_events_key in response_dict:
            return response_dict[file_events_key]

    @staticmethod
    def _get_insertion_timestamp_from_event(event):
        insertion_time_str = event[INSERTION_TIMESTAMP_FIELD_NAME]
        insertion_time = datetime.strptime(insertion_time_str, u"%Y-%m-%dT%H:%M:%S.%fZ")
        insertion_timestamp = convert_datetime_to_timestamp(insertion_time)
        return insertion_timestamp

    def _set_count_from_dict(self, response_dict):
        self._previous_query_total_count = self._get_total_count_from_dict(response_dict)

    @staticmethod
    def _get_total_count_from_dict(response_dict):
        total_count_key = "totalCount"
        if total_count_key in response_dict:
            return response_dict[total_count_key]

        return 0

    def _calculate_min_timestamp(self, min_timestamp_arg=None):
        recorded_min_timestamp = self._handlers.get_cursor_position()
        if recorded_min_timestamp is not None:
            return recorded_min_timestamp
        elif min_timestamp_arg is not None:
            return min_timestamp_arg
        else:
            return self._get_default_min_timestamp()

    @staticmethod
    def _get_default_min_timestamp():
        now = datetime.utcnow()
        start_day = timedelta(days=_DEFAULT_LOOK_BACK_DAYS)
        days_ago = now - start_day
        return convert_datetime_to_timestamp(days_ago)

    @staticmethod
    def _get_default_max_timestamp():
        return convert_datetime_to_timestamp(datetime.utcnow())
