import wx
from wx import Panel, CheckBox, SpinCtrl
from ..component.base_component import Serializable

class OptionName(Panel, Serializable):

    def __init__(self, parent, option_name, template_option, callback_func):
        super().__init__(parent)
        self.callback_func = callback_func
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)
        self.label = option_name
        self.checkbox = CheckBox(self, label=self.label)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckBox, self.checkbox)
        self.spin_ctrl = SpinCtrl(self, value='1', min=1, max=10)
        self.Bind(wx.EVT_SPINCTRL, self.OnSpinCtrl, self.spin_ctrl)

        self.checkbox.SetValue(template_option['is_checked'])
        self.spin_ctrl.SetValue(template_option['repeat'])

        sizer.Add(self.checkbox, 1, wx.ALL)
        sizer.Add(self.spin_ctrl, 1, wx.ALL)

    def is_short(self):
        """
        Return true iff this object represents a short option.
        """
        return len(self.label)==2 and self.label.startswith('-')

    def is_long(self):
        """
        Return true iff this object represents a long option.
        """
        return self.label.startswith('--')

    def is_bsd(self):
        """
        Return true iff this object represents a BSD option.
        """
        return len(self.label)==1

    def is_checked(self):
        """
        Return true iff this option is checked.
        """
        return self.checkbox.GetValue()

    def check(self, is_check):
        """
        Check the option's checkbox if "is_check" is True, uncheck it otherwise.
        This option does not call the callback function
        """
        self.checkbox.SetValue(is_check)

    def OnCheckBox(self, event):
        """
        This function is called when the user check/uncheck the checkbox.
        Call the callback function and trigger a CHANGE_VALUE_EVENT for the top window.
        """
        self.callback_func(event)
        self._trigger_change_event(event)

    def OnSpinCtrl(self, event):
        """
        This function is called when the user change the value in the spin control.
        It checks the checkbox and then call the "OnCheckBox" function.
        """
        self.check(True)
        event.SetId(self.checkbox.GetId())
        self.OnCheckBox(event)

    def as_command(self):
        if self.is_checked():
            if self.is_bsd():
                return self.label * self.spin_ctrl.GetValue()
            elif self.is_long():
                return ' '.join([self.label for i in range(self.spin_ctrl.GetValue())])
            elif self.is_short:
                return '-' + self.label.split('-')[-1]*self.spin_ctrl.GetValue()
        return ''

    def to_template(self):
        return {'repeat':self.spin_ctrl.GetValue(), 'is_checked':self.is_checked()}

class OptionArgumentName(OptionName):

    def __init__(self, parent, option_name, template_option, callback_func):
        super().__init__(parent, option_name, template_option, callback_func)
        self.spin_ctrl.Disable()
