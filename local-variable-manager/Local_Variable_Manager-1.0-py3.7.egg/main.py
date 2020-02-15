# Build-In Modules
import argparse
import os

# Local Modules
import lvmanager.manager as manager

# Global Variables
ROOT = os.getenv("HOME")

def buildArgs():
    """
    Helper function to build our args

    :return: Args ready to be parsed!
    :rtype: argparser
    """
    usage = "CLI for managing and maintaining tokens and key/certs."
    argparser = argparse.ArgumentParser(usage=usage)
    argparser.add_argument(
        "-add",
        help="Adds a file to lcm [--name required]",
        nargs=1,
    )
    argparser.add_argument(
        "-delete",
        help="Delete a saved file [--name required]",
        nargs=1
    )
    argparser.add_argument(
        "-setenv",
        help="Expose a saved file as an environmental variable [--name required]",
        nargs=1,
    )
    argparser.add_argument(
        "-name",
        help="Name to be used",
        nargs=1,
    )
    argparser.add_argument(
        "-ls",
        help="Display what currently stored",
        action='store_true',
    )
    argparser.add_argument(
        "-cleanup",
        help="Clean up exposed keys",
        action='store_true',
    )
    argparser.add_argument(
        "-e",
        help="Use encryption for values when storing or setting the environment [LVMANAGER_PW is needed as an environmental variable]",
        action='store_true',
    )
    argparser.add_argument(
        "-getkey",
        help="Get a new encryption key",
        action='store_true',
    )
    return argparser

def parseArgs(args):
    """
    Helper function to parse our args

    :param argparser args: Args that have been provided by the user
    """
    if args.add:
        if not args.name:
            print("[Error] No -name provided!")
        elif not manager.add(args.add[0], args.name[0], args.e):
            print(f"[Error] Unable to add {args.name}")
        else:
            print(f"Successfully added: {args.name[0]}")
    elif args.delete:
        if manager.delete(args.delete[0]):
            print(f"Successfully deleted {args.delete[0]}")
        else:
            print(f"[Error] Unable to delete: {args.delete}")
    elif args.setenv:
        if args.name:
            name = args.name[0]
        else:
            name = ""
        if manager.setenv(args.setenv[0], name, args.e):
            print(f"Successfully copied to clipboard for: {name}")
        else:
            print(f"[Error] Unable to setenv: {name}")
    elif args.ls:
        if not manager.ls():
            print(f"[Error] Something went wrong :(")
    elif args.cleanup:
        if not manager.cleanup():
            print(f"[Error] Something went wrong :(")
    elif args.getkey:
        if not manager.generateKey():
            print(f"[Error] Something went wrong :(")

def main():
    """
    Main function to parse args and take action
    """
    # Build our a list of arguments and parse them
    args = buildArgs().parse_args()

    # Ensure needed folders exits [lvm, exposed]
    if not os.path.exists(f"{ROOT}/.lvm"):
        os.mkdir(f"{ROOT}/.lvm")
    if not os.path.exists(f"{ROOT}/.exposed"):
        os.mkdir(f"{ROOT}/.exposed")

    # Parse our args and take action
    parseArgs(args)
