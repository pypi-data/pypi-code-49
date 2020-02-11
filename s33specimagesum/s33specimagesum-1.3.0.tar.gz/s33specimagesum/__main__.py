'''
 Copyright (c) 2019, UChicago Argonne, LLC
 See LICENSE file.
'''
from s33specimagesum.mainwindow import MainWindow
from PyQt5.Qt import QApplication
import sys

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()    