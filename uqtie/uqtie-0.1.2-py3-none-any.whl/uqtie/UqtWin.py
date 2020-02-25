#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
PyQt5 Application Main Window base class that does basic things that most of my GUI apps need.
"""
from __future__      import print_function
from pathlib         import Path

import sys, os, argparse, time

from PyQt5.QtCore    import Qt, QSettings
from PyQt5.QtGui     import QKeySequence, QFont, QFontInfo
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QMainWindow, QShortcut, QFontDialog
from uqtie           import UqtStylesheet

class MainWindow(QMainWindow):

    def __init__(self, parsedArgs, **kwargs ):
        super(MainWindow, self).__init__()

        self.fontDialog = None
        self.stylesheetFileName = None

        # Save the app so we can change its stylesheet
        if 'app' in kwargs:
            self.app = kwargs['app']

        # Create a QSettings. Qt stores this using your organization name and your application name
        # to determine the correct place for your user and their operating system
        # (e.g. on linux it's: ~/.config/Craton/SomeApp)
        if 'organizationName' in kwargs and 'appName' in kwargs:
            self.settings = QSettings(kwargs['organizationName'], kwargs['appName'])

            if self.settings and self.app:
                self.stylesheetMgr = UqtStylesheet.StylesheetManager(self.app, self.settings,
                                                                     kwargs['appName'])

            if self.stylesheetMgr:
                self.stylesheetMgr.read_stylesheet_vars()
                self.stylesheetMgr.apply()

        # stylesheet inspector is cool but needs improvement. Need to use the branch that has
        # the tree view. Need to make the inspector window re-sizable and use our font, so it
        # isn't ridiculously small or ridiculously large.
        self.connect_stylesheet_inspector(shortcut=QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_F12))

        appName = ''
        title = ''
        if 'appName' in kwargs:
            appName = kwargs['appName']
        if 'title' in kwargs:
            title = kwargs['title']

        if title == '':
            title = appName

        self.setup_base_ui( title )

    def connect_stylesheet_inspector(self, shortcut):
        self.shortcut = shortcut
        shortcut_ = QShortcut(self.shortcut, self)
        shortcut_.setContext(Qt.ApplicationShortcut)
        shortcut_.activated.connect(self.show_stylesheet_editor)

    def show_stylesheet_editor(self):
        style_sheet_inspector_class = self.get_stylesheet_inspector_class()
        style_sheet_inspector = [
            c for c in self.children() if
            isinstance(c, style_sheet_inspector_class)]
        if style_sheet_inspector:
            style_sheet_inspector = style_sheet_inspector[0]
        else:
            style_sheet_inspector = style_sheet_inspector_class(self)
            style_sheet_inspector.setFixedSize(800, 600)
        style_sheet_inspector.show()

    def get_stylesheet_inspector_class(self):
        """
        Indirection mostly to simplify tests.
        """
        try:
            from qt_style_sheet_inspector import StyleSheetInspector
        except ImportError as error:
            msg = 'You need to Install qt_style_sheet_inspector.'
            raise RuntimeError(msg)
        return StyleSheetInspector


    def setup_base_menus(self):
        # Create Menu Bar
        self.menuBar = self.menuBar()

        # Create Root Menus
        self.fileMenu = self.menuBar.addMenu('File')
        self.viewMenu = self.menuBar.addMenu('View')

        # Set up our handling of file menu
        self.fileMenu.triggered.connect(self.file_menu_selected)

        # Create Actions for menus
        self.quitAction = QAction('Quit', self)
        self.quitAction.setShortcut('Ctrl+Q')
        self.quitAction.triggered.connect(self.onQuit)

        # Should go in File->Preferences... ? Or View?
        self.fontAction = QAction('Font', self)
        self.fontAction.triggered.connect(self.on_font_menu_selected)

        self.zoomInAction = QAction('Zoom In', self)
        self.zoomInAction.setShortcut('Ctrl++')
        self.zoomInAction.triggered.connect(self.on_zoom_in)

        self.zoomOutAction = QAction('Zoom Out', self)
        self.zoomOutAction.setShortcut('Ctrl+-')
        self.zoomOutAction.triggered.connect(self.on_zoom_out)

        # Add actions to Menus
        self.fileMenu.addAction(self.quitAction)
        self.fileMenu.addAction(self.fontAction)
        self.viewMenu.addAction(self.zoomInAction)
        self.viewMenu.addAction(self.zoomOutAction)

        # Events
        #self.fileMenu.triggered.connect(self.selected)


    def setup_base_ui(self, title ):
        self.setup_base_menus()
        centralWindow = QWidget()
        self.setCentralWidget(centralWindow)

        # Restore the geometry from settings, default to an empty string
        geometry = self.settings.value('geometry', '')
        if geometry:
            self.restoreGeometry(geometry)

        self.setWindowTitle(title)

    def on_font_menu_selected(self):
        """User has selected 'Font...' from an app menu, put up font dialog"""

        # Clean up from Previous Font Dialog.
        self.disconnect_font_dialog()
        self.fontDialog = None

        self.fontDialog = QFontDialog(QFont())

        # if you don't do this, .font() may not give you the widget's actual font
        self.fontDialog.ensurePolished()
        font = self.fontDialog.font()
        #print ("Dialog Font Post-Polish")
        #print (font.family())
        #print (font.pointSize())
        #print (font.pixelSize())

        fontinfo = QFontInfo(font)
        #print ('fontinfo.family(): {s}'.format(s=fontinfo.family()))
        #print ('fontinfo.styleName(): {s}'.format(s=fontinfo.styleName()))

        # Resize the Dialog Box so it is reasonable for the actual current font
        # (Not sure how valid this ratio is for different systems, works nicely on my
        # Cygwin/X setup on which I have a large 4K monitor on which I use large fonts)
        self.fontDialog.resize( fontinfo.pointSize() * 40, fontinfo.pointSize() * 40 )

        self.fontDialog.setCurrentFont(font)
        self.fontDialog.currentFontChanged.connect(self.on_font_dialog_current_font_changed)
        self.fontDialog.accepted.connect(self.on_font_dialog_accepted)
        self.fontDialog.finished.connect(self.on_font_dialog_finished)
        self.fontDialog.rejected.connect(self.on_font_dialog_rejected)

        self.fontDialog.show()

    def disconnect_font_dialog(self):
        if self.fontDialog:
            self.fontDialog.currentFontChanged.disconnect()
            self.fontDialog.accepted.disconnect()
            self.fontDialog.finished.disconnect()
            self.fontDialog.rejected.disconnect()
        
    def on_font_dialog_accepted(self):
        #print ( "on_font_dialog_accepted")

        # The way I read the docs, this is what I should call:
        #font = self.fontDialog.selectedFont()

        # But... this is what gives me the actual user selection in practice:
        font = self.fontDialog.currentFont()
        #print ('currentFont(): {s}'.format(s=str(font)))
        #print ('font.family(): {s}'.format(s=font.family()))
        fontinfo = QFontInfo(font)
        #print ('fontinfo.family(): {s}'.format(s=fontinfo.family()))
        #print ('fontinfo.styleName(): {s}'.format(s=fontinfo.styleName()))

        self.stylesheetMgr.set_main_font_family(font.family())
        #self.stylesheetMgr.set_main_font_weight(fontinfo.styleName())
        self.stylesheetMgr.set_main_font_size(str(font.pointSize())+ 'pt')
        
        self.stylesheetMgr.apply()
        self.stylesheetMgr.save_stylesheet_vars()

    def on_font_dialog_finished(self):
        #print ('on_font_dialog_finished')
        # On Cygwin/X I get the finished event before the accepted, so I can't do this:
        #self.disconnect_font_dialog()
        #self.fontDialog = None
        pass

    def on_font_dialog_rejected(self):
        #print ('on_font_dialog_rejected')
        pass

    def on_font_dialog_current_font_changed(self, font):
        #print ('on_font_dialog_current_font_changed')        
        #print (font.family())
        pass

    def on_zoom_in(self):
        self.stylesheetMgr.zoom_in()
        self.stylesheetMgr.apply()
        self.stylesheetMgr.save_stylesheet_vars()

    def on_zoom_out(self):
        self.stylesheetMgr.zoom_out()
        self.stylesheetMgr.apply()
        self.stylesheetMgr.save_stylesheet_vars()

    def save_geometry_on_quit(self):
        """Get and save the geometry (size, aspect ratio, position) of the main window"""
        geometry = self.saveGeometry()
        self.settings.setValue('geometry', geometry)
        #print ( 'save_geometry_on_quit {g}'.format(g=geometry) )
        self.settings.sync()

    def onQuit(self):
        self.save_geometry_on_quit()
        self.app.quit()

    def closeEvent(self, event):
        """
        This overridden method is called whenever a window is closed when you hit the upper right X
        on the window, call the same function we call for handling CTRL-Q or File Menu->Quit
        """
        self.save_geometry_on_quit()

        # Pass the event to the class we inherit from
        super(MainWindow, self).closeEvent(event)

    def file_menu_selected(self, q):
        #print(q.text() + ' selected')
        if q.text() == 'Save':
            if self.currentFileName:
                # just perform the save
                self.saveFileDialog()
            else:
                # put up the Save file dialog
                self.saveFileDialog()
                pass
        elif q.text() == 'New':
            # What does New mean?
            pass
        elif q.text() == 'Save As':
            # Similar to New I guess
            pass
        elif q.text() == 'Open':
            # Put up the Open File Dialog
            pass

## Test Code
class TestAppMainWindow(MainWindow):
    """Class that demonstrates deriving a class from MainWindow"""
    def __init__(self, parsedArgs, **kwargs ):
        super(TestAppMainWindow, self).__init__(parsedArgs, **kwargs)
        self.show()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--test', help='Test Argument placeholder', default='Test')
    parsedArgs,unparsedArgs = parser.parse_known_args()

    # Pass unparsed args to Qt, might have some X Windows args, like --display
    qtArgs = sys.argv[:1] + unparsedArgs
    app = QApplication(qtArgs)

    mainw = TestAppMainWindow(parsedArgs, app=app, organizationName='Craton', appName='UqtWinTest',
                              title='Main Window' )

    sys.exit(app.exec_())

