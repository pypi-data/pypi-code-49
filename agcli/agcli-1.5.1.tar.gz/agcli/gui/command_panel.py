import wx
from wx import Panel, Button, TextCtrl, StaticText, CheckBox
from wx.lib.dialogs import ScrolledMessageDialog
from ..utils import terminal
from ..event import event_handler


class CommandPanel(Panel):

    def __init__(self, parent):
        """
        Create the panel that handles the display of the build command and the
         buttons that allows the user to refresh, copy or execute this command.
        """
        super().__init__(parent)
        main_sizer =  wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        first_line_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(main_sizer)

        label = StaticText(self, label='Command:')
        self.checkbox = CheckBox(self, label="Read only")
        self.checkbox.SetValue(True)
        self.checkbox.SetToolTip("If unchecked, consistancy between the GUI and the command is not guaranteed.")
        self.refresh_button = Button(self, label="Refresh")
        self.refresh_button.Disable()

        self.command_field = TextCtrl(self, value=self.GetParent().as_command(), style=wx.TE_READONLY)
        exec_button = Button(self, label="Run")
        terminal_button = Button(self, label="Run in Terminal")
        copy_button = Button(self, label="Copy to clipboard")

        self.checkbox.Bind(wx.EVT_CHECKBOX, self.OnCheckbox)
        self.refresh_button.Bind(wx.EVT_BUTTON, self.OnRefresh)
        self.GetParent().Bind(event_handler.EVT_VALUE_CHANGED, self.OnRefresh, id=wx.ID_ANY)
        self.Bind(wx.EVT_BUTTON, self.OnTerminal, terminal_button)
        self.Bind(wx.EVT_BUTTON, self.OnCopy, copy_button)
        self.Bind(wx.EVT_BUTTON, self.OnExec, exec_button)


        button_sizer.Add(exec_button, 1, wx.EXPAND)
        button_sizer.Add(terminal_button, 1, wx.EXPAND)
        button_sizer.Add(copy_button, 1, wx.EXPAND)
        first_line_sizer.Add(label, 1, flag=wx.ALIGN_LEFT|wx.ALL|wx.EXPAND)
        first_line_sizer.Add(self.checkbox, flag=wx.ALIGN_RIGHT|wx.ALL, border=2)
        first_line_sizer.Add(self.refresh_button, flag=wx.ALIGN_RIGHT|wx.ALL, border=2)
        main_sizer.Add(first_line_sizer, 1, wx.EXPAND)
        main_sizer.Add(self.command_field, 1, wx.EXPAND)
        main_sizer.Add(button_sizer, 1, wx.EXPAND)
        main_sizer.Layout()

    def OnCheckbox(self, event):
        if self.checkbox.IsChecked():
            self.refresh_button.Disable()
            self.command_field.SetWindowStyle(wx.TE_READONLY)
        else:
            self.refresh_button.Enable()
            # 0 is the default window style
            self.command_field.SetWindowStyle(0)

    def OnTerminal(self, event):
        """
        Execute the build command and display the result in the current CLi.
        """
        terminal.to_cli(self.command_field.GetValue(), pipe=False, timeout=None)

    def OnExec(self, event):
        """
        Execute the build command and display the result in a popup window.
        """
        output = self._exec_command(self.command_field.GetValue())
        dlg = ScrolledMessageDialog(self, output,
         "Output of the command:", size=(600, 300))
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def _exec_command(self, command):
        """
        Execute a command and return its result.
        """
        returncode, stdout, stderr = terminal.to_cli(command)
        if returncode == 0:
            return stdout
        else:
            return stderr

    def OnCopy(self, event):
        """
        Copy the build command into the clipboard.
        """
        clipdata = wx.TextDataObject()
        clipdata.SetText(self.command_field.GetValue())
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(clipdata)
        wx.TheClipboard.Close()

    def OnRefresh(self, event):
        """
        Refresh the display of the build command.
        """
        self.command_field.ChangeValue(self.GetParent().as_command())
