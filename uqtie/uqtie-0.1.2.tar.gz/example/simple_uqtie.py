#!/usr/bin/env python3
"""
Example app that does nothing. You can select the font
from the File menu, or zoom via the View menu.
"""

import argparse, sys

from   uqtie           import UqtWin
from   PyQt5.QtWidgets import QApplication, QVBoxLayout

class TestAppMainWindow(UqtWin.MainWindow):

    def __init__(self, parsedArgs, **kwargs ):
        super(TestAppMainWindow, self).__init__(parsedArgs, **kwargs)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        vbox = QVBoxLayout(self.centralWidget())

        # Here you can add widgets to the vbox layout
        # ... etc.

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--test', help='Test Argument placeholder', default='Test')
    parsedArgs,unparsedArgs = parser.parse_known_args()

    # Pass unparsed args to Qt, might have some X Windows args, like --display
    qtArgs = sys.argv[:1] + unparsedArgs
    app = QApplication(qtArgs)

    # can add optional title='OptionalTitle' if it is different from your app name
    mainw = TestAppMainWindow(parsedArgs, app=app, organizationName='Craton', appName='UqtTest')

    sys.exit(app.exec_())
