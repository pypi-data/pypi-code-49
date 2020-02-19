# -*- coding: utf-8 -*-

# Copyright 2010-2020 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sushy

from sushycli import base


SYSTEM_ID_HELP = (
    'The canonical path to the ComputerSystem resource that the driver '
    'will interact with. It should include the root service, version and '
    'the unique resource path to a ComputerSystem. For example: '
    '/redfish/v1/Systems/1'
)


class SystemPowerShow(base.BaseLister):
    """Show machine power state"""

    def get_parser(self, prog_name):
        """Power state management command parser.

        :param prog_name: name of the cliff command being executed
        :returns: an `argparse.ArgumentParser` instance
        """
        parser = super(SystemPowerShow, self).get_parser(prog_name)

        parser.add_argument(
            '--system-id',
            required=True,
            help=SYSTEM_ID_HELP)

        return parser

    def take_action(self, args):
        """Power state management command action.

        :param args: a namespace of command-line option-value pairs that
            come from the user
        :returns: CLI process exit code
        """
        root = super(SystemPowerShow, self).take_action(args)

        sys_inst = root.get_system(args.system_id)

        return ['Power state'], [[sys_inst.power_state]]


class SystemPowerSet(base.BaseCommand):
    """Change machine power state"""

    def get_parser(self, prog_name):
        """Power state management command parser.

        :param prog_name: name of the cliff command being executed
        :returns: an `argparse.ArgumentParser` instance
        """
        parser = super(SystemPowerSet, self).get_parser(prog_name)

        parser.add_argument(
            '--system-id',
            required=True,
            help=SYSTEM_ID_HELP)

        parser.add_argument(
            'state',
            metavar='on|off',
            type=lambda x: x.lower(),
            choices=['on', 'off'],
            help='Set machine power state')

        return parser

    def take_action(self, args):
        """Power state management command action.

        :param args: a namespace of command-line option-value pairs that
            come from the user
        :returns: CLI process exit code
        """
        root = super(SystemPowerSet, self).take_action(args)

        sys_inst = root.get_system(args.system_id)

        sys_inst.reset_system(
            sushy.RESET_TYPE_ON
            if args.state == 'on' else sushy.RESET_TYPE_FORCE_OFF)

        return 0
