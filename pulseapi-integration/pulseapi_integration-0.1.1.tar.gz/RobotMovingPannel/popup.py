from PyQt5 import QtCore, QtGui, QtWidgets

class PopUp_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(345, 125)
        self.label_messege = QtWidgets.QLabel(Dialog)
        self.label_messege.setGeometry(QtCore.QRect(10, 20, 321, 31))
        self.label_messege.setObjectName("label_messege")
        self.agry_button = QtWidgets.QPushButton(Dialog)
        self.agry_button.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.agry_button.setObjectName("agry_button")
        self.disagry_button = QtWidgets.QPushButton(Dialog)
        self.disagry_button.setGeometry(QtCore.QRect(260, 90, 75, 23))
        self.disagry_button.setObjectName("disagry_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_messege.setText(_translate("Dialog", "TextLabel"))
        self.agry_button.setText(_translate("Dialog", "PushButton"))
        self.disagry_button.setText(_translate("Dialog", "PushButton"))
