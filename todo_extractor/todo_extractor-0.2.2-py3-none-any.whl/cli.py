"""CLI to the module."""
import argparse
import os

from .todo_extractor import search_todos


def main():
    """Main function for the cli, taking care of the user facing parts."""
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("folder", help="Folder to look for TODO notes", default=os.getcwd(), nargs="?")
    args = args_parser.parse_args()

    print(search_todos(args.folder))
