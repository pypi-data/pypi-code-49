from . import docopt_parser, explainshell_parser, naive_parser, docparser

_name_to_parser = {
    "docopt": docopt_parser.DocoptParser,
    "explainshell": explainshell_parser.ExplainShellParser,
    "naive": naive_parser.NaiveParser
}

class ParametersExtractor():

    def __init__(self, cmd, parsers_to_use):
        self.parsers = []
        self.options = []
        self.arguments = []
        self.commands = []
        self._init_parser(cmd, parsers_to_use)
        self._extract_parameters()

    def _init_parser(self, cmd, parsers_to_use):
        """
        Create the parsers according the option passed in the command line
        """
        for parser in parsers_to_use.strip('\"').strip('\'').split(','):
            parser_constructor = _name_to_parser[parser.strip()]
            self.parsers.append(parser_constructor(cmd))

    def _extract_parameters(self):
        """
        Extract the options, arguments and subcommands from each parser
        """
        for parser in self.parsers:
            self._extract_info(self.options, parser.options, self._are_same_options)
            self._extract_info(self.arguments, parser.arguments, self._are_same_arguments)
            self._extract_info(self.commands, parser.commands, self._are_same_commands)
            self._kill_double(self.options, self._are_same_options)

    def _extract_info(self, current_info_list, new_info_list, are_same_info):
        """
        Update the current options, arguments and subcommands info with a
         parser info
        """
        info_to_add = []
        for new_info in new_info_list:
            is_update = False
            for current_info in current_info_list:
                if are_same_info(current_info, new_info):
                    docparser.update_parameter(current_info, new_info)
                    is_update = True
                    break
            if not is_update:
                info_to_add.append(new_info)
        current_info_list.extend(info_to_add)

    def _kill_double(self, current_info_list, are_same_info):
        """
        Kills all the duplicated informations in 'current_info_list' by merging them.
        The function 'are_same_info' is used to know if 2 items are the same.
        This function is useful only on the "self.options" list because all duplicate
        in the other list are handleld before.
        """
        for i, option1 in enumerate(current_info_list):
            for j, option2 in enumerate(current_info_list):
                if i != j and are_same_info(option1, option2):
                    docparser.update_parameter(option1, option2)
                    del current_info_list[j]

    def _are_same_options(self, option1, option2):
        """
        Return True iif the 2 options represents the same option
        """
        for name in option1['names']:
            if name in option2['names']:
                return True
        return False

    def _are_same_arguments(self, arg1, arg2):
        """
        Return True iif the 2 arguments represents the same argument
        """
        return arg1['name'] == arg2['name']

    def _are_same_commands(self, subcmd1, subcmd2):
        """
        Return True iif the 2 subcommands represents the same subcommand
        """
        return subcmd1['name'] == subcmd2['name']
