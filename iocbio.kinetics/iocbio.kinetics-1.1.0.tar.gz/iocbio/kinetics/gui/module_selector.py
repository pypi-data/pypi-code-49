import os, sys, glob, copy
from PyQt5 import Qt, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets


class ListView(QListView):
    def __init__(self):
        super(ListView, self).__init__()

    def paintEvent(self, event):
        QListView.paintEvent(self,event)
        if (self.model() and self.model().rowCount(self.rootIndex()) > 0): return
        qp = QPainter(self.viewport())
        qp.drawText(self.rect(), QtCore.Qt.AlignCenter, "No Items");


class DeleteDialog(QDialog):
    def __init__(self, stringlist=[], checked=False, parent=None, ):

        super(DeleteDialog, self).__init__(parent)
        self.setWindowTitle('Select modules to delete')
        self.setGeometry(300, 300, 750, 250)
        self.model = QStandardItemModel()
        self.listView = ListView()
        for string in stringlist:
            item = QStandardItem(string)
            item.setText(string)
            item.setCheckable(True)
            check = \
                (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(check)
            self.model.appendRow(item)
        self.listView.setModel(self.model)
        cancelButton = QPushButton('Cancel')
        selectButton = QPushButton('Select All')
        unselectButton = QPushButton('Unselect All')
        deleteButton = QPushButton('Delete')
        #self.mlist=[]
        self.deletelist =[]

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)
        hbox.addWidget(selectButton)
        hbox.addWidget(unselectButton)
        hbox.addWidget(deleteButton)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        cancelButton.clicked.connect(self.reject)
        selectButton.clicked.connect(self.select)
        unselectButton.clicked.connect(self.unselect)
        deleteButton.clicked.connect(self.delete)


    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)

    def delete(self):

        self.choices = [self.model.item(i).index() for i in
                        range(self.model.rowCount())
                        if self.model.item(i).checkState()
                        == QtCore.Qt.Checked]
        self.deletelist =[self.model.item(i).text() for i in
                         range(self.model.rowCount())
                       if self.model.item(i).checkState()
                         == QtCore.Qt.Checked]
        for el in self.choices:
            self.model.clearItemData(el)

        #self.mlist = [self.model.item(i).text() for i in
         #                 range(self.model.rowCount())
          #            if not self.model.item(i).text() == '']

        self.show()
        self.accept()


class ChecklistDialog(QDialog):

    def __init__(self, moduledict, icon=None, parent=None):
        super(ChecklistDialog, self).__init__(parent)
        checked=False
        self.moduledict = copy.deepcopy(moduledict)
        self.icon = icon
        self.model = QStandardItemModel()
        self.listView = ListView()
        self.setGeometry(300, 300, 750, 250)
        self.modulelist = []
        for elem in self.moduledict:
            modul =elem['path']
            self.modulelist.append(modul)
            item = QStandardItem(modul)
            item.setCheckable(True)
            checked = elem['enabled']
            check = \
                (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(check)
            self.model.appendRow(item)

        self.listView.setModel(self.model)

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        selectButton = QPushButton('Select All')
        unselectButton = QPushButton('Unselect All')
        addButton = QPushButton('Add')
        deleteButton= QPushButton('Delete ...')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(selectButton)
        hbox.addWidget(unselectButton)
        hbox.addWidget(addButton)
        hbox.addWidget(deleteButton)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setWindowTitle('Folders with modules')
        if self.icon:
            self.setWindowIcon(self.icon)

        okButton.clicked.connect(self.onAccepted)
        cancelButton.clicked.connect(self.reject)
        selectButton.clicked.connect(self.select)
        unselectButton.clicked.connect(self.unselect)
        addButton.clicked.connect(self.onadd)
        deleteButton.clicked.connect(self.ondelete)



    def onAccepted(self):
        self.choices = [self.model.item(i).text() for i in
                        range(self.model.rowCount())
                        if self.model.item(i).checkState()
                        == QtCore.Qt.Checked]
        for elem in self.moduledict:
            if elem['path'] in self.choices:
                elem['enabled'] = True
            else:
                elem['enabled'] = False

        self.accept()


    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)


    def onadd(self):
        fname = str(QFileDialog.getExistingDirectory(self, caption = 'Select Folder'))
        if fname != '':
            item = QStandardItem(fname)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Checked)
            self.model.appendRow(item)
            self.modulelist.append(item.text())
            newmoduldict = {'path': fname, 'enabled' : True, 'nodelete': False}
            self.moduledict.append(newmoduldict)


    def ondelete(self):
        deletelist = []
        for elem in self.moduledict:
            if elem['nodelete'] == False:
                deletelist.append(elem['path'])

        dialog = DeleteDialog(deletelist, checked = False)
        if dialog.exec_() == QDialog.Accepted:
            for el in dialog.deletelist:
                self.modulelist.remove(el)
                item = self.model.findItems(el)[0]
                self.model.removeRow(item.row())
                self.moduledict = [i for i in self.moduledict if not (i['path'] == el)]

# Testing
if __name__ == '__main__':

    folders  = [{'path':'/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/spectro','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/respiration','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/misc','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/mechanics','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/electrophysiology','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/sysbio/confocal_catransient','enabled': True, 'nodelete' : True },
                {'path': '/home/mari/code/kinetics/iocbio/kinetics/modules/tutorial','enabled': False, 'nodelete' : False }]

    app = QApplication(sys.argv)
    form = ChecklistDialog(folders)
    if form.exec_()==QDialog.Accepted:
        print('form', form.moduledict)
