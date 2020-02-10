from ..utils import yaml
from .component import option_component, subcommand_component, argument_component, base_component, custom_notebook
from .component.parameter_component import ParametersComponent
from wx import Panel, Button
from ..event import event_handler
from ..template.template_generator import DefaultGenerator
import wx
from . import command_panel, information_panel


instance = None

class CommandNoteBook(Panel):

    def __init__(self, parent, cmd, template_file, interface_file):
        super(Panel, self).__init__(parent)
        global instance
        instance = self
        self.command = cmd
        self.other_tab = None
        self.notebook = custom_notebook.CustomNotebook(self)
        self.Bind(event_handler.EVT_ADD_TAB, self.OnAddTab, self.notebook)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        template = yaml.open_yaml(template_file)
        self.interface = yaml.open_yaml(interface_file)
        self._create_tabs(template)

        self.cmd_panel = command_panel.CommandPanel(self)
        info_panel = information_panel.InformationPanel(self, cmd)

        sizer.Add(info_panel, 1, wx.EXPAND)
        sizer.Add(self.notebook, 10 , wx.EXPAND)
        sizer.Add(self.cmd_panel, 1, wx.EXPAND )

        sizer.Layout()
        self.GetParent().Layout()

    def fill_template(self, complete_template):
        """
        Fill the template with the informations gathered by the "complete" option
        of the program.
        """
        for page in range(self.notebook.GetPageCount()):
            component = self.notebook.GetPage(page)
            for parameter in complete_template['Complete']:
                index = component.get_parameter_index(parameter['ID'])
                if not index is None:
                    component.delete_parameter(index)
        self._create_template_tabs(complete_template, select=True)
        event_handler.trigger_value_changed_event(self)

    def _create_tabs(self, template):
        """
        Create all the tabs according to the 'template' argument and create another
        tab caintaining all paramaters that doesn't appears in 'template'.
        """
        self._create_template_tabs(template)
        self._create_other_tab(template)

    def _create_template_tabs(self, template, select=False):
        """
        Create the tabs according to the template argument.
        """
        for tab_name in template:
            component = ParametersComponent(self.notebook, template[tab_name], self.interface)
            self.notebook.AddPage(component, tab_name, select=select)
            tab_index = self.notebook.GetPageCount()-1
            if tab_name == "Others":
                self.other_tab = self.notebook.GetPage(tab_index)
                self.notebook.SetCloseButton(tab_index, False)
            else:
                self.notebook.SetRenamable(tab_index, True)

    def _create_other_tab(self, template):
        """
        Create an "Others" tab that contains all the paramaters that are not listed
        in other tabs. If 'template' lists all parameters, this function does nothing.
        """
        if self.other_tab is None:
            other_param = self._get_unused_parameters(template)
            other_template = DefaultGenerator().generate_other_template(other_param)
            self._create_template_tabs(other_template)
            if len(other_param) < 1:
                self.notebook.HidePage(self.notebook.GetPageCount()-1, hidden=True)

    def delete_tab(self, tab_index):
        """
        Move the parameters of the "tab_index" tab to the "Others" tab. This
        funtion is meant to be called before deleting the "tab_index" tab.
        """
        deleted_tab = self.notebook.GetPage(tab_index)
        for parameter in deleted_tab.parameters:
            parameter.Collapse()
        self.other_tab.add_parameters(deleted_tab.parameters)
        self.notebook.HidePage(self.notebook.GetPageIndex(self.other_tab), hidden=False)

    def _get_unused_parameters(self, template):
        """
        Return all the parameters that doesn't appears in 'template'.
        """
        other_param = []
        for interface_paramater in self.interface:
            is_found = False
            for tab_name in template:
                for template_parameter in template[tab_name]:
                    if interface_paramater["ID"] == template_parameter["ID"]:
                        is_found = True
                        break
            if not is_found:
                other_param.append(interface_paramater)
        return other_param

    def _create_management_panel(self):
        """
        Create the panel containing the "add tabs" button.
        """
        panel = Panel(self)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)

        add_button = Button(self, label="Add a tab")
        self.Bind(wx.EVT_BUTTON, self.OnAddTab, add_button)

        sizer.Add(add_button, wx.ALIGN_LEFT)
        sizer.Layout()
        return panel

    def OnAddTab(self, event):
        """
        Display the form that allows the user the name of the new tab. It creates
        an empty tab if the user press the "OK" button.
        """
        dlg = wx.TextEntryDialog(self, "Choose the name of the new tab")
        if dlg.ShowModal() == wx.ID_OK:
            tab_name = dlg.GetValue()
            component = ParametersComponent(self.notebook, [], self.interface)
            self.notebook.AddPage(component, tab_name, select=True)
            self.cmd_panel.OnRefresh(None)
        dlg.Destroy()

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template
        """
        template = {}
        for page in range(self.notebook.GetPageCount()):
            if not self.notebook.GetHidden(page):
                tab_name = self.notebook.GetPageText(page)
                component = self.notebook.GetPage(page)
                template.update({tab_name:component.to_template()})
        return template

    def as_command(self):
        """
        This function return the part of the instruction it represents as a string
        """
        command = []
        for page in range(self.notebook.GetPageCount()):
            component = self.notebook.GetPage(page)
            command_part = component.as_command()
            if not command_part == '':
                command.append(command_part)
        return "{} {}".format(self.command, " ".join(command))
