from unittest import TestCase

import caselaw_tools

class TestHello(TestCase):
    def test_is_string(self):
        s = caselaw_tools.hello()
        self.assertTrue(isinstance(s, basestring))