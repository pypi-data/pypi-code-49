import sys

from PyQt4 import QtGui, Qt, QtCore
from horno.utiles.IO import IOSistema
from horno.utiles.Singleton import Singleton


#=============================================================================================
class UIControles (metaclass=Singleton):
   
    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        ''

    #------------------------------------------------------------------------------------------
    def AgregarControles(self, ctl_padre, layout_padre, info_ctl_hijos, txt_padre=None, width_label=100, horz=True):
        
        if horz:
            layout_hijo = QtGui.QHBoxLayout()
        else:
            layout_hijo = QtGui.QVBoxLayout()
            
        layout_padre.addLayout(layout_hijo)

        if txt_padre:
            lbl_padre = QtGui.QLabel(txt_padre, ctl_padre)
            if width_label: lbl_padre.setFixedWidth(width_label)
            layout_hijo.addWidget(lbl_padre)

        for (txt_hijo, ctl_hijo) in info_ctl_hijos:
            if txt_hijo:
                lbl_hijo = QtGui.QLabel(txt_hijo, ctl_padre)
                if width_label: lbl_hijo.setFixedWidth(width_label)
                layout_hijo.addWidget(lbl_hijo)
            layout_hijo.addWidget(ctl_hijo)

    #------------------------------------------------------------------------------------------
    def GenerarControlMultiple(self, items_dict, items_checked=[], width=0, height=0):

        ctl_lista = Qt.QListView()
        model = Qt.QStandardItemModel(ctl_lista)

        items = sorted(items_dict.items(), key = lambda p: p[0])
        for (clave, valor) in items: 
            ctl_item = Qt.QStandardItem('%s | %s' % (clave, str(valor)))
            ctl_item.setFlags(Qt.Qt.ItemIsUserCheckable | Qt.Qt.ItemIsEnabled)
            ctl_item.setData(Qt.Qt.Checked if clave in items_checked else Qt.Qt.Unchecked, Qt.Qt.CheckStateRole)
            model.appendRow(ctl_item)
        
        ctl_lista.setModel(model)
        if width: ctl_lista.setFixedWidth(width)
        if height: ctl_lista.setFixedHeight(height)
        
        return ctl_lista      

    #------------------------------------------------------------------------------------------
    def MostrarMensaje(self, mensaje, tipo):
        
        if tipo == 'ERROR':
            mb = QtGui.QMessageBox(QtGui.QMessageBox.Critical, tipo, mensaje)
        elif tipo == 'WARNING':
            mb = QtGui.QMessageBox(QtGui.QMessageBox.Warning, tipo, mensaje)
        elif tipo == 'INFO':
            mb = QtGui.QMessageBox(QtGui.QMessageBox.Information, tipo, mensaje)
            
        mb.exec_()

#=============================================================================================
class UISalida ():
    
    #------------------------------------------------------------------------------------------
    def __init__(self, ui, ctl):
        
        self.ui = ui
        self.ctl = ctl

        self.ui.connect(self.ui, QtCore.SIGNAL('Print'), self.PrintUi)
    
    #------------------------------------------------------------------------------------------
    def PrintLine(self, texto):
        
        self.Print(texto + IOSistema().NewLine())

    #------------------------------------------------------------------------------------------
    def Print(self, texto):
        
        self.ui.emit(QtCore.SIGNAL('Print'), texto)

    #------------------------------------------------------------------------------------------
    def PrintUi(self, texto):
        
        texto_ant = str(self.ctl.toPlainText()).encode(sys.stdout.encoding, errors='replace')
        self.ctl.setText(texto_ant + texto)
        self.ctl.moveCursor(QtGui.QTextCursor.End)

