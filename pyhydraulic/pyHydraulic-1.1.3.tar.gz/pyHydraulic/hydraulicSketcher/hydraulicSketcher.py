import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication, QListView, QListWidgetItem, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot, QSize, QEvent, Qt, QMimeData
from PyQt5.QtGui import QIcon, QDrag
from mainWindow_ui import Ui_MainWindow
from pyHydraulic.node_graphics_node import NODE_TYPES,componentsLib, QAbstractGraphicsNode
from pyHydraulic.node_graphics_edge import QDMGraphicsEdge
from pyHydraulic.node_node import  Node
from pyHydraulic.node_edge import Edge
import os
import json

DEBUG = True
class mainWindow_logical(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.name_company = '燕山大学-南京工程学院联合研究院'
        self.name_product = '液压编辑器'
        self.version = 1.0

        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.insertNodesQIcon() # 插入图标



        # 选中绘图中的信号
        self.mainWindow.nodeEditor.view.sceneItemSelected.connect(self.onItemSelected)
        self.mainWindow.nodeEditor.view.sceneItemSelected[str].connect(self.onItemSelected_str)




    def setTitle(self):
        title = "[Hydraulic Skechter] - "
        title += self.getCurrentNodeEditorWidget().getUserFriendlyFilename()
        self.setWindowTitle(title)



    # 获取nodeEditor控件对象
    def getCurrentNodeEditorWidget(self):
        return self.mainWindow.nodeEditor

    # 获取是否当前图改变了,如果改变了返回True
    def isModified(self):
        return self.getCurrentNodeEditorWidget().scene.has_been_modified

    # 判断存储
    def maybeSave(self):
        # return not self.isModified()
        # 如果已经存储过了
        if not self.isModified():
            return True
        # 如果已经改动，且没有存储过
        res = QMessageBox.warning(self, "About to loose your work?",
                "The document has been modified.\n Do you want to save your changes?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
              )

        if res == QMessageBox.Save:
            return self.on_actionSave_triggered()
        elif res == QMessageBox.Cancel:
            return False

        return True

        # 2019.8.12 添加
    # 插入listWidget菜单,并设置拖放模式
    def initListWidget(self, listWidget):
        # 使用QListView显示图标
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setIconSize(QSize(60, 60))
        listWidget.setGridSize(QSize(80, 80))
        # 设置QListView大小改变时，图标的调整模式，默认是固定的，但可以改成自动调整
        listWidget.setResizeMode(QListView.Adjust)
        # 设置图标可不可以移动，默认是可移动的，但可以改成静态的
        listWidget.setMovement(QListView.Static)

        # 添加list的拖拽过滤器，将其事件上交给父控件
        # self.mainWindow.listWidgetPump.installEventFilter(self)
        listWidget.setDragEnabled(True)
        listWidget.setDragDropMode(QAbstractItemView.DragOnly)  # list仅为只托不放
    # 根据nameList添加对应名称QIcon进入listWidget
    def addQIcon2ListWidget(self,nameList, listWidget):
        for node_name in nameList:
            addItem = QListWidgetItem(node_name)
            # addItem.setIcon(QIcon("./images/flow meter.png"))
            current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录, 非工作目录
            path = current_work_dir + "/images/" + node_name + ".png"

            addItem.setIcon(QIcon(path))
            listWidget.addItem(addItem)

    def insertNodesQIcon(self):
        # 初始化各个listWidget
        self.initListWidget(self.mainWindow.listWidgetDynamic)
        self.initListWidget(self.mainWindow.listWidgetExecutive)
        self.initListWidget(self.mainWindow.listWidgetControl)
        self.initListWidget(self.mainWindow.listWidgetAuxiliary)
        # 根据各个元件分类列表，添加图标
        self.addQIcon2ListWidget(componentsLib.getSecondListByName("dynamic components"),self.mainWindow.listWidgetDynamic)
        self.addQIcon2ListWidget(componentsLib.getSecondListByName("executive components"),self.mainWindow.listWidgetExecutive)
        self.addQIcon2ListWidget(componentsLib.getSecondListByName("control components"),self.mainWindow.listWidgetControl)
        self.addQIcon2ListWidget(componentsLib.getSecondListByName("auxiliary components"),self.mainWindow.listWidgetAuxiliary)

##################下面是action的动作###########

    # 这里放置除主窗口以外的事件
    # def eventFilter(self, watched, event):
    #     if (watched is self.mainWindow.listWidgetPump):
    #         print(event.type())
    #         if(event.type() == QEvent.MouseButtonPress):
    #             print("MouseButtonPress")
    #
    #             self.on_listWidgetump_mouseMove(event)
    #
    #     return super().eventFilter(watched, event)

    # # 把选中的控件名字放入数据，发送给drop site
    def on_listWidgetDynamic_itemPressed(self,item):
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(item.text())  # 把选中的控件名字放入数据，发送给drop site
        drag.setMimeData(mimedata)
        drag.exec_()  # exec()函数并不会阻塞主函数

    def on_listWidgetExecutive_itemPressed(self, item):
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(item.text())  # 把选中的控件名字放入数据，发送给drop site
        drag.setMimeData(mimedata)
        drag.exec_()  # exec()函数并不会阻塞主函数

    def on_listWidgetControl_itemPressed(self, item):
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(item.text())  # 把选中的控件名字放入数据，发送给drop site
        drag.setMimeData(mimedata)
        drag.exec_()  # exec()函数并不会阻塞主函数

    def on_listWidgetAuxiliary_itemPressed(self, item):
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(item.text())  # 把选中的控件名字放入数据，发送给drop site
        drag.setMimeData(mimedata)
        drag.exec_()  # exec()函数并不会阻塞主函数



    @pyqtSlot()
    def on_actionAbout_HS_triggered(self):
        print("on_actionAbout_HS_triggered")

        QMessageBox.warning(self, "关于本程序:" + str(self.version),
                            "本程序由“燕山大学-南京工程学院”采用python编写, 仅供学习，\n请勿用于商业目的，weChat联系人：leebjtu", QMessageBox.Ok)

    @pyqtSlot()
    def on_actionFileOpen_triggered(self):
        if self.maybeSave():
            fname, filter = QFileDialog.getOpenFileName(self, 'Open graph from file')

            if fname != '' and os.path.isfile(fname):
                self.getCurrentNodeEditorWidget().fileLoad(fname)
                self.setTitle()


    @pyqtSlot()
    def on_actionNew_triggered(self):
        if self.maybeSave(): # 如果已经存储过了
            self.getCurrentNodeEditorWidget().fileNew()
            self.setTitle()

    @pyqtSlot()
    def on_actionSave_triggered(self):
        if self.getCurrentNodeEditorWidget().filename is None: return self.on_actionSave_as_triggered()
        self.getCurrentNodeEditorWidget().fileSave()
        self.statusBar().showMessage("Successfully saved %s" % self.getCurrentNodeEditorWidget().filename)
        self.setTitle()
        return True

    @pyqtSlot()
    def on_actionSave_as_triggered(self):
        fname, filter = QFileDialog.getSaveFileName(self, 'Save graph to file')
        if fname == '':
            return False
        self.getCurrentNodeEditorWidget().fileSave(fname)
        self.statusBar().showMessage("Successfully saved as %s" % self.getCurrentNodeEditorWidget().filename)
        self.setTitle()
        return True

    def closeEvent(self, event):

        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_actionHS_help_triggered(self):
        import webbrowser
        webbrowser.open("https://pypi.org/project/pyHydraulic/")

    @pyqtSlot()
    def on_actionUndo_triggered(self):
        self.getCurrentNodeEditorWidget().scene.history.undo()

    @pyqtSlot()
    def on_actionRedo_triggered(self):
        self.getCurrentNodeEditorWidget().scene.history.redo()

    @pyqtSlot()
    def on_actionDelete_triggered(self):
        self.getCurrentNodeEditorWidget().scene.grScene.views()[0].deleteSelected()

    @pyqtSlot()
    def on_actionRotate_P90_triggered(self):
        self.getCurrentNodeEditorWidget().scene.grScene.views()[0].rotateSelected(90)

    @pyqtSlot()
    def on_actionRotate_N90_triggered(self):
        self.getCurrentNodeEditorWidget().scene.grScene.views()[0].rotateSelected(90)

    @pyqtSlot()
    def on_actionscalePlus_triggered(self):
        self.getCurrentNodeEditorWidget().scene.grScene.views()[0].scaleSelected(0.01)

    @pyqtSlot()
    def on_actionScaleMinus_triggered(self):
        self.getCurrentNodeEditorWidget().scene.grScene.views()[0].scaleSelected(-0.01)

    @pyqtSlot()
    def on_actionCut_triggered(self):
        data = self.getCurrentNodeEditorWidget().scene.clipboard.serializeSelected(delete=True)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    @pyqtSlot()
    def on_actionCopy_triggered(self):
        data = self.getCurrentNodeEditorWidget().scene.clipboard.serializeSelected(delete=False)
        str_data = json.dumps(data, indent=4)
        QApplication.instance().clipboard().setText(str_data)

    @pyqtSlot()
    def on_actionPaste_triggered(self):
        raw_data = QApplication.instance().clipboard().text()

        try:
            data = json.loads(raw_data)
        except ValueError as e:
            print("Pasting of not valid json data!", e)
            return

        # check if the json data are correct
        if 'nodes' not in data:
            print("JSON does not contain any nodes!")
            return

        self.getCurrentNodeEditorWidget().scene.clipboard.deserializeFromClipboard(data)

    @pyqtSlot()
    def on_actionselectAll_triggered(self):
        self.getCurrentNodeEditorWidget().selectAll()

    # 选中图中的某个绘图元素，item为其中绘图元素对象
    def onItemSelected_str(self, str):
        # 选中空对象时，清除表格
        self.mainWindow.tableWidget.clearContents()
    # 如果选中的是item对象
    def onItemSelected(self, item):

        itemType =""
        id = ""
        if isinstance(item, QAbstractGraphicsNode):   # 如果选中的是node对象或者子对象
            itemType = item.node._node_type
            id = item.node.id



        elif isinstance(item, QDMGraphicsEdge):  # 如果选中的是edge对象
            itemType = item.edge.edge_type
            id = item.edge.id
        # 填格子之前，把格子都清空，并清除选中格子状态
        self.mainWindow.tableWidget.clearContents()


        dictProperty = item.getProperty()  # 返回选中的元素的属性字典

        # 下面开始填格子
        self.mainWindow.tableWidget.setColumnCount(2) # 设置2列
        self.mainWindow.tableWidget.setHorizontalHeaderLabels(["Property", "value"]) # 设置标题
        self.mainWindow.tableWidget.setRowCount(len(dictProperty)) # 设置行，行数为属性个数
        row = 0

        for key, value in dictProperty.items():
            # 属性格子
            keynewItem = QTableWidgetItem(key)
            keynewItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            keynewItem.setForeground(Qt.lightGray)
            font = keynewItem.font()
            font.setBold(True)
            keynewItem.setFont(font)
            keynewItem.setFlags(Qt.ItemIsEditable|Qt.ItemIsSelectable)
            keynewItem.setBackground(Qt.black)
            self.mainWindow.tableWidget.setItem(row, 0, keynewItem)

            # 值格子
            valuenewItem = QTableWidgetItem(str(value))
            valuenewItem.setForeground(Qt.white)
            valuenewItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.mainWindow.tableWidget.setItem(row, 1, valuenewItem)

            if key == "id": # 如果是id格子，就不可写
                valuenewItem.setFlags(Qt.ItemIsEditable)
                valuenewItem.setForeground(Qt.lightGray)

            row = row + 1


    def on_tableWidget_cellChanged(self, row, column):
        currentItem = self.mainWindow.tableWidget.item(row, column)

        if (currentItem.isSelected()):
        # row 和column都是从0开始
        # print("row :%s, colum :%s"%(row,column))
        # self.mainWindow.tableWidget
        #     if(column == 1 and self.mainWindow.tableWidget.rowCount()>=2):
            idItem = self.mainWindow.tableWidget.item(1, 1)

            if( idItem != None):
                id = int(idItem.text())
                node = self.mainWindow.nodeEditor.getObjectByID(id) # 通过id获得node对象

                if(isinstance(node, Node)):
                    keyItem = self.mainWindow.tableWidget.item(row, column-1)
                    valueItem = self.mainWindow.tableWidget.item(row, column)
                    if hasattr(node.grNode, keyItem.text()): # 检查类是否有属性
                        valueText = valueItem.text()
                        try:
                            value = float(valueItem.text())
                            setattr(node.grNode, keyItem.text(), value)
                        except ValueError:
                            setattr(node.grNode, keyItem.text(),valueText)
                elif(isinstance(node, Edge)): # 如果选中改变的是edge对象
                    keyItem = self.mainWindow.tableWidget.item(row, column - 1)
                    valueItem = self.mainWindow.tableWidget.item(row, column)
                    if hasattr(node.grEdge, keyItem.text()):  # 检查类是否有属性
                        valueText = valueItem.text()
                        try:
                            value = float(valueItem.text())
                            setattr(node.grEdge, keyItem.text(), value)
                        except ValueError:
                            setattr(node.grEdge, keyItem.text(), valueText)


def run():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = mainWindow_logical()

    from Tool import QSSTool
    QSSTool.setQssToObj("skin.qss", app)  # 全局设置样式

    # import qdarkgraystyle
    # print(qdarkgraystyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())


    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()