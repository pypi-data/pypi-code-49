import traceback
import json
import datetime
import typing

from testreportng.utils import timestamp2str
from testreportng.constants import Label


class NGCaseDetail(object):
    def __init__(self, name: str, status: str = None):
        if not status:
            status = Label.LABEL_STATUS_INIT
        self.name: str = name
        self.status: str = status

        # data
        self._outcome = None

        # skip
        self.reason: str = ""

        # error
        self.error = None
        self.traceback = None

        # time
        self.start_time: typing.Optional[datetime.datetime] = None
        self.end_time: typing.Optional[datetime.datetime] = None
        self.duration: typing.Optional[datetime.timedelta] = None

    def is_passed(self) -> bool:
        return self.status == Label.LABEL_STATUS_PASS

    def is_failed(self) -> bool:
        return self.status == Label.LABEL_STATUS_FAIL

    def is_error(self) -> bool:
        return self.status == Label.LABEL_STATUS_ERROR

    def is_skipped(self) -> bool:
        return self.status == Label.LABEL_STATUS_SKIP

    def to_json(self) -> str:
        """
        dump Detail to json string

        :return:
        """
        res_dict = self.to_dict(safe_repr=True)
        return json.dumps(res_dict)

    def to_dict(self, safe_repr: bool = None) -> dict:
        """
        dump Detail to dict, for easier usage by others

        :param safe_repr:
            bool.
            dump all the objects to string if True.
            default to False.
        :return:
        """
        if safe_repr:
            error = repr(self.error) if self.error else ""
            traceback_str = (
                traceback.format_tb(self.traceback) if self.traceback else ""
            )
            start_time: str = timestamp2str(self.start_time)
            end_time: str = timestamp2str(self.end_time)
            duration: float = self.duration.total_seconds()

            return {
                Label.LABEL_CASE_NAME: self.name,
                Label.LABEL_STATUS: self.status,
                Label.LABEL_REASON: self.reason,
                Label.LABEL_ERROR: error,
                Label.LABEL_TRACEBACK: traceback_str,
                Label.LABEL_START_TIME: start_time,
                Label.LABEL_END_TIME: end_time,
                Label.LABEL_DURATION: duration,
            }
        return self.__dict__

    @property
    def outcome(self):
        """
        origin _outcome. same as unittest.TestCase

        :return:
        """
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        self._outcome = value

        # skipped
        if value.skipped:
            self.status = Label.LABEL_STATUS_SKIP
            self.reason = value.skipped[0][1]
            return

        # normal test
        error_list = value.errors
        if len(error_list) == 1:
            error = value.errors[0][1]
        else:
            error = value.errors[1][1]

        # no error happened
        if not error:
            self.status = Label.LABEL_STATUS_PASS
            return

        # error or fail
        if error[0] is AssertionError:
            self.status = Label.LABEL_STATUS_FAIL
        else:
            self.status = Label.LABEL_STATUS_ERROR

        self.error = error[1]
        self.traceback = error[2]

    def __str__(self):
        return f"<{__class__.__name__} name={self.name} status={self.status}>"

    __repr__ = __str__
