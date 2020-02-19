# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
#!/usr/bin/env python3

from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QSettings, QCoreApplication, QStandardPaths
from PyQt5.QtWidgets import QApplication, QMessageBox, QSplashScreen
from PyQt5.QtGui import QIcon, QPixmap
import hashlib, sys, gc, os, traceback

from ..gui.custom_widgets import SplashScreen
from ..gui.open import OpenExperiment
import iocbio.kinetics.io.db as dbwrapper


################################################################################
### Main app function
################################################################################

def app(app_instance, args, modules):
    from iocbio.kinetics.gui.mainwindow import MainGUI
    from iocbio.kinetics.handler.roi import ROIHandler
    from iocbio.kinetics.handler.experiment_generic import ExperimentGeneric
    from iocbio.kinetics.gui.dbconnect import ConnectDatabaseGUI

    app = app_instance
    database = None
    connect_to_db = args.db
    open_file = False
    repeat = True
    application_name = "IOCBIO Kinetics"

    settings = QSettings()
    devel_mode = (int(settings.value("development/exceptions_crash", 0)) > 0)

    splash_pixmap = QPixmap( os.path.join( os.path.dirname(os.path.realpath(__file__)), 'splash.png') )
    window_icon = QIcon( os.path.join( os.path.dirname(os.path.realpath(__file__)), 'icon.png') )

    # set window icon
    app.setWindowIcon(window_icon)

    while repeat:
        repeat = False
        while not database or not database.is_ok:
            if not connect_to_db:
                try:
                    database = dbwrapper.DatabaseInterface()
                except Exception as e:
                    errtxt = 'Error occurred:\n\n' + str(e) + "\n\n" + str(e)
                    print('\n' + errtxt + '\n\n')
                    print(traceback.format_exc())
                    if devel_mode:
                        sys.exit(-1)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle(application_name + ": Error")
                    msg.setInformativeText(errtxt)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()

            if connect_to_db or not database or not database.is_ok:
                connect = ConnectDatabaseGUI()
                connect.show()
                exit_code = app.exec_()
                connect.deleteLater()
                if not connect.save_settings:
                    sys.exit(exit_code)
                database = None
                connect_to_db = False

        try:
            # check if need to open file
            if open_file:
                dlg = OpenExperiment(modules)
                if dlg.exec_():
                    args = dlg.getResponse()
                    args.rw = True
                    args.force_rw = False

            # start splashscreen
            app.processEvents()
            splash = SplashScreen(splash_pixmap)
            splash.showMessage("Starting application")
            splash.show()
            app.processEvents()

            # init database
            ExperimentGeneric.database_schema(database)
            ROIHandler.database_schema(database)
            modules.database_schema(database)
            app.processEvents()

            if args and args.rw:
                database.set_read_only(False)
            else:
                database.set_read_only(True)

            if args and args.force_rw:
                database.disable_read_only = True
                database.set_read_only(False)

            data = modules.create_data(database, args = args)
            modules.database_process(database, data, args)

            gui_obj = MainGUI(database, data, modules, splash)
            gui_obj.show()
            splash.finish(gui_obj)
            app.processEvents()
            exit_code = app.exec_()
            connect_to_db = gui_obj.reopen_database_connection
            open_file = gui_obj.open_file
            repeat = (connect_to_db or open_file)

            database.close()
            del splash
            del gui_obj
            del database
            splash = None
            database = None
            gc.collect()

            args = None

        # catch exceptions and show them on terminal and GUI
        except Exception as e:
            errtxt = 'Error occurred:\n\n' + str(e) + "\n\n" + str(type(e))
            print('\n' + errtxt + '\n\n')
            print(traceback.format_exc())

            if devel_mode:
                sys.exit(-1)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(application_name + ": Error")
            msg.setInformativeText(errtxt)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    sys.exit(exit_code)


################################################################################
### Main entry point
################################################################################
def main():
    from iocbio.kinetics.io.modules import Modules
    import argparse

    # set application names
    QCoreApplication.setOrganizationName("iocbio")
    QCoreApplication.setApplicationName("kinetics")
    app_instance = QApplication([])

    # load modules
    modules = Modules()

    # fill arguments
    parser = argparse.ArgumentParser(description='IOCBIO Kinetics analyser', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', type=str, help='Input file')
    parser.add_argument('--db', action='store_true', help='Open database selection tool')
    parser.add_argument('--rw', action='store_true', help='If given, program started in Read/Write mode')
    # following is a hidden feature for forcing disabling read-only mode option
    parser.add_argument('--force-rw', action='store_true', help=argparse.SUPPRESS)

    # fill protocol help text and module specific args
    protocol = '''
Experiment protocols that can be specified on command line (enclose in '' if contains space).

'''
    protocol = modules.args(parser, protocol)
    parser.add_argument('--protocol', type=str, default=None, help = protocol)
    args = parser.parse_args()
    app(app_instance, args, modules)

# if run as a script
if __name__ == '__main__':
    main()
