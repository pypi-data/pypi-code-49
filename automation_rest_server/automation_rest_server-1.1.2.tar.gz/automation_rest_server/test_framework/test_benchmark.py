# coding=utf-8
# pylint: disable=unused-variable
from multiprocessing import Queue
from tool.fio.fio import Fio
from tool.iometer.iometer import IoMeter
from utils.process import MyProcess


class TestBenchmark(object):
    def __init__(self):
        self.tool = None
        self.process_run_ = None
        self.results = list()

    def _run(self, test_parameters, queue):
        tool_type = test_parameters["type"]
        tool = self.get_tool_with_type(tool_type)
        status, out_put, result = tool.run_benchmark(test_parameters)
        ret = True if status == 0 else False
        result = {"name": test_parameters["test_name"], "result": ret, "msg":out_put, "benchmark_result":result}
        queue.put(result)
        return result

    def run(self, test_parameters):
        queue = Queue()
        self.process_run_ = MyProcess(target=self._run, args=(test_parameters, queue, ))
        self.process_run_.start()
        self.process_run_.join()
        value = queue.get(True)
        self.results.append(value)
        return self.results

    def stop(self):
        print("TestBenchmark runner . stop")
        if self.process_run_ is not None:
            ret = self.process_run_.stop()
        else:
            ret = -1
        return ret

    def get_tool_with_type(self, tool_type):
        tool = None
        if tool_type == "fio":
            tool = Fio()
        elif tool_type == "iometer":
            tool = IoMeter()
        return tool
