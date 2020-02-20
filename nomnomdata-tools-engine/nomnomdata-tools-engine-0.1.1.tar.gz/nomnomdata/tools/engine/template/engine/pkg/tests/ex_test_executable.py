import logging
from unittest import TestCase

from nomnomdata.engine.test import NominodeMock
from nomnomdata.engine.test_creds import credentials

from ..executable import TemplateExecutable

config = {
    "3": credentials["aws_connection"],
}
base_params = {
    "config": config,
    "aws_connection": {"connection_uuid": "3"},
    "test_parameter_1": "5",
    "test_parameter_2": False,
}


class TestReportSync(TestCase):
    def tearDown(self):
        self.logger.info("teardown")

    def setUp(self):
        self.params = base_params.copy()
        self.logger = logging.getLogger("nomigen.test")

    def test_basic(self):
        nominode = NominodeMock(task_parameters=self.params)
        with nominode:
            executable = TemplateExecutable()
            executable.do_thing()
