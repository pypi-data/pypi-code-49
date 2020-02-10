import wx
import os
from ..docparser import docopt_parser
from ..docparser.docparser import NoVersionFoundError, CommandNotFoundError
from . import command_notebook
from ..utils import yaml
from ..utils import file_handler as fh
from wx.lib.dialogs import ScrolledMessageDialog


class MainWindow(wx.Frame):

    def __init__(self, cmd):
        self.app = wx.App()
        self.command = cmd
        self.template_dir = fh.file_handler.get_template_directory()
        self.interface_file = fh.file_handler.get_interface_file()
        self.default_template_file = fh.file_handler.get_default_template_file()
        self.current_template = self.default_template_file

        wx.Frame.__init__(self, None, title="AGCLI", size=(720, 480))
        self.pane = wx.Panel(self)
        self.pane_sizer = wx.BoxSizer()
        self.pane.SetSizer(self.pane_sizer)

        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        fileMenu = wx.Menu()
        menuOpen = fileMenu.Append(wx.ID_OPEN, "&Open"," Open another template")
        menuSave = fileMenu.Append(wx.ID_SAVE, "&Save"," Save in the current template")
        menuSaveAs = fileMenu.Append(wx.ID_SAVEAS, "&Save as"," Save in a new template")
        menuExit = fileMenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

        helpMenu = wx.Menu()
        menuCmdHelp = helpMenu.Append(wx.ID_HELP, "&Command help"," Show the command help")
        menuCmdVersion = helpMenu.Append(wx.ID_VIEW_DETAILS, "&Command version"," Show the command version")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnCmdHelp, menuCmdHelp)
        self.Bind(wx.EVT_MENU, self.OnCmdVersion, menuCmdVersion)

        # Create main panel
        self.command_tab = command_notebook.CommandNoteBook(self.pane,
         self.command, self.default_template_file, self.interface_file)
        self.pane_sizer.Add(self.command_tab, 1, wx.EXPAND)

        self.pane_sizer.Layout()

    def start_GUI(self):
        self.Show()
        self.app.MainLoop()

    def OnCmdVersion(self, e):
        """
        Display the version of the command currently processed in a new window
        """
        parser = docopt_parser.DocoptParser(self.command)
        try:
            version = parser.get_command_version()
        except NoVersionFoundError as e:
            version = "No version information available for this command."
        dlg =ScrolledMessageDialog(self, version,
         "Version information of {}".format(self.command), size=(600, 300))
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnCmdHelp(self, e):
        """
        Display the documentation of the command currently processed in a new window
        """
        try:
            parser = docopt_parser.DocoptParser(self.command)
            help_ = parser.get_command_doc()
        except CommandNotFoundError as e:
            help_ = "No help found for this command"
        dlg = ScrolledMessageDialog(self, help_,
         "Help for {}".format(self.command), size=(600, 300))
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        """
        Close the program
        """
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """
        Open a new window that lets the user choose a template file to load and
        to process. Theses files has to be in the YAML format.
        """
        dlg = wx.FileDialog(self, "Choose a file", self.template_dir, "", "YAML files (*.yaml;*.yml)|*.yaml;*.yml", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            template_file = os.path.join(self.dirname, self.filename)
            self.current_template = template_file
            self.pane_sizer.Hide(0)
            self.pane_sizer.Remove(0)
            self.command_tab.Destroy()
            self.command_tab = command_notebook.CommandNoteBook(self.pane,
             self.command, template_file, self.interface_file)
            self.pane_sizer.Insert(0, self.command_tab, 1, wx.EXPAND)
            self.pane_sizer.Layout()
        dlg.Destroy()

    def _save_template(self, template_file):
        """
        Save the current template to the 'template_file' file
        """
        template_data = self.command_tab.to_template()
        yaml.write_yaml(template_file, template_data)

    def OnSave(self, e):
        """
        Save the edited template to the current template file
        """
        self._save_template(self.current_template)

    def OnSaveAs(self, e):
        """
        Save the edited template to a file choosen by the user
        """
        dlg = wx.FileDialog(self, "Choose a file", self.template_dir, "", "YAML files (*.yaml;*.yml)|*.yaml;*.yml", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            if not (self.filename.endswith(".yaml") or self.filename.endswith(".yml")):
                self.filename += '.yaml'
            self.dirname = dlg.GetDirectory()
            template_file = os.path.join(self.dirname, self.filename)
            self._save_template(template_file)
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Sample editor")
    app.MainLoop()
