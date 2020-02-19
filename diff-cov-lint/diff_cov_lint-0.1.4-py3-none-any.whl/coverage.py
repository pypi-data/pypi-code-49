"""Module for processing coverage and filtering by dict
"""
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Tuple


#parse coverage.xml
def process_coverage_xml(path: str, repo_path: str) -> dict:
    """Parses coverage.xml from Cobertura (pytest-cov) format

    :param path: path to coverage.xml
    :type path: str
    :param repo_path: path to repo. Used to calculate relative paths to analyzed paths
    :type repo_path: str
    :return: dict in format {"file_name": {line_num: hit}}
    :rtype: dict
    """
    coverage_dict = dict()
    tree = ET.parse(str(path)).getroot()
    srcs = tree.findall("sources/source")
    root_path = Path(srcs[0].text)
    root_relative_path = root_path.relative_to(Path(repo_path).resolve())
    for package in tree.findall("packages/package"):
        for class_ in package.findall("classes/class"):
            filename = str(root_relative_path / class_.attrib["filename"])
            coverage_dict[filename] = dict()
            for line in class_.findall("lines/line"):
                line_num = int(line.attrib["number"])
                hit = int(line.attrib["hits"])
                coverage_dict[filename][line_num] = int(hit)
    return coverage_dict


def filter_coverage(diff_dict: dict, coverage_dict: dict) -> dict:
    """Filter coverage from coverage dict, leaving only lines that were added

    :param diff_dict: dict that was returned from :func:`~diff_cov_lint.diff.process_diff`
    :type diff_dict: dict
    :param coverage_dict: dict that was returned
        from :func:`~diff_cov_lint.coverage.process_coverage_xml`
    :type coverage_dict: dict
    :return: dict in same format as coverage_dict but with lines from diff only
    :rtype: dict
    """

    diff_coverage_dict = defaultdict(dict)

    for file_path in diff_dict:
        if file_path in coverage_dict:
            for line in diff_dict[file_path]:
                if line in coverage_dict[file_path]:
                    diff_coverage_dict[file_path][line] = coverage_dict[
                        file_path][line]
    return diff_coverage_dict


#Output
def produce_ranges(nums: Iterable[int]) -> List[Tuple[int, int]]:
    """Converts list of ints to tuple of ranges.
    Example: [1, 2, 3, 5, 6, 8, 10] -> [(1, 3), (5, 6), (8, 8), (10, 10)]

    :param nums: list of ints to convert to ranges
    :type nums: List[int]
    :return: list of pairs (range start, range end)
    :rtype: List[Tuple[int, int]]
    """
    nums = sorted(nums)
    first_num = nums[0]
    cur_range = (first_num, first_num)
    prev = first_num
    ans = []
    for i in nums[1:]:
        if i - prev == 1:
            cur_range = (cur_range[0], i)
        else:
            ans.append(cur_range)
            cur_range = (i, i)
        prev = i
    ans.append(cur_range)
    return ans


def diff_coverage_report(diff_coverage_dict: dict,
                         show_missing: bool = False) -> str:
    """Produce human readable output for diff coverage

    :param diff_coverage_dict: output produced
        by :func:`~diff_cov_lint.diff.filter_coverage`
    :type diff_coverage_dict: dict
    :param show_missing: whether to show missing lines (default False)
    :type show_missing: bool
    :return: string with output
    :rtype: str
    """
    ans = "=" * 24 + " DIFF COVERAGE " + "=" * 24 + "\n"
    padding = max((len(filename) for filename in diff_coverage_dict), default=0)
    ans += f"{'FILE':<{padding}}\t\t\t{'COVERED'}\t{'STMTS'}\t{'PERCENT'}"
    if show_missing:
        ans += "\tMISSING"
    ans += "\n"
    total_covered = 0
    total_statements = 0
    for filename in diff_coverage_dict:
        covered_num = sum(diff_coverage_dict[filename].values())
        statements_num = len(diff_coverage_dict[filename])
        total_covered += covered_num
        total_statements += statements_num
        ans += f"{filename:<{padding}}\t\t\t{covered_num:>7}\t{statements_num:>5}\t" \
        f"{covered_num/statements_num * 100:>6.1f}%"
        if show_missing and covered_num < statements_num:
            missing_lines = [
                line for line, hit in diff_coverage_dict[filename].items()
                if not hit
            ]
            missing_ranges = produce_ranges(missing_lines)
            missing_formatted = ", ".join(
                [f"{s}-{e}" if s != e else str(s) for s, e in missing_ranges])
            ans += f"\t{missing_formatted}"
        ans += "\n"
    ans += "=" * 63 + "\n"
    if total_statements:
        total_percentage = total_covered / total_statements
    else:
        total_percentage = 1
    ans += f"{'TOTAL DIFF COV':<{padding}}\t\t\t{total_covered:>7}\t{total_statements:>5}\t"\
        f"{total_percentage * 100:>6.1f}%\n"
    return ans
