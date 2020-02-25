"""
 Usage:
     ttmr current
     ttmr start
     ttmr stop
     ttmr view
     ttmr summary (--day|--week)
     ttmr weekly
     ttmr new  OBJTYPE
     ttmr list OBJTYPE [--inactive]

 Options:
   -h --help     Show this screen.
   --version     Show version.

"""
import codecs

import colorama

import ttmr.config as config
from ttmr.console import GREEN
from ttmr.console import RED
from ttmr.console import Console
from ttmr.util import replace_bad_char
from . import commands

__author__ = "Mark Gemmill"
__email__ = "mark@markgemmill.com"
__version__ = "0.5.3-alpha"


colorama.init()

codecs.register_error("ttmr", replace_bad_char)


def main_wrapper(func):
    def _wrapper_():
        try:
            title = f" Task Timer v{__version__}"
            underline = '-' * (len(title) - 1)
            Console.init()
            Console.newline()
            Console.write(GREEN)
            Console.write(title)
            Console.newline()
            Console.write(f" {underline}")
            Console.clear_formating()
            Console.newline()
            Console.cursor_up()

            func()

            Console.newline()

        except KeyboardInterrupt:
            Console.clear_formating()
            Console.newline()
            Console.newline()
            Console.write(RED)
            Console.writeline("*** Task has been canceled. ***")
            Console.clear_formating()
            Console.newline()

    return _wrapper_


@main_wrapper
def main():
    import docopt

    conf = config.get_config()
    args = docopt.docopt(__doc__, version="")
    conf.cli_args = args

    Console.newline()

    if args["stop"]:
        commands.stop_time_entry(conf)
    elif args["start"]:
        commands.start_time_entry(conf)
    elif args["current"]:
        commands.show_current_entry(conf)
    elif args["summary"] and args["--day"]:
        commands.day_summary(conf)
    elif args["summary"] and args["--week"]:
        commands.weekly_summary(conf)
    elif args["weekly"]:
        #  cmd.weekly_summary(conf)
        commands.list_current_weeks_entries(conf)
    elif args["view"]:
        #  cmd.view(conf)
        pass
    #  elif args["load"]:
    #  cmd.load(conf)
    #  pass
    #  elif args["config"]:
    #  cmd.display_config(conf)
    #  pass
    #  elif args["edit"] and args["OBJTYPE"] == "ent":
    #  cmd.edit_entry(conf)
    #  pass
    elif args["new"] and args["OBJTYPE"] in ("cat", "category"):
        commands.new_category(conf)
    elif args["list"] and args["OBJTYPE"] in ("cat", "category"):
        commands.list_categories(conf)
    elif args["new"] and args["OBJTYPE"] in (
        "prj",
        "proj",
        "inc",
        "project",
        "incident",
    ):
        commands.new_project(conf)
    elif args["list"] and args["OBJTYPE"] in (
        "prj",
        "proj",
        "inc",
        "project",
        "incident",
    ):
        commands.list_projects(conf)
    elif args["list"] and args["OBJTYPE"] in ("ent", "entry"):
        commands.list_entries(conf)
    #  elif args["start"] and args["day"]:
    #      commands.start_day(conf)
    else:
        print("Unknown command: could not complete your request.")
