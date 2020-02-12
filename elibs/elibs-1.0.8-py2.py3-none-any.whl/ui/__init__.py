from wx import *

ICON = None


class MainApp(App):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(args, kwargs)


class MainWindow(Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.SetIcon(ICON)
