#!/usr/bin/env python3

"""
This script sets some symlinks inside the AsciiDoc3 package
installed via pip / pip3 from 'https://pypi.org/project/asciidoc3/'
with 'pip3 install --user asciidoc3'.
Run it immediately subsequently after install.
See https://asciidoc3.org/pypi.html for more information.
Do _not_ run as root/Admin - nothing happens.

Copyright (C) 2018-2019 by Berthold Gehrke <berthold.gehrke@gmail.com>
Free use of this software is granted under the terms of the
GNU General Public License Version 2 or higher (GNU GPLv2+).
"""

import os
import platform
import re
import shutil
import subprocess
import sys

USERHOMEDIR = os.path.expanduser("~")
# GNU/Linux: '/home/<username>', root: '/root'
# Windows: 'C:\Users\<username>', Admin: 'C:\Windows\system32'

def main():
    """
    runs "pip show asciidoc3" to locate AsciiDoc3's config-dirs and sets symlinks;
    at first within AsciiDoc3, then from the user's home directory to the data-files.
    This should work with POSIX and with Windows, too.
    """

    ad3_location = ''
    try:
        runpip = subprocess.Popen("pip show asciidoc3", shell=True, stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, universal_newlines=True, bufsize=-1)
        runpip.wait()
        pip_show_status = runpip.returncode
        if pip_show_status:
            sys.exit("FATAL: 'pip show asciidoc3' ends with non-zero exit code")
        output = runpip.communicate()
    except OSError:
        sys.exit("FATAL: 'pip show asciidoc3' ends with an unidentified error ...")
    if output:
        output = output[0]
        output = re.split(r'Location: ', output, re.DOTALL)[1]
        output = re.split(r'\nRequires', output, re.DOTALL)[0]
        ad3_location = output
        #  string 'ad3_location' looks like this:
        #  GNU/Linux '/home/<username>/.local/lib/python3.5/site-packages'
        #  Windows 'c:\users\<username>\appdata\roaming\python\python37\site-packages'
        #  Windows venv 'c:\users\<username>\<venv-dir>\lib\site-packages'
    else:
        sys.exit("FATAL: 'pip show asciidoc3' gives no information ...")

    ###############################
    ### POSIX (GNU/Linux, BSD, ...)
    ###############################
    if os.name == 'posix':
        if USERHOMEDIR.lower().startswith(r'/root'):
            sys.exit("Do not run as root! Script does nothing at all.")

        # AsciiDoc3 distribution, set internal (relative) symlinks.
        # <...>/asciidoc3/filters/music/images --> ../../images
        if os.path.exists(ad3_location +r"/asciidoc3/filters/music/images"):
            os.unlink(ad3_location +r"/asciidoc3/filters/music/images")
        os.symlink(os.path.relpath(
            ad3_location + r"/asciidoc3/images", ad3_location + r"/asciidoc3/filters/music"),
                   ad3_location + r"/asciidoc3/filters/music/images")

        # <...>/asciidoc3/filters/graphviz/images --> ../../images
        if os.path.exists(ad3_location + r"/asciidoc3/filters/graphviz/images"):
            os.unlink(ad3_location + r"/asciidoc3/filters/graphviz/images")
        os.symlink(os.path.relpath(
            ad3_location + r"/asciidoc3/images", ad3_location + r"/asciidoc3/graphviz/music"),
                   ad3_location + r"/asciidoc3/filters/graphviz/images")

        # <...>/asciidoc3/doc/images --> ../images
        if os.path.exists(ad3_location + r"/asciidoc3/doc/images"):
            os.unlink(ad3_location + r"/asciidoc3/doc/images")
        os.symlink(os.path.relpath(
            ad3_location + r"/asciidoc3/images", ad3_location + r"/asciidoc3/doc"),
                   ad3_location + r"/asciidoc3/doc/images")

        # Set symlinks users home to AsciiDoc3's 'working/config' directories
        # Skip if running as root.
        if USERHOMEDIR != r'/root':
            if os.path.exists(USERHOMEDIR + r"/.asciidoc3"):
                os.replace(USERHOMEDIR + r"/.asciidoc3", USERHOMEDIR + r"/.asciidoc3_backup")
            os.symlink(ad3_location + r"/asciidoc3", USERHOMEDIR + r"/.asciidoc3")

            if os.path.exists(USERHOMEDIR + r"/asciidoc3"):
                os.replace(USERHOMEDIR + r"/asciidoc3", USERHOMEDIR + r"/asciidoc3_backup")
            os.symlink(ad3_location + r"/asciidoc3", USERHOMEDIR + r"/asciidoc3")

    ###############################
    ### Windows (Win7, Win8, Win10)
    ###############################
    elif platform.system().lower().startswith(r"win"):
        if USERHOMEDIR.lower().startswith(r'c:\win'):
            sys.exit("Do not run as ADMIN! Script does nothing at all.")

        # not using venv -> ad3_location looks like
        # 'c:\users\<username>\appdata\roaming\python\python37\site-packages'
        if ad3_location.count(r'appdata'):
            # we need modules in dir 'Scripts', that means sources without trailing '.py'
            shutil.copy(ad3_location[:-13]+r"Scripts\asciidoc3.exe", \
                        ad3_location[:-13]+r"Scripts\asciidoc3")
            shutil.copy(ad3_location[:-13]+r"Scripts\a2x3.exe", \
                        ad3_location[:-13]+r"Scripts\a2x3")

            # AsciiDoc3 distribution, set internal symlinks.
            # <...>/asciidoc3/filters/music/images --> ../../images
            if os.path.exists(ad3_location + r"\asciidoc3\filters\music\images"):
                os.unlink(ad3_location + r"\asciidoc3\filters\music\images")
            os.system(r"mklink /J "+ad3_location+r"\asciidoc3\filters\music\images "+ad3_location+r"\asciidoc3\images")

            # <...>/asciidoc3/filters/graphviz/images --> ../../images
            if os.path.exists(ad3_location + r"\asciidoc3\filters\graphviz\images"):
                os.unlink(ad3_location + r"\asciidoc3\filters\graphviz\images")
            os.system(r"mklink /J "+ad3_location+r"\asciidoc3\filters\graphviz\images "+ad3_location+r"\asciidoc3\images")

            # <...>/asciidoc3/doc/images --> ../images
            if os.path.exists(ad3_location + r"\asciidoc3\doc\images"):
                os.unlink(ad3_location + r"\asciidoc3\doc\images")
            os.system(r"mklink /J "+ad3_location+r"\asciidoc3\doc\images "+ad3_location+r"\asciidoc3\images")

            # make symlink for convenient use
            if os.path.exists(USERHOMEDIR + r"\asciidoc3"):
                if os.path.exists(USERHOMEDIR + r"\asciidoc3_backup"):
                    shutil.rmtree(USERHOMEDIR + r"\asciidoc3_backup")
                os.replace(USERHOMEDIR + r"\asciidoc3", USERHOMEDIR + r"\asciidoc3_backup")
            os.system(r"mklink /J "+USERHOMEDIR+r"\asciidoc3 "+ad3_location+r"\asciidoc3")

            # make symlink \.asciidoc3: mandatory since AsciiDoc3 looks here for config-files
            if os.path.exists(USERHOMEDIR + r"\.asciidoc3"):
                shutil.rmtree(USERHOMEDIR + r"\.asciidoc3")
            os.system(r"mklink /J "+USERHOMEDIR+r"\.asciidoc3 "+ad3_location+r"\asciidoc3")

            # we don't need this folder any more
            if os.path.exists(ad3_location[:-22]+r"asciidoc3"):
                shutil.rmtree(ad3_location[:-22]+r"asciidoc3")

        # using venv -> ad3_location looks like
        # 'c:\users\username\ad3\lib\site-packages'
        elif 'lib' in ad3_location.lower():
            # delete dir 'python3x\site-packages\asciidoc3'
            for folder in os.listdir(ad3_location[:-17]):
                if folder.lower().startswith('python3'):
                    if os.path.exists(ad3_location[:-17]+folder+r'\site-packages\asciidoc3'):
                        shutil.rmtree(ad3_location[:-17]+folder+r'\site-packages\asciidoc3')
                        if len(list(os.listdir(ad3_location[:-17]+folder))) == 1:
                            shutil.rmtree(ad3_location[:-17]+folder+r'\site-packages')
                            shutil.rmtree(ad3_location[:-17]+folder)

            # we need modules in dir 'Scripts', that means sources without trailing '.py'
            shutil.copy(ad3_location[:-17]+r"Scripts\asciidoc3.exe", \
                        ad3_location[:-17]+r"Scripts\asciidoc3")
            shutil.copy(ad3_location[:-17]+r"Scripts\a2x3.exe", \
                        ad3_location[:-17]+r"Scripts\a2x3")

            # AsciiDoc3 distribution, set internal symlinks.
            # <...>/asciidoc3/filters/music/images --> ../../images
            if os.path.exists(ad3_location[:-17] + r"\asciidoc3\filters\music\images"):
                os.unlink(ad3_location[:-17] + r"\asciidoc3\filters\music\images")
            os.system(r"mklink /J "+ad3_location[:-17]+r"\asciidoc3\filters\music\images "+ad3_location[:-17]+r"\asciidoc3\images")

            # <...>/asciidoc3/filters/graphviz/images --> ../../images
            if os.path.exists(ad3_location[:-17] + r"\asciidoc3\filters\graphviz\images"):
                os.unlink(ad3_location[:-17] + r"\asciidoc3\filters\graphviz\images")
            os.system(r"mklink /J "+ad3_location[:-17]+r"\asciidoc3\filters\graphviz\images "+ad3_location[:-17]+r"\asciidoc3\images")

            # <...>/asciidoc3/doc/images --> ../images
            if os.path.exists(ad3_location[:-17] + r"\asciidoc3\doc\images"):
                os.unlink(ad3_location[:-17] + r"\asciidoc3\doc\images")
            os.system(r"mklink /J "+ad3_location[:-17]+r"\asciidoc3\doc\images "+ad3_location[:-17]+r"\asciidoc3\images")

            # move folder asciidoc3 to apropriate location
            shutil.move(ad3_location[:-17] + r"\asciidoc3", ad3_location + r"\asciidoc3")

            # make symlink <venv>\asciidoc3
            os.system(r"mklink /J "+ad3_location[:-17] + r"\asciidoc3 "+ad3_location+r"\asciidoc3")

            # make copy <venv>\Scripts python - python3
            if not os.path.exists(ad3_location[:-17] + r"Scripts\python3.exe"):
                os.system(r"copy /Y "+ad3_location[:-17] + r"Scripts\python.exe "+ad3_location[:-17]+r"Scripts\python3.exe")

            # make symlink \.asciidoc3: mandatory since AsciiDoc3 looks here for config-files
            if os.path.exists(USERHOMEDIR + r"\.asciidoc3"):
                shutil.rmtree(USERHOMEDIR + r"\.asciidoc3")
            os.system(r"mklink /J "+USERHOMEDIR+r"\.asciidoc3 "+ad3_location+r"\asciidoc3")

    ###############################
    ### neither POSIX or Windows
    ###############################
    else:
        sys.exit("Your OS was not included in this script: you are on your own to handle symlinks ...")

if __name__ == '__main__':
    main()
