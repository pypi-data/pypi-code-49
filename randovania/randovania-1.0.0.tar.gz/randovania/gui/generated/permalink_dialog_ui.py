# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/travis/build/randovania/randovania/randovania/gui/ui_files/permalink_dialog.ui',
# licensing of '/home/travis/build/randovania/randovania/randovania/gui/ui_files/permalink_dialog.ui' applies.
#
# Created: Sun Feb  9 23:18:38 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PermalinkDialog(object):
    def setupUi(self, PermalinkDialog):
        PermalinkDialog.setObjectName("PermalinkDialog")
        PermalinkDialog.resize(539, 117)
        self.gridLayout = QtWidgets.QGridLayout(PermalinkDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.accept_button = QtWidgets.QPushButton(PermalinkDialog)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout.addWidget(self.accept_button, 5, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(PermalinkDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 5, 2, 1, 1)
        self.description_label = QtWidgets.QLabel(PermalinkDialog)
        self.description_label.setObjectName("description_label")
        self.gridLayout.addWidget(self.description_label, 1, 0, 1, 2)
        self.paste_button = QtWidgets.QPushButton(PermalinkDialog)
        self.paste_button.setObjectName("paste_button")
        self.gridLayout.addWidget(self.paste_button, 1, 2, 1, 1)
        self.permalink_edit = QtWidgets.QLineEdit(PermalinkDialog)
        self.permalink_edit.setObjectName("permalink_edit")
        self.gridLayout.addWidget(self.permalink_edit, 4, 0, 1, 3)

        self.retranslateUi(PermalinkDialog)
        QtCore.QMetaObject.connectSlotsByName(PermalinkDialog)

    def retranslateUi(self, PermalinkDialog):
        PermalinkDialog.setWindowTitle(QtWidgets.QApplication.translate("PermalinkDialog", "Import permalink", None, -1))
        self.accept_button.setText(QtWidgets.QApplication.translate("PermalinkDialog", "Accept", None, -1))
        self.cancel_button.setText(QtWidgets.QApplication.translate("PermalinkDialog", "Cancel", None, -1))
        self.description_label.setText(QtWidgets.QApplication.translate("PermalinkDialog", "<html><head/><body><p>Import a permalink that was shared by someone else.</p></body></html>", None, -1))
        self.paste_button.setText(QtWidgets.QApplication.translate("PermalinkDialog", "Paste", None, -1))
        self.permalink_edit.setPlaceholderText(QtWidgets.QApplication.translate("PermalinkDialog", "Permalink", None, -1))

