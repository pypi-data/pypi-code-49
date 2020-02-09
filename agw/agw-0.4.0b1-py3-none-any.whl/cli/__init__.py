"""
Usage:
    agw cursor [--prompt-for-name=<int>][--pause=<int>]
    agw jiggle
    agw screenshot (--capture | --find)

Options:
    --prompt-for-name=<int>  Prompt for position name after x seconds. [default: 0]
    --pause=<int>            Length in seconds between recording cursor position. [default: 1]
    --capture                Capture a screen shot.
    --find                   Find position of screen shot image.
    -h --help                Display this screen.
    --version                Display application version.
"""
import docopt
from .cursor import position as cursor
from .jiggler import jiggle
from .screen import capture, find


def main():
    args = docopt.docopt(__doc__)

    if args.get("cursor") is True:
        cursor(
            prompt_for_name=args.get("--prompt-for-name", 0),
            pause_time=args.get("--pause", 1),
        )
    elif args.get("jiggle") is True:
        jiggle()
    elif args.get("screenshot") is True and args.get("--capture"):
        capture()
    elif args.get("screenshot") is True and args.get("--find"):
        find()
