# type: ignore
"""Module contains main API to work with pytest-emoji-output plugin."""
import sys
from typing import Tuple
from _pytest.config import Config
from _pytest.config.argparsing import Parser, OptionGroup
from _pytest.reports import TestReport
from attr import dataclass


@dataclass(frozen=True, slots=True)
class _TestStatus:
    """The class represents test status element."""

    outcome: str
    short: str
    long: str


def pytest_addoption(parser: Parser) -> None:
    """Turns on emoji parser feature.

    Args:
        parser (Parser): cli parser
    """
    group: OptionGroup = parser.getgroup("emoji")
    group.addoption("--emoji-out", action="store_true", help="Adds emoji to pytest results")


def pytest_report_header(config: Config) -> str:
    """Adds header to pytest runner.

    Args:
        config (Config): configuration option
    """
    if config.getoption("emoji_out"):
        return f"Running on {sys.platform} platform: {'{}.{}.{}'.format(*sys.version_info[:3])} python version"


def pytest_report_teststatus(report: TestReport, config: Config) -> Tuple[str, str, str]:
    """Turn failures into opportunities.

    Args:
        report (TestReport): pytest report item
        config (Config): pytest configuration item
    """
    if report.when == "call" and config.getoption("emoji_out"):
        if report.passed:
            passed_outcome, passed_short, passed_long = _TestStatus(
                outcome=report.outcome, short="😇", long="😇 Yes sir, it is passed"
            )
            return passed_outcome, passed_short, passed_long
        if report.failed:
            failed_outcome, failed_short, failed_long = _TestStatus(
                outcome=report.outcome, short="😡", long="😡 Oh crap, it is failed"
            )
            return failed_outcome, failed_short, failed_long
