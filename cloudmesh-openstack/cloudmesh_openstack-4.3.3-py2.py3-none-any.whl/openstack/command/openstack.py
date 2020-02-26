from __future__ import print_function

from cloudmesh.common.console import Console
from cloudmesh.common.variables import Variables
from cloudmesh.configuration.Config import Config
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.common.Printer import Printer

class OpenstackCommand(PluginCommand):
    # noinspection PyUnusedLocal
    @command
    def do_openstack(self, args, arguments):
        """
        ::

          Usage:
                openstack list [--details]
                openstack [CLOUD] [--details]

          This command does some useful things.

          Arguments:
              CLOUD   name of the cloud

          Description:
              Prints the configuration file specification of openstack clouds
              If details is specified it also prints the secrets, so please do
              use it carefully

              openstack list [--details]
              openstack [CLOUD]

              NOTE: this command will be replaced with

              cms config list --kind=openstack --details
              cms config CLOUD --details

              The command is temporarily introduced for testing purposes
        """

        variables = Variables()
        cloud = arguments.CLOUD or variables["cloud"]
        config = Config()

        # noinspection PyPep8Naming
        def Print(entry):
            place = {
                "cloudmesh": {
                    "cloud": entry
                }
            }
            print(
                Config.cat_dict(place,
                                mask_secrets=not arguments["--details"]))

        def list_openstack_entries():
            clouds = config[f"cloudmesh.cloud"]
            for key, entry in clouds.items():
                if entry["cm"]["kind"] == 'openstack':
                    Print(entry)

        if arguments.list:
            images = list_openstack_entries()



        elif cloud:
            entry = config[f"cloudmesh.cloud.{cloud}"]
            if entry["cm"]["kind"] == "openstack":
                Print(entry)
            else:
                Console.error("The cloud {cloud} is not registered "
                              "as an openstack cloud")
                return ""

        else:
            list_openstack_entries()

        return ""
