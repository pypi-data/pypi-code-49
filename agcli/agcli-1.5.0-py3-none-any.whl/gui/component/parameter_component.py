from ..component.argument_component import ArgumentComponent
from ..component.subcommand_component import Subcommand
from ..component.option_component import SimpleOptionComponent, ArgumentOptionComponent
from ..component.base_component import Serializable
from ..drag_and_drop import ParameterPlaceholder
from wx.lib.scrolledpanel import ScrolledPanel
import wx

parameter_constructor = {
    "Argument": ArgumentComponent,
    "Subcommand": Subcommand,
    "Argument Option": ArgumentOptionComponent,
    "Flag Option": SimpleOptionComponent
    }

class ParametersComponent(Serializable, ScrolledPanel):

    def __init__(self, parent, template_parameters, interface):
        super().__init__(parent, style=wx.VSCROLL)
        self.parameters = []
        self.placeholders = []
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self.SetupScrolling()
        self.create_placeholder()
        for template_parameter in template_parameters:
            for interface_parameter in interface:
                if template_parameter["ID"] == interface_parameter["ID"]:
                    self.create_parameter(template_parameter, interface_parameter)
                    self.create_placeholder()
                    break
        self.Layout()

    def create_parameter(self, template, interface):
        """
        Create an argument component.
        """
        parameter = parameter_constructor[interface["type"]](self, template, interface)
        self.GetSizer().Add(parameter, flag=wx.EXPAND)
        self.parameters.append(parameter)

    def create_placeholder(self):
        """
        Create a placeholder that can receive a dragged parameter
        """
        index = len(self.placeholders)
        target = ParameterPlaceholder(self, index)
        self.GetSizer().Add(target, flag=wx.EXPAND)
        self.placeholders.append(target)

    def get_parameter_index(self, parameter_id):
        """
        Return the index of a parameter according to its ID
        """
        for i, parameter in enumerate(self.parameters):
            if parameter_id == parameter.id:
                return i

    def get_parameter_path(self, parameter_index):
        """
        Compute the path of a parameter based of its index in the parameters
        component.
        """
        tab_index = self.GetParent().GetPageIndex(self)
        return "{}/{}".format(tab_index, parameter_index)

    def delete_parameter(self, index):
        """
        Delete the parameter pointed by the "index" in the parameters component.
        Then the display of the parameters is updated. This function returns the
        deleted parameter.
        """
        param = self.parameters[index]
        del(self.parameters[index])
        self._update_parameter_display()
        return param

    def add_parameter(self, index, parameter):
        """
        Add the parameter at the specified index in the parameters component.
        Then the display of the parameters is updated.
        """
        self.parameters.insert(index, parameter)
        self._update_parameter_display()

    def add_parameters(self, parameter_list):
        """
        Add a list of parameter to the paramaters component in order that new
        parameters are displayed in the same order of the list of parameter and
        before the old parameters.
        """
        self.parameters = parameter_list + self.parameters
        self._update_parameter_display()

    def _update_parameter_display(self):
        """
        Refresh the display of list of parameters and placeholders
        """
        self.GetSizer().Clear()
        self._delete_placeholders()
        self.create_placeholder()
        for parameter in self.parameters:
            parameter.Reparent(self)
            self.GetSizer().Add(parameter, flag=wx.EXPAND)
            self.create_placeholder()
        self.Layout()
        self.PostSizeEvent()

    def _delete_placeholders(self):
        """
        Delete the placeholder list properly
        """
        for placeholder in self.placeholders:
            #placeholder.Destroy()
            placeholder.Hide()
        self.placeholders = []

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template
        """
        parameters_templates = []
        for param in self.parameters:
            parameters_templates.append(param.to_template())
        return parameters_templates

    def as_command(self):
        """
        This function return the part of the instruction it represents as a string
        """
        param_list = []
        for parameter in self.parameters:
            command = parameter.as_command()
            if not command == '':
                param_list.append(command)
        return ' '.join(param_list)
