from ..utils import yaml
from ..utils import file_handler as fh
import os.path

class DefaultGenerator():

    def __init__(self):
        self.template_file = fh.file_handler.get_default_template_file()
        self.interface = yaml.open_yaml(fh.file_handler.get_interface_file())

    def _split_parameters(self, options, arguments, subcommands, interface):
        """
        Fills the 'options', 'arguments' and 'subcommands' lists with the
         matching default template for each parameters contains in 'interface'.
        """
        for parameter in interface:
            if "Option" in parameter['type']:
                template_info = self._get_option_template(parameter)
                options.append(template_info)
            elif "Argument" == parameter['type']:
                template_info = self._get_argument_template(parameter)
                arguments.append(template_info)
            elif "Subcommand" == parameter['type']:
                template_info = self._get_subcommand_template(parameter)
                subcommands.append(template_info)

    def generate_other_template(self, sub_interface):
        """
        Generate a template that only contains parameters from "sub_interface".
        These template parameters are listed below the only key: "Others".
        """
        parameters = []
        options = []
        arguments = []
        subcommands = []
        self._split_parameters(options, arguments, subcommands, sub_interface)
        parameters.extend(options)
        parameters.extend(arguments)
        parameters.extend(subcommands)
        other_template = {
            "Others": parameters
        }
        return other_template

    def generate_complete_template(self, terminal_parameters):
        """
        Generate a template according to the parameters data gathered on the CLI.
        """
        template = []
        for parameter in terminal_parameters:
            for interface_parameter in self.interface:
                if parameter['ID'] == interface_parameter['ID']:
                    if interface_parameter['type'] == "Flag Option":
                        self._fill_flag_option_complete_template(interface_parameter,
                                                                 parameter, template)
                    elif interface_parameter['type'] == "Argument Option":
                        self._fill_argument_option_complete_template(interface_parameter,
                                                                     parameter, template)
                    elif interface_parameter['type'] == "Argument":
                        self._fill_argument_complete_template(interface_parameter,
                                                              parameter, template)
                    elif interface_parameter['type'] == "Subcommand":
                        self._fill_subcommand_complete_template(interface_parameter,
                                                                parameter, template)
        complete_template = {
            "Complete": template
        }
        return complete_template

    def _fill_flag_option_complete_template(self, interface_parameter, parameter, template):
        """
        Fill the flag option template generated according 'interface_parameter' with the values
        of "parameter". The result is store in the "template" list.
        """
        option = self._get_option_template(interface_parameter)
        option['is_collapsed'] = False
        index = self._get_name_option_index(interface_parameter, parameter['option'])
        option['names'][index]['is_checked'] = True
        option['names'][index]['repeat'] = parameter['count']
        template.append(option)

    def _fill_argument_option_complete_template(self, interface_parameter, parameter, template):
        """
        Fill the  argument option template generated according 'interface_parameter' with the values
        of "parameter". The result is store in the "template" list.
        """
        option = self._get_option_template(interface_parameter)
        option['is_collapsed'] = False
        index = self._get_name_option_index(interface_parameter, parameter['option'])
        option['names'][index]['is_checked'] = True
        option['values'] = parameter['arg']
        template.append(option)

    def _fill_argument_complete_template(self, interface_parameter, parameter, template):
        """
        Fill the argument template generated according 'interface_parameter' with the values
        of "parameter". The result is store in the "template" list.
        """
        argument = self._get_argument_template(interface_parameter)
        argument['is_collapsed'] = False
        argument['is_checked'] = True
        argument['values'] = parameter['value']
        template.append(argument)

    def _fill_subcommand_complete_template(self, interface_parameter, parameter, template):
        """
        Fill the subcommand template generated according 'interface_parameter' with the values
        of "parameter". The result is store in the "template" list.
        """
        subcommand = self._get_subcommand_template(interface_parameter)
        subcommand['is_collapsed'] = False
        subcommand['is_checked'] = True
        template.append(subcommand)

    def _get_name_option_index(self, interface_parameter, option_name):
        """
        Return the index of an 'option_name' according to the option interface.
        """
        for i, name in enumerate(interface_parameter['names']):
            if option_name == name:
                return i

    def _get_base_parameter_template(self, parameter):
        """
        Return template information shared by all types of parameters
        """
        return {'ID': parameter['ID'], 'is_collapsed':True}

    def _get_option_template(self, parameter):
        """
        Return template information of an option parameter
        """
        template_option = self._get_base_parameter_template(parameter)
        option_specific = {}
        self._create_option_name_template(parameter, option_specific)
        if "default_value" in parameter:
            option_specific['values'] = parameter['default_value']
            option_specific['argument_type'] = parameter['argument_type']
        template_option.update(option_specific)
        return template_option

    def _create_option_name_template(self, option_interface, option_template):
        """
        Generate the template for the 'name_type' options in the 'option_interface'.
        The results is stored in 'option_template'.
        """
        options = []
        for option_name in option_interface['names']:
            options.append({'repeat':1, 'is_checked':False})
        option_template['names'] = options

    def _get_argument_template(self, parameter):
        """
        Return template information of an argument parameter
        """
        template_argument = self._get_base_parameter_template(parameter)
        argument_specific = {'is_checked':False, 'values':[],
         'argument_type':parameter['argument_type']}

        template_argument.update(argument_specific)
        return template_argument

    def _get_subcommand_template(self, parameter):
        """
        Return template information of a subcommand parameter
        """
        template_subcommand = self._get_base_parameter_template(parameter)
        subcommand_specific = {'is_checked':False}
        template_subcommand.update(subcommand_specific)
        return template_subcommand

    def generate_default_template(self):
        """
        Find a way to propose a good default Template.
        Currently it returns an empty template. If the template already exists,
        it does nothing.
        """
        if os.path.isfile(self.template_file):
            #The template already exists
            return
        options = []
        arguments = []
        subcommands = []
        self._split_parameters(options, arguments, subcommands, self.interface)
        template_yaml = {
            "Options": options,
            "Arguments": arguments,
            "Subcommands": subcommands
        }
        yaml.write_yaml(self.template_file, template_yaml)
