"""CLI interface and entrypoint for diff_cov_lint
"""
import fire

from .diff import get_diff, process_diff
from .coverage import process_coverage_xml, filter_coverage, diff_coverage_report
from .lint import process_pylint_report, filter_lint, diff_lint_report

def diff_cov_lint(target_ref: str,
                  source_ref: str,
                  cov_report: str = None,
                  lint_report: str = None,
                  repo_path: str = ".",
                  show_missing: bool = False) -> None:
    """Filter coverage and pylint report, show only part considering diff between two branches in git

    :param source_ref: Source branch in repo
    :type source_ref: str
    :param target_ref: Target branch in repo
    :type target_ref: str
    :param cov_report: Path to coverage report in Cobertura (pytest-cov) format, If not stated, coverage report will not be produced
    :type cov_report: str, optional
    :param lint_report: Path to pylint report. If not stated, linting report will not be produced
    :type lint_report: str, optional
    :param repo_path: Path to repo folder, defaults to "."
    :type repo_path: str, optional
    :param show_missing: whether to show missing lines, defaults to false
    :type show_missing: bool
    """
    diff = get_diff(repo_path, target_ref, source_ref)
    diff_dict = process_diff(diff)
    if cov_report is not None:
        coverage_dict = process_coverage_xml(cov_report, repo_path)
        diff_coverage_dict = filter_coverage(diff_dict, coverage_dict)
        print(diff_coverage_report(diff_coverage_dict, show_missing))

    if lint_report is not None:
        lint_dict = process_pylint_report(lint_report)
        diff_lint_dict = filter_lint(diff_dict, lint_dict)
        print(diff_lint_report(diff_lint_dict))



def main():
    """Entry point for console script
    """
    fire.Fire(diff_cov_lint)
