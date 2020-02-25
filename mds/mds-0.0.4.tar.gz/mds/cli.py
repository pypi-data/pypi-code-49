import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Markdown Genie Command Line Options")
    parser.add_argument("notepath", nargs="?", default="./", help="Path to notes. Default is relative.")
    parser.add_argument("--host", default='localhost', help="Host")
    return parser

parser = create_parser()
args = parser.parse_args()
