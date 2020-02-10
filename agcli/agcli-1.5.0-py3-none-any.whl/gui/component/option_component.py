import wx
from wx import CheckBox, Panel, ComboBox
from wx.lib.scrolledpanel import ScrolledPanel
from ..component.base_component import BaseComponent
from ..component.base_argument_component import BaseArgumentComponent
from ..component import custom_widget
from .. import command_notebook
from ..component.option_name import OptionName, OptionArgumentName
from ...interface.interface_generator import types


class SimpleOptionComponent(BaseComponent):

    def __init__(self, parent, template_option, interface_option):
        super().__init__(parent, template_option, interface_option)
        self.frame = parent
        self.interface_option = interface_option
        self.help = interface_option['help']
        self.SetToolTip(self.help)
        self.options = []

        self._create_options(template_option, interface_option)
        self._refresh_command_label()
        self.refresh_collapse()
        self.GetParent().Layout()

    def _create_options(self, template_option, interface_option):
        """
        Create the different option name for one type of options
        """
        for index, option_name in enumerate(interface_option['names']):
            option = self._get_option_constructor()(self.GetPane(), option_name,
             template_option['names'][index], self.OnCheckBox)
            self.component_sizer.Add(option, 1, wx.ALL, 5)
            self.options.append(option)

    def _get_option_constructor(self):
        """
        Return the constructor to use to build an option name
        """
        return OptionName

    def OnCheckBox(self, event):
        """
        This function is called when the checkbox of an option name is checked.
        It ensures that at most one option name is checked.
        """
        for option in self.options:
            if not option.checkbox.GetId() == event.GetId():
                option.check(False)

    def to_template(self):
        template = super().to_template()
        names = []
        for option in self.options:
            names.append(option.to_template())
        template['names'] = names
        return template

    def get_command(self):
        for option in self.options:
            if option.is_checked():
                return option.as_command()
        return ''

class ArgumentOptionComponent(SimpleOptionComponent, BaseArgumentComponent):

    def __init__(self, parent, template, interface_option):
        super().__init__(parent, template, interface_option)

        self.refresh_collapse()
        self.GetParent().Layout()

    def _get_option_constructor(self):
        return OptionArgumentName

    def _get_default_value_dict(self, interface_option, template_option):
        """
        Check if an option has a value specified in its template.
        The value found is returned in a dictionnary of this form: {'value': value}
        where 'value' is the value mentioned above. If no value is found, an empty
        dictionnary is returned.
        """
        value = template_option.get('value', None)
        if value is None:
            return {}
        else:
            return {'value': value}

    def is_checked(self):
        for option in self.options:
            if option.is_checked():
                return True
        return False

    def _refresh_command_label(self):
        try:
            super()._refresh_command_label()
        except Exception as e:
            pass

    def to_template(self):
        option_template = SimpleOptionComponent.to_template(self)
        argument_template = BaseArgumentComponent.to_template(self)
        del argument_template['is_checked']
        option_template.update(argument_template)
        return option_template

    def get_command(self):
        command = SimpleOptionComponent.get_command(self)
        args = BaseArgumentComponent.get_command(self)
        if command == '':
            return ''
        elif command.startswith('--') and not args=='':
            #Add value to a long option
            command += "={}".format(args)
        elif not args=='':
            #Add value to a short or BSD option
            command += " {}".format(args)
        return command
