import difflib
import appdirs
import json
import subprocess
import sys, os
from tempfile import TemporaryFile, TemporaryDirectory
from pathlib import Path
import shutil
from ..signature import Signature
from .. import util
from ..general.contants import *
from ..general import test_comments, Runner
from ..py.py_eval_util import get_eval_util_path

EXECUTABLE_TIMEOUT = 5  # seconds

from .compile_examiner import compile_cpp_to_o

class OCache:
    def __init__(self):
        self._cache_dir = Path(appdirs.user_cache_dir(Signature.appname, Signature.appauthor))
        if not self._cache_dir.is_dir():
            self._cache_dir.mkdir(parents=True)

        files = util.get_files_in_dir(self._cache_dir)
        self._files = {file.stem:file for file in files}
    
    def get(self, name):
        if isinstance(name, Path):
            name = name.stem
        return self._files.get(name, None)

    def add(self, path, dependencies):
        with TemporaryDirectory() as t:
            tmp_path = Path(t, path.name)
            shutil.copy(path, tmp_path)
            for dependency in dependencies:
                shutil.copy(dependency, Path(t, dependency.name))

            cached_path = Path(self._cache_dir, path.name).absolute().as_posix()
            self._files[path.stem] = Path(compile_cpp_to_o(tmp_path.absolute().as_posix(), cached_path, working_dir=t))

    def add_or_get(self, path, dependencies):
        cached = self.get(path)
        if cached:
            return cached
        self.add(path, dependencies)
        return self.get(path.stem)

    def clear(self):
        if self._cache_dir.is_dir():
            shutil.rmtree(self._cache_dir.absolute().as_posix())
        self._cache_dir.mkdir(parents=True)
        self._files = {}


class CppLookup(util.Lookup):
    _compiler_warnings = "cpp_compiler_feedback.json"
    _static_warnings = "cpp_static_warnings.json"
    _style_feedback = "cpp_style_feedback.json"
    _eval_feedback = "cpp_eval_feedback.json"


class CppRunner(Runner):
    def __init__(self, tmp_files, run_args={}):
        super(CppRunner, self).__init__(tmp_files, run_args)
        self.cpp_lookup = CppLookup(tmp_files.lookup_dir)
        if self.verbose: print(f"Working dir: {tmp_files.tmp_dir}")

        self.o_cache = OCache()
        if "clear_cache" in run_args and run_args["clear_cache"]:
            self.o_cache.clear()

        self._copy_cpp_files()

    def _copy_to_tmp(self, path):
        assert path.is_file()
        new_path = Path(self.tmp_dir, path.name).absolute().as_posix()
        shutil.copy(path.absolute().as_posix(), new_path)
        return new_path
    
    def _copy_cpp_files(self):
        my_dir = util.get_current_dir()

        self._copy_to_tmp(Path(my_dir, JSON_HPP))
        self._copy_to_tmp(Path(my_dir, CPP_EVAL_UTIL_H))
        self._copy_to_tmp(self.cpp_lookup.eval_feedback)
        self.eval_util_cpp = self._copy_to_tmp(Path(my_dir, CPP_EVAL_UTIL_CPP))

    def run_test(self, config):
        self.feedbacks = []
        self.manual_feedbacks = []

        self.executable = None

        # Run a variety of tests, depending on the config file
        if hasattr(config, "compile"):      # Run compilation
            self.executable = self.test_compile(config.compile)
            
        if self.executable:
            if hasattr(config, "functionality"):   # Run compiled in testing
                self.test_functionality(config.functionality)
                
            if hasattr(config, "functionality_executable"):    # Run external testing
                self.test_executable_functionality(config.functionality_executable)
        else:   
            self.manual_feedbacks.append("Compilation failed")
            manual_weight = sum([config.functionality.weight if hasattr(config, "functionality") else 0,
                                 config.functionality_executable.weight if hasattr(config, "functionality_executable") else 0])

            self.feedbacks.append(util.manual_feedback_template(manual_weight))

        if hasattr(config, "static"):                         # Run static code evaluation
            self.static_code_analysis(config.static)
        
        if hasattr(config, "comments"):                       # Run comment density evaluation
            self.test_comments(config.comments)

        if hasattr(config, "style"):                          # Run style analysis
            self.test_code_style(config.style)

        return self.feedbacks, self.manual_feedbacks

    def test_functionality(self, config):
        # Here we run the .exe and read in the inputs, generated outputs and expected outputs
        if self.verbose: print("Testing functionality")

        output_file = os.path.join(self.tmp_dir, "result.json")
        _, stdout, stderr = util.execute([self.executable, output_file], self.tmp_dir, timeout=EXECUTABLE_TIMEOUT)
        if self.verbose: print(f"stdout:\n{stdout}\nstderr:\n{stderr}")

        try:
            with open(output_file) as json_file:
                result = json.load(json_file)
        except:
            result = None
        
        if result is not None:
            # Combine scores from test feedback
            score = sum([float(test['mark']) * test['weight'] for test in result if 'mark' in test and 'weight' in test])

            # Fix weight rounding
            for r in result:
                if "weight" in r:
                    r["weight"] = round(r["weight"], 3)

            self.feedbacks.append({
                "type": "functionality",
                "mark": round(score, 2),
                "weight": config.weight,
                "questions": result
            })
        else:
            # result = "No feedback file generated. Manual evaluation requried!"
            self.manual_feedbacks.append("Functionality evaluation failed to generate feedback file.")
            self.feedbacks.append(util.manual_feedback_template(config.weight))

    def test_executable_functionality(self, config):
        # Here we run the tester file, that runs the .exe
        if self.verbose: print("Testing executable functionality")
        output_file = os.path.join(self.tmp_dir, "result.json")
        _, stdout, stderr = util.execute([PY_RUNNER, self.tester_path, self.executable, output_file, get_eval_util_path()], self.tmp_dir, timeout=EXECUTABLE_TIMEOUT)
        if self.verbose: print(f"stdout:\n{stdout}\nstderr:\n{stderr}")

        try:
            with open(output_file) as json_file:
                result = json.load(json_file)
        except:
            result = None
        if result is not None:
            # Combine scores from test feedback
            score = sum([float(test['mark']) * test['weight'] for test in result if 'mark' in test and 'weight' in test])
            self.feedbacks.append({
                "type": "functionality",
                "mark": round(score, 2),
                "weight": config.weight,
                "questions": result
            })
        else:
            # result = "No feedback file generated. Manual evaluation requried!"
            self.manual_feedbacks.append("Executable functionality evaluation failed to generate feedback file.")
            self.feedbacks.append(util.manual_feedback_template(config.weight))

    def _process_issues_output(self, lines):
        if IS_WINDOWS:
            issue_lines = [line
                           for line in lines
                           if line.startswith(self.tmp_dir)]
            issues = [(i + 1, issue_line.split(":")[2], ':'.join(issue_line.split(":")[5:]))
                      for i, issue_line in enumerate(issue_lines)]
        else:
            issue_lines = [line.replace("]", "")
                           for line in lines
                           if line.startswith("[")]
            issues = [(i + 1, issue_line.split(":")[1], issue_line.split(")")[1])
                      for i, issue_line in enumerate(issue_lines)]
        return issues
        
    def static_code_analysis(self, config):
        if self.verbose: print("Running static code analysis")
        error_penalty = config.error_penalty if hasattr(config, "error_penalty") else 0.2

        _, stdout, stderr = util.execute(['cppcheck', self.tested_path], self.tmp_dir)
        if self.verbose: print(f"Raw result:\nstdout:\n{stdout}\nstderr:\n{stderr}")
        # Use cppcheck for static code analysis
        lines = stderr.replace('\r\n', '\n').split('\n')
        
        issues = self._process_issues_output(lines)

        n_issues = len(issues)

        with self.cpp_lookup.static_warnings.open() as json_file:
            static_feedback = json.load(json_file)

        fb = ""
        # build the feedback string
        n_issues_feedback = static_feedback['no_issues']
        n_issues_feedback.sort(key=lambda x: x['threshold'], reverse=True)

        for band in n_issues_feedback:
            if n_issues >= band['threshold']:
                fb += band["text"].format(n_issues)
                break

        contextual_feedback = static_feedback['contextual']
        if n_issues > 0:
            for issue_id, line_number, msg in issues:
                fb += (f"Issue {issue_id} on line {line_number}: `{msg}`\n\n")

                # loop through contextual feedback and add any relevant comments
                for key in contextual_feedback:
                    if key in msg:
                        fb += f'{contextual_feedback[key]}\n\n'

        self.feedbacks.append({
            "type": "static-analysis",
            "mark": round(max(1.0 - error_penalty * n_issues, 0), 2),
            "weight": config.weight,
            "feedback": fb
        })

    def test_code_style(self, config):
        if self.verbose: print("Testing code style")
        fixed_file = f"{self.tested_path}.fixed"
        
        selected_style = config.style if hasattr(config, "style") else "google"
        
        # Run clang-format
        with open(fixed_file, "w") as new_file:
            # Write output to file
            subprocess.call(['clang-format', f'-style={selected_style}', self.tested_path],
                            stdout=new_file)

        with open(fixed_file, "r") as f:
            fixed = f.readlines()
        with open(self.tested_path, "r") as f:
            orig = f.readlines()

        with open(self.cpp_lookup.style_feedback) as json_file:
            style_feedback = json.load(json_file)

        # This compares the fixed and original source files
        s = difflib.SequenceMatcher(None, fixed, orig)
        # value in the range 0.0 to 1.0
        score = s.ratio()

        # Generate feedback comments
        fb = [style_feedback['style_check'][PASS if score == 1.0 else FAIL]]
        
        if score < 1.0:
            # Now use diff to compare student file and clang tidied one
            _, stdout, _ = util.execute(['diff', '-y', '-W', '180', '-T', '-t', self.tested_path, fixed_file], self.tmp_dir)
            fb.append(util.as_md_code(stdout.replace("\r\n", "\n").split('\n')))

        fb.append(style_feedback['general'])

        self.feedbacks.append({
            "type": "style",
            "mark": round(score, 2),
            "weight": config.weight,
            "feedback": '\n\n'.join(fb)
        })

    def _compile_tester_to_o(self):
        my_dir = util.get_current_dir()

        eval_util_cpp = Path(my_dir, CPP_EVAL_UTIL_CPP)
        eval_util_h = Path(my_dir, CPP_EVAL_UTIL_H)
        json_hpp = Path(my_dir, JSON_HPP)

        tester_dependencies = [json_hpp, eval_util_cpp, eval_util_h] + \
                              [Path(file) for file in self.additional_files]

        cached_eval_util_o = self.o_cache.add_or_get(eval_util_cpp, [eval_util_h, json_hpp])
        cached_tester_o = self.o_cache.add_or_get(Path(self.tester_path), tester_dependencies)
        return self._copy_to_tmp(cached_tester_o), self._copy_to_tmp(cached_eval_util_o)

    def _compile_in_tmp(self, files, pedantic=False, link=True, output=None):
        run_params = [COMPILER, '-std=c++11', '-fnon-call-exceptions']
        if pedantic:
            run_params += ['-Wall', '-Wpedantic', '-Wextra']
        if not link:
            run_params += ["-c"]
        if output:
            run_params += ["-o", output]
        run_params += files
        
        _, stdout, stderr = util.execute([param for param in run_params if param != ""], self.tmp_dir)
        if self.verbose: print(f"stdout:\n{stdout}\nstderr:\n{stderr}")
        return stderr.replace(self.tmp_dir, "").split("\n"), output and os.path.isfile(output)

    def _failed_compilation_feedback(self, output):
        with self.cpp_lookup.compiler_warnings.open() as json_file:       # Load feedback file
            compiler_feedback = json.load(json_file)
        feedback = []
        feedback.append(compiler_feedback['compilation_result'][FAIL])   # Add comiplation failed feedback
        
        feedback.append(util.as_md_code(output))                               # Add compilation output to feedback
        error_feedback = compiler_feedback["contextual"]["error"]   # Get contextual feedback
        error_keys = set([key for key in error_feedback for line in output if key in line])
        feedback.append('\n\n'.join([f'`{key}`: {error_feedback[key]}' for key in error_keys]))    # analyse each error, and add each to the feedback
        return '\n'.join(feedback)

    def _warning_compilation_feedback(self, output, feedback, warning_penalty):
        with self.cpp_lookup.compiler_warnings.open() as json_file:       # Load feedback file
            compiler_feedback = json.load(json_file)
        # check if there were any warnings
        n_warnings = len([line for line in output if "warning" in line.lower()])
                
        score = max(1.0 - (n_warnings * warning_penalty), 0)     # Take points away for each warnig

        if n_warnings > 0:
            # add general feedback
            feedback.append(compiler_feedback['warning_check_result'][FAIL])
            
            # add the raw warnings to the feedback
            feedback.append(util.as_md_code(output))
            warning_feedback = compiler_feedback["contextual"]["warning"]
            warning_keys = set([key for key in warning_feedback for line in output if key in line])
            feedback.append('\n\n'.join([f'`{key}`: {warning_feedback[key]}' for key in warning_keys]))

        else:
            feedback.append(compiler_feedback['warning_check_result'][PASS])
        
        return '\n'.join(feedback), score

    def _compilation_result_template(self, score, weight, feedback):
        return {
            "type": "compilation",
            "mark": round(score, 2),
            "weight": weight,
            "feedback": '\n'.join(feedback) if type(feedback) == list else feedback
        }

    def test_compile(self, config):
        if self.verbose: print("Testing compilation")
        o_compile = hasattr(config, "type") and config.type == "o"
        tester_path = self.tester_path if self.tester_path.split('.')[-1] == "cpp" else ""
        eval_util_cpp = self.eval_util_cpp if self.tester_path.split('.')[-1] == "cpp" else ""
        warning_penalty = config.warning_penalty if hasattr(config, "warning_penalty") else 0.2

        compiled_executable = os.path.join(self.tmp_dir, COMPILED_EXECUTABLE)        # Executable path
        compiled_o = os.path.join(self.tmp_dir, COMPILED_O)

        if self.verbose: print(f"Compilation options: o_compile: {o_compile}, tester_path: {tester_path}")

        # see if file compiles
        if o_compile:
            output, compiled = self._compile_in_tmp([self.tested_path], link=False, output=compiled_o)
        else:
            output, compiled = self._compile_in_tmp([self.tested_path, tester_path, eval_util_cpp], output=compiled_executable)

        # Check whether compilation was succesful
        if not compiled:
            if self.verbose: print("Compilation failed")
            self.feedbacks.append(self._compilation_result_template(0, config.weight, self._failed_compilation_feedback(output)))
            return None
        
        with self.cpp_lookup.compiler_warnings.open() as json_file:       # Load feedback file
            compiler_feedback = json.load(json_file)

        if o_compile:
            if self.verbose: print("Linking o file to executable")
            tester_path, eval_util_o = self._compile_tester_to_o()
            output, compiled = self._compile_in_tmp([compiled_o, tester_path, eval_util_o], output=compiled_executable)
            
            if not compiled:
                self.feedbacks.append(self._compilation_result_template(0, config.weight, [compiler_feedback['compilation_result'][FAIL], util.as_md_code(output)]))
                return None

        feedback = []
        feedback.append(compiler_feedback['compilation_result'][PASS])

        # now look for warnings, so re-compile with warnings switched on
        if self.verbose: print("Pedantic recompile")
        output, _ = self._compile_in_tmp([self.tested_path], link=False, pedantic=True)
        feedback_result, score = self._warning_compilation_feedback(output, feedback, warning_penalty)
        
        # create feedback dictionary file
        self.feedbacks.append(self._compilation_result_template(score, config.weight, feedback_result))

        return compiled_executable
