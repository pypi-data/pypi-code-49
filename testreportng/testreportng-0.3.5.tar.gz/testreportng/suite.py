import unittest
import typing

from testreportng.result import NGResult


class NGSuite(unittest.TestSuite):
    ng_result: typing.Dict[str, NGResult] = dict()

    def __init__(self, tests: typing.Iterable = ()):
        super(NGSuite, self).__init__(tests)

    # function `run` from unittest.TestSuite
    # with result collector
    def run(self, result, debug=False):
        def _isnotsuite(test):
            "A crude way to tell apart testcases and suites with duck-typing"
            try:
                iter(test)
            except TypeError:
                return True
            return False

        topLevel = False
        if getattr(result, "_testRunEntered", False) is False:
            result._testRunEntered = topLevel = True

        for index, test in enumerate(self):
            if result.shouldStop:
                break

            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if getattr(test.__class__, "_classSetupFailed", False) or getattr(
                    result, "_moduleSetUpFailed", False
                ):
                    continue

            if not debug:
                test(result)
            else:
                test.debug()

            # collect results
            if not isinstance(test, NGSuite):
                self.ng_result[test.__class__.__name__] = test.ng_result

            if self._cleanup:
                self._removeTestAtIndex(index)

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False
        return result


class NGLoader(unittest.TestLoader):
    suiteClass = NGSuite
