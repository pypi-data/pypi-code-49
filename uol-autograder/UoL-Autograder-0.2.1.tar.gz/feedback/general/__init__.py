import subprocess
import os
from pathlib import Path
import json
import re
from .. import util
from .contants import *

class GeneralLookup(util.Lookup):
    _comment_feedback = "comment_feedback.json"

class Runner:
    def __init__(self, tmp_files, run_args={}):
        self.general_lookup = GeneralLookup(tmp_files.lookup_dir)
        self.feedbacks = []
        self.manual_feedbacks = []
        self.tmp_files = tmp_files
        self.tested_path = tmp_files.tested_path.absolute().as_posix()
        self.tester_path = tmp_files.tester_path.absolute().as_posix() if tmp_files.tester_path else None
        self.additional_files = [file.absolute().as_posix() for file in tmp_files.additional_files] if tmp_files.additional_files else None
        self.tmp_dir = tmp_files.tmp_dir.name
        self.verbose = run_args.get("verbose", False)

    def test_comments(self, config):
        if self.verbose:
            print("Testing comments")
        # cloc - Count Lines of Code
        _, stdout, _ = util.execute(['cloc', self.tested_path, "--csv", "--quiet"], self.tmp_dir)
        lines = list(stdout.splitlines()) 

        # Find the correct line in the result             
        result = None
        for line in lines:
            match = re.search(r'(?P<files>\d*),(?P<language>.*),(?P<blank>\d*),(?P<comment>\d*),(?P<code>\d*)', line)
            if match:
                result = match
        
        if result:
            # Unpack results
            n_blank, n_comments, n_code = [int(result.group(name)) for name in ["blank", "comment", "code"] ]
            comment_density = n_comments / (n_code + n_comments)
        else:
            n_blank, n_comments, n_code, comment_density = 0, 0, 0, 0

        if self.verbose:
            print(f"Blank lines: {n_blank}, Comment lines: {n_comments}, Code lines: {n_code}, Comment density: {comment_density}")
        

        with open(self.general_lookup.comment_feedback) as json_file:
            comment_feedback = json.load(json_file)

        # Format feedback with results
        fb = comment_feedback["stats"].format(n_code, n_comments, n_blank)
        score = comment_density

        # Find the right feedback line
        density_feedback = comment_feedback["density_feedback"]
        density_feedback.sort(key=lambda x: x["threshold"])

        for band in density_feedback:
            if comment_density <= band["threshold"]:
                fb += band["text"]
                score += band["bonus"]
                break

        score = min(score, 1.0)

        self.feedbacks.append({
            "type": "comments",
            "mark": round(score, 2),
            "weight": config.weight,
            "feedback": fb
        })

def test_comments(tested_file, config, working_dir, lookup_dir):
    general_lookup = GeneralLookup(lookup_dir)
    # cloc - Count Lines of Code
    _, stdout, _ = util.execute(['cloc', tested_file, "--csv", "--quiet"], working_dir)
    lines = list(stdout.splitlines())

    # Find the correct line in the result             
    result = None
    for line in lines:
        match = re.search(r'(?P<files>\d*),(?P<language>.*),(?P<blank>\d*),(?P<comment>\d*),(?P<code>\d*)', line)
        if match:
            result = match
    
    assert result
    # Unpack results
    n_blank, n_comments, n_code = [int(result.group(name)) for name in ["blank", "comment", "code"] ]

    with open(general_lookup.comment_feedback) as json_file:
        comment_feedback = json.load(json_file)

    # Format feedback with results
    fb = comment_feedback["stats"].format(n_code, n_comments, n_blank)

    comment_density = n_comments / (n_code + n_comments)
    score = comment_density

    # Find the right feedback line
    density_feedback = comment_feedback["density_feedback"]
    density_feedback.sort(key=lambda x: x["threshold"])

    for band in density_feedback:
        if comment_density <= band["threshold"]:
            fb += band["text"]
            score += band["bonus"]
            break

    score = min(score, 1.0)

    return {
        "type": "comments",
        "mark": round(score, 2),
        "weight": config.weight,
        "feedback": fb
    }
