import os
import shutil
from io import StringIO
from django.test import TestCase, modify_settings
from django.core.management import call_command
from django.core.management.base import CommandError
from django.conf import settings


class ConfigenCommandTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        # create folders and files required for tests
        cls.dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testfiles')
        cls.templates_dir = os.path.join(cls.dir, 'templates')
        cls.output_dir = os.path.join(cls.dir, 'output')

        os.mkdir(cls.dir)
        os.mkdir(cls.templates_dir)
        os.mkdir(cls.output_dir)

        cls.template_1 = 'test1.conf'
        cls.template_2 = 'test2.conf'

        with open(os.path.join(cls.templates_dir, cls.template_1), 'w') as f:
            f.write("{{ test_var }}")

        with open(os.path.join(cls.templates_dir, cls.template_2), 'w') as f:
            f.write("{{ test_var }}")

        cls.patch_settings()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.dir)
        super().tearDownClass()

    def tearDown(self):
        # delete created files after each test
        for f in os.scandir(self.output_dir):
            os.remove(f.path)

        # restore settings
        self.patch_settings()

    @classmethod
    def patch_settings(cls):
        settings.CONFIGEN_TEMPLATES_DIR = cls.templates_dir
        settings.CONFIGEN_OUTPUT_DIR = cls.output_dir
        settings.CONFIGEN_CONFIG_PROCESSORS = []
        settings.CONFIGEN_DEFAULT_CONTEXT = {}
        settings.CONFIGEN_DEFAULT_META = {}

    def read_outfile(self, filename):
        with open(os.path.join(self.output_dir, filename), 'r') as f:
            return f.read()

    def test_command_raises_error_if_templates_dir_setting_not_set(self):
        delattr(settings, 'CONFIGEN_TEMPLATES_DIR')
        
        with self.assertRaises(CommandError):
            call_command('configen')

    def test_command_raises_error_if_output_dir_setting_not_set(self):
        delattr(settings, 'CONFIGEN_OUTPUT_DIR')

        with self.assertRaises(CommandError):
            call_command('configen')

    def test_default_context_global_is_passed_to_every_template(self):
        settings.CONFIGEN_DEFAULT_CONTEXT = {
            '*': {
                'test_var': 'Hello'
            }
        }

        call_command('configen', verbosity=0)

        self.assertEqual(self.read_outfile(self.template_1), 'Hello')
        self.assertEqual(self.read_outfile(self.template_2), 'Hello')

    def test_default_context_global_is_overridden_by_template_context(self):
        settings.CONFIGEN_DEFAULT_CONTEXT = {
            '*': {
                'test_var': 'Hello'
            },
            self.template_1: {
                'test_var': 'Bye'
            }
        }

        call_command('configen', verbosity=0)

        # test overrides for template_1
        self.assertEqual(self.read_outfile(self.template_1), 'Bye')
        # test doesn't override for template_2
        self.assertEqual(self.read_outfile(self.template_2), 'Hello')

    def test_default_context_for_a_template_is_only_passed_to_its_template(self):
        settings.CONFIGEN_DEFAULT_CONTEXT = {
            self.template_1: {
                'test_var': 'Hello'
            },
            self.template_2: {
                'test_var': 'Bye'
            }
        }

        call_command('configen', verbosity=0)

        # test overrides for template_1
        self.assertEqual(self.read_outfile(self.template_1), 'Hello')
        # test doesn't override for template_2
        self.assertEqual(self.read_outfile(self.template_2), 'Bye')

    def test_config_processors_override_default_context(self):
        settings.CONFIGEN_DEFAULT_CONTEXT = {
            self.template_1: {
                'test_var': 'Hello'
            },
            self.template_2: {
                'test_var': 'Bye'
            }
        }

        settings.CONFIGEN_CONFIG_PROCESSORS = [
            'configen.tests.config_processor1'
        ]

        call_command('configen', verbosity=0)

        # test overrides for template_1
        self.assertEqual(self.read_outfile(self.template_1), 'Processor')
        # test doesn't override for template_2
        self.assertEqual(self.read_outfile(self.template_2), 'Processor')

    def test_default_meta_global_is_applied_to_every_template(self):
        settings.CONFIGEN_DEFAULT_META = {
            '*': {
                'outfile': '{template_name}.out'
            }
        }

        call_command('configen', verbosity=0)

        # name of output file should've been changed of every template
        self.assertIn(self.template_1 + '.out', os.listdir(self.output_dir))
        self.assertIn(self.template_2 + '.out', os.listdir(self.output_dir))

        # test no files with original names exist
        self.assertNotIn(self.template_1, os.listdir(self.output_dir))
        self.assertNotIn(self.template_2, os.listdir(self.output_dir))


    def test_default_meta_for_a_template_overrides_global_config(self):
        settings.CONFIGEN_DEFAULT_META = {
            '*': {
                'outfile': '{template_name}.out'
            },
            self.template_1: {
                'outfile': 'test1_override.conf'
            }
        }

        call_command('configen', verbosity=0)

        self.assertIn('test1_override.conf', os.listdir(self.output_dir))
        # template_2 get global meta
        self.assertIn(self.template_2 + '.out', os.listdir(self.output_dir))

        self.assertNotIn(self.template_1 + '.out', os.listdir(self.output_dir))
        self.assertNotIn(self.template_1, os.listdir(self.output_dir))
        self.assertNotIn(self.template_2, os.listdir(self.output_dir))

    def test_default_meta_for_a_template_is_only_applied_to_its_template(self):
        settings.CONFIGEN_DEFAULT_META = {
            self.template_1: {
                'outfile': 'test1_override.conf'
            },
            self.template_2: {
                'outfile': 'test2_override.conf'
            }
        }

        call_command('configen', verbosity=0)

        self.assertIn('test1_override.conf', os.listdir(self.output_dir))
        self.assertIn('test2_override.conf', os.listdir(self.output_dir))

        self.assertNotIn(self.template_1, os.listdir(self.output_dir))
        self.assertNotIn(self.template_2, os.listdir(self.output_dir))

    def test_config_processors_override_default_meta(self):
        settings.CONFIGEN_DEFAULT_META = {
            self.template_1: {
                'outfile': 'test1_override.conf'
            },
            self.template_2: {
                'outfile': 'test2_override.conf'
            }
        }

        settings.CONFIGEN_CONFIG_PROCESSORS = [
            'configen.tests.config_processor2'
        ]

        call_command('configen', verbosity=0)

        self.assertIn(self.template_1 + '.Processor', os.listdir(self.output_dir))
        self.assertIn(self.template_2 + '.Processor', os.listdir(self.output_dir))

        self.assertNotIn('test1_override.conf', os.listdir(self.output_dir))
        self.assertNotIn('test2_override.conf', os.listdir(self.output_dir))
        self.assertNotIn(self.template_1, os.listdir(self.output_dir))
        self.assertNotIn(self.template_2, os.listdir(self.output_dir))

    def test_outfile_name_override(self):
        """Currently tested in previous four methods"""
        pass

    def test_print_option(self):
        out = StringIO()
        call_command('configen', print=True, stdout=out, verbosity=0)

        # test that output file isn't generated
        self.assertEqual(os.listdir(self.output_dir), [])

    def test_printname_option(self):
        out = StringIO()
        call_command('configen', print=True, stdout=out, verbosity=0)

        # test that output file isn't generated
        self.assertEqual(os.listdir(self.output_dir), [])


def config_processor1(template_name, *args):
    """Config processor for tests. 
    returns context
    """
    return {'test_var': 'Processor'}


def config_processor2(template_name, *args):
    """Config processor for tests.
    returns config
    """
    return ({}, {'outfile': '%s.Processor' % template_name})
