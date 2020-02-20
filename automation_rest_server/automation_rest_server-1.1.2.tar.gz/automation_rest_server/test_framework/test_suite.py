# coding=utf-8
# pylint: disable=unused-variable
import os
import time
import yaml
from test_framework.test_base import TestBase
from utils import log
from test_framework.test_runner import Runner


class TestSuite(TestBase):

    def __init__(self):
        super(TestSuite, self).__init__()
        self.runner = None
        self.working_path = os.environ["working_path"]
        self.test_suite_folder = self.get_test_suite_path()
        self.test_suites = self.list_test_suite()

    def get_test_suite_path(self):
        test_suite_path = None
        dirs = os.listdir(self.working_path)
        for item in dirs:
            temp_path = os.path.join(self.working_path, item)
            if os.path.isdir(temp_path) and "suite" in item.lower():
                    test_suite_path = temp_path
        return test_suite_path

    def load_test_suite(self, test_suite):
        test_suite = test_suite + ".yaml"
        test_suite_path = self.get_file_path(self.test_suite_folder, test_suite)
        if test_suite_path is not None and os.path.exists(test_suite_path):
            file_ = open(test_suite_path)
            test_suites = yaml.load(file_)
        else:
            raise Exception("TestSuite not exist: {}".format(test_suite))
        return test_suites

    def run(self, test_suite):
        self.runner = Runner()
        try:
            test_suites = self.load_test_suite(test_suite)
        except BaseException as message:
            print(message)
            result = [{"name": test_suite, "result": False}]
            return result

        for loop in range(int(test_suites["loop"])):
            log.INFO("Test Suite:%s, loop:%d", test_suites["name"], loop)
            for tests in test_suites["cases"]:
                test_path = self.get_all_script_path(tests["script"])
                if not test_path:
                    log.ERR("TestCase not find: %s", tests["script"])
                    break
                result = self.runner.process_run(tests["script"], test_path[0], tests["loop"], tests["duration"])
                if result["result"] is False:
                    break
                time.sleep(3)
        self.print_results(test_suite)
        return self.runner.get_results()

    def list_test_suite(self):
        return self.list_and_filter_tests("all")

    def get_test_suites(self):
        return self.test_suites

    def list_and_filter_tests(self, filters):
        test_suites = []
        if self.test_suite_folder is not None:
            for root, dirs, files in os.walk(self.test_suite_folder):
                for file_ in files:
                    if filters.lower() == "all":
                        test_suites.append(file_.split(".")[0])
                        continue
                    if filters in file_:
                        test_suites.append(file_.split(".")[0])
        return test_suites

    def print_results(self, test_suite):
        result = self.runner.get_results()
        log.INFO("###########################################################")
        log.INFO("********************* Result Summary **********************")
        log.INFO("********************* TestSuite: %s ***********************", test_suite)
        pass_items = filter(lambda x: x["result"] is True, result)
        fail_items = filter(lambda x: x["result"] is False, result)
        for item in result:
            if item["result"] is True:
                log.INFO("TestCase: %s, result: PASS", item["name"])
            else:
                log.ERR("TestCase: %s, result: FAIL", item["name"])
        log.INFO("Total run %s, pass %s, fail %s", len(result), len(list(pass_items)), len(list(fail_items)))
        log.INFO("###########################################################")


if __name__ == '__main__':
    T = TestSuite()
    T.run("test_1")
