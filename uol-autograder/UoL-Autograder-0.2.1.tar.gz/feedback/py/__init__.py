import json
import subprocess
import sys, os
from collections import namedtuple
from tempfile import TemporaryFile
from pathlib import Path
from .. import util
from ..general import test_comments, Runner
from ..general.contants import *
from ..py.py_eval_util import get_eval_util_path

class PyLookup(util.Lookup):
    _runner_feedback = "py_runner_feedback.json"
    _eval_feedback = "py_eval_feedback.json"

class PyRunner(Runner):
    def __init__(self, tmp_files, run_args={}):
        super(PyRunner, self).__init__(tmp_files, run_args)
        self.py_lookup = PyLookup(tmp_files.lookup_dir)
        if self.verbose: print(f"Working dir: {tmp_files.tmp_dir}")


    def run_test(self, config):
        self.feedbacks = []
        self.manual_feedbacks = []

        if hasattr(config, "syntax"):         # Try running Python file, if it did, it works!
            ran = self.test_syntax(config.syntax)
            # TODO: This is not an instant termination, other checks can run, just add manual check requirement to test_functionality if that fails
            if not ran:                             # If failed to run, return with results
                return self.feedbacks
        
        if hasattr(config, "functionality"):  # Run testing file around the tested file
            self.test_functionality(config.functionality)

        if hasattr(config, "comments"):       # Run comment density analysis
            self.test_comments(config.comments)

        return self.feedbacks, self.manual_feedbacks

    def test_syntax(self, config):
        if self.verbose: print("Testing syntax")
        # Here we check whether the code runs
        retval, _, output = util.execute([PY_RUNNER, self.tested_path], self.tmp_dir)

        runs = retval == 0

        # Provide feedback
        with self.py_lookup.runner_feedback.open() as json_file:
            syntax_feedback = json.load(json_file)
        
        feedback = [syntax_feedback[PASS if retval == 0 else FAIL]]
        if not runs:
            feedback.append(util.as_md_code(output))
            if self.verbose: print(f"Error output:\n{output}")

        # create feedback dictionary file
        self.feedbacks.append({
            "type": "syntax",
            "mark": round(1 if retval == 0 else 0, 2),
            "weight": config.weight,
            "feedback": '\n'.join(feedback)
        })

        return runs


    def test_functionality(self, config):
        if self.verbose: print("Testing functionality")
        output_file = Path(self.tmp_files.tmp_dir.name, "result.json")
      
        # Run tester file that evaluates tested file
        args = [PY_RUNNER, self.tester_path, self.tested_path, output_file.absolute().as_posix(), get_eval_util_path()]
        _, stdout, stderr = util.execute(args, self.tmp_dir)
        if self.verbose: print(f"stdout:\n{stdout}\nstderr:\n{stderr}")

        # Read results file
        with output_file.open() as json_file:
            result = json.load(json_file)
        
        # Combine scores from test feedback
        score = sum([test['mark'] * test['weight'] for test in result])

        # create feedback dictionary file
        self.feedbacks.append({
            "type": "functionality",
            "mark": round(score, 2),
            "weight": config.weight,
            "questions": result
        })
