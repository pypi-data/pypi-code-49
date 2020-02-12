import time
import glob

from abc import ABC, abstractmethod
from typing import List
from tabulate import tabulate

from msbase.subprocess_ import try_call_std
from msbase.utils import append_pretty_json, datetime_str
from msbase.utils import load_jsonl, write_pretty_json

class Spec(ABC):
    skip_if_exist = None

    @staticmethod
    @abstractmethod
    def get_output(self, *args, **kwargs):
        raise NotImplementedError

    def impl(self, *args, **kwargs):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        spec_output = self.get_output(*args, **kwargs)
        outputs = []
        if isinstance(spec_output, list):
            for f in spec_output:
                outputs.append(f)
        else:
            outputs.append(spec_output)

        if self.skip_if_exist and all([os.path.exists(f) for f in outputs ]):
            return

        ret = self.impl(*args, **kwargs)

        assert all([os.path.exists(f) for f in outputs ])
        return ret

    def run_output(self, *args, **kwargs):
        self.run(*args, **kwargs)
        return self.get_output(*args, **kwargs)

def to_matrix_internal(config_pairs):
    if not len(config_pairs):
        return [{}]
    key, values = config_pairs[0]
    configs = []
    tail_configs = to_matrix_internal(config_pairs[1:])
    for v in values:
        if not tail_configs:
            configs.append([(key, v)])
        configs.extend([dict(config, key=v) for config in tail_configs])
    return configs

def to_matrix(configs):
    return to_matrix_internal(list(configs.items()))

class Step(object):
    def __init__(self, name: str, command: List[str], cwd:str=None, env={}):
        self.name = name
        self.command = command
        self.cwd = cwd
        self.env = env

class AbstractLab(ABC):
    def __init__(self, name: str, steps: List[Step], configurations={}):
        self.config_matrix = to_matrix(configurations)
        self.name  = name
        self.steps = steps

    @abstractmethod
    def digest_output(self, name: str, output, command: List[str]):
        '''digest the step name,
        the command output (stdout: str, stderr: str, return_code: int),
        the command sequence.

        return a dictionary indexed by columns as in digest_column_names
        '''
        raise NotImplementedError

    @abstractmethod
    def digest_column_names(self):
        '''defines the output of digest_output'''
        raise NotImplementedError

    def log(self, content):
        append_pretty_json(content, path=self.session_id + ".log")

    def run_with_config(self, config):
        for step in self.steps:
            start_seconds = time.time()
            output = try_call_std(step.command, cwd=step.cwd,
                                  env=dict(step.env, **config),
                                  noexception=True)
            _, _, return_code = output
            seconds_spent = time.time() - start_seconds
            stat = {"step_name": step.name, "seconds": seconds_spent,
                    "output": output, "command": step.command }
            stat = dict(config, **stat)
            self.log(stat)
            if return_code != 0:
                return

    def run(self):
        self.session_id = "run-%s-%s" % (self.name, datetime_str())
        for config in self.config_matrix:
            self.run_with_config(config)

    def analyze(self):
        table = [["Step", "Runtime (s)"] + self.digest_column_names()]

        for f in sorted(glob.glob("run-%s-*.log" % self.name)):
            print("importing %s" % f)
            for log in load_jsonl(f):
                row = []
                row.append(log['step_name'])
                row.append(log['seconds'])
                digest = self.digest_output(log['step_name'], log['output'], log["command"])
                for col in self.digest_column_names():
                    row.append(digest[col])
                table.append(row)
                print('STDOUT')
                print(log['output'][0])
                print('STDERR')
                print(log['output'][1])
                print('CODE')
                print(log['output'][2])

        print(tabulate(table, headers="firstrow", tablefmt="github"))

        tex_result = tabulate(table, headers="firstrow", tablefmt="latex_raw")
        open("results.tex", "w").write(tex_result)

        write_pretty_json(table, "results.json")
