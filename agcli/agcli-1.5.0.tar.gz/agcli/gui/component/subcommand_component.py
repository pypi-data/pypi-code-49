import wx
from wx import ComboBox, Panel
from .base_component import BaseComponent, Serializable
from .. import command_notebook

class Subcommand(BaseComponent):

    def __init__(self, parent, template_subcommand, interface):
        super().__init__(parent, template_subcommand, interface)
        self.name = interface['name']
        self.checkbox = wx.CheckBox(self.GetPane(), label=self.name)
        self.checkbox.SetToolTip(interface['help'])
        self.checkbox.SetValue(template_subcommand['is_checked'])
        self.Bind(wx.EVT_CHECKBOX, self._trigger_change_event, self.checkbox)
        self.component_sizer.Add(self.checkbox)
        self._refresh_command_label()
        self.refresh_collapse()
        self.GetParent().Layout()

    def get_command(self):
        if self.checkbox.GetValue():
            return self.name
        else:
            return ''

    def to_template(self):
        template = super().to_template()
        template['is_checked'] = self.checkbox.GetValue()
        return template
