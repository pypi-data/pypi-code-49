import platform
import time
import socket
import threading
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from quarchpy.disk_test.dtsGlobals import dtsGlobals

class DTSCommms:

    def __init__(self):
        # declaring variables used in sending messages at different sections of class
        self.standardHeader = "QuarchCSSelection"
        self.versionNumber = "1.01"


    # Legacy code - 01/01/2020
    # def notifyChoiceOption(self, count, option):
    #     sendString = "QuarchDTS::" + str(count) + "=" + str(option)
    #     # Send to GUI server
    #     self.sendMsgToGUI(sendString)

    def newNotifyChoiceOption(self, type, dict, dictValue, moduleType = None, outputMode = None):
        sendString = ""
        if type == "qpsmodule":
            sendString = self.createXMLSelectionModule(dict, dictValue, outputMode, itemType="qpsmodule")
        if type == "module":
            sendString = self.createXMLSelectionModule(dict, dictValue)
        elif "drive" in type:
            sendString = self.createXMLSelectionDrive(dict, dictValue, moduleType)

        sendString = "QuarchDTS::" + sendString

        # printText(sendString)

        self.sendMsgToGUI(sendString)


    """
    Function for any item being sent to GUI 
    Default is to wait 3 seconds, but can be set for longer / infinite
    """
    def sendMsgToGUI(self, toSend, timeToWait=5):

        # Opening socket using ip of connected device.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((dtsGlobals.GUI_TCP_IP, 9921))

        
        # printText("Item Sent across : " + toSend)
        toSend = str.encode(toSend)

        # sending message
        s.sendall(toSend + b"\n")

        # basically infinite wait
        if timeToWait is None:
            timeToWait = 999999

        # function for response + timeout
        self.processTimeoutAndResult(s, timeToWait)

        # Close socket on way out
        s.close()


    """
    Starts a subprocess to attempt to receive a return packet from java
    if timeout of 3 seconds is exceeded, break
    """
    def processTimeoutAndResult(self, socket, timeToWait):
        processObject = threading.Thread(target=self.getReturnPacket(socket))
        processObject.start()
        # timeout of 3 seconds
        start = time.time()
        while time.time() - start <= timeToWait:
            if processObject.is_alive():
                # printText("Sleeping, timeout Left = " + str(TIMEOUT - (time.time() - start)))
                time.sleep(.1)  # Just to avoid hogging the CPU
            else:
                # All the processes are done, break now.
                break
        else:
            # We only enter this if we didn't 'break' above.
            # printText("Response Timeout Reached")
            processObject.terminate()
            processObject.join()


    """
    reads data from socket passed
    """
    def getReturnPacket(self, socket):
        BUFFER_SIZE = 4096
        data = ""
        while (True):
            data = socket.recv(BUFFER_SIZE)
            if "OK" in bytes.decode(data):
                if "QCSVersion" in bytes.decode(data):
                    dtsGlobals.QCSVersionValid = self.isVersionCompat(bytes.decode(data))
                break
            if "choiceResponse" in bytes.decode(data):
                dtsGlobals.choiceResponse = data
                break
            if "STOP" in bytes.decode(data):
                # User requested to stop a test
                dtsGlobals.continueTest = False
                break
            if "INVALID VERSION" in bytes.decode(data):
                dtsGlobals.validVersion = False
                break
        return

    def isVersionCompat(self, data):
        # Split the version numbers first
        versionNumber = data.split("=")
        # If the min version is current version, it is fine
        if versionNumber == dtsGlobals.minQCSVersion:
            return True
        versionNumbers = versionNumber[1].split(".")
        minVersionNumbers = dtsGlobals.minQCSVersion.split(".")
        # Iterate through each number to ensure compat
        for i, number in enumerate(versionNumbers):
            # If same item is > it is a pass
            if versionNumbers[i] > minVersionNumbers[i]:
                return True
            # If same item is < it is a fail
            if versionNumbers[i] < minVersionNumbers[i]:
                return False

            # Should be redundant as we'll already know if they're the same
            # If last item of list
            if i == len(versionNumbers) - 1:
                if versionNumbers[i] == minVersionNumbers[i]:
                    return True
        return True




    def createXMLSelectionDrive(self, key, values, driveType):

        top = Element(self.standardHeader)
        retString = ""

        # Drive types come in different dictionary types - different key names
        if "pcie" in driveType:

            child = SubElement(top, 'Name')
            child.text = str(values['vendor'])

            child = SubElement(top, 'Standard')
            # needs to send standard in form pcie:xx:xx:x
            child.text = str(key) #str(values['slot'])

            child = SubElement(top, 'ConnType')
            child.text = str("PCIe")

            child = SubElement(top, 'Description')
            child.text = str(values['device'])

            child = SubElement(top, 'XmlVersion')
            child.text = str(self.versionNumber)

            child = SubElement(top, 'itemType')
            child.text = str("Drive")

            # If backward compat needed with v1.01 QCS
            # retString = values["vendor"] + ", " + values["device"] + "=" + bytes.decode(tostring(top))

        elif "sas" in driveType:
            if platform.system() == 'Windows':
                child = SubElement(top, 'Name')
                child.text = str(values['model'])

                child = SubElement(top, 'Standard')
                child.text = str(key)

                child = SubElement(top, 'ConnType')
                child.text = str("SAS")

                child = SubElement(top, 'itemType')
                child.text = str("Drive")

                child = SubElement(top, 'XmlVersion')
                child.text = str(self.versionNumber)

                # If backward compat needed with v1.01 QCS
                # retString = str(key) + "=" + values["model"] + ", " + values["size"] + "=" + bytes.decode(tostring(top))
                # printText(retString)
            else:
                child = SubElement(top, 'Name')
                child.text = str(values['vendor'])

                child = SubElement(top, 'Standard')
                child.text = str(key)

                child = SubElement(top, 'ConnType')
                child.text = str("SAS")

                child = SubElement(top, 'Description')
                child.text = str(values['model'] + ", " + values['size'])

                child = SubElement(top, 'itemType')
                child.text = str("Drive")

                child = SubElement(top, 'XmlVersion')
                child.text = str(self.versionNumber)

                # If backward compat needed with v1.01 QCS
                # retString = str(key) + "=" + values["model"] + ", " + values["size"] + "=" + bytes.decode(tostring(top))
                # printText(retString)

        retString = bytes.decode(tostring(top))
        return retString


    def createXMLSelectionModule(self, dict, dictValue, outputMode = None, itemType="Module"):

        top = Element(self.standardHeader)

        indexOfColon = dict.find(":")
        conType = str(dict[:indexOfColon])
        IpAddress = str(dict[indexOfColon + 1:])

        child = SubElement(top, 'ConnType')
        child.text = str(conType)

        child = SubElement(top, 'QtlNum')
        child.text = str(dictValue)

        if outputMode is not None:
            child = SubElement(top, "OutputMode")
            child.text = str(outputMode)

        child = SubElement(top, 'XmlVersion')
        child.text = str(self.versionNumber)

        child = SubElement(top, 'itemType')
        child.text = str(itemType)

        child = SubElement(top, 'IpAddress')
        child.text = str(dict[indexOfColon + 1:])

        #return str(dict) + "=" + str(dictValue) + "=" + bytes.decode(tostring(top))
        return bytes.decode(tostring(top))

