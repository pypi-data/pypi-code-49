# -*- coding: utf-8 -*-

# Copyright 2020 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

import sushy

from sushycli.cmd.sushycli import main
from sushycli.tests.unit import base


@mock.patch.object(sushy, 'Sushy', autospec=True)
class SuchyCliTestCase(base.TestCase):

    @mock.patch('sys.stdout.write', autospec=True)
    def test_version(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_root.redfish_version = '1.2.3'

        main(['version', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calles = [
            mock.call('+---------+\n'
                      '| Version |'
                      '\n+---------+\n'
                      '| 1.2.3   |\n'
                      '+---------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calles)

    @mock.patch('sys.stdout.write', autospec=True)
    def test_system_power_show(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_system = mock_root.get_system.return_value

        mock_system.power_state = 'on'

        main(['system', 'power', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calles = [
            mock.call('+-------------+\n'
                      '| Power state |\n'
                      '+-------------+\n'
                      '| on          |\n'
                      '+-------------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calles)

    def test_system_power_on(self, mock_sushy):

        main(['system', 'power',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1',
              'on'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        mock_root = mock_sushy.return_value

        mock_root.get_system.assert_called_once_with(
            '/redfish/v1/Systems/1')

        mock_system = mock_root.get_system.return_value

        mock_system.reset_system.assert_called_once_with('on')

    def test_system_power_off(self, mock_sushy):

        main(['system', 'power',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1',
              'Off'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        mock_root = mock_sushy.return_value

        mock_root.get_system.assert_called_once_with(
            '/redfish/v1/Systems/1')

        mock_system = mock_root.get_system.return_value

        mock_system.reset_system.assert_called_once_with('force off')
