import typing
import json
import datetime

from testreportng.detail import NGCaseDetail
from testreportng.constants import Label


class NGResult(object):
    """ result of suite """

    def __init__(self, kls_name: str, data: typing.Dict[str, NGCaseDetail] = None):
        self.kls_name: str = kls_name
        self.data: typing.Dict[str, NGCaseDetail] = data or dict()

    def set(self, cur: NGCaseDetail):
        self.data[cur.name] = cur

    def get(self, name: str) -> typing.Optional[NGCaseDetail]:
        if name not in self.data:
            return None
        return self.data[name]

    def get_count_by_label(self, label_name: str):
        summary = self.summary()
        assert label_name in summary, f"label {label_name} not in summary"
        return summary[label_name]

    def get_data_by_status(self, label_name: str) -> typing.Dict[str, NGCaseDetail]:
        return {_: v for _, v in self.data.items() if v.status == label_name}

    @property
    def start_time(self) -> typing.Optional[datetime.datetime]:
        result = [each.start_time for each in self.data.values()]
        return min(result) if result else None

    @property
    def end_time(self) -> datetime.datetime:
        result = [each.end_time for each in self.data.values()]
        return max(result) if result else None

    @property
    def duration(self) -> float:
        if not (self.start_time and self.end_time):
            return 0.0

        return (self.end_time - self.start_time).total_seconds()

    @property
    def total_num(self) -> int:
        return len(self.data.values())

    @property
    def pass_num(self) -> int:
        return len([each for each in self.data.values() if each.is_passed()])

    @property
    def fail_num(self) -> int:
        return len([each for each in self.data.values() if each.is_failed()])

    @property
    def error_num(self) -> int:
        return len([each for each in self.data.values() if each.is_error()])

    @property
    def skip_num(self) -> int:
        return len([each for each in self.data.values() if each.is_skipped()])

    @property
    def fail_or_error_num(self) -> int:
        return self.fail_num + self.error_num

    @property
    def pass_rate(self) -> float:
        # no case
        if not self.total_num:
            return 0.0

        return self.pass_num / self.total_num

    def summary(self) -> dict:
        return {
            Label.LABEL_NAME: self.kls_name,
            Label.LABEL_TOTAL: self.total_num,
            Label.LABEL_START_TIME: self.start_time,
            Label.LABEL_END_TIME: self.end_time,
            Label.LABEL_DURATION: self.duration,
            Label.LABEL_PASS_RATE: self.pass_rate,
            # cases
            Label.LABEL_STATUS_PASS: self.pass_num,
            Label.LABEL_STATUS_FAIL: self.fail_num,
            Label.LABEL_STATUS_ERROR: self.error_num,
            Label.LABEL_STATUS_SKIP: self.skip_num,
        }

    def to_dict(self, safe_repr: bool = None) -> typing.Dict[str, dict]:
        """
        dump Result to dict, for easier usage by others

        :param safe_repr:
            bool.
            dump all the objects to string if True.
            default to False.
        :return:
        """
        r = dict()
        for name, result in self.data.items():
            r[name] = result.to_dict(safe_repr=safe_repr)
        return r

    def to_json(self) -> str:
        """
        dump Detail to json string

        :return:
        """
        r = self.to_dict(True)
        return json.dumps(r)

    def __str__(self):
        return f"<{__class__.__name__} result={self.data}>"

    __repr__ = __str__


class NGResultOperator(object):
    """ high level operator over multi Result objects """

    def __init__(self):
        self.data: typing.Set[NGResult] = set()

    def load(self, suite_dict: typing.Dict[str, NGResult]):
        for each in suite_dict.values():
            self.data.add(each)

    @staticmethod
    def merge(suite_name: str, suite_dict: typing.Dict[str, NGResult]) -> NGResult:
        new_data: typing.Dict[str, NGCaseDetail] = dict()

        for each_suite_name, result in suite_dict.items():
            for each_case in result.data.values():
                new_case_name: str = f"{each_suite_name}.{each_case.name}"
                new_data[new_case_name] = each_case
        return NGResult(suite_name, new_data)

    def get_data_by_status(
        self, label_name: str
    ) -> typing.Dict[str, typing.Dict[str, NGCaseDetail]]:
        ret = dict()
        for each in self.data:
            ret[each.kls_name] = each.get_data_by_status(label_name)
        return ret

    def add(self, new: NGResult):
        self.data.add(new)

    def remove(self, old: NGResult):
        self.data.remove(old)

    def reset(self):
        self.data = set()

    def get_start_time(self) -> datetime.datetime:
        result = [each.start_time for each in self.data]
        return min(result) if all(result) else None

    def get_end_time(self) -> datetime.datetime:
        result = [each.end_time for each in self.data]
        return max(result) if all(result) else None

    def get_duration(self) -> float:
        start = self.get_start_time()
        end = self.get_end_time()
        if not (start or end):
            return 0.0
        return (self.get_end_time() - self.get_start_time()).total_seconds()

    def summary(self) -> typing.Dict:
        result = {}
        for each_label in (
            Label.LABEL_TOTAL,
            Label.LABEL_STATUS_PASS,
            Label.LABEL_STATUS_FAIL,
            Label.LABEL_STATUS_ERROR,
            Label.LABEL_STATUS_SKIP,
        ):
            result[each_label] = self.get_case_count(each_label)
        result[Label.LABEL_START_TIME] = self.get_start_time()
        result[Label.LABEL_END_TIME] = self.get_end_time()
        result[Label.LABEL_DURATION] = self.get_duration()
        return result

    def get_case_count(self, case_type: str) -> int:
        type_list = (
            Label.LABEL_TOTAL,
            Label.LABEL_STATUS_PASS,
            Label.LABEL_STATUS_FAIL,
            Label.LABEL_STATUS_ERROR,
            Label.LABEL_STATUS_SKIP,
        )
        assert (
            case_type in type_list
        ), f"status {case_type} should be one of {type_list}"
        return sum([each.get_count_by_label(case_type) for each in self.data])
