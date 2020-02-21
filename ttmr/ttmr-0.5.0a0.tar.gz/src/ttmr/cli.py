"""
 Usage:
     ttmr
     ttmr current
     ttmr stop
     ttmr view
     ttmr summary
     ttmr weekly
     ttmr edit OBJTYPE [--curr-obj]
     ttmr new  OBJTYPE
     ttmr list OBJTYPE [--inactive]
     ttmr load
     ttmr config

 Options:
   -h --help     Show this screen.
   --version     Show version.

"""
import codecs
import colorama
import ttmr.config as config
import ttmr.cmd as cmd
from . import commands
from ttmr.console import Console, GREEN, RED
from ttmr.util import replace_bad_char


__author__ = "Mark Gemmill"
__email__ = "mark@markgemmill.com"
__version__ = "0.5.0-alpha"


colorama.init()

codecs.register_error("ttmr", replace_bad_char)


def main_wrapper(func):
    def _wrapper_():
        try:
            Console.init()
            Console.newline()
            Console.write(GREEN)
            Console.write(" Task Timer v{}".format(__version__))
            Console.newline()
            Console.write(" -----------------")
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
        cmd.stop_entry(conf)
    elif args["current"]:
        cmd.show_current_entry(conf)
    elif args["summary"]:
        cmd.summary(conf)
    elif args["weekly"]:
        cmd.weekly_summary(conf)
    elif args["view"]:
        cmd.view(conf)
    elif args["load"]:
        cmd.load(conf)
    elif args["config"]:
        cmd.display_config(conf)
    elif args["edit"] and args["OBJTYPE"] == "ent":
        cmd.edit_entry(conf)
    elif args["new"] and args["OBJTYPE"] in ("cat", "category"):
        commands.new_category(conf)
    elif args["list"] and args["OBJTYPE"] in ("cat", "category"):
        commands.list_categories(conf)
    elif args["new"] and args["OBJTYPE"] in ("prj", "proj", "inc", "project", "incident"):
        commands.new_project(conf)
    elif args["list"] and args["OBJTYPE"] in ("prj", "proj", "inc", "project", "incident"):
        commands.list_projects(conf)
    elif args["list"] and args["OBJTYPE"] in ("ent", "entry"):
        commands.list_entries(conf)
    else:
        commands.time_entry(conf)
