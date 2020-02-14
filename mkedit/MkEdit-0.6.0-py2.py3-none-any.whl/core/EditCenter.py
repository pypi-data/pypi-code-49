#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QHBoxLayout, QToolBar, QMessageBox
from PySide2.QtCore import QMargins, QFileInfo, Signal, Qt
from PySide2.QtGui import QTextDocument
from .DataClass import FileInfo
from .MkEdit import MkEdit
from menusbar.core import MemusBar
import os


class EditCenter(QWidget):
    createEditSignal = Signal(MkEdit)
    destoryEditSignal = Signal(MkEdit)
    # Tab change signal
    currentTabChangedSignal = Signal(int)

    currentEditPageChangedSignal = Signal(int)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.init()

    def startInit(self):
        self._initUI()
        self._initData()
        self._initEvent()

    def __del__(self):
        pass

    def init(self):
        self.toolbar: QToolBar = None

    def _initEvent(self):
        self.getMenusBar.openFileSignal.connect(self.openFileCallBack)
        self.getMenusBar.handlerBeforeEvent = self.handlerBeforeEvent
        self.getMenusBar.handlerAfterEvent = self.handlerAfterEvent

    def handlerBeforeEvent(self, type: int, filePath: str) -> bool:

        if type == self.getMenusBar.HANLDER_DELETE_FILE:
            msgBox = QMessageBox()
            msgBox.setFixedWidth(200)
            msgBox.setFixedHeight(200)
            msgBox.setText("删除提示")
            msgBox.setInformativeText("删除后将无法恢复，确认要删除：%s 文件？" % os.path.basename(filePath))
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                for index in range(0, self.mdiare.count()):
                    tab = self.mdiare.widget(index)
                    if tab.property("title") == filePath:
                        self.mdiare.removeTab(index)
            elif ret == QMessageBox.No:
                return False



        elif type == self.getMenusBar.HANLDER_DELETE_DIR:
            msgBox = QMessageBox()
            msgBox.setFixedWidth(200)
            msgBox.setFixedHeight(200)
            msgBox.setText("删除提示")
            msgBox.setInformativeText("将删除该目录下所有文件，确认要删除：%s 目录？" % os.path.basename(filePath))
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                for index in range(0, self.mdiare.count()):
                    tab = self.mdiare.widget(index)
                    if str(tab.property("title")).startswith(filePath):
                        self.mdiare.removeTab(index)
            elif ret == QMessageBox.No:
                return False

        return True

    def handlerAfterEvent(self, type: int, filePath: str):
        pass

    def openFileCallBack(self, file: QFileInfo):
        if file.isFile():
            fileInfo = FileInfo(file.fileName(), file.filePath())
            self.openFileInfo(fileInfo)

    def openFileInfo(self, value: FileInfo):
        has = False
        for index in range(0, self.mdiare.count()):
            tab = self.mdiare.widget(index)
            if tab and tab.property("title") == value.filePath:
                self.mdiare.setCurrentIndex(index)
                has = True
                break
        if not has:
            edit = MkEdit(self)
            edit.loadData(value.filePath)
            edit.setProperty("title", value.filePath)
            edit.fileInfoChangedCall.connect(self.fileInfoChangedCall)
            self.mdiare.addTab(edit, value.fileName)
            self.mdiare.setTabToolTip(self.mdiare.count() - 1, value.filePath)
            self.mdiare.setCurrentIndex(self.mdiare.count() - 1)
            self.createEditSignal.emit(edit)

    def getCurrentDocment(self) -> QTextDocument:
        edit: MkEdit = self.mdiare.currentWidget()
        return edit.getDocument()

    def getCurrentEdit(self) -> MkEdit:
        edit: MkEdit = self.mdiare.currentWidget()
        return edit

    def tabCloseRequested(self, index):
        _currentTab: MkEdit = self.mdiare.widget(index)
        if not _currentTab.interceptClose():
            self.createEditSignal.emit(self.mdiare.widget(index))
            self.mdiare.removeTab(index)

    def fileInfoChangedCall(self, filePath, hasSave):
        for index in range(0, self.mdiare.count()):
            tab = self.mdiare.widget(index)
            if tab and tab.property("title") == filePath:
                if not hasSave:
                    self.mdiare.tabBar().setTabTextColor(index, Qt.red)
                else:
                    self.mdiare.tabBar().setTabTextColor(index, Qt.black)

    def tabBarClicked(self, index):
        pass

    def tabBarDoubleClicked(self, index):
        pass

    def currentTabChanged(self, index):
        self.currentTabChangedSignal.emit(index)

    def currentChanged(self, index):
        self.currentEditPageChangedSignal.emit(index)

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...):
        QWidget(EditCenter, self).destroy(destroyWindow, destroySubWindows)

    def create(self, arg__1: int = ..., initializeWindow: bool = ..., destroyOldWindow: bool = ...):
        QWidget(EditCenter, self).create(arg__1, initializeWindow, destroyOldWindow)

    def _initUI(self):
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.menuBar = MemusBar(self)
        self.mainLayout.addWidget(self.menuBar)
        self.rightLayout = QVBoxLayout()
        self.rightLayout.setContentsMargins(QMargins(0, 0, 0, 0))

        self.mainTab = QTabWidget(self)
        self.mainTab.setMovable(True)
        self.mainTab.currentChanged.connect(self.currentTabChanged)
        self.mainTab.setTabPosition(QTabWidget.West)
        self.mdiare = QTabWidget(self)
        self.mdiare.setDocumentMode(True)
        # 注册关闭按钮信号
        self.mdiare.tabCloseRequested.connect(self.tabCloseRequested)
        self.mdiare.tabBarClicked.connect(self.tabBarClicked)
        self.mdiare.tabBarDoubleClicked.connect(self.tabBarDoubleClicked)
        self.mdiare.currentChanged.connect(self.currentChanged)
        self.mdiare.setMovable(True)
        self.mdiare.setTabsClosable(True)

        if len(self.extendTabWidget()) <= 0:
            self.rightLayout.addWidget(self.mdiare)
        else:
            self.mainTab.addTab(self.mdiare, "编辑中心")
            for node in self.extendTabWidget():
                name, widget = node
                self.mainTab.addTab(widget, name)

            self.rightLayout.addWidget(self.mainTab)
            self.mainTab.setCurrentIndex(0)

        self.mainLayout.addLayout(self.rightLayout, 1)
        self.setLayout(self.mainLayout)

    def _initData(self):
        pass
        # edit = Edit(self)
        # self.mdiare.addTab(edit, "xxxx")
        # for i in range(10):

    def setToolBar(self, toolBar: QToolBar):
        if toolBar:
            if self.toolbar:
                self.rightLayout.removeWidget(self.toolbar)
            self.toolbar = toolBar
            self.rightLayout.insertWidget(0, self.toolbar)

    def extendTabWidget(self) -> list:
        return list()

    @property
    def getMenusBar(self):
        return self.menuBar
