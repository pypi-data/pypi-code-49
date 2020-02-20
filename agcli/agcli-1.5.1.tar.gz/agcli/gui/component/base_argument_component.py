import wx
from ...event import event_handler
from wx import CheckBox, Panel, Button, ComboBox
from wx.lib.agw.pycollapsiblepane import PyCollapsiblePane
from ...interface.interface_generator import types
from . import custom_widget
from .base_component import BaseComponent


class BaseArgumentComponent(BaseComponent):

    def __init__(self, parent, template, interface):
        super().__init__(parent, template, interface)
        self.widget_type = template['argument_type']
        self._create_management_panel()
        self.widget_sizer = wx.BoxSizer(wx.VERTICAL)

        self.argument_components = []
        self._create_component_list(template)
        self.refresh_collapse()

    def _create_management_panel(self):
        """
        Create the panel containing the checkbox , the add button and the remove
        button. It also creates the combobox that allow to modify the types of
        the widgets.
        """
        add_button = Button(self.GetPane(), label="+")
        self.Bind(wx.EVT_BUTTON, self.OnAddWidget, add_button)
        self.management_sizer.Add(add_button, flag=wx.ALL, border=2)
        remove_button = Button(self.GetPane(), label="-")
        self.Bind(wx.EVT_BUTTON, self.onRemoveWidget,remove_button)
        self.management_sizer.Add(remove_button, flag=wx.ALL, border=2)
        self.change_type_button = ComboBox(self.GetPane(), choices=types,
            value=self.widget_type, style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.OnChangeType, self.change_type_button)
        self.management_sizer.Add(self.change_type_button, flag=wx.ALL, border=2)

    def OnChangeType(self, event):
        """
        Is called when the user change the type of the widgets. It changes the
        old widgets by new ones with the good type.
        """
        self.widget_type = self.change_type_button.GetValue()
        self.widget_sizer.Clear()
        number_arguments = len(self.argument_components)
        self._clear_argument_components()
        for i in range(number_arguments):
            self._create_component()
        self.refresh_collapse()
        self.GetParent().PostSizeEvent()
        self._trigger_change_event(None)

    def _clear_argument_components(self):
        """
        Properly remove all the items in "self.argument_components" and destroy
        all of it.
        """
        for i in range(len(self.argument_components)):
            self.argument_components[i].Destroy()
        self.argument_components = []

    def OnAddWidget(self, event):
        """
        Add a widget to the argument
        """
        component = self._create_component()
        self.refresh_collapse()
        self.GetParent().PostSizeEvent()
        self._trigger_change_event(None)

    def onRemoveWidget(self, event):
        """
        Remove a widget from the argument.
        It ensures at least one widget remains.
        """
        # This condition ensure it has at least 1 widget
        if len(self.argument_components) > 1:
            # The 2 following lines hides and remove the last argument component
            # controls of index 0 is the management_panel
            self.widget_sizer.Remove(len(self.argument_components)-1)
            self.argument_components[-1].Destroy()
            self.argument_components.pop()
            self.refresh_collapse()
            self.GetParent().PostSizeEvent()
            self._trigger_change_event(None)

    def onValueChanged(self, event):
        """
        This function is called when the value of a widget is changed. It checks
        the checkbox related to this widget and propagate the event to the top window.
        """
        event.Skip(True)

    def _create_component_list(self, template):
        """
        Create the checkbox for the component.
        Also create one component by value specified in "template['values']". Each component contains
        one value in "values". It also create an additional empty component.
        """
        sizer = self._create_component_sizer()
        self.component_sizer.Add(sizer, flag=wx.ALL|wx.EXPAND, proportion=1)

        if len(template['values']) > 0:
            for value in template['values']:
                self._create_component(value)
        else:
            self._create_component()

    def _create_component_sizer(self):
        return self.widget_sizer

    def _create_component(self, value=None):
        """
        Create a single argument component with "value" as value. If "value"
        is None then the default value is used. The default value depends on
        the argument type
        """
        if value is None:
            component = custom_widget.create_widget(self.widget_type, self.GetPane())
        else:
            component = custom_widget.create_widget(self.widget_type, self.GetPane(), value=value)
        self.Bind(event_handler.EVT_VALUE_CHANGED, self.onValueChanged, component)
        self.widget_sizer.Add(component, proportion=1, flag=wx.ALL|wx.EXPAND, border=2)
        self.argument_components.append(component)

    def to_template(self):
        """
        This function translate the object into a template dict in order to ease
        the writing of yaml template
        """
        template = super().to_template()
        values = []
        for component in self.argument_components:
            values.append(component.get_value())
        template.update({'is_checked': self.is_checked(), 'values': values,
            'argument_type':self.widget_type})
        return template

    def get_command(self):
        """
        This function return the part of the instruction it represents as a string
        """
        values = []
        if not self.is_checked():
            return ''
        for component in self.argument_components:
            values.append(str(component.get_value()))
        return ' '.join(values)

    def is_checked(self):
        """
        Return true if this parameteris selected by the user, i.e. the command
        generate by this parameter must appear in the final command
        """
        raise NotImplementedError
