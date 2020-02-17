#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import eurekaroom


class UnitTests(unittest.TestCase):
    def test_import_dir(self):
        self.assertIsNotNone(eurekaroom)

    def test_imports(self):
        eurekaroom.init_routes()
        self.assertIsNotNone(eurekaroom.myapp)
        self.assertIsNotNone(eurekaroom.config)

if __name__ == "__main__":
    unittest.main()