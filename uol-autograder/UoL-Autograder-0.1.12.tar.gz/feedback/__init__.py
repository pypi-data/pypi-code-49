import inspect, shutil
import json
from pathlib import Path
from collections import namedtuple
from tempfile import TemporaryDirectory
from . import cpp
from . import py
from .util import create_feedback_json, get_current_dir, dict_to_namedtuple
from .general.contants import LOOKUP_DIR

def load_config(config_file):
    if not isinstance(config_file, Path):
        config_file = Path(config_file)
    assert config_file.is_file()                      # Check if config file exists
    with config_file.open() as json_file:                    # Load config file as a named tuple (so it can be indexed as names, not with strings)
        return dict_to_namedtuple(json.load(json_file))

# Setup script, prepare everything for testing, create tmp directory, and move all relevant files there
class TmpFiles:
    def __init__(self, tested_file, config):
        assert isinstance(tested_file, Path)
        self.my_dir = get_current_dir()     # Get this exact directory, regardless where it was called from.

        self.lookup_dir = Path(self.my_dir, LOOKUP_DIR)      # Define lookup directory, and check if it exists
        assert self.lookup_dir.is_dir()

        self.tmp_dir = TemporaryDirectory()

        assert tested_file.is_file()                     # Check if tested file exists
        self.tested_path = Path(self.tmp_dir.name, tested_file.name)      # Copy it to tmp dir
        shutil.copyfile(tested_file, self.tested_path)

        self.tester_path = None
        self.additional_files = []

        if hasattr(config, "execution"):
            assert hasattr(config.execution, "tester_file")       # Check if config has tester file
            tester_file = Path(config.execution.tester_file)
            assert tester_file.is_file()                                                  # Check if tester file exists
            self.tester_path = Path(self.tmp_dir.name, tester_file.name)                  # Copy tester file to tmp dir
            shutil.copyfile(tester_file, self.tester_path)

            if hasattr(config.execution, "additional_files"):                                   # Copy every additional file to the tmp dir
                additional_files = [Path(file_name) for file_name in config.execution.additional_files]
                assert all(path.is_file() for path in additional_files)
                for f in additional_files:
                    path = Path(self.tmp_dir.name, f.name)
                    self.additional_files.append(path)
                    shutil.copyfile(f, path)
    
    # Delete tmp dir and all its contents
    def teardown(self):
        self.tmp_dir.cleanup()

    def save_tmpdir(self, target_dir):
        if Path(self.tmp_dir.name).is_dir():
            shutil.copy(self.tmp_dir.name, target_dir)


# Find the right testing function based on the tested file extension
def get_test_runner(tested_file):
    extension = tested_file.suffix      # Get the file extension
    if extension == ".cpp":
        return cpp.CppRunner
    elif extension == ".py":
        return py.PyRunner
    raise Exception(f"No runner found for extension {extension}")       # Throw error if the extension is invalid

# Actual entry point, with actual parameters
def run_test(tested_file, config_file, run_args={}):
    config = load_config(config_file)

    tested_file = tested_file if isinstance(tested_file, Path) else Path(tested_file)

    tmp_files = TmpFiles(tested_file, config)

    test_runner = get_test_runner(tested_file)(tmp_files, run_args)        # Get the right testing function
    feedback, manual_feedback = test_runner.run_test(config.tests)

    tmp_files.teardown()                                                   # Remove tmp dir

    return create_feedback_json(feedback, manual_feedback)            # Create json file