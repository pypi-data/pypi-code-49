# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tcpServer(object):
    def setupUi(self, tcpServer):
        tcpServer.setObjectName("tcpServer")
        tcpServer.resize(579, 136)
        self.gridLayout = QtWidgets.QGridLayout(tcpServer)
        self.gridLayout.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(tcpServer)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.plainTextEditDebug = QtWidgets.QPlainTextEdit(tcpServer)
        self.plainTextEditDebug.setPlainText("")
        self.plainTextEditDebug.setObjectName("plainTextEditDebug")
        self.gridLayout.addWidget(self.plainTextEditDebug, 1, 4, 5, 1)
        self.lineEditPort = QtWidgets.QLineEdit(tcpServer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPort.sizePolicy().hasHeightForWidth())
        self.lineEditPort.setSizePolicy(sizePolicy)
        self.lineEditPort.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditPort.setObjectName("lineEditPort")
        self.gridLayout.addWidget(self.lineEditPort, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(tcpServer)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 6, 1)
        self.label_2 = QtWidgets.QLabel(tcpServer)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        self.lineEditIP = QtWidgets.QLineEdit(tcpServer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditIP.sizePolicy().hasHeightForWidth())
        self.lineEditIP.setSizePolicy(sizePolicy)
        self.lineEditIP.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditIP.setObjectName("lineEditIP")
        self.gridLayout.addWidget(self.lineEditIP, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(tcpServer)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnStart = QtWidgets.QPushButton(tcpServer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 4, 1, 1, 1)
        self.label_3.setBuddy(self.lineEditIP)
        self.label_2.setBuddy(self.lineEditPort)
        self.label.setBuddy(self.lineEditIP)

        self.retranslateUi(tcpServer)
        QtCore.QMetaObject.connectSlotsByName(tcpServer)

    def retranslateUi(self, tcpServer):
        _translate = QtCore.QCoreApplication.translate
        tcpServer.setWindowTitle(_translate("tcpServer", "start the server"))
        self.label_3.setText(_translate("tcpServer", "Logs:"))
        self.lineEditPort.setText(_translate("tcpServer", "5004"))
        self.label_2.setText(_translate("tcpServer", "&port"))
        self.lineEditIP.setText(_translate("tcpServer", "192.168.99.235"))
        self.label.setText(_translate("tcpServer", "&IP"))
        self.btnStart.setText(_translate("tcpServer", "start server"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tcpServer = QtWidgets.QWidget()
    ui = Ui_tcpServer()
    ui.setupUi(tcpServer)
    tcpServer.show()
    sys.exit(app.exec_())
