# -*- coding: utf-8 -*-
# Copyright (c) 2019  Red Hat, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Written by Chenxiong Qi <cqi@redhat.com>

import json
import os
import shutil
import six
import tempfile
import unittest
from argparse import Namespace
from mock import patch
from tests import TEST_DATA_DIR, MockMBSBuildsData, make_mmd
from ursa_major.handlers.add_module import AddModuleHandler
if six.PY3:  # SafeConfigParser == ConfigParser, former deprecated in >= 3.2
    from six.moves.configparser import ConfigParser
else:
    from six.moves.configparser import SafeConfigParser as ConfigParser


class TestAddModuleHandler(unittest.TestCase):
    def setUp(self):
        config_file = os.path.join(TEST_DATA_DIR, 'ursa-major-test.conf')
        config = ConfigParser()
        config.read(config_file)
        self.handler = AddModuleHandler(config)

        self.tmpdir = tempfile.mkdtemp(suffix='_ursa_major_test')
        self.tag_config_file = os.path.join(self.tmpdir, 'default.json')
        with open(self.tag_config_file, 'w') as f:
            json.dump({}, f)

        self.set_args()

        self.koji_session_patcher = patch('koji.ClientSession')
        self.mock_koji_session = self.koji_session_patcher.start().return_value

        self.request_get_patcher = patch('requests.get')
        self.mock_request_get = self.request_get_patcher.start()
        self.mock_request_get.side_effect = MockMBSBuildsData([]).get

    def tearDown(self):
        self.koji_session_patcher.stop()
        self.request_get_patcher.stop()
        try:
            shutil.rmtree(self.tmpdir)
        except:  # noqa
            pass

    def set_args(self, **kwargs):
        kwargs.setdefault("tag_config_file", self.tag_config_file)
        kwargs.setdefault("tag", "f30-build")
        kwargs.setdefault("module_requires", None)
        kwargs.setdefault("module_buildrequires", None)
        kwargs.setdefault("debug", False)
        kwargs.setdefault("dry_run", False)
        args = Namespace()
        for k, v in kwargs.items():
            setattr(args, k, v)
        self.handler.set_args(args)

    def write_tag_config_file(self, content):
        """ Write content to tag config file.

        :param content: content in dict format
        """
        with open(self.tag_config_file, 'w') as f:
            json.dump(content, f, indent=2, sort_keys=True)

    def read_tag_config_file(self):
        with open(self.tag_config_file, 'r') as f:
            return json.load(f)

    def test_add_new_module_with_nonexist_name_stream(self):
        """
        Add a completely new module.
        """
        self.write_tag_config_file({})
        self.set_args(module_name="testmodule", module_stream="master", priority=50)

        self.handler.run()

        expected = [{
            'name': 'testmodule',
            'stream': 'master',
            'priority': 50
        }]

        tag_configs = self.read_tag_config_file()
        assert expected == tag_configs['f30-build']['modules']

    @patch('ursa_major.handlers.add_module.AddModuleHandler.write_tag_config')
    def test_add_new_module_with_conflict_priority_in_config(self, write_tag_config):
        """
        Add a new module but priority conflicts with existing one in config.
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'priority': 50,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)

        self.set_args(module_name="mariadb", module_stream="10.4", priority=50)
        with self.assertRaises(ValueError) as ctx:
            self.handler.run()

        self.assertIn("Priority 50 is used by other modules in config",
                      str(ctx.exception))
        write_tag_config.assert_not_called()

    @patch('ursa_major.handlers.add_module.AddModuleHandler.write_tag_config')
    def test_add_new_module_with_conflict_priority_in_koji(self, write_tag_config):
        """
        Add a new module but priority conflicts with existing one in tag inheritance.
        """
        self.write_tag_config_file({})
        mock_builds = [
            {
                'koji_tag': 'module-mariadb-10.4-3020190313091759-a5b0195c',
                'modulemd': make_mmd(name='mariadb', stream='10.4',
                                     version='3020190313091759', context='a5b0195c',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
            {
                'koji_tag': 'module-mariadb-10.4-3020190304180835-a5b0195c',
                'modulemd': make_mmd(name='mariadb', stream='10.4',
                                     version='3020190304180835', context='a5b0195c',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
        ]
        mock_builds_data = MockMBSBuildsData(mock_builds)
        self.mock_request_get.side_effect = mock_builds_data.get

        inheritance_data = [
            {
                'parent_id': 20,
                'name': 'module-ant-1.10-20181122140939-819b5873',
                'priority': 50,
            },
            {
                'parent_id': 101,
                'name': 'module-mariadb-10.4-3020190304180835-a5b0195c',
                'priority': 20,
            },
        ]
        self.mock_koji_session.getInheritanceData.return_value = inheritance_data

        self.set_args(module_name="mariadb", module_stream="10.4", priority=50)
        with self.assertRaises(ValueError) as ctx:
            self.handler.run()

        self.assertIn("Priority 50 is used by other modules in tag f30-build's inheritance",
                      str(ctx.exception))
        write_tag_config.assert_not_called()

    def test_update_module_with_new_priority(self):
        """
        Update an existing module with a new priority value
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'priority': 50,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)

        self.set_args(module_name="testmodule", module_stream="master", priority=100)
        self.handler.run()

        expected = [{
            'name': 'testmodule',
            'stream': 'master',
            'priority': 100
        }]

        tag_configs = self.read_tag_config_file()
        self.assertEqual(expected, tag_configs['f30-build']['modules'])

    def test_update_module_with_new_priority_and_requires(self):
        """
        Update an existing module with a new priority and requires
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'requires': {'platform': 'rawhide'},
                        'buildrequires': {'platform': 'rawhide'},
                        'priority': 50,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)
        self.set_args(module_name="testmodule", module_stream="master",
                      module_requires=[('platform', 'f30')],
                      module_buildrequires=[('platform', 'f30')],
                      priority=100)

        self.handler.run()

        expected = [{
            'name': 'testmodule',
            'stream': 'master',
            'priority': 100,
            'requires': {'platform': 'f30'},
            'buildrequires': {'platform': 'f30'},
        }]

        tag_configs = self.read_tag_config_file()
        self.assertEqual(expected, tag_configs['f30-build']['modules'])

    def test_update_module_removing_requires_and_new_priority(self):
        """
        Update an existing module with a new priority and remove requires
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'requires': {'platform': 'rawhide'},
                        'buildrequires': {'platform': 'rawhide'},
                        'priority': 50,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)
        self.set_args(module_name="testmodule", module_stream="master", priority=100)

        self.handler.run()

        expected = [{
            'name': 'testmodule',
            'stream': 'master',
            'priority': 100,
        }]

        tag_configs = self.read_tag_config_file()
        self.assertEqual(expected, tag_configs['f30-build']['modules'])

    @patch('ursa_major.handlers.add_module.AddModuleHandler.write_tag_config')
    def test_add_an_existing_module(self, write_tag_config):
        """
        Add a module which already exists in config file with same config.
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'requires': {'platform': 'f30'},
                        'buildrequires': {'platform': 'f30'},
                        'priority': 50,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)
        self.set_args(module_name="testmodule", module_stream="master",
                      module_requires=[('platform', 'f30')],
                      module_buildrequires=[('platform', 'f30')],
                      priority=50)

        self.handler.run()

        expected = [{
            'name': 'testmodule',
            'stream': 'master',
            'priority': 50,
            'requires': {'platform': 'f30'},
            'buildrequires': {'platform': 'f30'},
        }]

        tag_configs = self.read_tag_config_file()
        self.assertEqual(expected, tag_configs['f30-build']['modules'])
        write_tag_config.assert_not_called()

    @patch('ursa_major.handlers.add_module.AddModuleHandler.write_tag_config')
    def test_multiple_name_stream_modules_in_config(self, write_tag_config):
        """
        Test multiple modules for the same name+stream found in config file
        """
        config_content = {
            'f30-build': {
                'modules': [
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'priority': 50,
                    },
                    {
                        'name': 'testmodule',
                        'stream': 'master',
                        'requires': {'platform': 'f30'},
                        'priority': 100,
                    }
                ],
                'owners': ['owner@example.com']
            }
        }
        self.write_tag_config_file(config_content)

        self.set_args(module_name="testmodule", module_stream="master", priority=200)
        with self.assertRaises(RuntimeError) as ctx:
            self.handler.run()

        self.assertIn("Unexpected error, found multiple modules in config file with "
                      "name 'testmodule' and stream 'master'",
                      str(ctx.exception))
        write_tag_config.assert_not_called()
