# Copyright (c) 2019 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from __future__ import absolute_import, print_function, unicode_literals

import sys

import qumulo.lib.opts
import qumulo.rest.roles as roles
from qumulo.lib.identity_util import Identity
from qumulo.lib.opts import str_decode
from qumulo.lib.util import TextAligner

class ListRolesCommand(qumulo.lib.opts.Subcommand):
    NAME = 'auth_list_roles'
    SYNOPSIS = 'List all of the roles.'

    @staticmethod
    def print_roles(auth_roles, all_members, aligner):
        for role_name, role in sorted(auth_roles.items()):
            aligner.add_line(role_name)
            with aligner.indented():
                ListRoleCommand.print_role(
                    role, all_members[role_name], aligner)
            aligner.add_line("")

    @staticmethod
    def options(parser):
        parser.add_argument("--json", action="store_true",
            help="Print JSON representation of auth roles.")

    @staticmethod
    def main(conninfo, credentials, args):
        auth_roles = roles.list_roles(conninfo, credentials)

        if args.json:
            print(auth_roles)
        else:
            aligner = TextAligner()
            role_members = {
                role: roles.list_members(
                    conninfo, credentials, role).data['members']
                for role in auth_roles.data}
            ListRolesCommand.print_roles(auth_roles.data, role_members, aligner)
            aligner.write(sys.stdout)

class ListRoleCommand(qumulo.lib.opts.Subcommand):
    NAME = 'auth_list_role'
    SYNOPSIS = 'List a role.'

    @staticmethod
    def _filter_member_info(info):
        return info[0] not in ["domain", "name"] and info[1] is not None

    @staticmethod
    def print_role(role, members, aligner):
        aligner.add_line(role["description"])
        aligner.add_line("Members:")
        with aligner.indented():
            for member in members.values():
                name = member["name"]
                if name is None or name == "":
                    name = "auth_id:{}".format(member["auth_id"])
                aligner.add_line(name)
                with aligner.indented():
                    aligner.add_wrapped_table(
                        sorted(
                            filter(
                                ListRoleCommand._filter_member_info,
                                member.items())))

    @staticmethod
    def options(parser):
        parser.add_argument("-r", "--role", type=str_decode, required=True,
            help="Name of the role to lookup")
        parser.add_argument("--json", action="store_true",
            help="Print JSON representation of auth role.")

    @staticmethod
    def main(conninfo, credentials, args):
        role = roles.list_role(conninfo, credentials, args.role)
        members = roles.list_members(
            conninfo, credentials, args.role).data['members']
        if args.json:
            print(role)
        else:
            aligner = TextAligner()
            ListRoleCommand.print_role(role.data, members, aligner)
            aligner.write(sys.stdout)

def get_api_id_from_trustee(trustee):
    return Identity(trustee).dictionary()

class AssignRoleCommand(qumulo.lib.opts.Subcommand):
    NAME = 'auth_assign_role'
    SYNOPSIS = 'Assign a user to a role'

    @staticmethod
    def options(parser):
        parser.add_argument("-r", "--role", type=str_decode, required=True,
            help="Name of the role to assign")
        parser.add_argument("-t", "--trustee", type=str_decode, required=True,
            help="Assign the role to this trustee.  e.g. Everyone, "
            "uid:1000, gid:1001, sid:S-1-5-2-3-4, or auth_id:500")

    @staticmethod
    def main(conninfo, credentials, args):
        api_id = get_api_id_from_trustee(args.trustee)
        roles.add_member(conninfo, credentials, args.role, **api_id)

class UnassignRoleCommand(qumulo.lib.opts.Subcommand):
    NAME = 'auth_unassign_role'
    SYNOPSIS = 'Unassign a user from a role'

    @staticmethod
    def options(parser):
        parser.add_argument("-r", "--role", type=str_decode, required=True,
            help="Name of the role to unassign")
        parser.add_argument("-t", "--trustee", type=str_decode, required=True,
            help="Unassign the role from this trustee.  e.g. Everyone, "
            "uid:1000, gid:1001, sid:S-1-5-2-3-4, or auth_id:500")

    @staticmethod
    def main(conninfo, credentials, args):
        api_id = get_api_id_from_trustee(args.trustee)
        roles.remove_member(conninfo, credentials, args.role, **api_id)
