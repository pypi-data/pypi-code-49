import wx
from .base_argument_component import BaseArgumentComponent
from .. import command_notebook
from wx import CheckBox, Panel, Button, ComboBox
from wx.lib.scrolledpanel import ScrolledPanel
from ...event import event_handler


class ArgumentComponent(BaseArgumentComponent):

    def __init__(self, parent, template, interface):
        self.frame = parent
        self.name = interface['name']
        self.id = interface['ID']
        self.template = template

        super().__init__(parent, template, interface)
        self.SetToolTip(interface['help'])

        self.GetPane().Layout()
        self.GetParent().PostSizeEvent()
        self.GetParent().Layout()

    def _create_component_sizer(self):
        wrap_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.checkbox = CheckBox(self.GetPane(), label=self.name)
        self.Bind(wx.EVT_CHECKBOX, self._trigger_change_event, self.checkbox)
        self.checkbox.SetValue(self.template['is_checked'])
        wrap_sizer.Add(self.checkbox, flag=wx.ALL|wx.ALIGN_LEFT, border=5)
        wrap_sizer.Add(self.widget_sizer, proportion=1, flag=wx.ALL)
        return wrap_sizer

    def onValueChanged(self, event):
        """
        This function is called when the value of a widget is changed. It checks
        the checkbox related to this widget and propagate the event to the top window.
        """
        super().onValueChanged(event)
        self.checkbox.SetValue(True)

    def is_checked(self):
        """
        Return True if the checkbox is checked, False otherwise.
        """
        return self.checkbox.IsChecked()
