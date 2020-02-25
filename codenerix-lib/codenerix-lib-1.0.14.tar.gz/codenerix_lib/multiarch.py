#! /usr/bin/env python3

import subprocess
from codenerix_lib.debugger import Debugger


def multiarch_import(name, sufix=None, using=False):
    '''Dynamic import for multiarch libraries  to match the machine architecture'''

    # Initialize debugger
    d = Debugger()
    d.set_debug()
    d.set_name("Multiarch")

    # Detecte if sufix was given
    imported = None
    if sufix:
        # Use it as expected
        try:
            imported = __import__("{}{}".format(name, sufix))
            if using:
                d.debug("Using {}{}".format(name, sufix), color='cyan')
        except Exception as e:
            d.warning("I have tried to import the library '{}' as you requested using sufix '{} but I have failed to import {}{}, maybe you have forgotten to install the python library, I will try to import the default library!".format(name, sufix, name, sufix))

    elif sufix is not "":

        # No sufix was given, try to detect the architecture using 'gcc'
        whatismyarch = '''echo "`gcc -### -E - -march=native 2>&1 | sed -r '/cc1/!d;s/(")|(^.* - )//g' | sed -r 's# #\n#g' | grep march | cut -d "=" -f 2 || echo "Unknown"`"'''
        try:
            output = subprocess.check_output([whatismyarch]).decode()
            arch = output.split("\n")[0]
        except Exception as e:
            d.warning("I have tried to guess your machine architecture using 'gcc', but the command has failed, probably you don't have gcc installed?, I will try to import the default library! (Output was: {})".format(output))

        # We got an architecture
        if arch:

            # Try to import detected architecture
            try:
                imported = __import__("{}_{}".format(name, arch))
                if using:
                    d.debug("Using {}_{}".format(name, arch), color='cyan')
            except Exception as e:
                d.warning("I have guessed with 'gcc' that your architecture is '{}', but I have failed to import {}_{}, maybe you have forgotten to install the python library for your architecture, I will try to import the default library!".format(arch, name, arch))
        else:
            d.warning("I couldn't find your architecture with 'gcc', it will try to import the default library!")

    if not imported:
        # No architecture detected, try to import the base library!
        try:
            imported = __import__(name)
            if using:
                d.debug("Using {}".format(name), color='cyan')
        except Exception as e:
            d.debug("Error while import {}, maybe you have forgotten to install the python base library or your environment doesn't have it installed. This script is not able to find it!".format(name), color="red")
            raise

    return imported
