from PySide2.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QPlainTextEdit
from PySide2.QtGui import QTextDocument, QTextCursor
from PySide2 import QtWidgets
from PySide2.QtCore import QSize, Signal, QRegularExpression


class SearchHitDialog(QDialog):
    _instance = None

    _object = None

    @classmethod
    def getInstance(cls):
        if not cls._object:
            cls._object = SearchHitDialog()
        return cls._object

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SearchHitDialog, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    def init(self, edit: QPlainTextEdit):
        self.edit = edit

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("检索")
        self.initView()
        size = QSize()
        size.setHeight(200)
        size.setWidth(450)
        self.setFixedSize(size)

    def initView(self):
        label = QLabel()
        label.setText("搜索关键词：")
        self.input = QLineEdit()
        searchForString = QPushButton("字符搜索")
        searchForRegex = QPushButton("正则搜索")
        searchForRegex.clicked.connect(self.clickRegex)
        searchForString.clicked.connect(self.clickString)

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(label, 0, 0, 1, 1)
        mainLayout.addWidget(self.input, 0, 1, 1, 5)
        mainLayout.addWidget(searchForString, 2, 4, 1, 2)
        mainLayout.addWidget(searchForRegex, 3, 4, 1, 2)

        self.setLayout(mainLayout)

    def clickRegex(self):
        searchTxt = self.input.text()
        if len(searchTxt) <= 0:
            return
        expression = QRegularExpression(searchTxt)
        if not self.edit.find(expression):
            cursor: QTextCursor = self.edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            self.edit.setTextCursor(cursor)

    def clickString(self):
        searchTxt = self.input.text()
        if len(searchTxt) <= 0:
            return
        if not self.edit.find(searchTxt):
            cursor: QTextCursor = self.edit.textCursor()
            cursor.movePosition(QTextCursor.Start)
            self.edit.setTextCursor(cursor)
