from __future__ import print_function

import platform

from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.test.CloudmeshTest import CloudmeshTest


class TestCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_test(self, args, arguments):
        """
        ::

          Usage:
                test

          This command is intended to check if your windows set up is
          correctly done.

          Bugs:
              This program is supposed to be implemented. It is at this
              time just a template

          Description:

          Checks we do

             1. are you running python 3.8.1
             2. are you having the newest version of pip
             3. is cl installed
             4. is nmake installed
             5. is the username without spaces


          Checks that are missing or need implemented

             6. are you running in a vnenv
             7. is the default mongo port used
             8. do you have docker installed
             9. do you have vbox installed
            10. is hyperv switched on or off
            11. how much memory do you have
            12. do you have free diskspace
            13. are containers running
            14. .... other tyings that can help us debug your environment

        """

        tester = CloudmeshTest()

        #
        # Python setup
        #
        tester.check_venv()
        tester.check_command("python --version", test="3.8.1")
        tester.check_python()
        tester.check_command("pip --version", test="20.0.2")

        #
        # command tool setup
        #

        if platform.system() == "Windows":
            tester.check_command("cl")
            tester.check_command("nmake")
        tester.check_command("git --version", test="git version")
        tester.check_command("ssh", test="usage", show=False)
        tester.check_command("ssh-keygen --help", test="usage", show=False)

        tester.is_user_name_valid()
        tester.check_mongo()
        tester.check_command("docker --version", test="Docker version")
        tester.check_command("VirtualBox --help", test="Oracle VM VirtualBox VM Selector", show=False)

        tester.usage()
        tester.check_command("yamllint", test="usage: yamllint", show=False)
        tester.check_yaml()
        return ""
