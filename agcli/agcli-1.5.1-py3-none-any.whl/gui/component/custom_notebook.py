import wx
import os
from wx.lib.agw.aui.auibook import AuiNotebook, EVT_AUINOTEBOOK_PAGE_CLOSED, AUI_BUTTON_CLOSE, AUI_NB_TAB_SPLIT, AUI_NB_CLOSE_ON_ALL_TABS
from wx.lib.agw.aui.tabart import VC71TabArt
from ...event import event_handler
from ..drag_and_drop import TabDropTarget
import pkg_resources

class CustomNotebook(AuiNotebook):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        # DO not use os.path.join because it does not represent an os path
        bmp_location = '/'.join(["assets", "+.bmp"])
        bmp_file = pkg_resources.resource_filename('agcli', bmp_location)
        bitmap = wx.Bitmap()
        bitmap.LoadFile(bmp_file)
        self.SetArtProvider(VC71TabArt())
        self.add_button_ID = wx.NewId()
        self.AddTabAreaButton(self.add_button_ID, wx.RIGHT, name="+",
                                normal_bitmap=bitmap,
                                disabled_bitmap=bitmap)
        self.SetAGWWindowStyleFlag(self.GetAGWWindowStyleFlag() | AUI_NB_CLOSE_ON_ALL_TABS)

    def InitNotebook(self, agwStyle):
        super().InitNotebook(agwStyle)
        self.Bind(EVT_AUINOTEBOOK_PAGE_CLOSED, self.OnTabClosed,
                  id=wx.ID_ANY)
        # Make tabs receive drop informations for drag and drop
        new_tab = self.GetActiveTabCtrl()
        tab_drop_target = TabDropTarget(new_tab)
        new_tab.SetDropTarget(tab_drop_target)

    def OnTabClosed(self, event):
        """
        Trigger an EVT_VALUE_CHANGED event when a tab is closed and prepare the
        concerned tab to be deleted.
        """
        event_handler.trigger_value_changed_event(self)
        self.GetParent().delete_tab(event.GetSelection())

    def OnTabEndDrag(self, event):
        """
        Trigger an EVT_VALUE_CHANGED event when a tab is moved
        """
        event_handler.trigger_value_changed_event(self)

    def OnTabButton(self, event):
        """
        Manage the addition of a new tab
        """
        super().OnTabButton(event)
        if event.GetInt() == self.add_button_ID:
            event_handler.trigger_add_tab_event(self)

    def move_parameter(self, from_path, to_path):
        """
        Move the parameter pointed by the "from_path" to the place pointed by
         the "to_path". "from_path" and "to_path" are both of the form
         "{tab_index}/{parameter_index}" where "tab_index" is the index of the
         tab and "parameter_index" is the index of the parameter in the
         "tab_index" tab.
        """
        if self._is_move_required(from_path, to_path):
            converted_to_path = self._convert_dest_path(from_path, to_path)
            parameter = self._delete_parameter(from_path)
            self._add_parameter(converted_to_path, parameter)
            self.SetSelection(int(converted_to_path.split('/')[0]))
            event_handler.trigger_value_changed_event(self)

    def _is_move_required(self, from_path, to_path):
        """
        Return false iif a parameter is asked to move on the same tab and in an
        adjacent placeholder
        """
        is_in_same_tab = self._is_in_same_tab(from_path, to_path)
        is_adjacent_placeholder = self._is_adjacent_placeholder(from_path, to_path)
        return not (is_in_same_tab and is_adjacent_placeholder)

    def _is_in_same_tab(self, from_path, to_path):
        """
        Return true iif the two paths refers to two location in the same tab
        """
        from_tab_index = int(from_path.split('/')[0])
        to_tab_index = int(to_path.split('/')[0])
        return from_tab_index == to_tab_index

    def _is_adjacent_placeholder(self, from_path, to_path):
        """
        Return True iif the parameter index of "from_path" and "to_path" point
         to adjacent place INDEPENDENTLY of the tab index of these paths.
        """
        from_parameter_index = int(from_path.split('/')[1])
        to_parameter_index = int(to_path.split('/')[1])
        # The destination above a parameter has the same index as it.
        # The destination under a parameter has the same index as it plus one.
        return (
                from_parameter_index+1 == to_parameter_index or
                from_parameter_index == to_parameter_index
                )

    def _convert_dest_path(self, from_path, to_path):
        """
        Convert the "to_path" in order that he still points the right index after
        the removal of the parameter pointed by the "from_path".
        """
        if not self._is_in_same_tab(from_path, to_path):
            return to_path
        else:
            from_parameter_index = int(from_path.split('/')[1])
            to_parameter_index = int(to_path.split('/')[1])
            if from_parameter_index < to_parameter_index:
                return "{}/{}".format(to_path.split('/')[0], to_parameter_index-1)
            else:
                return to_path

    def _add_parameter(self, path, parameter):
        """
        Add the parameter at the specified "path". "from_path" and "to_path" are
         both of the form "{tab_index}/{parameter_index}" where "tab_index" is
         the index of the tab and "parameter_index" is the index of the
         parameter in the "tab_index" tab.
        """
        to_tab_index = int(path.split('/')[0])
        to_parameter_index = int(path.split('/')[1])
        for tab_index in range(self.GetPageCount()):
            if tab_index == to_tab_index:
                parameter_component = self.GetPage(tab_index)
                parameter_component.add_parameter(to_parameter_index, parameter)

    def _delete_parameter(self, path):
        """
        Deleted the parameter pointed by the path
        """
        from_tab_index = int(path.split('/')[0])
        from_parameter_index = int(path.split('/')[1])
        for tab_index in range(self.GetPageCount()):
            if tab_index == from_tab_index:
                parameter_component = self.GetPage(tab_index)
                return parameter_component.delete_parameter(from_parameter_index)
