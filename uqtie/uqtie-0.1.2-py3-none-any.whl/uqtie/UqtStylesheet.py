#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Class that manages a UQtie application's stylesheet

There are advantages and disadvantages to Qt stylesheets, Qt settings, and
Qt Style. They aren't mutually exclusive, and they don't all play together
either.

This module attempts to make it possible to use a stylesheet while still
using the QFontDialog to select fonts, and zoom-in/zoom-out shortcuts such
as CTRL-+.

The idea is that we have variables (which come from somewhere, right now a
pickled dictionary, but later could be elsewhere, or multiple elsewheres).
These variables can be used in the stylesheet, such that the dynamic changes in
appearance can be made at runtime without requiring stylesheet changes, and the
changes can be persisted also without changing the stylesheet.

Font, font size and widget sizes (e.g QScrollBar:vertical { width } ) seem like
good candidates to be determined dynamically instead of via hardcoded values
in a stylesheet. That way, when you have high-DPI monitor and less-than-perfect
vision, you can adjust easily.

Part of my motivation for doing this is because PyQt running on Windows, Linux,
MacOS and Cygwin doesn't behave identically, not even close to identical in
some ways. If they would all have identical QScreens given identical monitors
and graphics cards, then you could just make reasonable choices for your stylesheet,
and rely on the OS GUI settings.

Variables you can use in a QSS file are:

 $main_font_family
 $main_font_weight (not supported yet)
 $main_font_size
 $scroll_bar_width

Futures:
1) Add more variables
2) Make an inspector widget for stylesheet variables

"""

from   __future__      import print_function
from   pathlib         import Path

import os,re,pickle

from   PyQt5.QtCore    import QSettings

class StylesheetManager(object):
    """
    Class that manages a UQtie application's stylesheet
    """

    # If no stylesheet has been provided, use this one. Should this
    # really have  scroll bar dimensions?
    defaultStylesheet = """
    QWidget {
        font-family:   $main_font_family;
        font-weight:   $main_font_weight;
        font-size:     $main_font_size;
    }
    
    QScrollBar:vertical {
        width:         $scroll_bar_width;
    }
    
    QScrollBar:horizontal {
        height:        $scroll_bar_width;
    }
    """
    def __init__(self, app, settings, appName ):

        self.stylesheetFileName     = None
        self.stylesheetVarsFileName = None
        self.app                    = app
        self.appName                = appName
        self.appSettings            = settings
        self.varsDict               = {}

        self.defaultVarsDict        = {
            'main_font_family': 'Arial',
            'main_font_weight': 'Regular',
            'main_font_size'  : '16pt',
            'scroll_bar_width': '15px',
        }

        self.determine_stylesheet_filenames(appName)

    def determine_stylesheet_path(self):
        """
        Fill in self.appDirPath appropriately
        """
        self.appDirPath = None
        if os.name == 'nt':
            # running on Windows
            appDirPath = Path(os.path.expanduser('~')) / 'Application Files'
            if not appDirPath.is_dir():
                print ( '{p} is not a directory'.format(p=appDirPath))
                return

            appDirPath /= self.appName
            if not appDirPath.is_dir():
                try:
                    appDirPath.mkdir()
                except:
                    print ( 'Could not create directory {p}'.format(p=appdirPath))
                    return
            self.appDirPath = appDirPath
        else:
            # On other OS, we use Settings to determine where stylesheet lives
            if self.appSettings:
                self.appDirPath = Path(os.path.dirname(self.appSettings.fileName()))


    def determine_stylesheet_filenames(self, appName):
        """
        Fill in stylesheet filenames appropriately
        """
        self.determine_stylesheet_path()
        if self.appDirPath:
            #print ("self.appDirPath: {}".format(self.appDirPath))
            baseName = str(self.appDirPath / appName)
            self.stylesheetFileName = baseName + '.qss'
            self.stylesheetVarsFileName = baseName + 'Vars.pickle'

    def apply(self):
        """
        Apply the application window stylesheet, including variable value substitution
        """
        # This means:
        # 1) Read it from a file
        # 2) Replace all '{' and '}' which are QSS syntax (e.g. 'QWidget {') with 
        #    '{{' and '}}'. This protects the QSS syntax during the next steps.
        # 3) Replace all $word with {word} thus turning the string into a Python
        #    string with argument specifiers (e.g. '{main_font_family}'). 
        # 4) Replace all the format-string argument specifiers with variables
        # 5) Apply the resulting stylesheet to the App

        #print ( "apply: {}".format(self.stylesheetFileName))
        stylesheetText = None

        try:
            with open(self.stylesheetFileName, 'r') as content_file:
                stylesheetText = content_file.read()
        except:
            pass

        if not stylesheetText:
            print(f'No file {self.stylesheetFileName}')
            stylesheetText = self.defaultStylesheet
            try:
                with open(self.stylesheetFileName, 'w') as content_file:
                    content_file.write(stylesheetText)
            except:
                print(f'Could not write default stylesheet file {self.stylesheetFileName}')
                

        # These next two could be done in one pass using the cool multiple_replace() from
        # https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python
        # But this is easier to read
        stylesheetText = stylesheetText.replace('{', '{{')
        stylesheetText = stylesheetText.replace('}', '}}')

        # Turn all $word into {word}
        stylesheetText = re.sub(r'\$(([a-z]|[A-Z])\w*)', r'{\1}',  stylesheetText)
        # for k, v in self.varsDict.items():
        #    print ( f'{k}: {v}' )

        # substitute everything from our variables dict
        result = stylesheetText.format_map(self.varsDict)

        # apply
        self.app.setStyleSheet(result)

    def save_stylesheet_vars(self ):
        """Write our variables dict out to a file"""
        with open(self.stylesheetVarsFileName, 'wb') as h:
            pickle.dump(self.varsDict, h)

    def set_missing_stylesheet_vars(self ):
        """Set all the missing variables in the variables dict to default values"""
        for k in self.defaultVarsDict:
            self.varsDict.setdefault(k, self.defaultVarsDict[k])

    def read_stylesheet_vars(self ):
        """Read all the variables from saved file into our dict"""
        try:
            with open(self.stylesheetVarsFileName, 'rb') as h:
                self.varsDict = pickle.loads(h.read())
        except FileNotFoundError as e:
            print(e)
        # Maybe some values are missing, fix it up
        self.set_missing_stylesheet_vars()

    def zoom_in(self):
        """Increase the value of variables that influence the size of the UI"""
        # Trim off 'pt' at the end of the string. Maybe a little fragile...
        fontSize = int(self.varsDict['main_font_size'][0:-2])
        fontSize += 1
        self.varsDict['main_font_size'] = f'{fontSize}pt'

        # Trim off 'px' at the end of the string. Also a little fragile...
        scrollBarWidth = int(self.varsDict['scroll_bar_width'][0:-2])
        scrollBarWidth += 1
        self.varsDict['scroll_bar_width'] = f'{scrollBarWidth}px'

    def zoom_out(self):
        """Decrease the value of variables that influence the size of the UI"""
        # Trim off 'pt' at the end of the string. Maybe a little fragile...
        fontSize = int(self.varsDict['main_font_size'][0:-2])
        if fontSize > 0:
            fontSize -= 1
            self.varsDict['main_font_size'] = f'{fontSize}pt'

        # Trim off 'px' at the end of the string. Also a little fragile...
        scrollBarWidth = int(self.varsDict['scroll_bar_width'][0:-2])
        if scrollBarWidth > 0:
            scrollBarWidth -= 1
            self.varsDict['scroll_bar_width'] = f'{scrollBarWidth}px'

    # Variable setters / Properties - don't want to keep adding these for every variable
    # and the way it is evolving, it seems like we don't have to
    def set_main_font_family(self, family):
        self.varsDict['main_font_family'] = family

    def set_main_font_weight(self, weight):
        self.varsDict['main_font_weight'] = weight

    def set_main_font_size(self, size):
        self.varsDict['main_font_size'] = size

## Test Code
import argparse, sys
from   PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow

class TestAppMainWindow(QMainWindow):

    def __init__(self, parsedArgs, **kwargs ):
        super(TestAppMainWindow, self).__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        vbox = QVBoxLayout(self.centralWidget())

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--test-write-vars', action='store_const', const=True,
                        help='Test writing variables to file')
    parser.add_argument('-r', '--test-read-vars', action='store_const', const=True,
                        help='Test reading variables from file')
    parsedArgs,unparsedArgs = parser.parse_known_args()

    organizationName='Craton'
    appName='StyMgrTest'

    # Pass unparsed args to Qt, might have some X Windows args, like --display
    qtArgs = sys.argv[:1] + unparsedArgs
    app = QApplication(qtArgs)

    settings = QSettings(organizationName, appName)

    styMgr = StylesheetManager(app, settings, appName)

    if parsedArgs.test_write_vars:
        print('write')
        styMgr.save_stylesheet_vars()
        sys.exit(0)

    if parsedArgs.test_read_vars:
        print('read')
        styMgr.read_stylesheet_vars()
        for k, v in styMgr.varsDict.items():
            print(k, v)
        sys.exit(0)

    mainw = TestAppMainWindow(parsedArgs, app=app, organizationName=organizationName, appName=appName)
    
    sys.exit(app.exec_())
