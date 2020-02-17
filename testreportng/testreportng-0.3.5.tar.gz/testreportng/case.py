import unittest
import typing

from testreportng.result import NGCaseDetail, NGResult
from testreportng.constants import Label
from testreportng.utils import get_timestamp


class NGCase(unittest.TestCase):
    # default cls
    ng_detail_kls = NGCaseDetail
    ng_result_kls = NGResult

    # result inst
    ng_result: NGResult
    ng_cur_result: typing.Optional[ng_detail_kls]

    # ng hook
    def _start_hook(self, name: str):
        mapping = {
            Label.LABEL_STATUS_PASS: "when_pass",
            Label.LABEL_STATUS_FAIL: "when_fail",
            Label.LABEL_STATUS_ERROR: "when_error",
            Label.LABEL_STATUS_SKIP: "when_skip",
        }
        assert name in mapping, f"hook [ {name} ] not found"
        target = mapping[name]
        assert hasattr(self, target)
        return getattr(self, target)()

    def when_pass(self):
        """ will execute when case passed """

    def when_fail(self):
        """ will execute when case failed """

    def when_error(self):
        """ will execute when case error """

    def when_skip(self):
        """ will execute when case skipped """

    def when_always(self):
        """ will execute after each cases """

    # wrap for origin hook
    @classmethod
    def ng_setup_class(cls) -> None:
        cls.ng_result: NGResult = cls.ng_result_kls(cls.__name__)

    def ng_setup(self) -> None:
        # init this case
        cur = self.ng_detail_kls(self._testMethodName)
        # time record
        cur.start_time = get_timestamp()
        # save the pointer of current case (function)
        self.ng_cur_result = cur
        self.ng_result.set(cur)

    def ng_teardown(self) -> None:
        # update case's result
        self.ng_cur_result.end_time = get_timestamp()
        self.ng_cur_result.duration = self.ng_cur_result.end_time - self.ng_cur_result.start_time
        self.ng_cur_result.outcome = getattr(self, "_outcome")
        self.ng_result.set(self.ng_cur_result)

        # ng hook
        self._start_hook(self.ng_cur_result.status)
        self.when_always()

        # unbind
        self.ng_cur_result = None

    # origin hook
    @classmethod
    def setUpClass(cls) -> None:
        cls.ng_setup_class()

    def setUp(self) -> None:
        self.ng_setup()
        self.addCleanup(self.ng_teardown)
