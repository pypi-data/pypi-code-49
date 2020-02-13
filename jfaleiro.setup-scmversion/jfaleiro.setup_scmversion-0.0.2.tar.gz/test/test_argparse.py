import unittest
from argparse import ArgumentError, ArgumentParser


class TestCommand(unittest.TestCase):

    def testSubparsers(self):
        parser = ArgumentParser()
        sp = parser.add_subparsers()
        sp_auto = sp.add_parser('auto')
        sp_auto.add_argument('--auto', action='store_true')
        sp_package = sp.add_parser('manual')
        sp_package.add_argument('package')
        sp_package.add_argument('file')

        parser.parse_args('auto --auto'.split())

    def testCompositeChoice(self):
        parser = ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--detect', action='store_true')
        group.add_argument('--manual', nargs=2)

        with self.assertRaises(SystemExit):
            parser.parse_args('--manual'.split())

        parser.parse_args('--detect'.split())
        parser.parse_args('--manual package file'.split())

    def testCompositeChoiceSimpler(self):
        parser = ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument('--auto', action='store_true')
        group.add_argument('package', nargs='?')
        parser.add_argument('file', nargs='?')
        parser.parse_args('--auto'.split())
        parser.parse_args('package file'.split())
        with self.assertRaises(SystemExit) as e:
            parser.parse_args('--help'.split())
        self.assertEquals(e.exception.code, 0)
