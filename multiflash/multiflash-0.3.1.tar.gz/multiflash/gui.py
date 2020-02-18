# Copyright 2020 John Reese
# Licensed under the MIT License

import random

from PySide2 import QtCore, QtWidgets


class MultiflashWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello world", "Hallo welt", "Hola mundo"]
        self.button = QtWidgets.QPushButton("Click")
        self.text = QtWidgets.QLabel("Hello world")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


def start():
    app = QtWidgets.QApplication([])
    window = MultiflashWidget()
    window.resize(1600, 900)
    window.show()
    return app.exec_()
