import inspect, os, sys
import json
import datetime
from collections.abc import Mapping
from collections import namedtuple
from pathlib import Path
from tempfile import TemporaryFile
import subprocess

class Lookup:
    def __init__(self, lookup_dir):
        for name, value in inspect.getmembers(self):
            if "__" not in name and name.startswith("_") and not os.path.isabs(value):
                setattr(self, name.lstrip("_"), Path(lookup_dir, value))

decoder = lambda x: str(x.decode('UTF-8'))

def execute(args, working_dir, shell=False, timeout=None):
    try:
        with TemporaryFile() as err, TemporaryFile() as out:
            retval = subprocess.call(args, cwd=working_dir, stderr=err, stdout=out, shell=shell, timeout=timeout)
            err.seek(0)
            out.seek(0)
            return retval, decoder(out.read()), decoder(err.read())
    except subprocess.TimeoutExpired:
        return None, None, None

def feedback_to_tests(test, index):
    if test["type"] != "functionality":
        return [{
                "name": test["type"],
                "score": round(test["mark"] * test["weight"] * 100, 2),
                "max_score": round(test["weight"] * 100, 2),
                "output": test["feedback"],
                "number": str(index)
            }]
    return [
            {
                "name": f'functionality - {question["question"].replace("_", " ")}',
                "score": round(float(question["mark"]) * question["weight"] * test["weight"] * 100, 2),
                "max_score": round(question["weight"] * test["weight"] * 100, 2),
                "output": question["feedback"],
                "number": f"{index}.{i + 1}"
            }
            for i, question in enumerate(test["questions"])
        ]

# Create the feedback.json file in correct format
def create_feedback_json(fb_array, manual_feedback):
    # total = sum([item['weight'] * item['mark'] for item in fb_array]) * 100
    dictionary = {
        "tests":
        [
            item
            for i, test in enumerate(fb_array)
            for item in feedback_to_tests(test, i + 1)
        ]
    }
    # dictionary["total"] = round(total, 2)
    # dictionary["results"] = fb_array

    return dictionary

def save_feedback_file(dictionary, filename="result.json", verbose=False):
    with open(filename, "w") as ofile:
        json.dump(dictionary, ofile, indent=4)
    if verbose: print(f"Saved result to {os.path.abspath(filename)}")

def get_current_dir():
    origin = sys._getframe(1) if hasattr(sys, "_getframe") else None
    return os.path.dirname(os.path.abspath(inspect.getfile(origin)))


def dict_to_namedtuple(mapping):
    if isinstance(mapping, Mapping):
        for key, value in mapping.items():
            mapping[key] = dict_to_namedtuple(value)
        return namedtuple_from_mapping(mapping)
    return mapping

def namedtuple_from_mapping(mapping, name="Tupperware"):
    this_namedtuple_maker = namedtuple(name, mapping.keys())
    return this_namedtuple_maker(**mapping)


def manual_feedback_template(weight):
    return {
        "type": "manual-evaluation",
        "mark": 0,
        "weight": weight,
        "feedback": ""
    }

def get_files_in_dir(dir_path):
    assert dir_path.is_dir()
    return [f for f in dir_path.glob('**/*') if f.is_file()]

def as_md_code(lines):
    return "```\n{}\n```".format('\n'.join(lines))