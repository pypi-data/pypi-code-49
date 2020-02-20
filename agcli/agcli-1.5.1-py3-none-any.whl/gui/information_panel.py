import wx
from ..utils import terminal
from .component.custom_collapsible_pane import CustomCollapsiblePane

MAX_INFORMATION_LINE = 7

class InformationPanel(CustomCollapsiblePane):

    def __init__(self, parent, command_name):
        super().__init__(parent, label="Short help")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.GetPane().SetSizer(sizer)
        info_message = self._get_info_message(command_name)
        self.SetLabel(info_message.split('\n')[0])
        static_text = wx.StaticText(self.GetPane(), label=info_message)
        sizer.Add(static_text, flag=wx.EXPAND|wx.ALL, border=5, proportion=1)
        self.GetParent().Layout()
        self.GetParent().PostSizeEvent()

    def _get_info_message(self, cmd):
        """
        Retrieve the help message of the command and format it to take the summary
        part of the help. If the command doesn't support the "--help" option,
        only "cmd" is returned.
        """
        return_code, out, err = terminal.to_cli("{} --help".format(cmd))
        if return_code == 0:
            info_message = out.split('\n\n')[0]
        else:
            info_message = cmd
        info_message.strip()
        info_message = self._cut_info_message(info_message)
        return info_message

    def _cut_info_message(self, message):
        """
        Cut the message to only show a particular number of lines.
        """
        info_line = message.split("\n")
        if len(info_line) >= MAX_INFORMATION_LINE:
            info_line = info_line[:MAX_INFORMATION_LINE] + ["..."]
        return "\n".join(info_line)
