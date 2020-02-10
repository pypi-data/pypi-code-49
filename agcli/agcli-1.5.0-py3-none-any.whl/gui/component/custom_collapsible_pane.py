import wx
from wx import CollapsiblePane


class CustomCollapsiblePane(CollapsiblePane):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.OnStateChange)

    def OnStateChange(self, sz):
        """
        This function is called when the collapsible pane is collapsed/uncollapse
        and is use to refresh the parent window.
        """
        self.GetParent().PostSizeEvent()
        self.GetParent().Layout()

    def refresh_collapse(self):
        """
        Force the widget to compute the size of an expanded panel because the
        size of the panel is not good if it is expanded before other widgets are
        added.
        """
        self.Collapse(not self.IsCollapsed())
        self.Collapse(not self.IsCollapsed())
