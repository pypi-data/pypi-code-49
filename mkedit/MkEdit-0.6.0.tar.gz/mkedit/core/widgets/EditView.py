#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide2.QtWidgets import QPlainTextEdit, QTextEdit, QShortcut, QMessageBox
from PySide2.QtGui import QKeyEvent, QColor, QTextFormat, QPainter, QPalette, Qt, QTextCursor, QKeySequence, \
    QTextDocument
from .LineNumberArea import LineNumberArea
from PySide2.QtCore import QRect, Signal
import PySide2
import os
from mkedit.core.dialog import SearchHitDialog


class EditView(QPlainTextEdit):
    addImageEventSignal = Signal(list)

    def __init__(self, parent=None):
        QPlainTextEdit.__init__(self, parent)
        self.init()
        self.initEvent()

    def init(self):
        self.haseSave = True
        self.showLineCount = None
        self.lineNumberArea = LineNumberArea(self)
        self.noSelection = False
        self.supportImageSuffix = [".png", '.jpeg', '.jpg', '.svg', '.gif', '.bmp', '.webp', '.icon']
        self.searchDialog = None

    def initEvent(self):
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.updateLineNumberAreaWidth()

        # highlight line
        self.textChanged.connect(self.highlightCurrentLine)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        shortcut.activated.connect(self.search)

    def search(self):
        # 弹出搜索输入弹窗
        if not self.searchDialog:
            self.searchDialog = SearchHitDialog.getInstance()
        else:
            self.searchDialog.close()

        self.searchDialog.init(self)
        self.searchDialog.show()

    def updateLineNumberAreaWidth(self):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):

        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth()

    def lineNumberAreaPaintEvent(self, event):

        if self.isReadOnly():
            return

        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor(38, 38, 38))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())
        currentLine = self.document().findBlock(self.textCursor().position()).blockNumber()

        painter.setPen(self.palette().color(QPalette.Text))

        while block.isValid() and top <= event.rect().bottom():

            # default grey
            textColor = QColor(155, 155, 155)

            if blockNumber == currentLine and self.hasFocus():
                # current line
                textColor = QColor(255, 170, 0, 255)

            painter.setPen(textColor)

            number = "%s " % str(blockNumber + 1)
            painter.drawText(4, top, self.lineNumberArea.width(), self.fontMetrics().height(), Qt.AlignHCenter,
                             number)

            # Move to the next block
            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            blockNumber += 1

    def lineNumberAreaWidth(self):
        digits = 1
        maxNum = max(1, self.blockCount())
        while maxNum >= 10:
            maxNum /= 10
            digits += 1

        space = 7 + self.fontMetrics().width('9') * digits
        return space

    def resizeEvent(self, event):
        QPlainTextEdit.resizeEvent(self, event)

        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        '''
        Highlight currently selected line
        '''

        extraSelections = []

        selection = QTextEdit.ExtraSelection()

        lineColor = QColor(230, 230, 230, 255)

        if not self.hasFocus() or self.isReadOnly():
            lineColor.setAlpha(0)

        selection.format.setBackground(lineColor)
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor = self.textCursor()
        selection.cursor.clearSelection()

        extraSelections.append(selection)

        self.setExtraSelections(extraSelections)

    def scrollContentsBy(self, dx: int, dy: int):

        if dy > 0:
            # print("下滑 第一个可见line:%s| 最后一个可见行: %s" % (
            #     self.firstVisibleBlock().blockNumber(), self.getLastVisibleBlock()))
            self.scrollContentEvent(self.firstVisibleBlock().blockNumber(), -1)

        elif dy < 0:
            # print("上滑 第一个可见line:%s| 最后一个可见行: %s" % (
            #     self.firstVisibleBlock().blockNumber(), self.getLastVisibleBlock()))
            self.scrollContentEvent(self.firstVisibleBlock().blockNumber(), 1)

        QPlainTextEdit.scrollContentsBy(self, dx, dy)

    def scrollContentEvent(self, firstVisitLine, up):
        print("scrollCallBack# firstVisitLine= %s and percentage=%s" % (
            firstVisitLine, firstVisitLine / self.blockCount()))
        pass

    def findBlocks(self, first=0, last=None, exclude=[]):
        '''
        Divide text in blocks
        '''

        blocks = []
        if last == None:
            last = self.document().characterCount()
        for pos in range(first, last + 1):
            block = self.document().findBlock(pos)
            if block not in blocks and block not in exclude:
                blocks.append(block)
        return blocks

    def blocks2list(self, blocks, mode=None):
        '''
        Convert a block to a string.
        If a mode is specified, preform custom modification to the text.
        '''

        text = []

        toggle = None

        for block in blocks:

            blockText = block.text()
            # ------------------------------------------------------------------------------------------

            if mode == 'unindent':

                if blockText.startswith(' ' * 4):
                    blockText = blockText[4:]
                    self.lastChar -= 4

                elif blockText.startswith('\t'):
                    blockText = blockText[1:]
                    self.lastChar -= 1
            # ------------------------------------------------------------------------------------------

            elif mode == 'indent':
                blockText = ' ' * 4 + blockText
                self.lastChar += 4
            # ------------------------------------------------------------------------------------------

            elif mode == 'comment':
                unindentedBlockText = blockText.lstrip()
                indents = len(blockText) - len(unindentedBlockText)

                if toggle is None:
                    toggle = not unindentedBlockText.startswith('#')

                # kill comment
                if unindentedBlockText.startswith('# '):
                    unindentedBlockText = unindentedBlockText[2:]

                elif unindentedBlockText.startswith('#'):
                    unindentedBlockText = unindentedBlockText[1:]

                # combine
                blockText = (' ' * indents) + ('# ' * int(toggle)) + unindentedBlockText

            # ------------------------------------------------------------------------------------------

            text.append(blockText)
        return text

    def getCursorInfo(self):

        self.cursor = self.textCursor()

        self.firstChar = self.cursor.selectionStart()
        self.lastChar = self.cursor.selectionEnd()

        self.noSelection = False
        if self.firstChar == self.lastChar:
            self.noSelection = True

        self.originalPosition = self.cursor.position()
        self.cursorBlockPos = self.cursor.positionInBlock()


    def indentation(self, mode):
        '''
        Indent selected
        '''

        self.getCursorInfo()

        # if nothing is selected and mode is set to indent, simply insert as many
        # space as needed to reach the next indentation level.

        if self.noSelection and mode == 'indent':
            remainingSpaces = 4 - (self.cursorBlockPos % 4)
            self.insertPlainText(' ' * remainingSpaces)
            return

        selectedBlocks = self.findBlocks(self.firstChar, self.lastChar)
        beforeBlocks = self.findBlocks(last=self.firstChar - 1, exclude=selectedBlocks)
        afterBlocks = self.findBlocks(first=self.lastChar + 1, exclude=selectedBlocks)

        beforeBlocksText = self.blocks2list(beforeBlocks)
        selectedBlocksText = self.blocks2list(selectedBlocks, mode)
        afterBlocksText = self.blocks2list(afterBlocks)

        combinedText = '\n'.join(beforeBlocksText + selectedBlocksText + afterBlocksText)

        # make sure the line count stays the same
        originalBlockCount = len(self.toPlainText().split('\n'))
        combinedText = '\n'.join(combinedText.split('\n')[:originalBlockCount])

        self.clear()
        self.setPlainText(combinedText)
        self.restoreSelection()

    def restoreSelection(self):
        '''
        Restore the original selection and cursor posiftion modifing the text.
        '''

        if self.noSelection:
            self.cursor.setPosition(self.lastChar)

        # check whether the the original selection was from top to bottom or vice versa
        else:
            if self.originalPosition == self.firstChar:
                first = self.lastChar
                last = self.firstChar
                firstBlockSnap = QTextCursor.EndOfBlock
                lastBlockSnap = QTextCursor.StartOfBlock
            else:
                first = self.firstChar
                last = self.lastChar
                firstBlockSnap = QTextCursor.StartOfBlock
                lastBlockSnap = QTextCursor.EndOfBlock

            self.cursor.setPosition(first)
            self.cursor.movePosition(firstBlockSnap, QTextCursor.MoveAnchor)
            self.cursor.setPosition(last, QTextCursor.KeepAnchor)
            self.cursor.movePosition(lastBlockSnap, QTextCursor.KeepAnchor)

        self.setTextCursor(self.cursor)

    def keyPressEvent(self, event: QKeyEvent):
        # print(event.key())
        # if Tab convert to Space
        if event.key() == 16777217:
            self.indentation('indent')

        # if Shift+Tab remove indent
        elif event.key() == 16777218:
            self.indentation('unindent')
        else:
            QPlainTextEdit.keyPressEvent(self, event)

    def getLastVisibleBlock(self) -> int:
        if not self.showLineCount:
            self.showLineCount = self.getShowLines()
        lastVisibleBlockNumber = int(self.showLineCount) + self.firstVisibleBlock().blockNumber()
        return lastVisibleBlockNumber

    def getShowLines(self) -> int:
        height = self.height()
        lineHeight = self.blockBoundingRect(self.firstVisibleBlock()).height()
        showLineCount = height / lineHeight
        return int(showLineCount)

    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent):
        print("dragEnterEvent")
        accept = False
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                print(url)
                if url.isLocalFile():
                    suffix = os.path.splitext(url.toLocalFile())[-1]
                    print(suffix)
                    if suffix in self.supportImageSuffix:
                        accept = True
                        break

        if accept:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: PySide2.QtGui.QDropEvent):
        data = event.mimeData()
        if data.hasUrls():
            urls = data.urls()
            if len(urls) <= 0:
                return
            files = list()
            for fileUrl in urls:
                if fileUrl.isLocalFile():
                    files.append(fileUrl.toLocalFile())
            self.addImageEventSignal.emit(files)

    def insertFromMimeData(self, source: PySide2.QtCore.QMimeData):
        if source.hasUrls():
            urls = source.urls()
            if len(urls) <= 0:
                return
            files = list()
            for fileUrl in urls:
                if fileUrl.isLocalFile():
                    suffix = os.path.splitext(fileUrl.toLocalFile())[-1]
                    if suffix in self.supportImageSuffix:
                        files.append(fileUrl.toLocalFile())
            self.addImageEventSignal.emit(files)
        elif source.hasImage():
            # 获取剪贴板的图片
            self.addImageEventSignal.emit([source])
            return False
        else:
            return QPlainTextEdit.insertFromMimeData(self, source)
