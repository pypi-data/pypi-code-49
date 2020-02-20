# coding=utf-8
import time
import os
from multiprocessing import Queue
from nose import run
from utils import log
from utils.process import MyProcess


class Runner(object):

    def __init__(self):
        # manager = Manager()
        self.results = list()
        self.process_run_ = None
        self.working_path = os.environ["working_path"]
        self.log_path = self.get_log_path()

    def get_results(self):
        return self.results

    def get_log_path(self):
        log_path = os.path.join(self.working_path, "log")
        if os.path.exists(log_path) is False:
            os.mkdir(log_path)
        return log_path

    def run_nose_tests(self, test_case, test_path, queue):
        test_function = test_case.split(".")
        xml_name = "nosetests_%s_%s.xml" % (test_function[-1], time.time())
        xml_path = os.path.join(self.log_path, xml_name)
        argv = (['--exe', '--nocapture', '--with-xunit', '--xunit-file=%s' % xml_path, '-x'])
        argv.append(test_path)
        log.INFO("************ Begin to run tests:%s", test_case)
        ret = run(argv=argv, exit=False)
        if ret is True:
            log.INFO("TestCase run succeed.%s", test_case)
        else:
            log.ERR("TestCase run failed. %s", test_case)
        log_path = log.LoggerVenus.get_log_path()
        xml_path = xml_path
        result = {"name":test_case, "result": ret, "log_path": log_path, "xml_path": xml_path}
        queue.put(result)
        return ret

    def stop(self):
        print("test runner . stop")
        if self.process_run_ is not None:
            ret = self.process_run_.stop()
        else:
            ret = -1
        return ret

    def process_run(self, test_case, test_case_path, loop=1, timeout=0):
        value = None
        for item in range(loop):
            log.INFO("Run test in loop: %s", item)
            start_time = time.time()
            current_time = start_time
            queue = Queue()
            self.process_run_ = MyProcess(target=self.run_nose_tests, args=(test_case, test_case_path, queue,))
            self.process_run_.start()
            if timeout > 0:
                while current_time - start_time < timeout:
                    current_time = time.time()
                    time.sleep(5)
                # os.kill(self.process_run_.pid, signal.CTRL_BREAK_EVENT)
                self.process_run_.terminate()
            else:
                self.process_run_.join()
            value = queue.get(True)
            self.results.append(value)
        return value


if __name__ == '__main__':
    pass
