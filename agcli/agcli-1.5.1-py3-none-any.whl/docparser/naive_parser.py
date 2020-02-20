from . import docparser
from ..utils import terminal


class NaiveParser(docparser.DocParser):

    def parse(self, doc):
        is_presentation_lines = True
        for line in doc.split('\n'):
            #Handle presentation over multiple lines
            if is_presentation_lines and (self.cmd in line or line.startswith(' ')):
                self._parse_presentation_line(line)
            elif line.startswith(' '):
                self._parse_parameter_line(line)
            else:
                is_presentation_lines = False
        self.add_ID()
        self.format_help()

    def _parse_presentation_line(self, line):
        """
        Extract options and arguments from the presentation lines. We call
        presentation the lines that are similar to this format:
        usage : git [--version] [--help] [-C <chemin>] [-c <nom>=<valeur>]
           [--exec-path[=<chemin>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<chemin>] [--work-tree=<chemin>] [--namespace=<nom>]
           <commande> [<args>]
        """
        # if it is the first line of presentation, we only care about the string
        # after the command name => "line.split(self.cmd)[1]"
        if self.cmd in line:
            presentation = line.split(self.cmd)[1].strip().split(' ')
        else:
            presentation = line.split(self.cmd)[0].strip().split(' ')
        for parameter in presentation:
            parameter = parameter.replace('[', '').replace(']', '').replace('<', '').replace('>', '')
            # Handles expressions similar to [-p | --paginate | --no-pager]
            for word in parameter.split('|'):
                word = word.strip()
                if self._is_option_name(word):
                    self._parse_option_line([word, ''])
                else:
                    self._parse_argument_line([word, ''])

    def _parse_parameter_line(self, line):
        """
        A parameter line is a line that begin with a blank space and is not part
        of the presentation lines. From these lines, we extract option and
        subcommand information such as their names and help message.
        A parameter line looks like this:
           clone      Cloner un dépôt dans un nouveau répertoire
        """
        info = line.strip(' ').split('  ')
        info = self._delete_empty_items(info)
        if len(info) >=2:
            if self._is_option_name(info[0]):
                self._parse_option_line(info)
            else:
                self._parse_subcommand_line(info)

    def _delete_empty_items(self, list_):
        """
        Browses a list of sting items and return a new list containing only the
        non-empty strings from the first list.
        """
        new_list = []
        for item in list_:
            if item != "":
                new_list.append(item)
        return new_list

    def _is_option_name(self, expr):
        """
        Returns True if the first word of a line refers to a short, long or BSD
        option.
        """
        long_or_short_option = expr.startswith('-')
        bsd_option = len(expr.split(',')[0]) == 1
        return long_or_short_option or bsd_option

    def _parse_option_line(self, expr_list):
        """
        Extract the help message of the option found and check if the same option
        has already been extracted. If it is the case, the option information
        are updated thanks to the current option being processed.
        """
        option = self._process_option_names( expr_list[0])
        option['help'] = expr_list[1]
        self._handle_duplicate(self.options, option, self._are_same_option)

    def _process_option_names(self, option_expr):
        """
        Extract all the option informtion from a parameter line, such as the
        names, if it takes an argument and the name of it.
        """
        option = {}
        names = []
        for name in option_expr.split(','):
            name = name.strip()
            if ' ' in name:
                names.append(name.split(' ')[0])
                option.update({'argument_name': name.split(' ')[1],
                               'default_value': []})
            elif '=' in name:
                names.append(name.split('=')[0])
                option.update({'argument_name': name.split('=')[1],
                               'default_value': []})
            else:
                names.append(name)
        option['names'] = names
        return option

    def _handle_duplicate(self, parameter_list, current_parameter, comp_function):
        """
        If "current_parameter" as a similar parameter in "parameter_list", it
        updates this parameter information. Otherwise, it append "current_parameter"
        to "parameter_list". "comp_function" is the fonction used to determine if
        a parameter from "parameter_list" is the same as "current_parameter".
        """
        index, parameter_already_exist = self._parameter_already_exist(parameter_list,
                                                                       current_parameter,
                                                                       comp_function)
        if parameter_already_exist:
            docparser.update_parameter(parameter_list[index], current_parameter)
        else:
            parameter_list.append(current_parameter)

    def _parameter_already_exist(self, parameter_list, new_parameter, comp_function):
        """
        If "current_parameter" as a similar parameter in "parameter_list", it
        returns the index of this parameter in "parameter_list" and True.
        Otherwise, it returns None and False. "comp_function" is the fonction
        used to determine if a parameter from "parameter_list" is the same as
        "current_parameter".
        """
        for i, parameter in enumerate(parameter_list):
                if comp_function(parameter, new_parameter):
                        return i, True
        return None, False

    def _are_same_option(self, option1, option2):
        """
        Check if "option1" is the same option as "option2"
        """
        # ensure 'option1' and 'option2' are of the same type
        if option1.keys() == option2.keys():
            for name in option1['names']:
                if name in option2['names']:
                    return True
        else:
            return False

    def _are_same_argument(self, arg1, arg2):
        """
        Check if "arg1" is the same argument as "arg2"
        """
        return arg1['name'] == arg2['name']

    def _are_same_subcommand(self, sub1, sub2):
        """
        Check if "sub1" is the same subcommand as "sub1"
        """
        return sub1['name'] == sub2['name']

    def _parse_subcommand_line(self, expr_list):
        """
        Extract the subcommand informations from the current line such as the
        subcommand name and its help message. It adds these informations to the
        to the subcommands list.
        """
        # check if subcommand name is only 1 word, if not, "expr_list" is not
        # what we are looking for
        if len(expr_list[0].split()) == 1:
            subcommand = {'name': expr_list[0].strip(), 'help': expr_list[1]}
            self._handle_duplicate(self.commands, subcommand, self._are_same_subcommand)

    def _parse_argument_line(self, expr_list):
        """
        Extract the argument informations from the current line such as the
        argument name and its help message. It adds these informations to the
        to the arguments list.
        """
        name = expr_list[0].strip()
        name = name.replace('.', '')
        if name == '' or "option" in name.lower():
            return
        else:
            argument = {'name': name, 'help': expr_list[1]}
            self._handle_duplicate(self.arguments, argument, self._are_same_argument)

    def get_command_doc(self):
        try:
            returncode, stdout, stderr = terminal.to_cli("{} {}".format(self.cmd, '--help'))
            if returncode == 0:
                return stdout
            else:
                raise docparser.NoDocumentationFoundError(self.cmd)
        except FileNotFoundError as e:
            raise docparser.CommandNotFoundError(self.cmd)
