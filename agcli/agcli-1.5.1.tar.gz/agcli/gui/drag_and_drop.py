import wx
from wx import TextDropTarget, Window


class BlankDropTarget(TextDropTarget):
    """ This object implements Drop Target functionality for windows """

    def __init__(self, parameter_component, place_holder):
        super().__init__()
        self.place_holder = place_holder
        self.parameter_component = parameter_component

    def OnDropText(self, x, y, from_path):
        """ Implement Text Drop """
        to_path = self.parameter_component.get_parameter_path(self.place_holder.index)
        self.parameter_component.GetParent().move_parameter(from_path, to_path)
        return True

class ParameterPlaceholder(Window):
    """ This object implements Drop Target functionality for windows """

    def __init__(self, parent, index):
        super().__init__(parent)
        self.index = index
        self.SetDropTarget(BlankDropTarget(parent, self))
        self.SetBackgroundColour(wx.BLACK)
        self.SetMinSize(wx.Size(10, 10))

class TabDropTarget(TextDropTarget):

    def __init__(self, tab_control):
        super().__init__()
        self.tab_control = tab_control

    def OnDropText(self, x, y, from_path):
        """ Implement Text Drop """
        parameter_component = self.tab_control.GetPointedToTab()
        if parameter_component is None:
            return False
        else:
            to_path = parameter_component.get_parameter_path(0)
            parameter_component.GetParent().move_parameter(from_path, to_path)
            return True
