# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/travis/build/randovania/randovania/randovania/gui/ui_files/game_input_dialog.ui',
# licensing of '/home/travis/build/randovania/randovania/randovania/gui/ui_files/game_input_dialog.ui' applies.
#
# Created: Sun Feb  9 23:18:38 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_GameInputDialog(object):
    def setupUi(self, GameInputDialog):
        GameInputDialog.setObjectName("GameInputDialog")
        GameInputDialog.resize(407, 243)
        self.gridLayout = QtWidgets.QGridLayout(GameInputDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.output_file_button = QtWidgets.QPushButton(GameInputDialog)
        self.output_file_button.setObjectName("output_file_button")
        self.gridLayout.addWidget(self.output_file_button, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 3)
        self.description_label = QtWidgets.QLabel(GameInputDialog)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.gridLayout.addWidget(self.description_label, 0, 0, 1, 3)
        self.input_file_button = QtWidgets.QPushButton(GameInputDialog)
        self.input_file_button.setObjectName("input_file_button")
        self.gridLayout.addWidget(self.input_file_button, 2, 2, 1, 1)
        self.accept_button = QtWidgets.QPushButton(GameInputDialog)
        self.accept_button.setObjectName("accept_button")
        self.gridLayout.addWidget(self.accept_button, 6, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(GameInputDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 6, 2, 1, 1)
        self.output_file_edit = QtWidgets.QLineEdit(GameInputDialog)
        self.output_file_edit.setObjectName("output_file_edit")
        self.gridLayout.addWidget(self.output_file_edit, 4, 0, 1, 2)
        self.input_file_edit = QtWidgets.QLineEdit(GameInputDialog)
        self.input_file_edit.setObjectName("input_file_edit")
        self.gridLayout.addWidget(self.input_file_edit, 2, 0, 1, 2)
        self.output_file_label = QtWidgets.QLabel(GameInputDialog)
        self.output_file_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.output_file_label.setObjectName("output_file_label")
        self.gridLayout.addWidget(self.output_file_label, 3, 0, 1, 2)
        self.input_file_label = QtWidgets.QLabel(GameInputDialog)
        self.input_file_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.input_file_label.setObjectName("input_file_label")
        self.gridLayout.addWidget(self.input_file_label, 1, 0, 1, 2)

        self.retranslateUi(GameInputDialog)
        QtCore.QMetaObject.connectSlotsByName(GameInputDialog)

    def retranslateUi(self, GameInputDialog):
        GameInputDialog.setWindowTitle(QtWidgets.QApplication.translate("GameInputDialog", "Game Patching", None, -1))
        self.output_file_button.setText(QtWidgets.QApplication.translate("GameInputDialog", "Select File", None, -1))
        self.description_label.setText(QtWidgets.QApplication.translate("GameInputDialog", "<html><head/><body><p>In order to create the randomized game, a ISO file of Metroid Prime 2: Echoes for the Nintendo Gamecube is necessary.</p><p>After using it once, a copy is kept by Randovania for later use.</p></body></html>", None, -1))
        self.input_file_button.setText(QtWidgets.QApplication.translate("GameInputDialog", "Select File", None, -1))
        self.accept_button.setText(QtWidgets.QApplication.translate("GameInputDialog", "Accept", None, -1))
        self.cancel_button.setText(QtWidgets.QApplication.translate("GameInputDialog", "Cancel", None, -1))
        self.output_file_edit.setPlaceholderText(QtWidgets.QApplication.translate("GameInputDialog", "Path where to place randomized game", None, -1))
        self.input_file_edit.setPlaceholderText(QtWidgets.QApplication.translate("GameInputDialog", "Path to vanilla Gamecube ISO", None, -1))
        self.output_file_label.setText(QtWidgets.QApplication.translate("GameInputDialog", "Output File", None, -1))
        self.input_file_label.setText(QtWidgets.QApplication.translate("GameInputDialog", "Input File (Vanilla Gamecube ISO)", None, -1))

