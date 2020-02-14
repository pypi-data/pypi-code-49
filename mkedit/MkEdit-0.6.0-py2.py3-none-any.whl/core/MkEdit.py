#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QShortcut, QToolBar, QFileDialog, QDialog, \
    QInputDialog

from PySide2.QtGui import QFont, QFontMetrics, QKeySequence, QTextDocument, QTextOption, QDesktopServices, QTextCursor
from PySide2.QtCore import QMargins, Signal, QUrl, QFileInfo, Qt
from os import path, stat
from rx import operators as ops, scheduler
from .FileUtils import updateFile
import PySide2
import rx
from scheduler.PySild2QtScheduler import qtScheduler
from .widgets import PreView, EditView, ToolBarButton, ToolBarMenuInfo
from .dialog import PrewViewDialog, ComboBoxDialog
from .MkUtuls import MkUtuls
import os
import hashlib


class MkEdit(QWidget):
    beInterceptMenuCall = Signal(ToolBarMenuInfo)
    fileInfoChangedCall = Signal(str, bool)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.init()
        self.initUI()
        self.initEvent()
        self.initToolBar()

    def init(self):
        self.mkUtuls = MkUtuls()
        self.toolBar: QToolBar = QToolBar(self)
        self.toolBarMenusList = list()
        self.enableRightPreView: bool = False
        self.rightPreView = None
        self.leftEdit = None
        self.lastModifyTime = None
        self.timerCount = 0
        self.firstVisitLine = 1
        self.scrollUp = False
        self.shortcutList = list()
        self.needInterceptIds = list()
        self.fileName: str = None
        self.currentMd5Value = None

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(0)
        self.initLeftEdit()
        if self.leftEdit:
            self.contentLayout.addWidget(self.leftEdit, 1)
        self.enableRightView(self.enableRightPreView)
        if self.toolBar:
            self.mainLayout.addWidget(self.toolBar)
        self.mainLayout.addLayout(self.contentLayout, 1)
        self.setLayout(self.mainLayout)

    def initLeftEdit(self):
        self.leftEdit = EditView(self)
        self.leftEdit.setWordWrapMode(QTextOption.WordWrap)
        shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_S), self.leftEdit)
        shortcut.activated.connect(self.save)
        font = QFont("Menlo", 14)
        self.leftEdit.setFont(font)
        self.leftEdit.setTabStopWidth(4 * QFontMetrics(font).width(" "))
        self.leftEdit.textChanged.connect(self.leftEditTextChange)

    def initEvent(self):
        self.startTimerTask()
        self.leftEdit.scrollContentEvent = self.fireScroll

    def fireScroll(self, firstVisitLine, up):
        self.scrollUp = (up == 1)

    def checkPreViewScroll(self):
        if self.rightPreView:
            line = self.leftEdit.firstVisibleBlock().blockNumber()
            if self.firstVisitLine != line:
                self.firstVisitLine = line
                if self.scrollUp:
                    # 由下往上滑
                    self.rightPreView.scrollContent(
                        (self.firstVisitLine + self.leftEdit.getShowLines()) / self.leftEdit.blockCount())
                else:
                    self.rightPreView.scrollContent(self.firstVisitLine / self.leftEdit.blockCount())

    # 执行定时器
    def startTimerTask(self):
        rx.interval(1).pipe(
            qtScheduler.QtScheduler()
        ).subscribe(
            on_next=lambda v: self.onTimer()
        )

    # 处理定时任务
    def onTimer(self):
        self.checkPreViewScroll()
        self.timerCount = self.timerCount + 1
        if self.timerCount % 10 == 0:
            self.trySave()

    def trySave(self):
        # print("trySave window is active:%s" % self.isActiveWindow())
        if not self.isActiveWindow():
            return
        if self.checkFileChange():
            # 提示用户源文件已发生改变
            msgBox = QMessageBox()
            msgBox.setText("%s-源文档已被修改" % self.fileName)
            msgBox.setInformativeText("点击YES将更新改动内容至当前文档,点击NO将以当前文本内容覆盖本地内容")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                self.loadData(self.filePath)

            elif ret == QMessageBox.No:
                self.startSave()

    def initToolBar(self):
        self.toolBarMenusList.clear()
        self.toolBarMenusList.append(
            ToolBarMenuInfo("undo", "fa5s.undo-alt", shortcut=Qt.CTRL + Qt.Key_Z,
                            callBack=lambda: self.leftEdit.undo()))

        self.toolBarMenusList.append(ToolBarMenuInfo("redo", "fa5s.redo-alt", callBack=lambda: self.leftEdit.redo()))

        self.toolBarMenusList.append(
            ToolBarMenuInfo("save", "fa5s.save", callBack=lambda: self.save()))

        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("bold", "fa5s.bold"))

        self.toolBarMenusList.append(ToolBarMenuInfo("italic", "fa5s.italic"))

        self.toolBarMenusList.append(ToolBarMenuInfo("heading", "fa5s.heading"))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(
            ToolBarMenuInfo("code", "fa5s.code", shortcut=Qt.CTRL + Qt.SHIFT + Qt.Key_C,
                            callBack=self.converToCodeFormat))

        self.toolBarMenusList.append(ToolBarMenuInfo("quote", "fa5s.quote-left"))

        self.toolBarMenusList.append(ToolBarMenuInfo("list-ul", "fa5s.list-ul"))

        self.toolBarMenusList.append(ToolBarMenuInfo("list-ol", "fa5s.list-ol"))

        self.toolBarMenusList.append(
            ToolBarMenuInfo("table", "fa5s.table", shortcut=Qt.CTRL + Qt.SHIFT + Qt.Key_Z, callBack=self.insertTable))

        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("link", "fa5s.link", shortcut=Qt.CTRL + Qt.SHIFT + Qt.Key_L, ))
        self.toolBarMenusList.append(ToolBarMenuInfo("images", "fa5s.images", shortcut=Qt.CTRL + Qt.SHIFT + Qt.Key_I))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(
            ToolBarMenuInfo("eye", "fa5s.eye", shortcut=Qt.CTRL + Qt.SHIFT + Qt.Key_P,
                            callBack=lambda: self.showPreDialog()))
        self.toolBarMenusList.append(ToolBarMenuInfo("exchange", "fa5s.exchange-alt", shortcut=Qt.CTRL + Qt.Key_P,
                                                     callBack=lambda: self.enableRightView(
                                                         not self.enableRightPreView)))
        # self.toolBarMenusList.append(ToolBarMenuInfo("arrows", "fa5s.arrows-alt"))
        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("export", "fa5s.share-square", callBack=self.export))

        self.toolBarMenusList.append(ToolBarMenuInfo(separator=True))

        self.toolBarMenusList.append(ToolBarMenuInfo("question", "fa5s.question-circle"))

    def refreshToolBar(self):
        self.toolBar.clear()
        for data in self.toolBarMenusList:
            if data.separator:
                self.toolBar.addSeparator()
            else:
                menu = ToolBarButton()
                menu.setAwesomeIcon(data.icon)
                menu.setProperty("id", data.id)
                menu.clicked.connect(self.clickToolBarMenu)

                if data.shortcut:
                    shortcut = QShortcut(QKeySequence(data.shortcut), self)
                    shortcut.setProperty("id", data.id)
                    shortcut.setProperty("shortcut", data.shortcut)
                    shortcut.activated.connect(self.fireToolBarMenusShortcut)
                self.toolBar.addWidget(menu)

    def addExtendToolBar(self, index, button: ToolBarMenuInfo):
        self.toolBarMenusList.insert(index, button)

    def fireToolBarMenusShortcut(self):
        shortcut = self.sender().property("shortcut")
        print("shortcut:%s" % shortcut)
        for menu in self.toolBarMenusList:
            if menu.shortcut and menu.shortcut == shortcut:
                if len(self.needInterceptIds) > 0 and menu.id in self.needInterceptIds:
                    self.beInterceptMenuCall.emit(menu)
                elif menu.callBack:
                    menu.callBack()

    def clickToolBarMenu(self):
        id = self.sender().property("id")
        for menu in self.toolBarMenusList:
            if menu.id and menu.id == id:
                if len(self.needInterceptIds) > 0 and menu.id in self.needInterceptIds:
                    self.beInterceptMenuCall.emit(menu)
                elif menu.callBack:
                    menu.callBack()

    def showPreDialog(self):
        dialog = PrewViewDialog(self)
        dialog.setPreHtml(self.getRenderHtml(self.leftEdit.toPlainText()))

    def insertTable(self):
        (text, ok) = QInputDialog.getInt(None, "插入表格", "请输入需要创建的列数")
        if ok and text:
            try:
                col = int(text)
                titles = "|"
                tables = "|"
                contents = "|"

                for index in range(col):
                    titles += " 标题%s |" % index
                    tables += " ---- |"
                    contents += " 内容%s |" % index
                self.insertPlainText("%s\n" % titles)
                self.insertPlainText("%s\n" % tables)
                self.insertPlainText("%s\n" % contents)
            except Exception as e:
                print(e)

    def converToCodeFormat(self):
        comboBoxDialog = ComboBoxDialog(self)
        comboBoxDialog.initData(
            ['java', 'kotlin', 'mermaid', 'c', 'c++', 'c#', 'javascript', 'html', 'css', 'php', 'python', 'swift',
             'nodejs',
             'object-c', 'sql', 'ruby', 'go', 'R', 'D', 'groovy', 'dart', 'rust', 'scala', 'lua'])
        ret = comboBoxDialog.exec_()
        if ret == QDialog.Accepted:
            result = comboBoxDialog.result
            self.insertPlainText("``` %s\n\n```\n" % result)
            textCursor: QTextCursor = self.leftEdit.textCursor()
            textCursor.movePosition(QTextCursor.PreviousRow)
            textCursor.movePosition(QTextCursor.PreviousRow)
            self.leftEdit.setTextCursor(textCursor)
    def export(self):
        fileDialog = QFileDialog(self)
        fileDialog.setFileMode(QFileDialog.Directory)
        fileDialog.setWindowTitle("选择导出目录")
        ret = fileDialog.exec_()
        if ret == QDialog.Accepted:
            fileName = fileDialog.selectedFiles()
            splitResult = self.fileName.split(".")
            name = self.fileName
            if len(splitResult) == 2:
                name = splitResult[0]
            name = "%s.html" % name
            html = self.getRenderHtml(self.leftEdit.toPlainText())
            html = PreView().leftHtml + html + PreView().rightHtml
            saveHtmlPath = os.path.join(fileName[0], name)
            with open(saveHtmlPath, mode='w') as f:
                f.write(html)
            msgBox = QMessageBox()
            msgBox.setText("导出成功,是否查看导出文件")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                url = QUrl("file:%s" % fileName[0],
                           QUrl.TolerantMode)
                QDesktopServices.openUrl(url)

    def enableRightView(self, enable):
        if self.enableRightPreView != enable:
            self.enableRightPreView = enable
            if self.enableRightPreView:
                if not self.rightPreView:
                    self.rightPreView = PreView(self)
                    self.contentLayout.addWidget(self.rightPreView, 1)
                    self.foreRefreshPreViewInfo()

            else:
                if self.rightPreView:
                    self.contentLayout.removeWidget(self.rightPreView)
                    self.rightPreView.deleteLater()
                    del self.rightPreView
                    self.rightPreView = None

    def interceptClose(self):
        if path.exists(self.filePath) and not self.haseSave:
            msgBox = QMessageBox()
            msgBox.setText("%s-文档已被修改" % self.fileName)
            msgBox.setInformativeText("是否保存修改后的文档")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec_()
            if ret == QMessageBox.Save:
                self.save()
                self.haseSave = True
            elif ret == QMessageBox.Cancel:
                self.haseSave = False
            elif ret == QMessageBox.Discard:
                return False

        return not self.haseSave

    def save(self):
        if not self.haseSave:
            if not path.exists(self.filePath):
                msgBox = QMessageBox()
                msgBox.setText("%s-文档不存在" % self.fileName)
                msgBox.setInformativeText("请检查是否文件已被删除或转移至其他目录")
                msgBox.setStandardButtons(QMessageBox.Close)
                msgBox.setDefaultButton(QMessageBox.Close)
            else:
                self.startSave()

    def startSave(self):
        if not self.haseSave:
            updateFile(self.filePath, self.leftEdit.toPlainText()).pipe(
                ops.subscribe_on(scheduler.ThreadPoolScheduler())
            ).subscribe(on_completed=lambda: self.handlerSaveResult())

    def handlerSaveResult(self):
        self.haseSave = True
        self.recordFileExtendInfo()
        self.fileInfoChangedCall.emit(self.filePath, self.haseSave)

    def loadData(self, filePath):
        self.filePath = filePath
        self.fileName = path.basename(self.filePath)

        with open(self.filePath, mode='r') as f:
            self.leftEdit.setPlainText("".join(f.readlines()))
        self.recordFileExtendInfo()
        self.haseSave = True

    def recordFileExtendInfo(self):
        if path.exists(self.filePath):
            self.lastModifyTime = stat(self.filePath).st_mtime
            self.currentMd5Value = hashlib.md5(open(self.filePath, 'rb').read()).hexdigest()

    def checkFileChange(self) -> bool:
        try:
            lastMd5Value = hashlib.md5(open(self.filePath, 'rb').read()).hexdigest()
            currentModifyTime = stat(self.filePath).st_mtime
            if currentModifyTime != self.lastModifyTime and lastMd5Value != self.currentMd5Value:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def setPlainText(self, text: str = ""):
        self.leftEdit.setPlainText(text)

    def insertPlainText(self, text: str = ""):
        self.leftEdit.insertPlainText(text)

    def getDocument(self) -> QTextDocument:
        return self.leftEdit.document()

    def leftEditTextChange(self):
        self.haseSave = False
        self.fileInfoChangedCall.emit(self.filePath, self.haseSave)
        if self.rightPreView:
            self.rightPreView.setPreContent(self.getRenderHtml(self.leftEdit.toPlainText()))
            line = self.leftEdit.textCursor().blockNumber()
            if line > self.leftEdit.blockCount() - self.leftEdit.getShowLines():
                self.rightPreView.scrollContent(1.0)

    def foreRefreshPreViewInfo(self):
        if self.rightPreView:
            self.rightPreView.setPreContent(self.getRenderHtml(self.leftEdit.toPlainText()))

    def getRenderHtml(self, txt):
        result = self.mkUtuls.parse(txt)
        return result

    def enterEvent(self, event: PySide2.QtCore.QEvent):
        self.trySave()
