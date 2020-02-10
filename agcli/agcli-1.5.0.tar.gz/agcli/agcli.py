"""
AGCLI.

Usage:
  agcli [--empty] [--parsers=<names>] [--config-dir=<dir>] [--complete=<instr>] <cmd>
  agcli [--empty] [--parsers=<names>] [--config-dir=<dir>] [--complete=<instr>] <cmd> <sub-cmd>
  agcli (-h | --help)
  agcli (-v | --version)


Options:
  -h --help             Show this screen.
  -v --version          Show the version of the command.
  --empty               Don't look command documentation and generate empty interface.
  --parsers=<names>     The name of the parsers to use in order to analyze the documentation.
                        The possible values are 'explainshell' and 'docopt' [default: "naive, docopt, explainshell"].
  --config-dir=<dir>    The directory where the "agcli" package is installed. By default, this is the user directory.
  -c, --complete=<instr>    Parse the "instr" instruction in order to fill the GUI.
"""

from .interface import interface_generator
from .template import template_generator, cli_parser
from .docparser import new_docopt
from .utils.file_handler import FileHandler
from .gui.main_window import MainWindow
from .gui.command_notebook import instance as cmd_notebook
from .template.template_generator import DefaultGenerator
from pathlib import Path

__version__ = 'agcli version 1.5.0'

def cli():
    arguments = new_docopt.docopt(__doc__, version=__version__)
    if arguments['<sub-cmd>'] is None:
        cmd = arguments['<cmd>']
    else:
        cmd = '{} {}'.format(arguments['<cmd>'], arguments['<sub-cmd>'])
    config_dir = Path.home()
    if arguments['--config-dir'] is not None:
        config_dir =  arguments['--config-dir']
    FileHandler(cmd, config_dir)

    inter_generator = interface_generator.InterfaceGenerator(cmd)
    inter_generator.generate_interface(arguments['--empty'], arguments['--parsers'])

    temp_generator = template_generator.DefaultGenerator()
    temp_generator.generate_default_template()

    main_window = MainWindow(cmd)
    if arguments["--complete"] is not None:
        parser = cli_parser.CLIParser(cmd, arguments["--complete"])
        terminal_parameters = parser.parse()
        complete_template = DefaultGenerator().generate_complete_template(terminal_parameters)
        main_window.command_tab.fill_template(complete_template)
    main_window.start_GUI()

if __name__ == '__main__':
    cli()
