from ..utils import terminal

class NoDocumentationFoundError(Exception):
    def __init__(self, cmd):
        message = "No documentation found for command \"{}\"".format(cmd)
        super().__init__(message)

class NoVersionFoundError(Exception):
    def __init__(self, cmd):
        message = "No version information found for command \"{}\"".format(cmd)
        super().__init__(message)

class ParsingError(Exception):
    def __init__(self, cmd):
        message = "Impossible to parse the documentation of the command \"{}\"".format(cmd)
        super().__init__(message)

class CommandNotFoundError(Exception):
    def __init__(self, cmd):
        message = "Impossible to find the command \"{}\"".format(cmd)
        super().__init__(message)

class ExplainShellError(Exception):
    def __init__(self, cmd):
        message = "Impossible to find the command \"{}\" on ExplainShell".format(cmd)
        super().__init__(message)

class ExplainShellConnexionError(Exception):
    def __init__(self):
        message = "Impossible to reach the ExplainShell website"
        super().__init__(message)

def update_parameter(old_parameter, new_parameter):
    """
    Works as the 'update' of dictionnaries but instead of replacing a list
    by another one, this method add each element of a list to the other by
    skipping duplicate.
    """
    for key in new_parameter:
        if key in old_parameter:
            if isinstance(old_parameter[key], list):
                for string_ in new_parameter[key]:
                    if string_ not in old_parameter[key]:
                        old_parameter[key].append(string_)
            else:
                old_parameter[key] = new_parameter[key]
        else:
            old_parameter[key] = new_parameter[key]

class DocParser():

    def __init__(self, cmd):
        self.cmd = cmd
        self.options = []
        self.arguments = []
        self.commands = []
        try:
            doc = self.get_command_doc()
            self.parse(doc)
        except Exception as e:
            pass

    def get_command_doc(self):
        """
        This function receive a command name and return its string documentation.
        If no documentation is found, it raises a NoDocumentationFoundError.
        If the command is not found, it raises a CommandNotFoundError
        """
        raise NotImplementedError

    def parse(self, doc):
        """
        This function receive a string documentation and parse its arguments, options
        and commands. It assign them to the instance variables with the same name.
        If it is impossible to parse the documentation, it raises a ParsingError
        """
        raise NotImplementedError

    def get_command_version(self):
        """
        Return the version information of the command. This raises a NoVersionFoundError
        if the command doesn't support the '--version' option.
        """
        try:
            returncode, stdout, stderr = terminal.to_cli("{} {}".format(self.cmd, '--version'))
            if returncode == 0:
                return stdout
            else:
                raise NoVersionFoundError(self.cmd)
        except FileNotFoundError as e:
            raise CommandNotFoundError(self.cmd)

    def _add_empty_help(self, elements):
        """
        Add a field 'help' with empty string as value for a list of dict.
        """
        for element in elements:
            element['help'] = ''

    def _add_option_ID(self):
        """
        Add the "ID" field to the option parameters
        """
        for option in self.options:
            if 'argument_name' in option:
                type_ = "Argument Option"
            else:
                type_ = "Flag Option"
            name = option['names'][0]
            option['ID'] = "{}: {}".format(type_, name)
            option['type'] = type_

    def _add_argument_ID(self):
        """
        Add the "ID" field to the argument parameters
        """
        for argument in self.arguments:
            argument['ID'] = "Argument: {}".format(argument['name'])
            argument['type'] = 'Argument'

    def _add_subcommand_ID(self):
        """
        Add the "ID" field to the subcommand parameters
        """
        for command in self.commands:
            command['ID'] = "Subcommand: {}".format(command['name'])
            command['type'] = 'Subcommand'

    def add_ID(self):
        """
        Add the "ID" field to the parameters
        """
        self._add_option_ID()
        self._add_argument_ID()
        self._add_subcommand_ID()

    def _format_parameter_list_help(self, parameter_list):
        """
        Prevent help to contain the newline char ('\n') in the "parameter_list"
        """
        for parameter in parameter_list:
            parameter['help'] = parameter['help'].replace('\n', '')

    def format_help(self):
        """
        Format the help of all the parameters
        """
        self._format_parameter_list_help(self.options)
        self._format_parameter_list_help(self.commands)
        self._format_parameter_list_help(self.arguments)
