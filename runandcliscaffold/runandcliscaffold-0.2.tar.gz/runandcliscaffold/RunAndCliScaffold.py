import logging
import argparse
from abc import ABC, abstractmethod

"""
Core (abstract) Processing module for running a class's entry points in either CLI or Script calls

Defines the following methods:
    _defineFunctionsWithArgs() (abstract): allows the overriding class to define a custom list of appropriate functions
    and arguments available to be used
    run(): Processes a call made from either the console or script. Utilizes _defineFunctionsWithArgs function to define
     the relevant functions with the defined args in conjunction with argparse to determine the parameters provided by 
     the user/caller. Arguments are then passed to the requested function which maintains the logic in the inherited 
     class
"""


class RunAndCliScaffold(ABC):
    def __init__(self, label, loggingLvl=logging.DEBUG):
        self.label = label
        self.requestArgs = {}
        self.loggingLvl = loggingLvl

    @abstractmethod
    def _defineFunctionsWithArgs(self):
        pass

    def run(self, backend_args=None):
        # Define a parent parser for subparsers (this allows the subparsers to share input arguments)
        parser = argparse.ArgumentParser(description=self.label)
        subparsers = parser.add_subparsers()

        arg_defs = self._defineFunctionsWithArgs()

        for function in arg_defs:
            sub_parser = subparsers.add_parser(function.__name__)
            for arg in arg_defs[function]:
                sub_parser.add_argument('-' + str(arg['short']), '--' + str(arg['long']),
                                type=arg['type'],
                                help=arg.get('help', "No help available"),
                                required=arg.get('required', False),
                                default=arg.get('default', None))
            sub_parser.set_defaults(func=function)


        parsed_args = parser.parse_args(backend_args)

        try:
            return parsed_args.func(parsed_args)
        except AttributeError:
            parser.error("too few arguments")


