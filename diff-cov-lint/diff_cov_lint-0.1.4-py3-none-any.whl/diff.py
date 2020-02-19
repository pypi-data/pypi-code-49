"""Module for processing git diff
"""
from io import StringIO
from collections import defaultdict

from git import Repo
from unidiff import PatchSet


def get_diff(repo_path: str, target_ref: str, source_ref: str) -> StringIO:
    """Returns diff between two branches in repo in gitdiff format

    :param repo_path: path to repo folder
    :type repo_path: str
    :param target_ref: target branch or commit sha
    :type target_ref: str
    :param source_ref: Source branch or commit sha
    :type source_ref: str
    :return: diff between branches in gitdiff format
    :rtype: str
    """
    repo = Repo(repo_path)
    diff_text = repo.git.diff(target_ref,
                              source_ref,
                              ignore_blank_lines=True,
                              ignore_space_at_eol=True)
    diff_text = StringIO(diff_text)
    return diff_text


def process_diff(diff_text: str) -> dict:
    """Process diff text to return dict of added lines in files

    :param diff_text: text of diff in gitdiff format
    :type diff_text: str
    :return: Dict of added lines in format {"file_path": [1,2,3,5,6,7]}
    :rtype: dict
    """
    patch_set = PatchSet(diff_text)

    added_lines = defaultdict(list)

    for patched_file in patch_set:
        file_path = patched_file.path  # file name
        for hunk in patched_file:
            for line in hunk:
                if line.is_added and line.value.strip() != '':
                    added_lines[file_path].append(line.target_line_no)
    return added_lines
