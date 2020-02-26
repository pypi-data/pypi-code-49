#!/usr/bin/python3
import datetime
import sys
from pathlib import Path
from PyQt5 import QtWidgets, QtCore, QtGui, uic

try:
    from .frontend import flowcell as flowcell_ui
    from .__id__ import ID, APP_NAME
    from .backend.hc05 import Socket
    from .backend.database import Database
except ImportError:
    from __id__ import ID, APP_NAME
    from backend.hc05 import Socket
    from backend.database import Database

LOCAL = Path(__file__).parent
SETTINGS_FILE = Path.home() / ".config" / ID / "settings.json"


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.enabled = False

        self.bt = Socket(self)
        self._initUI()
        self._initDB()
        self._initBT()

        self.ui.sendButton.clicked.connect(self.bt.send)
        self.ui.connectButton.clicked.connect(self._toggle)
        self.ui.browseButton.clicked.connect(self._browse)
        self.ui.resetButton.clicked.connect(self._reset)
        self.ui.daysBox.valueChanged.connect(self._timerUpdate)
        self.ui.hoursBox.valueChanged.connect(self._timerUpdate)
        self.ui.minutesBox.valueChanged.connect(self._timerUpdate)
        self.ui.secondsBox.valueChanged.connect(self._timerUpdate)
        self.show()

    def _browse(self):
        """ Open a browse dialog to select the CSV output directory """
        dialog = QtWidgets.QFileDialog(self, "Choose an output directory")
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
        dialog.setDirectory(self.ui.outputLine.text())
        if dialog.exec_():
            folder = dialog.selectedFiles()[0]
            self.ui.outputLine.setText(folder)

    def _getHeader(self):
        """ Return the list of columns used for the CSV columns """
        header = self.ui.headerLine.text()
        header = header.split(",")
        return header

    def _getInterval(self):
        """ Return the acquisition interval in milliseconds """
        interval = 1000 * self.ui.secondsBox.value()
        interval += 1000 * 60 * self.ui.minutesBox.value()
        interval += 1000 * 60 * 60 * self.ui.hoursBox.value()
        interval += 1000 * 60 * 60 * 24 * self.ui.daysBox.value()
        if interval:
            return interval
        return 1

    def _initBT(self):
        """ Initiate Bluetooth timers and populate the address combobox with paired devices """
        self.readTimer = QtCore.QTimer()
        self.readTimer.timeout.connect(self.bt.read)
        self.readTimer.setInterval(self._getInterval())
        self.connectTimer = QtCore.QTimer(interval=6000)
        self.connectTimer.timeout.connect(self.bt.connect)
        self.bt.agent.start()
        self.setStatus("Device discovery in progress ...")

    def _initDB(self):
        """ Initiate the settings database and track widget values """
        self.db = Database(SETTINGS_FILE)
        self.db.fields.track((
                             self.ui.macBox,
                             self.ui.autoconnectBox,
                             self.ui.outputLine,
                             self.ui.headerLine,
                             self.ui.daysBox,
                             self.ui.hoursBox,
                             self.ui.minutesBox,
                             self.ui.secondsBox,
                             ))

    def _initLog(self):
        """ Create a new CSV file as YYYY_MM_DD.csv """
        now = datetime.datetime.now()
        timestamp = f"{now.year:02d}_{now.month:02d}_{now.day:02d}"
        output_dir = Path(self.ui.outputLine.text())
        output_dir.mkdir(parents=True, exist_ok=True)
        self.output = output_dir / f"{timestamp}.csv"
        self._write(self._getHeader(), mode="w")

    def _initUI(self):
        """ Load widgets and icons """
        try:
            self.ui = flowcell_ui.Ui_MainWindow()
            self.ui.setupUi(self)
        except NameError:
            path = LOCAL / "frontend" / "flowcell.ui"
            self.ui = uic.loadUi(path, self)

        path = LOCAL / "frontend" / "flowcell.svg"
        icon = QtGui.QIcon(str(path))
        self.setWindowIcon(icon)
        self.setWindowTitle(APP_NAME)
        self.ui.sendLine = SendLine(self)
        self.ui.sendLayout.insertWidget(0, self.ui.sendLine)

    def _reset(self):
        """ Reset configuration to default """
        self.db.reset()
        self.db.fields.load()

    def _timerUpdate(self):
        """ Update the interval of the acquisition read timer """
        self.readTimer.setInterval(self._getInterval())

    def _toggle(self):
        """ Toggle the connection with the selected device """
        self.enabled = not self.enabled
        if self.enabled:
            self.ui.connectButton.setText("Disconnect")
            self.ui.macBox.setEnabled(False)
            self.bt.connect()
        else:
            self.ui.connectButton.setText("Connect")
            self.ui.macBox.setEnabled(True)
            self.bt.disconnect()

    def _write(self, array: list, mode="a"):
        """ Join list elements with a semicolon separator, append the string to the current CSV file """
        if any(array):
            try:
                with open(self.output, mode) as f:
                    line = ";".join(array)
                    f.write(f"{line}\n")
            except PermissionError:
                print(f"PermissionError: could not write to '{self.output}'")
            except FileNotFoundError:
                print(f"FileNotFoundError: could not find '{self.output}'")
                self._initLog()

    def closeEvent(self, event=None):
        """ Save database before exit """
        self.db.save()
        self.parent.exit()

    def connected(self):
        """ Slot: connection successful """
        self.setStatus("Connected")
        self.ui.sendButton.setEnabled(True)
        self.ui.sendLine.setEnabled(True)
        self.ui.consoleText.setEnabled(True)
        self._initLog()
        self.readTimer.start()

    def disconnected(self):
        """ Slot: connection terminated """
        self.ui.sendButton.setEnabled(False)
        self.ui.sendLine.setEnabled(False)
        self.ui.consoleText.setEnabled(False)
        if self.enabled:
            self.connectTimer.start()

    def render(self, data: dict):
        """ Forward the raw acquisition result to the console and the parsed result to the CSV file """
        if self.bt.isConnected() and any(data):
            # Output raw data to console
            text = str(data)[1:-1]
            self.ui.consoleText.appendPlainText(text)

            # Output parsed data to CSV
            line = []
            for h in self._getHeader():
                cell = data.get(h, "")
                line.append(cell)
            self._write(line)

    def setStatus(self, status=""):
        """ Update main window status bar """
        self.statusBar().showMessage(status)


class SendLine(QtWidgets.QLineEdit):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setEnabled(False)

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.parent.bt.send()
        QtWidgets.QLineEdit.keyPressEvent(self, event)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setDesktopFileName(ID)
    app.setApplicationName(APP_NAME)
    Main(app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
