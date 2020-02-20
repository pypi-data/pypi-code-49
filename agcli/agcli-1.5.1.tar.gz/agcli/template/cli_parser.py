import argparse
import os
from ..utils import file_handler as fh
from ..utils import yaml


class CLIParser():

    def __init__(self, command, instruction):
        self.parser = argparse.ArgumentParser(prog=command, add_help=False)
        self.instruction = []
        if not instruction is None:
            self._format_instruction(instruction)
        self.interface = self._get_interface()
        self.spoiled_ID = []
        self.current_ID = None
        self._init_parser()

    def _format_instruction(self, instruction):
        """
        Make 'self.instruction' be a list of sublist. Each sublist contains some
        words from the 'instruction' so that if a sublist contains an option, it
        is the first element of the sublist. Each sublist concatenate forms the
        'instruction' back.The words surrounded by " or ' are considered as a
        single word.
        """
        current_index = 0
        self.instruction.append([instruction.split()[0]])
        is_one_arg = False
        for word in instruction.split()[1:]:
            if is_one_arg:
                if word.endswith("\"") or word.endswith("\'"):
                    is_one_arg = False
                self.instruction[current_index][-1] = "{} {}".format(self.instruction[current_index][-1], word)
            elif word.startswith('-'):
                self.instruction.append([word])
                current_index = current_index + 1
            else:
                if word.startswith("\"") or word.startswith("\'"):
                    is_one_arg = True
                self.instruction[current_index].append(word)

    def parse(self):
        """
        Parse the instruction written by the user and return a list of the parameter
        used and they arguments if they have any.
        """
        if len(self.instruction) == 0:
            return {}
        else:
            ordered_parameters = []
            for parameter in self.instruction:
                args = self.parser.parse_args(parameter)
                parameters = self._post_processing(args)
                for v in parameters.values():
                    parameter_already_exist, index = self._parameter_already_exist(v, ordered_parameters)
                    if parameter_already_exist:
                        ordered_parameters[index].update(v)
                    else:
                        ordered_parameters.append(v.copy())
            self._merge_same_arguments(ordered_parameters)
            self.spoiled_ID = []
            self.current_ID = None
            return ordered_parameters

    def _parameter_already_exist(self, parameter, parameter_list):
        """
        Check if the "parameter" parameter appears in the "parameter_list". If
        this is the case, it returns True and the parameter's index that match
        "parameter". Otherwise, it returns False and None.
        """
        for i, param in enumerate(parameter_list):
            if param['ID'] == parameter['ID']:
                return True, i
        return False, None

    def _get_interface(self):
        """
        Open the interface of the current command and return it.
        """
        interface_file = fh.file_handler.get_interface_file()
        return yaml.open_yaml(interface_file)

    def _init_parser(self):
        """
        Initialize the parser in order to detect the option, subcommands and
        arguments.
        """
        for parameter in self.interface:
            if parameter['type'] == "Argument Option":
                names = self._get_option_names(parameter)
                if len(names)>0:
                    self.parser.add_argument(*names, action=ArgOptAction,
                                             default={'ID':parameter['ID']}, nargs='*')
            elif parameter['type'] == "Flag Option":
                names = self._get_option_names(parameter)
                if len(names)>0:
                    self.parser.add_argument(*names, action=FlagAction,
                                             default={'ID':parameter['ID']})
            elif parameter['type'] == "Subcommand":
                self.parser.add_argument(parameter['name'], action=ArgumentAction,
                                         default={},nargs='?')
            elif parameter['type'] == "Argument":
                self.parser.add_argument(parameter['name'], action=ArgumentAction,
                                         default={}, nargs='*')

    def _get_option_names(self, option):
        """
        Extract the names of "option" by ignoring the BSD names as Argparse doesn't
        support it.
        """
        names = []
        for name in option['names']:
            # avoid BSD option, they are not supported by argparse
            if len(name)>1:
                names.append(name)
        return names

    def _post_processing(self, args):
        """
        Compute the results of the 'argparse' parser in order to format them.
        """
        args_dict = args.__dict__
        args_dict = self._delete_useless_parameters(args_dict)
        args_dict = self._extract_subcommands(args_dict)
        args_dict = self._extract_arguments(args_dict)
        args_dict = self._delete_useless_parameters(args_dict)
        return args_dict

    def _merge_same_arguments(self, parameters):
        """
        Merge the values of parameters that have the same 'ID'
        """
        for i, param1 in enumerate(parameters):
            for j, param2 in enumerate(parameters):
                if (param1['ID'] == param2['ID'] and
                    i != j and param1.get('value', None) is not None):
                    param1['value'].extend(param2['value'])
                    del parameters[j]

    def _extract_arguments(self, args):
        """
        Add an 'ID' field to the remaining parameters. This function must be called
        when subcommands have been extracted to be sure only arguments need 'ID'.
        The same 'ID' can only be assigned to consecutive argument.
        """
        new_args = args
        for argument in args.keys():
            if args[argument].get('value', None) is None:
                if self.current_ID is not None:
                    self.spoiled_ID.append(self.current_ID)
                    self.current_ID = None
            else:
                argument_ID = self._get_argument_ID(args[argument]['value'])
                new_args[argument]['ID'] = argument_ID
                self.current_ID = argument_ID
                #new_args[argument]['value'] = [args[argument]['value']]
        return new_args

    def _get_argument_ID(self, argument):
        """
        Look for the argument that match the type of a particular value of the parsed
        instruction. This return the argument which type is the most specific for
        the value implied. ('String' arguments are considered in last)
        """
        string_parameter = None
        for parameter in self.interface:
            if parameter['type'] == "Argument":
                if (self._is_type_compatible(parameter['argument_type'], argument[0]) and
                    parameter['ID'] not in self.spoiled_ID):
                    if not parameter['argument_type'] == "String":
                        return parameter['ID']
                    elif string_parameter is None:
                        string_parameter = parameter
        return string_parameter['ID']

    def _is_type_compatible(self, arg_type, arg_value):
        """
        Check if the "arg_value" can match the "arg_type".
        """
        if arg_type == "Directory":
            return os.path.isdir(arg_value)
        elif arg_type == "File":
            return os.path.isfile(arg_value)
        elif arg_type == "Percentage":
            try:
                converted = float(arg_value)
                return 0. <= converted <= 1.
            except:
                return False
        elif arg_type == "Integer":
            try:
                converted = int(arg_value)
                return True
            except:
                return False
        else:
            return arg_type == "String"

    def _extract_subcommands(self, args):
        """
        Add a "ID" field to the subcommand parameters.
        """
        new_args = {}
        for argument in args.keys():
            if args[argument].get('value', None) is None:
                new_args[argument] = args[argument]
            else:
                new_args.update(self._split_arguments(args[argument]['value'], argument))
        return new_args

    def _split_arguments(self, arg_list, arg_name):
        """
        Browse the "arg_list", for each item of this list, if it is a subcommand,
        a new subcommand is added to the parameters dictionnary. Otherwise, if
        it is an argument value, a new argumet is added to the parameters dictionnary.
        If two or more arguments follows each others, they will be merge in the
        same dictionnary value.
        This function returns the parameters dictionnary.
        """
        splitted_param = {}
        last_arg = None
        for i, value in enumerate(arg_list):
            is_subcommand, subcommand_ID = self._get_subcommand_ID(value)
            if is_subcommand:
                #create a subcommand dict
                splitted_param[value] = {'ID':subcommand_ID}
                last_arg = None
            else:
                # value is an arg value
                if last_arg is None:
                    name = "{}_{}".format(arg_name, i)
                    splitted_param[name] = {'value':[value]}
                    last_arg = name
                else:
                    splitted_param[last_arg]['value'].append(value)
        return splitted_param

    def _get_subcommand_ID(self, argument):
        """
        Check if an argument matches a subcommand name. If so, 'True' and the
        'ID' of this subcommand are returned. Else, 'False' and 'None' are returned.
        """
        for parameter in self.interface:
            if parameter['type'] == "Subcommand" and parameter['name'] == argument:
                return True, parameter["ID"]
        return False, None

    def _delete_useless_parameters(self, args):
        """
        Create a new dictionnary that only contains keys which associated values
        are not 'None'.
        """
        new_dict = {}
        for key in args.keys():
            if not args[key] is None:
                if 'value' in args[key] and args[key]['value'] == []:
                    #This key is an argument and it has empty 'value'
                    continue
                elif 'option' in args[key] and args[key]['option'] is None:
                    #This key is an option but it doesn't appear in the cli
                    continue
                new_dict[key] = args[key]
        return new_dict

class CustomAction(argparse.Action):
    """
    Inherit from the 'argparse' Action in order to be able to do custom actions
    with the 'argparse' parser.
    """

    def __init__(self, option_strings, dest, nargs=None, const=None,
                 default=None, type=None, choices=None, required=False,
                 help=None, metavar=None):
        self.id = default
        super(CustomAction, self).__init__( option_strings, dest, nargs=nargs,
                                          const=const, default=None, type=type,
                                          choices=choices, required=required,
                                          help=help, metavar=metavar)

    def get_value_dict(self, namespace):
        """
        Return the dictionnary that hold all the informations about the parameter.
        If it doesn't exist yet, it is created with the default value precised
        in the 'add_argument' of an 'argparse' parser.
        """
        if getattr(namespace, self.dest) is None:
            value_dict = self.id
        else:
            value_dict = getattr(namespace, self.dest)
        return value_dict

class FlagAction(CustomAction):
    """
    Represents the action to be taken when the parser find a flag option.
    """

    def __init__(self, option_strings, dest, default=None,
                 required=False, help=None):
        super(FlagAction, self).__init__( option_strings=option_strings,
                                            dest=dest, nargs=0, default=default,
                                            required=required, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        if option_string is None:
            return
        value_dict = self.get_value_dict(namespace)
        value_dict['count'] = value_dict.get('count', 0) + 1
        value_dict['option'] = option_string
        setattr(namespace, self.dest, value_dict)

class ArgOptAction(CustomAction):
    """
    Represents the action to be taken when the parser find an argument option.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        if option_string is None:
            return
        value_dict = self.get_value_dict(namespace)
        value_dict['arg'] = values
        value_dict['option'] = option_string
        setattr(namespace, self.dest, value_dict)

class ArgumentAction(CustomAction):
    """
    Represents the action to be taken when the parser find an argument or a subcommand.
    We are not able to make the difference at this point of the process.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        if values is None:
            setattr(namespace, self.dest, None)
            return
        value_dict = self.get_value_dict(namespace)
        value_dict['value'] = values
        setattr(namespace, self.dest, value_dict)
