import re

from PyQt4 import QtGui, QtCore
from horno.datos.Encoding import Encoding
from horno.utiles.IO import IOSistema


#==============================================================================================================================
class VistaGraficaBase (QtGui.QWidget):
    
    #------------------------------------------------------------------------------------------
    def __init__(self, controlador, args=[]):

        self._controlador = controlador
        self._args = args
        self._app = QtGui.QApplication(self._args)
        self._helper = VistaGraficaHelper(self)
        QtGui.QWidget.__init__(self)

    #------------------------------------------------------------------------------------------
    def Mostrar(self):
        
        self._app.setActiveWindow(self)
        self.show()
        self._app.exec_()

    #---------------------------------------------------------------------------------------------------------
    def Notificar(self, signal, pars=None):

        self.emit(QtCore.SIGNAL(signal), *pars)

    #---------------------------------------------------------------------------------------------------------
    def ConectarEvento(self, signal, callback):

        self.connect(self, QtCore.SIGNAL(signal), callback)
            

#==============================================================================================================================
class VistaGraficaHelper:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, padre):
        
        self._padre = padre

    #------------------------------------------------------------------------------------------
    def AgregarLayout(self, padre, horz):
        
        layout = QtGui.QHBoxLayout() if horz else QtGui.QVBoxLayout()
        try: 
            padre.addLayout(layout)
        except:
            padre.setLayout(layout)
            
        return layout

    #------------------------------------------------------------------------------------------
    def AgregarWidget(self, padre, widget, horz, texto):
        
        layout = self.AgregarLayout(padre, horz)

        if texto:
            lbl = QtGui.QLabel(texto)
            layout.addWidget(lbl)

        wgt = widget
        layout.addWidget(wgt)
        return [lbl, wgt]

    #------------------------------------------------------------------------------------------
    def AgregarTab(self, padre, texto, w=None, h=None):
        
        tab = QtGui.QWidget()
        if w: tab.setMaximumWidth(w)
        if h: tab.setMaximumHeight(h)
        padre.addTab(tab, texto)
        return tab

    #------------------------------------------------------------------------------------------
    def AgregarTexto(self, padre, horz, texto, readonly=False, w=None, h=None):

        layout = self.AgregarLayout(padre, horz)
        lbl = QtGui.QLabel(texto)
        layout.addWidget(lbl)

        txt = QtGui.QTextEdit()
        if w: txt.setFixedWidth(w)
        if h: txt.setFixedHeight(h)
        txt.setReadOnly(readonly)
        txt.setAlignment(QtCore.Qt.AlignTop)
        layout.addWidget(txt)
        return [lbl, txt]

    #------------------------------------------------------------------------------------------
    def AgregarWeb(self, padre, horz, texto, w=None, h=None):

        layout = self.AgregarLayout(padre, horz)
        lbl = QtGui.QLabel(texto)
        layout.addWidget(lbl)

        from PyQt4.QtWebKit import QWebView
        
        web = QWebView()
        if w: web.setFixedWidth(w)
        if h: web.setFixedHeight(h)
        layout.addWidget(web)
        return [lbl, web]

    #------------------------------------------------------------------------------------------
    def AgregarBoton(self, padre, texto, callback):

        btn = QtGui.QPushButton(texto)
        btn.clicked.connect(callback)
        padre.addWidget(btn)
        return btn

    #------------------------------------------------------------------------------------------
    def AgregarLista(self, padre, horz, texto, callback):
        
        layout = self.AgregarLayout(padre, horz)
        lbl = QtGui.QLabel(texto)
        layout.addWidget(lbl)
        
        lst = QtGui.QListWidget()
        lst.currentItemChanged.connect(callback)
        layout.addWidget(lst)
        return [lbl, lst]

    #------------------------------------------------------------------------------------------
    def AgregarTabla(self, padre, horz, texto):

        layout = self.AgregarLayout(padre, horz)
        lbl = QtGui.QLabel(texto)
        layout.addWidget(lbl)

        tbl = QtGui.QTableWidget()
        layout.addWidget(tbl)
        return [lbl, tbl]

    #------------------------------------------------------------------------------------------
    def CargarLista(self, lst, items):

        lst.clear()
        for item in items:
            lst.addItem(item)

    #------------------------------------------------------------------------------------------
    def CargarTabla(self, tbl, columnas, filas):

        if not columnas:
            columnas = ['(vacio)']

        tbl.setRowCount(len(filas))
        tbl.setColumnCount(len(columnas))
        tbl.setHorizontalHeaderLabels(columnas)
        for n, fila in enumerate(filas):
            for i, d in enumerate(fila):
                d_str = Encoding().ToUnicode(d, 'utf-8') if d else ''
                item = QtGui.QTableWidgetItem(d_str)
                item.setToolTip(d_str)
                tbl.setItem(n, i, item)
            
    #------------------------------------------------------------------------------------------
    def GuardarTabla(self, tbl, ruta_csv):
        
        sep = ','
        quo = '"'
        
        with open(ruta_csv, 'wb') as io:
            
            columnas = [self.AUnicode(tbl.horizontalHeaderItem(i).text()) for i in range(tbl.columnCount())]
            
            header = sep.join([quo + c.replace(quo, quo * 2) + quo for c in columnas])
            io.write(Encoding().ToString(header + '\n'))
            
            for f in range(tbl.rowCount()):
                fila = []
                for c in range(tbl.columnCount()):
                    item = tbl.item(f, c)
                    fila.append(self.AUnicode(item.text()) if item is not None else '')
                
                datos = sep.join([quo + d.replace(quo, quo * 2) + quo for d in fila])
                io.write(Encoding().ToString(datos + '\n'))
                                
    #------------------------------------------------------------------------------------------
    def ObtenerTabla(self, tbl):
        
        res = []
        
        for f in range(tbl.rowCount()):
            fila = []
            for c in range(tbl.columnCount()):
                item = tbl.item(f, c)
                fila.append(self.AUnicode(item.text()).strip() if item is not None else '')
            res.append(fila)
            
        return res
                                
    #------------------------------------------------------------------------------------------
    def ObtenerTexto(self, txt, selected=False, solo_ascii=False):

        valor = ''
        if selected: valor = self.AUnicode(txt.textCursor().selectedText())
        if not selected or not valor: valor = self.AUnicode(txt.toPlainText())
        if solo_ascii: valor = re.sub(r'[^\x00-\x7F]+',' ', valor)
        return valor

    #------------------------------------------------------------------------------------------
    def SetearTexto(self, ctl, valor):

        ctl.setText(valor)

    #------------------------------------------------------------------------------------------
    def SetearEstilo(self, ctl, estilo):

        ctl.setStyleSheet("QWidget {color:%s}" % (estilo))

    #------------------------------------------------------------------------------------------
    def SetearHabilitado(self, ctl, valor):

        ctl.setEnabled(valor)

    #------------------------------------------------------------------------------------------
    def ObtenerItem(self, lst):

        item = lst.currentItem()
        valor = str(item.text()) if item else ''
        return valor

    #------------------------------------------------------------------------------------------
    def AUnicode(self, txt):
        
        return txt # unicode(txt)
        

#==============================================================================================================================
class VistaConsolaBase (object):
    
    #------------------------------------------------------------------------------------------
    def __init__(self, controlador, args=[]):

        self._controlador = controlador
        self._args = args
        
    #------------------------------------------------------------------------------------------
    def Mostrar(self):
        
        IOSistema().PrintLine('Hola, soy una VistaConsolaBase y me estoy mostrando')

