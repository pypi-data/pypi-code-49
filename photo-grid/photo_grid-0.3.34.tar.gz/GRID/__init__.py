__author__ = "Chunpeng James Chen"
__version__ = "0.3.33"
__update__ = "Feb 20, 2020"

# imports
import subprocess
import json
import sys
from urllib import request
from pkg_resources import parse_version


# welcome message
print("~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~")
print("                 Welcome to GRID Ver.%s    " % __version__)
print("~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~")
print("Author      : James Chen <chun-peng.chen@wsu.edu>    " )
print("Last update : %s              " % __update__)

if "-m" not in sys.argv[0]:
    # if in the command-line environment
    print("    Try 'python -m grid' in Terminel to launch GRID GUI,")
    print("         as command-line version is not ready yet.")
print("~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~")


# self update
url = 'https://pypi.python.org/pypi/photo_grid/json'
releases = json.loads(request.urlopen(url).read())['releases']
new_version = sorted(releases, key=parse_version, reverse=True)[0]
if __version__ != new_version:
    # Dialog
    ans = None
    bol_ans = None
    possible_pos_ans = ["y", "Y", "yes"]
    possible_neg_ans = ["n", "N", "no"]

    while bol_ans is None:
        ans = input(
            "A newer version of GRID (ver. %s) is now available, upgrade? (y/n) " % new_version)
        if ans in possible_pos_ans:
            bol_ans = True
        elif ans in possible_neg_ans:
            bol_ans = False

    if bol_ans:
        subprocess.check_call([sys.executable,
                              '-m', 'pip', 'install',
                               'photo_grid==%s' % new_version, '--upgrade'])
        print("\n")
        print("~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~")
        print("          Please re-launch GRID to finish the update")
        print("~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~*~~~~~~~~~")
        print("\n")
        quit()


# self imports
from .grid import *


"""
Update Log

- Feb 20, 2020 (0.3.0)
    * Support different display modes in the center detection step
    * Support auto-update feature
    * Bug fixes

- Oct 29, 2019 (0.2.0)
    * Add progress bars
    * Enhance the support for low resolution monitors
    * Improve UI

- Oct 22, 2019 (0.1.3)
    * Optimize default setting of refining parameters
    * Fix wrong angle detection
    * Minor bug fixes

- Oct 19, 2019 (0.1.2)
    * Support rhombus field layout
    * Bug fixes

- Sep 17, 2019 (0.0.16)
    * Improve memory efficiency on Windows OS

- Sep 12, 2019 (0.0.15)
    * Fix problems wiht fixed segmentation
    * Organize file structure
    * Add dark mode
"""
