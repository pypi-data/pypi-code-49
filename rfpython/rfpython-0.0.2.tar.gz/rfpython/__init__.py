from .__about__ import __author__, __author_email__, __version__, __website__

import subprocess
import os
import argparse


def dir_logic(pyfile):
    dirname = os.path.dirname(pyfile)
    if dirname:
        base_dir = os.getcwd()
        full_path = os.path.join(base_dir, dirname)
        cmd = "import sys; sys.path.append('{0}'); ".format(full_path)
    else:
        cmd = ""
    return cmd


def run(pyfile, function):

    cmd = dir_logic(pyfile)
    base_file_name = os.path.basename(pyfile).split(".")[0]

    command = cmd + "import {0}; {0}.{1}()".format(base_file_name, function)

    subprocess.call(["python", "-c", command])


def main():

    parser = argparse.ArgumentParser(description="Videos to images")
    parser.add_argument("pyfile", type=str, help="Python file")
    parser.add_argument("function", type=str, help="Python function")
    args = parser.parse_args()

    run(args.pyfile, args.function)

    return


__all__ = [
    "__version__",
    "__author__",
    "__author_email__",
    "__website__",
    "main",
]
