from orangewidget import widget, gui
from orangewidget.settings import Setting


class OWWidgetName(widget.OWBaseWidget):
    name = "Widget Name"
    id = "orangewidget.widget_category.widget_name"
    description = ""
    icon = "icons/Unknown.svg"
    priority = 10
    category = ""
    keywords = ["list", "of", "keywords"]
    want_main_area = False
    outputs = [("Name", type)]
    inputs = [("Name", type, "handler")]

    foo = Setting(True)

    def __init__(self):
        super().__init__()

        # controls
        gui.rubber(self.controlArea)
