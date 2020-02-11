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
from ursa_major.handlers.remove_module import RemoveModuleHandler
if six.PY3:  # SafeConfigParser == ConfigParser, former deprecated in >= 3.2
    from six.moves.configparser import ConfigParser
else:
    from six.moves.configparser import SafeConfigParser as ConfigParser


class TestRemoveModuleHandler(unittest.TestCase):
    def setUp(self):
        config_file = os.path.join(TEST_DATA_DIR, 'ursa-major-test.conf')
        config = ConfigParser()
        config.read(config_file)
        self.handler = RemoveModuleHandler(config)

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

    @patch('ursa_major.handlers.remove_module.log')
    def test_remove_module_in_config(self, log):
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
        self.set_args(module_name="testmodule", module_stream="master")
        self.handler.run()

        log.info.assert_any_call(
            "No match tag found in tag %s's inheritance data", "f30-build")
        tag_configs = self.read_tag_config_file()
        self.assertEqual(tag_configs['f30-build']['modules'], [])

    @patch('ursa_major.handlers.remove_module.log')
    def test_remove_module_which_is_also_in_koji(self, log):
        """
        Remove a module which has module build tag in koji inheritance data
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
        mock_builds = [
            {
                'koji_tag': 'module-testmodule-master-202002021111-abcd1234',
                'modulemd': make_mmd(name='testmodule', stream='master',
                                     version='202002021234', context='abcd1234',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
            {
                'koji_tag': 'module-mariadb-10.4-202002023333-abcd2345',
                'modulemd': make_mmd(name='testmodule', stream='master',
                                     version='202002023333', context='abcd2345',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
        ]
        mock_builds_data = MockMBSBuildsData(mock_builds)
        self.mock_request_get.side_effect = mock_builds_data.get

        inheritance_data = [
            {
                'parent_id': 20,
                'name': 'module-testmodule-master-202002021111-abcd1234',
                'priority': 50,
            },
            {
                'parent_id': 101,
                'name': 'module-mariadb-10.4-3020190304180835-a5b0195c',
                'priority': 20,
            },
        ]
        self.mock_koji_session.getInheritanceData.return_value = inheritance_data

        self.set_args(module_name="testmodule", module_stream="master")
        #               module_requires=[("platform", "f30")],
        #               module_buildrequires=[("platform", "f30")])

        self.handler.run()
        log.info.assert_any_call(
            "Found match module tags under %s:\n%s",
            "f30-build",
            ["module-testmodule-master-202002021111-abcd1234"])

        tag_configs = self.read_tag_config_file()
        self.assertEqual(tag_configs['f30-build']['modules'], [])

    @patch('ursa_major.handlers.remove_module.log')
    def test_remove_module_with_requires(self, log):
        """
        Remove a module with requires and buildrequires specified
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
        mock_builds = [
            {
                'koji_tag': 'module-testmodule-master-202002021111-abcd1234',
                'modulemd': make_mmd(name='testmodule', stream='master',
                                     version='202002021234', context='abcd1234',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
            {
                'koji_tag': 'module-mariadb-10.4-202002023333-abcd2345',
                'modulemd': make_mmd(name='testmodule', stream='master',
                                     version='202002023333', context='abcd2345',
                                     requires={'platform': 'f30'},
                                     buildrequires={'platform': 'f30'}).dumps(),
            },
        ]
        mock_builds_data = MockMBSBuildsData(mock_builds)
        self.mock_request_get.side_effect = mock_builds_data.get

        inheritance_data = [
            {
                'parent_id': 20,
                'name': 'module-testmodule-master-202002021111-abcd1234',
                'priority': 50,
            },
            {
                'parent_id': 101,
                'name': 'module-mariadb-10.4-3020190304180835-a5b0195c',
                'priority': 20,
            },
        ]
        self.mock_koji_session.getInheritanceData.return_value = inheritance_data

        self.set_args(module_name="testmodule", module_stream="master",
                      module_requires=[("platform", "f30")],
                      module_buildrequires=[("platform", "f30")])

        self.handler.run()
        log.info.assert_any_call(
            "Found match module tags under %s:\n%s",
            "f30-build",
            ["module-testmodule-master-202002021111-abcd1234"])

        tag_configs = self.read_tag_config_file()
        self.assertEqual(tag_configs['f30-build']['modules'], [])

    @patch('ursa_major.handlers.remove_module.log')
    @patch('ursa_major.handlers.remove_module.RemoveModuleHandler.write_tag_config')
    def test_remove_non_exist_module(self, write_tag_config, log):
        """
        Remove a non exist module from config file
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
        self.set_args(module_name="testmodule", module_stream="f30")
        self.handler.run()
        log.warning.assert_any_call(
            "Specified module is not found under tag %s in tag config file, nothing to change",
            "f30-build")
        write_tag_config.assert_not_called()

    @patch('ursa_major.handlers.remove_module.log')
    @patch('ursa_major.handlers.remove_module.RemoveModuleHandler.write_tag_config')
    def test_remove_module_from_non_exist_tag(self, write_tag_config, log):
        """
        Remove a module from non exist tag in tag config file
        """
        self.write_tag_config_file({})
        self.set_args(module_name="testmodule", module_stream="master")
        self.handler.run()
        log.warning.assert_any_call(
            "Tag %s is not in tag config file %s, nothing to change",
            "f30-build",
            self.handler.tag_config_file)
        write_tag_config.assert_not_called()
