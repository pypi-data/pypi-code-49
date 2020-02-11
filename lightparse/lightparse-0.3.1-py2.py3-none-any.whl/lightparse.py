"""
Lightweight argument parser to make defining argument parser more compact and
nicer to write for short and quickly written scripts.
"""
from __future__ import print_function

import sys
import copy


class PreParseException(Exception):
    """
    Exception from setting up the parser, before even getting to the parsing
    phase.
    """
    pass


class ParserException(Exception):
    """
    Parsing specific exception.
    """
    def __init__(self, message, args):
        Exception.__init__(self, message)
        self.parsed_args = args


class Args(object):
    """
    Storage class to store parsed arguments.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Parser(object):
    """
    Argument parser.
    """
    class Behaviour(object):
        """
        Class to define and tune the behaviour of the parser.
        """
        def __init__(self,
                mutable=True,
                auto_help_on_empty=False,
                combine_flags=True,
                raise_on_invalid_description=True,
                variable_arguments=False):
            self.auto_help_on_empty = auto_help_on_empty
            self.combine_flags = combine_flags
            self.raise_on_invalid_description = raise_on_invalid_description
            # if setting to immutable, this needs to be the last line
            self.mutable = mutable
            self.variable_arguments = variable_arguments

        def __setattr__(self, attr, value):
            if hasattr(self, "mutable") and not self.mutable:
                raise PreParseException("Trying to redefine behaviour from"
                        " immutable Behaviour object: {}".format(attr))
            object.__setattr__(self, attr, value)

    def __init__(self, behaviour=None, parent=None):
        self.positional = []
        self.optional = {}
        self.flags = {"-h": "help"}
        self.description = ""
        self.field_descriptions = {}
        self.mappers = {}
        if behaviour:
            self.behaviour = behaviour
        elif parent and parent.behaviour:
            self.behaviour = parent.behaviour
        else:
            self.behaviour = Parser.Behaviour()
        if parent:
            self.pos(parent.positional)
            self.opt(parent.optional)
            self.fla(parent.flags)
            self.map(parent.mappers)
            self.describe("",
                    {k:v
                    for k, v in parent.field_descriptions.items()
                    if k not in parent.subcommands})


    def _check_behaviour_conflict_combine_flags(self):
        if any(x.startswith("-")
                    and not x.startswith("--")
                    and len(x) > 2
                for x in list(self.optional) + list(self.flags)):
            self.behaviour.combine_flags = False

    def _check_behaviour_auto_help_on_empty(self):
        if self.positional:
            self.behaviour.auto_help_on_empty = True

    def _validate_behaviour_raise_on_invalid_description(self):
        if self.behaviour.raise_on_invalid_description and any(
                x not in self.positional
                    and x not in self.optional.values()
                    and x not in self.flags.values()
                for x in self.field_descriptions.keys()):
            raise PreParseException("Description for non-existent options: {}"
                    .format(", ".join(
                        x for x in self.field_descriptions.keys()
                            if x not in self.positional
                            and x not in self.optional.values()
                            and x not in self.flags.values())))

    def pos(self, *args):
        """
        Sets names of positional arguments. Takes the names as strings into
        argument list.
        """
        self.positional.extend(args)
        self._check_behaviour_auto_help_on_empty()
        return self

    def opt(self, key2var):
        """
        Sets triggers and variable names of optional arguments. Takes a
        dictionary from trigger to variable name. Cannot share trigger with
        flag. Optional arguments take exactly one string as input.
        """
        self.optional.update(key2var)
        self._check_behaviour_conflict_combine_flags()
        return self

    def fla(self, key2var):
        """
        Sets triggers and variable names of flags. Takes a dictionary from
        trigger to variable name. Cannot share trigger with optional argument.
        Flags take no input.
        """
        self.flags.update(key2var)
        self._check_behaviour_conflict_combine_flags()
        return self

    def map(self, var2mapper):
        """
        Sets mappers for parsed argument values. If a mapper throws ValueError,
        parsing will fail and print which argument failed and what was the
        ValueError message for the failure.
        """
        self.mappers.update(var2mapper)
        return self

    def _parse_raw(self, source=None):
        """
        Parses the source argument list into Args storage class object based on
        defined rules. Throws an exception on failure.
        """
        if source is None:
            source = sys.argv[1:]
        if self.behaviour.variable_arguments and not self.positional:
            raise ParserException("At least one positional argument needs to be"
                    " defined with variable arguments behaviour.")
        ## Parse the arguments
        argdict = {}
        position = 0
        reading_optional = None
        potential_misflags = []
        if self.behaviour.variable_arguments:
            argdict[self.positional[-1]] = []
        for token in source:
            if reading_optional is not None:
                argdict[reading_optional] = token
                reading_optional = None
            elif token in self.optional:
                reading_optional = self.optional[token]
            elif token in self.flags:
                argdict[self.flags[token]] = True
            elif self.behaviour.combine_flags\
                    and token.startswith("-")\
                    and not token.startswith("--"):
                # Handle combined flags.
                for letter in token[1:]:
                    subtoken = "-" + letter
                    if reading_optional is not None:
                        raise ParserException("Multiple argument taking"
                                " options in a single combined flag: {}"
                                .format(token), Args())
                    elif subtoken in self.optional:
                        reading_optional = self.optional[subtoken]
                    elif subtoken in self.flags:
                        argdict[self.flags[subtoken]] = True
                    else:
                        raise ParserException("Unknown flag: {}".format(
                                subtoken), Args())
            else:
                if token.startswith("-"):
                    potential_misflags.append(token)
                if position >= len(self.positional) - 1 \
                        and self.behaviour.variable_arguments:
                    argdict[self.positional[-1]].append(token)
                    position = len(self.positional)
                elif position < len(self.positional):
                    argdict[self.positional[position]] = token
                    position += 1
                else:
                    position += 1
        ## Fill missing values
        self.handle_modify_argdict(argdict)
        for var in self.optional.values():
            if var not in argdict:
                argdict[var] = None
        for var in self.flags.values():
            if var not in argdict:
                argdict[var] = False
        ## Validate the result
        args = Args(**argdict)
        if reading_optional is not None:
            raise ParserException(
                    "Arguments ended before finishing read of {}"
                            .format(reading_optional),
                    args)
        if position < len(self.positional):
            raise ParserException("Too few positional arguments", args)
        if position > len(self.positional):
            if potential_misflags:
                raise ParserException(
                        "Too many positional arguments, unknown flags:"
                        " {}".format(", ".join(potential_misflags)),
                        args)
            else:
                raise ParserException("Too many positional arguments", args)
        ## Map the values through mappers if any defined.
        for key, value in argdict.items():
            if value is not None and key in self.mappers:
                try:
                    if self.behaviour.variable_arguments and key == self.positional[-1]:
                        newlist = []
                        for item in value:
                            newlist.append(self.mappers[key](item))
                        argdict[key] = newlist
                    else:
                        argdict[key] = self.mappers[key](value)
                except ValueError as e:
                    reverse_opt = {v: k for k, v in self.optional.items()}
                    reverse_fla = {v: k for k, v in self.flags.items()}
                    if key in reverse_opt:
                        key = reverse_opt[key]
                    elif key in reverse_fla:
                        key = reverse_fla[key]
                    raise ParserException(
                            "Invalid value for '{}': {}".format(key, e.message),
                            args)
                    raise ParserException("Cannot parse argument as {}: {}"
                            .format(self.mappers[key].__name__, value), args)
        # Recreate the Args object after mapping
        args = Args(**argdict)
        ## Return
        return args

    def handle_modify_argdict(self, argdict):
        """
        Handles special changes to collected argument dictionary before
        converting to Args object.
        """
        if not argdict and self.positional\
                and self.behaviour.auto_help_on_empty:
            argdict["help"] = True

    def _handle_postparse(self, args):
        """
        Handles special case flags, which should execute and exit even when the
        arguments were otherwise invalid.
        """
        if hasattr(args, "help") and args.help:
            self.help()
            self.exit(0)

    def parse(self, source=None):
        """
        Parses the source argument list into Args storage class object based on
        defined rules. Prints an error and exits on failure.
        """
        try:
            args = self._parse_raw(source)
            self._handle_postparse(args)
            return args
        except ParserException as e:
            self._handle_postparse(e.parsed_args)
            print("Error: {}".format(e.args[0]))
            self.exit(1)

    def describe(self, main_description, field_descriptions):
        """
        Provides a descriptions to print in the help for the program and for
        each field.
        """
        self.description = main_description
        self.field_descriptions = field_descriptions
        self._validate_behaviour_raise_on_invalid_description()
        return self

    def help(self):
        """
        Prints usage help.
        """
        def rewidth(text, left, right):
            """
            Reformats the paragraphs from given text to be positioned between left
            and right character columns.
            """
            lines = []
            words = text.split()
            while words:
                word = words.pop(0)
                if not lines or len(lines[-1]) + len(word) + 1 > right:
                    lines.append(" " * left + word)
                else:
                    lines[-1] += " " + word
            return "\n".join(lines)

        def rewidth_argument_description(text, keylen):
            """
            Reformats the argument description in help to be between correct
            character columns.
            """
            if keylen < 30:
                return rewidth(description, keylen + 6, 80).lstrip()
            else:
                return "\n" + rewidth(description, 12, 80)

        def vartype(var):
            if var in self.mappers:
                return self.mappers[var].__name__
            return "str"

        def format_positional_usage(i):
            if i == len(self.positional) -1 and \
                    self.behaviour.variable_arguments:
                return "<{}...>".format(self.positional[i])
            return "<{}>".format(self.positional[i])
        print("usage: {} [options] {}".format(
                sys.argv[0],
                " ".join(format_positional_usage(i)
                    for i in range(len(self.positional)))))
        print("")
        if self.description:
            for paragraph in self.description.split("\n\n"):
                print(rewidth(paragraph, 0, 80))
                print("")
        keylen = max(
                [len(key) + len(vartype(var)) + 3
                    for key, var in self.optional.items()]
                + [len(key) for key in self.flags.keys()]
                + [len(var) + len(vartype(var)) + 3
                    for var in self.positional]
                + [1])
        if any(x in self.field_descriptions for x in self.positional):
            print("Positional arguments:")
            for variable in self.positional:
                description = self.field_descriptions.get(variable, variable)
                description = rewidth_argument_description(description, keylen)
                print("    {}  {}".format(
                    "<{}:{}>".format(variable, vartype(variable)).ljust(keylen),
                    description))
            print("")
        print("Optional arguments:")
        for key, variable in sorted(self.optional.items()):
            description = self.field_descriptions.get(variable, variable)
            description = rewidth_argument_description(description, keylen)
            print("    {}  {}".format(
                "{} <{}>".format(key, vartype(variable)).ljust(keylen),
                description))
        print("")
        print("Optional flags:")
        for key, variable in sorted(self.flags.items()):
            description = self.field_descriptions.get(variable, variable)
            description = rewidth_argument_description(description, keylen)
            print("    {}  {}".format(
                key.ljust(keylen),
                description))

    def exit(self, code):
        sys.exit(code)


class SubcommandParser(Parser):
    """
    Parser for splitting by subcommand.
    """
    def __init__(self, behaviour=None):
        self.positional = []
        self.optional = {}
        self.flags = {"-h": "help"}
        self.description = ""
        self.field_descriptions = {}
        self.mappers = {}
        if behaviour:
            self.behaviour = behaviour
        else:
            self.behaviour = Parser.Behaviour()
            self.behaviour.auto_help_on_empty = True
        self.subcommands = {}

    def _validate_behaviour_raise_on_invalid_description(self):
        if self.behaviour.raise_on_invalid_description and any(
                x not in self.subcommands
                    and x not in self.positional
                    and x not in self.optional.values()
                    and x not in self.flags.values()
                for x in self.field_descriptions.keys()):
            raise PreParseException("Description for non-existent options: {}"
                    .format(", ".join(
                        x for x in self.field_descriptions.keys()
                            if x not in self.subcommands
                            and x not in self.positional
                            and x not in self.optional.values()
                            and x not in self.flags.values())))

    def sub(self, key2parser):
        """
        Registers sub parsers with corresponding subcommands.
        """
        self.subcommands.update(key2parser)
        return self

    def pos(self, *args):
        """
        Calls pos for all subcommands and registers the positional arguments
        for listing as common arguments in help.
        """
        for parser in self.subcommands.values():
            parser.pos(*args)
        self.positional.extend(args)
        return self

    def opt(self, key2var):
        """
        Calls opt for all subcommands and registers the optional arguments
        for listing as common arguments in help.
        """
        for parser in self.subcommands.values():
            parser.opt(key2var)
        self.optional.update(key2var)
        return self

    def fla(self, key2var):
        """
        Calls fla for all subcommands and registers the flags for listing as
        common arguments in help.
        """
        for parser in self.subcommands.values():
            parser.fla(key2var)
        self.flags.update(key2var)
        return self

    def map(self, var2mapper):
        """
        Calls map for all subcommands and registers the mappings for displaying
        in help.
        """
        for parser in self.subcommands.values():
            parser.map(var2mapper)
        self.mappers.update(var2mapper)
        return self

    def parse(self, source=None):
        """
        Parses the source argument list into Args storage class object based on
        defined rules. Prints an error and exits on failure.
        """
        if len(self.subcommands) == 0:
            raise PreParseException(
                    "No subcommands defined for subcommand parser")
        if source is None:
            source = sys.argv[1:]
        if len(source) == 0:
            if self.behaviour.auto_help_on_empty:
                self.help()
                self.exit(0)
            print("Error: no subcommand provided, run with -h for help")
            self.exit(3)
        command = source[0]
        rest = source[1:]
        if command == "-h":
            self.help()
            self.exit(0)
        if command not in self.subcommands:
            print("Error: unknown subcommand: '{}'".format(command))
            self.exit(2)
        parser = self.subcommands[command]
        args = parser.parse(rest)
        return command, args


    def help(self):
        """
        Prints usage help.
        """
        def rewidth(text, left, right):
            """
            Reformats the paragraphs from given text to be positioned between left
            and right character columns.
            """
            lines = []
            words = text.split()
            while words:
                word = words.pop(0)
                if not lines or len(lines[-1]) + len(word) + 1 > right:
                    lines.append(" " * left + word)
                else:
                    lines[-1] += " " + word
            return "\n".join(lines)

        def rewidth_argument_description(text, keylen):
            """
            Reformats the argument description in help to be between correct
            character columns.
            """
            if keylen < 30:
                return rewidth(description, keylen + 6, 80).lstrip()
            else:
                return "\n" + rewidth(description, 12, 80)

        def vartype(var):
            if var in self.mappers:
                return self.mappers[var].__name__
            return "str"

        def format_positional_usage(i):
            if i == len(self.positional) -1 and \
                    self.behaviour.variable_arguments:
                return "<{}...>".format(self.positional[i])
            return "<{}>".format(self.positional[i])
        print("usage: {} <subcommand> [subcommand arguments]")
        print("subcommand help: {} <subcommand> -h")
        print("")
        if self.description:
            for paragraph in self.description.split("\n\n"):
                print(rewidth(paragraph, 0, 80))
                print("")
        keylen = max(
                [len(key) + len(vartype(var)) + 3
                    for key, var in self.optional.items()]
                + [len(key) for key in self.subcommands.keys()]
                + [len(key) for key in self.flags.keys()]
                + [len(var) + len(vartype(var)) + 3
                    for var in self.positional]
                + [1])
        print("Subcommands:")
        for key, parser in self.subcommands.items():
            description = self.field_descriptions.get(key, key)
            description = rewidth_argument_description(description, keylen)
            print("    {}  {}".format(key.ljust(keylen), description))
        print("")

        if any(x in self.field_descriptions for x in self.positional):
            print("Common positional arguments:")
            for variable in self.positional:
                description = self.field_descriptions.get(variable, variable)
                description = rewidth_argument_description(description, keylen)
                print("    {}  {}".format(
                    "<{}:{}>".format(variable, vartype(variable)).ljust(keylen),
                    description))
            print("")
        print("Common optional arguments:")
        for key, variable in sorted(self.optional.items()):
            description = self.field_descriptions.get(variable, variable)
            description = rewidth_argument_description(description, keylen)
            print("    {}  {}".format(
                "{} <{}>".format(key, vartype(variable)).ljust(keylen),
                description))
        print("")
        print("Common optional flags:")
        for key, variable in sorted(self.flags.items()):
            description = self.field_descriptions.get(variable, variable)
            description = rewidth_argument_description(description, keylen)
            print("    {}  {}".format(
                key.ljust(keylen),
                description))
