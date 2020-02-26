#!/usr/bin/python3
import bluetooth
import datetime
import sys
from PyQt5 import QtCore, QtBluetooth


class Socket(QtCore.QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.lastCmd = ""

        self.agent = QtBluetooth.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.setLowEnergyDiscoveryTimeout(1000)
        self.agent.deviceDiscovered.connect(self._add)
        self.agent.finished.connect(self._autoConnect)
        self.agent.error.connect(self._errorAgent)

    def _add(self, dev):
        name = dev.name()
        addr = dev.address().toString()
        if name != addr.replace(":", "-"):
            entry = f"{addr} ({name})"
            if self.parent.ui.macBox.findText(entry) == -1:
                self.parent.ui.macBox.addItem(entry)
                self._select(addr, name)

    def _autoConnect(self):
        self.agent.finished.disconnect(self._autoConnect)
        if self.parent.ui.autoconnectBox.isChecked():
            self.parent.ui.connectButton.setText("Disconnect")
            self.parent.ui.macBox.setEnabled(False)
            self.parent.enabled = True
            QtCore.QTimer.singleShot(5000, self.connect)

    def _errorSocket(self, error):
        self.parent.disconnected()
        try:
            err = str(error)[1:-1]
            err = err.split(", ")
            err = err[1][1:-1]
            if err != "Bad file descriptor":  # Socket closed
                self.parent.setStatus(f"Connection failed: {err}")
        except IndexError:
            self.parent.setStatus(f"Connection failed: {error}")

    def _errorAgent(self, error):
        sender = QtCore.QObject.sender(self)
        error = sender.errorString().lower()
        self.parent.disconnected()
        self.parent.setStatus(f"Connection failed: {error}")

    def _parse(self, line):
        try:
            data = {}
            for element in line.split(";"):
                key, value = element.split("=")
                data[key] = value
            now = datetime.datetime.now()
            data["date"] = f"{now.day:02d}/{now.month:02d}/{now.year:02d}"
            data["time"] = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
            self.parent.render(data)
        except ValueError:
            pass

    def _select(self, addr, name):
        mac = self.parent.db["mac"]
        isHC = not mac and name.startswith("HC0")
        if addr == mac or isHC:
            self.parent.ui.macBox.setCurrentText(f"{addr} ({name})")

    def connect(self):
        print("connect")
        mac = self.parent.ui.macBox.currentText()
        active = self.parent.enabled and not self.isConnected()
        print(self.isConnected())
        if mac and active:
            mac = mac.split()[0]
            self.parent.db["mac"] = mac
            self.parent.setStatus(f"Connecting to {mac} ...")

            self.agent.stop()
            self.parent.connectTimer.stop()
            try:
                self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                self.socket.connect((self.parent.db["mac"], 1))
                self.parent.connected()
                self.parent.setStatus("Connected")
            except bluetooth.btcommon.BluetoothError:
                self._errorSocket(sys.exc_info()[1])
                self.parent.disconnected()

    def disconnect(self):
        try:
            self.socket.close()
        except AttributeError:
            pass
        self.parent.disconnected()
        self.parent.setStatus("Disconnected")
        self.agent.start()

    def isConnected(self):
        try:
            self.socket.getpeername()
            return True
        except:
            return False

    def _hasData(self):
        return self.socket.canReadLine() and self.isConnected()

    def read(self):
        line = ""
        while not line.endswith("\r\n"):
            try:
                line += self.socket.recv(1024).decode()
            except bluetooth.btcommon.BluetoothError:
                self.parent.disconnected()
                self._errorSocket(sys.exc_info()[1])
                self.connect()
                break

        if line.endswith("\r\n"):
            last = line.splitlines()[-1]
            self._parse(last)

    def send(self):
        cmd = self.parent.ui.sendLine.text()
        cmd = cmd if cmd else self.lastCmd
        self.lastCmd = cmd
        if cmd:
            self.parent.ui.consoleText.appendPlainText(f"> {cmd}")
            self.parent.ui.sendLine.clear()
            self.socket.send(f"{cmd}\n")
