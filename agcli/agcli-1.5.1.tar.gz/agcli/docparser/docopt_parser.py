from . import new_docopt, docparser
from ..utils import terminal

_option_mapping = {
    "short": "short_names",
    "long": "long_names",
    "value": "default_value",
    "arg_name": "argument_name",
    "description": "help"
    }

_argument_mapping = {
    "name": "name"
}

_subcommand_mapping ={
    "name": "name"
}

class DocoptParser(docparser.DocParser):

    def parse(self, doc):
        try:
            # Get options short or/and long name + default value
            usage_sections = new_docopt.parse_section('usage:', doc)
            if len(usage_sections) == 0:
                usage_sections=""
            else:
                usage_sections = usage_sections[0]
            options = new_docopt.parse_defaults(doc)
            # Get relations between the commands, arguments and options: mutually exclusive, optional, ...
            pattern = new_docopt.parse_pattern(new_docopt.formal_usage(usage_sections), options)
            # Get arguments
            arguments = set(pattern.flat(new_docopt.Argument))
            #Get commands
            commands = set(pattern.flat(new_docopt.Command))
            self.options = set(options)
            self.arguments = arguments
            self.commands = commands
            self.format_parameters()
        except Exception as e:
            raise docparser.ParsingError(self.cmd)

    def get_command_doc(self):
        try:
            returncode, stdout, stderr = terminal.to_cli("{} {}".format(self.cmd, '--help'))
            if returncode == 0:
                return stdout
            else:
                raise docparser.NoDocumentationFoundError(self.cmd)
        except FileNotFoundError as e:
            raise docparser.CommandNotFoundError(self.cmd)

    def format_parameters(self):
        """
        Format the data obtained by parsing the doc in order to ease the creation
        of the interface
        """
        self.options = self.extract_elements(self.options, _option_mapping)
        self._to_namelist(self.options)
        self._to_arg_list(self.options)

        self.arguments = self.extract_elements(self.arguments, _argument_mapping)
        self.arguments = self.erase_char_in_prop(self.arguments, 'name', ['<', '>'])
        self._add_empty_help(self.arguments)

        self.commands = self.extract_elements(self.commands, _subcommand_mapping)
        self._add_empty_help(self.commands)
        self.add_ID()
        self.format_help()

    def _to_namelist(self, options):
        """
        Transform the name of options into a list of names
        """
        for option in options:
            names = option.get('names', [])
            if 'long_names' in option:
                names.append(option['long_names'])
                del option['long_names']
            if 'short_names' in option:
                names.append(option['short_names'])
                del option['short_names']
            option['names'] = names

    def _to_arg_list(self, options):
        """
        Transform the 'default_value' of argument option into a list containing
        this 'default_value'.
        """
        for option in options:
            if 'default_value' in option:
                option['default_value'] = [option['default_value']]

    def transfer_data(self, old_dict, mapping):
        """
        Copy the data from 'old_dict' and returns it. Only fields that are keys of
        of the mapping and with a value different from False and None. The values of
        these fields are not modified but the new key is the value of mapping for the
        old key (new_key = mapping[old_key]).
        """
        new_dict = {}
        for old_name in mapping:
            new_name = mapping[old_name]
            new_value = old_dict[old_name]
            if not new_value==False and new_value is not None:
                new_dict[new_name] = new_value
        return new_dict

    def erase_char_in_prop(self, elements, prop_name, to_erase):
        """
        Erase some chars of the value of the key 'prop_name' for all 'elements'.
        The chars to erase are given in the list 'to_erase'.
        """
        for elem in elements:
            new_value = elem[prop_name]
            for pattern in to_erase:
                new_value = new_value.replace(pattern, '')
            elem[prop_name] = new_value
        return elements

    def extract_elements(self, elements, mapping):
        """
        Take a set of elements from the parser and format it into a list of dict in
        order to ease the export of the data in YAML format
        """
        extracted_elements = []
        for element in elements:
            extracted_element = self.transfer_data(element.__dict__, mapping)
            extracted_elements.append(extracted_element)
        return extracted_elements



if __name__ == "__main__":
    parser = DocoptParser('ls')
    print(parser.options)
    print(parser.arguments)
    print(parser.commands)
