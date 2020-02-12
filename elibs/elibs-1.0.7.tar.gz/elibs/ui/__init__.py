from wx import *

ICON = None


class MainApp(App):
    def __init__(self, parent):
        super(MainApp, self).__init__()
        self.parent = parent


class MainWindow(Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.SetIcon(ICON)
