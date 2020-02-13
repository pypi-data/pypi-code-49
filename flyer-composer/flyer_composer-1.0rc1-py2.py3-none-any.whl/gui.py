#!/usr/bin/env python3
"""
flyer_composer.gui - Qt5 GUI for flyer-composer
"""
#
# Copyright 2019-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of flyer-composer.
#
# flyer-composer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# flyer-composer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with flyer-composer. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# The idea on how to load PDF documents using popplerqt5 and the
# load-callback is based on code
#   Copyright 2018 by Akkana Peck: share and enjoy under the GPLv2 or later.

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2019-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"

import os
import sys
import traceback

from PyQt5.QtWidgets import (QWidget, QApplication, QShortcut,
                             QAction, QLabel, QSizePolicy, QStackedWidget,
                             QStackedLayout, QSpinBox, QFormLayout,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QMainWindow, QPushButton, QComboBox,
                             QFileDialog, QFrame)
from PyQt5.QtGui import QPainter, QColor, QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl, QTimer, pyqtSignal
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.Qt import QDesktopServices

from popplerqt5 import Poppler

from . import (main, APPLICATION_NAME, POINTS_PER_INCH,
               decide_num_cols_rows, Box)
from .i18n import _

DONATION_URL = _("http://crazy-compilers.com/donate.html")

PREVIEW_SIZE = (300, 300)

LAYOUT_OPTIONS = (
    (_("A4"), ("a4", "a4")),
    (_("A5 on A4"), ("a5", "a4")),
    (_("A6 on A4"), ("a6", "a4")),
    (_("DIN Lang on A4"), ("dinlang", "a4")),
    )


class RichStatusbar(QLabel):
    def __init__(self, permanentText=""):
        super().__init__(permanentText)
        self.permanentText = permanentText
        self.setTextFormat(Qt.RichText)
        self.setWordWrap(True)
        self.setMargin(5)
        self.setAlignment(Qt.AlignHCenter)
        self.setOpenExternalLinks(True)
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self.clear)

    def clear(self):
        self._timer.stop()
        self.setText(self.permanentText)

    def message(self, text, timeout=0):
        self._timer.stop()
        self.setText(text)
        if timeout:
            self._timer.start(timeout)

    def error(self, text, timeout=0):
        self.message("<font color='red'>" + text + "</font>", timeout)


class PDFDocumentLoader(QNetworkAccessManager):
    def __init__(self):
        super().__init__()
        self.finished.connect(self.download_finished)

    def start_load(self, url):
        qurl = QUrl(url)
        if qurl.scheme():
            # If it's not a local file, we'll need to load it.
            # http://doc.qt.io/qt-5/qnetworkaccessmanager.html
            self.get(QNetworkRequest(qurl))
        else:
            # load local file directly
            document = Poppler.Document.load(url)
            if not document:
                self.loadFailed.emit(url)
            else:
                document.setRenderHint(Poppler.Document.TextAntialiasing)
                document.filename = url
                self.documentLoaded.emit(document)

    documentLoaded = pyqtSignal(object)
    loadFailed = pyqtSignal(object)

    def download_finished(self, network_reply):
        qbytes = network_reply.readAll()
        document = Poppler.Document.loadFromData(qbytes)
        if not document:
            self.loadFailed.emit(network_reply.url().toString())
        else:
            document.setRenderHint(Poppler.Document.TextAntialiasing)
            document.filename = network_reply.url().fileName(QUrl.FullyDecoded)
            self.documentLoaded.emit(document)


class PDFPageLabel(QLabel):
    '''
    A widget showing one page of a PDF.
    Will try to resize to a reasonable size to fit inside the
    geometry passed in.
    '''
    def __init__(self, geometry=PREVIEW_SIZE):
        super().__init__()
        self.setFixedSize(*geometry)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.cols = 1
        self.rows = 1
        self._clear()

    def _clear(self):
        self.document = None
        self.setPixmap(QPixmap())

    def document_loaded(self, document):
        assert self.document is None
        self.document = document

    def page_selected(self, pageno):
        """`pageno` is 1- based"""
        self.page = self.document.page(pageno-1)
        self.pagesize = self.page.pageSize()
        self._get_page_pixmap()
        self.render()

    def _get_page_pixmap(self):
        # self.pagesize is sized in pixels assuming POINTS_PER_INCH;
        # adjust that so the page barely fits on in (width, height).
        height = self.height()
        width = self.width()

        # First assume that it's portrait aspect ratio and that
        # vertical size will be the limiting factor.
        dpi = POINTS_PER_INCH * height / self.pagesize.height()

        # Was that too much: will it overflow in width?
        if (self.pagesize.width() * dpi / POINTS_PER_INCH > width):
            dpi = POINTS_PER_INCH * width / self.pagesize.width()
        # Get a pixmap of the PDF page
        pimg = self.page.renderToImage(dpi, dpi)
        self.pixmap = QPixmap.fromImage(pimg)

    def set_layout(self, cols, rows):
        self.cols = cols
        self.rows = rows
        if self.document:
            self.render()

    def render(self):
        '''Render to a pixmap at the current DPI setting.
        '''
        width = self.pixmap.width()
        height = self.pixmap.height()
        cols = self.cols
        rows = self.rows
        if self.pagesize.width() > self.pagesize.height():
            # landscape: switch number of rows and cols
            rows, cols = cols, rows
        preview = QPixmap(width * cols, height * rows)

        painter = QPainter()
        painter.begin(preview)
        # paint page several time
        for c in range(cols):
            for r in range(rows):
                painter.drawPixmap(c * width, r * height, self.pixmap)
        # draw page edges
        pen = painter.pen()
        pen.setWidth(4)  # TODO: depend on screen resolution
        # pen.setColor(QColor(0, 255, 255))  # turkis
        pen.setColor(QColor(255, 127, 255))  # pink
        painter.setPen(pen)
        for c in range(1, cols):
            painter.drawLine(c * width, 0, c * width, preview.height())
        for r in range(1, rows):
            painter.drawLine(0, r * height, preview.width(), r * height)
        painter.end()
        preview = preview.scaled(self.width(), self.height(),
                                 Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(preview)


class PreviewBox(QStackedWidget):

    def __init__(self, geometry=PREVIEW_SIZE, parent=None):
        super().__init__()
        self._parent = parent
        self.document = None
        self._loader = PDFDocumentLoader()
        self._loader.documentLoaded.connect(self.document_loaded)
        self._loader.loadFailed.connect(self._parent._load_failed)

        self.stack1 = QFrame()
        self.stack1.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.stack1.setLineWidth(1)
        self.stack2 = QFrame()
        self.stack2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.stack2.setLineWidth(1)

        self.addWidget(self.stack1)
        self.addWidget(self.stack2)

        self.stack1UI()
        self.stack2UI()

        self.open_button.clicked.connect(self.open)
        self.remove_button.clicked.connect(self.remove_page)
        self.page_select.valueChanged.connect(self.page_selected)

        self.remove_page()
        self.setCurrentWidget(self.stack1)

    def stack1UI(self):
        layout = QHBoxLayout()
        btn = QPushButton(QIcon.fromTheme("document-open"), _('&Open…'))
        btn.setToolTip(_('Open PDF document to use for this page'))
        btn.setIconSize(btn.iconSize() * 1.5)
        btn.setMinimumHeight(btn.iconSize().height() * 3)
        layout.addWidget(btn)
        self.open_button = btn
        self.stack1.setLayout(layout)

    def stack2UI(self, cols=1, rows=1, geometry=PREVIEW_SIZE):
        layout = QStackedLayout()
        layout.setStackingMode(QStackedLayout.StackAll)
        self.setFixedSize(*geometry)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # page preview
        self.page_label = PDFPageLabel(geometry=geometry)
        layout.addWidget(self.page_label)

        # "Remove page" button
        btn = QPushButton(QIcon.fromTheme("entry-delete"), "")
        btn.setFlat(True)  # no border
        self.remove_button = btn
        btn.setToolTip(_('Remove this page'))
        btn.setMaximumSize(btn.iconSize())  # FIXME: required?

        # page selector - This quite complicated, since a layout can not be
        # added to a layout and style-sheets can only be applied to widgets.
        w1 = QWidget()  # outer widget to hold the grip-layout
        layout.addWidget(w1)
        grid = QGridLayout(w1)  # required to make the form-layout small
        grid.addWidget(btn, 1, 1)
        grid.setRowStretch(2, 100)
        grid.setColumnStretch(2, 75)  # found by experiment
        grid.setColumnStretch(4, 100)

        w2 = QWidget()  # to hold the form-layout
        grid.addWidget(w2, 3, 3)

        # actual page selector
        form = QFormLayout(w2)
        l3 = QLabel(_("Select page:"))
        self.page_select = QSpinBox()
        form.addRow(l3, self.page_select)
        form.setFormAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        w2.setStyleSheet("background-color: rgba(200,200,200,0.5)")
        for e in (l3, self.page_select):
            e.setStyleSheet("background-color:none")

        self.stack2.setLayout(layout)

    def open(self, *args):
        filename = QFileDialog.getOpenFileName(
            self,
            _("Open document") + " - " + APPLICATION_NAME,  # caption
            "",
            _("PDF document (*.pdf);;All Files (*)"),
            options=QFileDialog.Options(QFileDialog.DontResolveSymlinks))[0]
        if filename:
            self.load_file(filename)

    def load_file(self, filename):
        # Create the Poppler document we'll use to render the pages.
        # The loader then will signal to document_loaded.
        self._loader.start_load(filename)

    documentLoaded = pyqtSignal()

    def document_loaded(self, document=None, pageno=0):
        assert not self.document
        assert document
        self.document = document
        self.page_label.document_loaded(self.document)
        self.page_select.setMinimum(1)
        self.page_select.setMaximum(self.document.numPages())
        self.page_select.setValue(pageno+1)
        self.setCurrentWidget(self.stack2)
        if self.document.numPages() > 1:
            pages = self._parent.pages
            if self is pages[0] and not pages[1].document:
                pages[1].document_loaded(self.document, 1)
            elif self is pages[1] and not pages[0].document:
                pages[0].document_loaded(self.document, 1)
            self.documentLoaded.emit()

    def page_selected(self, pageno):
        self.pageno = pageno
        if pageno > 0:
            self.page_label.page_selected(pageno)

    def remove_page(self):
        self.setCurrentWidget(self.stack1)
        # set to 0 so `valueChanged` will be emitted when setting pageno in
        # `page_selected()`
        self.page_select.setMinimum(0)
        self.page_select.setValue(0)
        self.page_label._clear()
        self.document = None


class MainWindow(QMainWindow):

    def __init__(self, filename=None):
        super().__init__()
        self.output_filename = None
        self.saved = True

        self.setWindowTitle(APPLICATION_NAME)

        QShortcut("ESC", self, activated=self.close)

        # Menu & Toolbar
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu(_('&File'))
        act = QAction(QIcon.fromTheme("application-exit"), _('&Exit'), self)
        act.setShortcut('Ctrl+Q')
        act.triggered.connect(self.close)
        fileMenu.addAction(act)

        # Create a widget inside the Main Window
        main_content = self._create_primary_widget()
        self.setCentralWidget(main_content)
        self.show()

    def _create_primary_widget(self):
        # A grid to layout all the pages
        grid = QGridLayout()

        # labels for the preview grid
        self.page_labels = [QLabel(_("Front page")), QLabel(_("Back page"))]
        self.pages = [PreviewBox(parent=self), PreviewBox(parent=self)]
        for i, (pl, pw) in enumerate(zip(self.page_labels, self.pages)):
            grid.addWidget(pl, 0, i*2, Qt.AlignHCenter)
            grid.addWidget(pw, 1, i*2, Qt.AlignHCenter)

        self.status_msg = RichStatusbar(_(
            'If you find %(APPLICATION_NAME)s useful, '
            'please <a href="%(DONATION_URL)s">donate</a>!') % globals())
        grid.addWidget(self.status_msg, 2,0,1,3)

        choice_box = QVBoxLayout()
        choice_box.addWidget(QLabel(_("Select target layout:")),
                             alignment=Qt.AlignBottom | Qt.AlignHCenter)
        cb = QComboBox()
        for text, dummy in LAYOUT_OPTIONS:
            cb.addItem(text)
        choice_box.addWidget(cb, alignment=Qt.AlignTop)
        cb.currentIndexChanged.connect(self._layout_choosen)
        self._layout_choosen(0)
        for pw in self.pages:
            pw.documentLoaded.connect(cb.setFocus)

        # buttons
        button_box = QVBoxLayout()

        button_box.addStretch(1)
        button_box.addLayout(choice_box)
        button_box.addStretch(1)

        btn = QPushButton(QIcon.fromTheme("document-save-as"), _('&Save as…'))
        btn.setToolTip(_('Save flyer as PDF'))
        btn.setIconSize(btn.iconSize() * 1.5)
        btn.setMinimumHeight(btn.iconSize().height() * 3)
        btn.clicked.connect(self.save_as)
        btn.setDefault(True)
        button_box.addWidget(btn)
        button_box.addStretch(2)

        btn = QPushButton(QIcon.fromTheme("help-donate"), _('&Donate…'))
        btn.setToolTip(_('Support development of this project'))
        btn.setIconSize(btn.iconSize() * 1.5)
        btn.clicked.connect(self.open_donattion_url)
        button_box.addWidget(btn)
        button_box.addStretch(1)

        grid.addLayout(button_box, 1, 1)

        widget = QWidget()
        widget.setLayout(grid)
        return widget

    def _load_failed(self, url):
        self.status_msg.error(_("Failed to load the file %s") % url, 10*1000)

    def _layout_choosen(self, index=None):
        # TODO: If index is None, take it from choice_box
        if index is None:
            index = 0
        self.saved = False
        flyersize_name, mediasize_name = LAYOUT_OPTIONS[index][-1]
        self.flyersize_name = flyersize_name
        self.mediasize_name = mediasize_name
        flyerbox, self.cols, self.rows = \
            decide_num_cols_rows(Box.from_papersize(flyersize_name),
                                 Box.from_papersize(mediasize_name))
        for page in self.pages:
            page.page_label.set_layout(self.rows, self.cols)

    def open_donattion_url(self):
        QDesktopServices.openUrl(QUrl(DONATION_URL))

    def save_as(self, *args):
        pages = [p for p in self.pages if p.document]
        if not pages:
            # nothing to save
            return
        input_filename = pages[0].document.filename
        if not self.output_filename:
            filename = _("-flyer").join(os.path.splitext(input_filename))
        else:
            filename = self.output_filename
        filename = QFileDialog.getSaveFileName(
            self,
            _("Save document") + " - " + APPLICATION_NAME,  # caption
            filename,
            _("PDF document (*.pdf);;All Files (*)"),
            options=QFileDialog.Options(QFileDialog.DontResolveSymlinks))[0]
        if filename:
            main(outfilename=filename,
                 flyer_size = self.flyersize_name,
                 media_size = self.mediasize_name,
                 infilename = pages[0].document.filename,
                 front_page = pages[0].pageno-1,
                 back_page = pages[1].pageno-1 if len(pages) > 1 else None,
                 infilename_back = (pages[1].document.filename
                                    if len(pages) > 1 else None)
                 )
            self.output_filename = filename
            self.saved = True
            print("saved", filename)
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.output_filename))


def run():
    #
    # PyQt is super crashy. Any little error, like an extra argument in a slot,
    # causes it to kill Python with a core dump.
    # Setting sys.excepthook works around this , and execution continues.
    #
    def excepthook(excType=None, excValue=None, tracebackobj=None, *,
                   message=None, version_tag=None, parent=None):
        # print("exception! excValue='%s'" % excValue)
        # logging.critical(''.join(traceback.format_tb(tracebackobj)))
        # logging.critical('{0}: {1}'.format(excType, excValue))
        traceback.print_exception(excType, excValue, tracebackobj)

    sys.excepthook = excepthook

    app = QApplication(sys.argv)
    w = MainWindow()
    if len(sys.argv) > 1:
        w.pages[0].load_file(sys.argv[1])
    else:
        QTimer.singleShot(0, w.pages[0].open)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
