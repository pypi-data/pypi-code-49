from .logging import get_report_logger


class NoopReporter:
    """do nothing"""
    def report(self, span):
        pass


class LogReporter:
    """record span to log"""
    def __init__(self):
        self.logger = get_report_logger()

    def report(self, span):
        self.logger.info(span.to_dict())
