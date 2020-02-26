"""
Editor for the ArrayViewer
"""
# Author: Alex Schwarz <alex.schwarz@informatik.tu-chemnitz.de>

from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QPushButton, QWidget, QTableView, QVBoxLayout
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
import sys
import numpy as np

# data = np.array([['1','2','3','4'],
#                   ['1','2','1','3'],
#                   ['1','1','2','1']])
data = np.array([[1,2,3,4],
                 [1,2,1,3],
                 [1,1,2,1]])

class numpyModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def changeDatatype(self, newtype):
        try:
            self._data = self._data.astype(newtype)
        except ValueError:
            try:
                self._data = self._data.astype(float).astype(newtype)
            except ValueError:
                return False
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def setData(self, index, value, role=Qt.EditRole):
        try:
            if (self._data.dtype == int):
                self._data[index.row(), index.column()] = int(float(value))
            else:
                self._data[index.row(), index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        except ValueError:
            return False

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role in [Qt.DisplayRole, Qt.EditRole]:
            return QVariant(str(self._data[index.row()][index.column()]))


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("")
    CWgt = QWidget(window)
    window.setCentralWidget(CWgt)
    QFra = QVBoxLayout(CWgt)

    table = QTableView()
    model = numpyModel(data, table)
    table.setModel(model)
    table.resizeColumnsToContents()
    table.resizeRowsToContents()
    QFra.addWidget(table)

    pushBtn = QPushButton("Show me the data")
    pushBtn.clicked.connect(lambda: print(repr(model._data)))
    QFra.addWidget(pushBtn)

    typeComb = QComboBox()
    typeComb.addItems(['int', 'float', 'str'])
    typeComb.currentIndexChanged.connect(lambda i: model.changeDatatype(typeComb.itemText(i)))
    QFra.addWidget(typeComb)

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
