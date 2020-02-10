import wx.lib.newevent
import wx

ValueChangedEvent, EVT_VALUE_CHANGED = wx.lib.newevent.NewCommandEvent()
AddTabEvent, EVT_ADD_TAB = wx.lib.newevent.NewCommandEvent()

def trigger_value_changed_event(origin):
    """
    Trigger a EVT_VALUE_CHANGED event that is propagatate to the top window.
    """
    event = ValueChangedEvent(origin.GetId())
    # Set the number of times the event must be propagate to 100 in order to be
    # sure the top level window is reached
    event.ResumePropagation(100)
    wx.PostEvent(origin.GetEventHandler(), event)

def trigger_add_tab_event(origin):
    """
    Trigger a EVT_ADD_TAB event that parent can catch.
    """
    event = AddTabEvent(origin.GetId())
    wx.PostEvent(origin.GetEventHandler(), event)
