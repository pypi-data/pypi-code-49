from ...event import event_handler
from wx import Panel, Button, StaticText
from .custom_collapsible_pane import CustomCollapsiblePane
import wx

class Serializable():

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template. Return nothing if no template should be written.
        """
        raise NotImplementedError

    def as_command(self):
        """
        This function return the part of the instruction it represents as a string.
        Return the empty string if no command should be build.
        """
        raise NotImplementedError

    def _trigger_change_event(self, event):
        """
        Trigger an event to notify that the command has to be refreshed
        """
        event_handler.trigger_value_changed_event(self)

class BaseComponent(CustomCollapsiblePane, Serializable):

    def __init__(self, parent, template, interface):

        super().__init__(parent, style=wx.TAB_TRAVERSAL)
        if "Option" in interface['type']:
            type = "Option: {}".format(interface['names'][0])
        else:
            type = interface['ID']
        name = "{}        \"{}\"".format(type, interface['help'])
        name = self.Ellipsize(name, wx.ScreenDC(), wx.ELLIPSIZE_END, 480)
        self.SetLabel(name)
        self.id = interface['ID']

        self.command = StaticText(self.GetPane(), label="")
        self.Bind(event_handler.EVT_VALUE_CHANGED, self.OnValueChanged)

        self.component_sizer = wx.BoxSizer(wx.VERTICAL)
        self.management_sizer = wx.BoxSizer(wx.VERTICAL)
        self.pane_sizer = wx.BoxSizer(wx.HORIZONTAL)
        global_sizer = wx.BoxSizer(wx.VERTICAL)
        self.GetPane().SetSizer(global_sizer)
        #self.GetPane().SetBackgroundColour("RED")
        self.pane_sizer.Add(self.component_sizer,flag=wx.ALL|wx.EXPAND, border=5, proportion=1)
        self.pane_sizer.Add(self.management_sizer, flag=wx.ALIGN_RIGHT|wx.ALL, border=5)

        global_sizer.Add(self.command,flag=wx.ALL|wx.EXPAND, border=5, proportion=1)
        global_sizer.Add(self.pane_sizer,flag=wx.ALL|wx.EXPAND)

        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnStateChange)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.HandleMouseEvent)
        self.Collapse(template['is_collapsed'])

        self.GetParent().Layout()
        self.GetParent().PostSizeEvent()

    def OnValueChanged(self, event):
        """
        Refresh the command label of the parameter and propaget the event to the
        top window.
        """
        event.Skip(True)
        self._refresh_command_label()

    def _refresh_command_label(self):
        """
        Update the label representing the command
        """
        self.command.SetLabel(self.get_command())

    def OnStateChange(self, sz):
        """
        This function is called when the collapsible pane is collapsed/uncollapse
        and is use to refresh the parent window.
        """
        self._trigger_change_event(None)
        super().OnStateChange(sz)

    def HandleMouseEvent(self, event):
        """
        Handle the mouse events in which this widget is interested in.
        """
        if event.ButtonDown(wx.MOUSE_BTN_LEFT):
            self._begin_drag_and_drop()
        elif event.Moving():
            self._change_cursor()

    def _begin_drag_and_drop(self):
        """
        It is called when the user begin a drag and drop action (left button
        mouse is kept down). It computes the data that will be send by the drag
        and drop.
        """
        # Create a Text Data Object, which holds the index of the parameter
        # that is to be dragged
        parameter_index = self.GetParent().get_parameter_index(self.id)
        parameter_path = self.GetParent().get_parameter_path(parameter_index)
        tdo = wx.TextDataObject(parameter_path)
        tds = wx.DropSource(self)
        tds.SetData(tdo)
        # Initiate the Drag Operation
        tds.DoDragDrop(True)

    def _change_cursor(self):
        """
        Change the default cursor to the "hand cursor" in order to indicate the
        user can interact (drag and drop) with the widget.
        """
        mouse_cursor = wx.Cursor(wx.CURSOR_HAND)
        self.SetCursor(mouse_cursor)

    def get_command(self):
        """
        This function return the commands the component must returned if the panel
        is not collapsed
        """
        raise NotImplementedError

    def as_command(self):
        if self.IsCollapsed():
            return ''
        else:
            return self.get_command()

    def to_template(self):
        return {"ID": self.id, 'is_collapsed':self.IsCollapsed()}
