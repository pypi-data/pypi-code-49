#!/usr/bin/python3
import datetime
from PyQt5 import QtCore, QtBluetooth


class Socket(QtCore.QObject):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.lastCmd = ""

        protocol = QtBluetooth.QBluetoothServiceInfo.RfcommProtocol
        self.socket = QtBluetooth.QBluetoothSocket(protocol)
        self.socket.connected.connect(self.parent.connected)
        self.socket.disconnected.connect(self.parent.disconnected)
        self.socket.error.connect(self._error)

        self.agent = QtBluetooth.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.setLowEnergyDiscoveryTimeout(2000)
        self.agent.deviceDiscovered.connect(self._add)
        self.agent.finished.connect(self._autoConnect)
        self.agent.error.connect(self._error)

    def _add(self, dev):
        """ Append the discovered device to the address combobox """
        name = dev.name()
        addr = dev.address().toString()
        if name != addr.replace(":", "-"):
            entry = f"{addr} ({name})"
            if self.parent.ui.macBox.findText(entry) == -1:
                self.parent.ui.macBox.addItem(entry)
                self._select(addr, name)

    def _autoConnect(self):
        """ Initiate a connection with the last used address on startup """
        last = self.parent.db["mac"]
        auto = self.parent.ui.autoconnectBox.isChecked()
        self.parent.setStatus("Ready")
        if last and auto:
            self.parent.ui.connectButton.setText("Disconnect")
            self.parent.ui.macBox.setEnabled(False)
            self.parent.enabled = True
            self.connect()

    def _error(self, error):
        """ Send a disconnect signal and forward a connection error string to the main window """
        sender = QtCore.QObject.sender(self)
        error = sender.errorString().lower()
        self.parent.disconnected()
        self.parent.setStatus(f"Connection failed: {error}")

    def _hasData(self):
        """ Return true if device is connected and has an available line """
        return self.socket.canReadLine() and self.isConnected()

    def _parse(self, line: str):
        """ Parse the raw data string into a dict and return it """
        data = {}
        try:
            for element in line.split(";"):
                key, value = element.split("=")
                data[key] = value
            now = datetime.datetime.now()
            data["date"] = f"{now.day:02d}/{now.month:02d}/{now.year:02d}"
            data["time"] = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
        except ValueError:
            pass
        return data

    def _select(self, addr, name):
        """ Restore last MAC address into the combobox, or find a new Flowcell device """
        mac = self.parent.db["mac"]
        isHC = not mac and name.startswith("Flowcell")
        if addr == mac or isHC:
            self.parent.ui.macBox.setCurrentText(f"{addr} ({name})")

    def connect(self):
        """ Initiate the connection """
        mac = self.parent.ui.macBox.currentText()
        active = self.parent.enabled and not self.isConnected()
        if mac and active:
            mac = mac.split()[0]
            self.parent.db["mac"] = mac
            self.parent.setStatus(f"Connecting to {mac} ...")

            addr = QtBluetooth.QBluetoothAddress(mac)
            uuid = QtBluetooth.QBluetoothUuid(QtBluetooth.QBluetoothUuid.SerialPort)
            self.parent.connectTimer.stop()
            self.agent.stop()
            self.socket.abort()
            self.socket.connectToService(addr, uuid, QtCore.QIODevice.ReadWrite)

    def disconnect(self):
        """ Abort the connection """
        self.socket.abort()
        self.parent.setStatus("Disconnected")

    def isConnected(self):
        """ Return true if the device is connected """
        isConnected = bool(self.socket.state() == QtBluetooth.QBluetoothSocket.ConnectedState)
        return isConnected

    def read(self):
        """ Read the raw string from the Bluetooth device """
        buffer = []
        while self._hasData():
            line = bytes(self.socket.readLine(128))
            line = line.decode("utf8").strip()
            buffer.append(line)
        if len(buffer) > 1:
            last = buffer[-1]
            parsed = self._parse(last)
            self.parent.render(parsed)

    def send(self):
        """ Send a string to the Bluetooth device """
        cmd = self.parent.ui.sendLine.text()
        cmd = cmd if cmd else self.lastCmd
        self.lastCmd = cmd
        if cmd:
            data = f"{cmd}\n".encode("utf8")
            self.socket.write(data)
            self.parent.ui.sendLine.clear()
            self.parent.ui.consoleText.appendPlainText(f"> {cmd}")
