import wx
import sys
from wx import Panel, TextCtrl, Button, Slider, SpinCtrl
from ...event import event_handler


class Widget(Panel):

    def __init__(self, parent, alignment):
        super().__init__(parent)
        self.sizer = wx.BoxSizer(alignment)
        self.SetSizer(self.sizer)

    def add_components(self, *args):
        """
        Add the 'args' component to the main sizer
        """
        for arg in args:
            self.sizer.Add(arg, proportion=1)
        self.sizer.Layout()

    def get_value(self):
        """
        Return the value represented by the widget
        """
        raise NotImplementedError

    def OnValueChanged(self, _event):
        """
        Trigger a EVT_VALUE_CHANGED event that parent can catch. Subclass must
        call this function themself when the value of the widget is changed.
        """
        event_handler.trigger_value_changed_event(self)

class FileChooser(Widget):

    def __init__(self, parent, value=""):
        super().__init__(parent, wx.HORIZONTAL)
        self.text = TextCtrl(self, value=value, style=wx.TE_READONLY)
        self.file_button = Button(self, label="Choose a file")
        self.Bind(wx.EVT_BUTTON, self.OnChooseFile, self.file_button)
        self.GetSizer().Add(self.text, proportion=1)
        self.GetSizer().Add(self.file_button)

    def OnChooseFile(self, event):
        """
        Open a new window that allow the user to choose a file
        """
        dlg = wx.FileDialog(self, message="Choose a file",
         defaultFile=self.get_value(), style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.OnValueChanged(None)
            choosen_file = dlg.GetPath().replace(' ', '\ ')
            self.text.ChangeValue(choosen_file)

    def get_value(self):
        return self.text.GetLineText(0)

class DirectoryChooser(Widget):

    def __init__(self, parent, value=""):
        super().__init__(parent, wx.HORIZONTAL)
        self.text = TextCtrl(self, value=value, style=wx.TE_READONLY)
        self.file_button = Button(self, label="Choose a directory")
        self.Bind(wx.EVT_BUTTON, self.OnChooseFile, self.file_button)
        self.GetSizer().Add(self.text, proportion=1)
        self.GetSizer().Add(self.file_button)

    def OnChooseFile(self, event):
        """
        Open a new window that allow the user to choose a directory
        """
        dlg = wx.DirDialog(self, message="Choose a directory",
         defaultPath=self.get_value(), style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.OnValueChanged(None)
            choosen_file = dlg.GetPath().replace(' ', '\ ')
            self.text.ChangeValue(choosen_file)

    def get_value(self):
        return self.text.GetLineText(0)

class TextField(Widget):

    def __init__(self, parent, value=""):
        super().__init__(parent, wx.HORIZONTAL)
        self.text = TextCtrl(self, value=str(value))
        self.add_components(self.text)
        self.Bind(wx.EVT_TEXT, self.OnValueChanged, self.text)

    def get_value(self):
        value = self.text.GetLineText(0)
        if ' ' in value:
            return '\"{}\"'.format(value)
        else:
            return value

class PercentageSlider(Widget):

    def __init__(self, parent, value=0.):
        super().__init__(parent, wx.HORIZONTAL)
        value = float(value)
        current_percentage = int(value*100)
        self.slider = Slider(self, value=current_percentage, size=wx.Size(200, 30))
        self.GetSizer().Add(self.slider, proportion=1)
        self.Bind(wx.EVT_SLIDER, self.OnValueChanged, self.slider)

    def get_value(self):
        return self.slider.GetValue() /100.

class IntegerField(Widget):

    def __init__(self, parent, value=0):
        super().__init__(parent, wx.HORIZONTAL)
        # SpinCtrl are not usable in our context because they NEED a min and a max value
        self.spin = SpinCtrl(self, initial=int(value), min=-1000000, max=1000000)
        self.add_components(self.spin)
        self.Bind(wx.EVT_SPINCTRL, self.OnValueChanged, self.spin)
        self.Bind(wx.EVT_TEXT, self.OnValueChanged, self.spin)

    def get_value(self):
        return self.spin.GetValue()


_type_to_widget = {
    "String": TextField,
    "File": FileChooser,
    "Directory": DirectoryChooser,
    "Percentage": PercentageSlider,
    "Integer": IntegerField
}

def create_widget(type_, parent, **kwargs):
    """
    Create a widget according to the type it represents
    """
    widget = _type_to_widget[type_]
    return widget(parent, **kwargs)
