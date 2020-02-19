"""Module for processing pylint output and filtering by diff
"""
import re
from collections import defaultdict

P_PYLINT_ERROR = re.compile(
    r"^(?P<file>.+?):(?P<line>[0-9]+):(?P<column>[0-9]+): "
    r"(?P<type>[a-z])(?P<errno>\d+): (?P<msg>.+)", re.IGNORECASE)


def process_pylint_report(report_path: str) -> dict:
    """Parse and convert pylint report to dict

    :param report_path: path to pylint report
    :type report_path: str
    :return: Dict in format {filename: {line: {'error': error_slug, 'msg': message}}}
    :rtype: dict
    """
    lint_dict = defaultdict(lambda: defaultdict(dict))
    with open(report_path) as report_file:
        lines = report_file.readlines()
        for line in lines:
            match = re.search(P_PYLINT_ERROR, line)
            if match is not None:
                groupdict = match.groupdict()
                filename = groupdict['file']
                line = int(groupdict['line'])
                error = groupdict['type'] + groupdict['errno']
                msg = groupdict['msg']
                lint_dict[filename][line] = {'error': error, 'msg': msg}
    return lint_dict


def filter_lint(diff_dict: dict, lint_dict: dict) -> dict:
    """Filter linting messages from lint dict, leaving only lines that were added

    :param diff_dict: dict that was returned from :func:`~diff_cov_lint.diff.process_diff`
    :type diff_dict: dict
    :param lint_dict: dict that was returned
        from :func:`~diff_cov_lint.lint.process_pylint_report`
    :type lint_dict: dict
    :return: dict in same format as lint_dict but with lines from diff only
    :rtype: dict
    """

    diff_lint_dict = defaultdict(dict)

    for file_path in diff_dict:
        if file_path in lint_dict:
            for line in diff_dict[file_path]:
                if line in lint_dict[file_path]:
                    diff_lint_dict[file_path][line] = lint_dict[file_path][
                        line]
    return diff_lint_dict


def diff_lint_report(diff_lint_dict: dict) -> str:
    """Generate report in same format as pylint, but for diff only

    :param diff_lint_dict: dict as produced by :func:`~diff_cov_lint.lint.filter_lint`
    :type diff_lint_dict: dict
    :return: output with errors in diff only
    :rtype: str
    """
    ans = "=" * 26 + " DIFF LINT " + "=" * 26 + "\n"
    for filename in diff_lint_dict:
        for line in diff_lint_dict[filename]:
            ans += f"{filename}:{line}:0 {diff_lint_dict[filename][line]['error']}: "\
            f"{diff_lint_dict[filename][line]['msg']}\n"
    return ans
