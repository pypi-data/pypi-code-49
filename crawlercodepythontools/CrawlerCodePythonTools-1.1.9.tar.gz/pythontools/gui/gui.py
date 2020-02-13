from PyQt5 import QtWidgets, QtGui
import sys

class App(object):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def setSysExitOperationToAppExit(self):
        sys.exit(self.app.exec_())

class Dialog(object):

    def __init__(self, name, width, height, onClose=None):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle(name)
        self.dialog.setFixedSize(width, height)
        self.buttons = []
        self.labels = []
        self.editlines = []
        if onClose is not None:
            self.dialog.closeEvent = onClose


    def createButton(self, name, pos, on_click, font_size=10, size=(80, 30), color=None, ):
        button = QtWidgets.QPushButton(name, self.dialog)
        button.move(pos[0], pos[1])
        button.setFixedSize(size[0], size[1])
        button.setFont(QtGui.QFont("Time", font_size, QtGui.QFont.Normal))
        button.clicked.connect(on_click)
        if color is not None:
            button.setStyleSheet("QPushButton { color: " + color + "; }")
        self.buttons.append(button)
        return button

    def createLabel(self, text, pos, font_size=10, size=(200, 30), color=None, style="normal"):
        label = QtWidgets.QLabel(self.dialog)
        label.move(pos[0], pos[1])
        label.setFixedSize(size[0], size[1])
        if style == "bold":
            style = QtGui.QFont.Bold
        else:
            style = QtGui.QFont.Normal
        label.setFont(QtGui.QFont("Time", font_size, style))
        label.setText(text)
        if color is not None:
            label.setStyleSheet("QLabel { color: " + color + "; }")
        self.labels.append(label)
        return label

    def createEditLine(self, pos, on_change=None, font_size=10, size=(120, 30)):
        editline = QtWidgets.QLineEdit(self.dialog)
        editline.move(pos[0], pos[1])
        editline.setFixedSize(size[0], size[1])
        editline.setFont(QtGui.QFont("Time", font_size, QtGui.QFont.Normal))
        if on_change is not None:
            editline.textChanged.connect(on_change)
        self.editlines.append(editline)
        return editline

    def openFileDialog(self, name, file="", validFiles="All Files (*)"):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.dialog, name, file, validFiles, options=options)
        if fileName:
            return fileName
        return None

    def saveFileDialog(self, name, file="", validFiles="All Files (*)"):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.dialog, name, file, validFiles, options=options)
        if fileName:
            return fileName
        return None

    def show(self):
        self.dialog.show()