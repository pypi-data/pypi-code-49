#!/usr/bin/env python
'''
This file contains the core functions for the drive test suite.
Functions are placed here for the core setup functions called during the init stage of a test (or CSV parsed test set)


########### VERSION HISTORY ###########

03/01/2019 - Andy Norrie        - First Version

########### INSTRUCTIONS ###########

N/A

####################################
'''
from __future__ import print_function
import sys
import os
import multiprocessing
import logging
import pkg_resources
import importlib
from datetime import datetime
import traceback
import xml.etree.ElementTree as cElementTree

from quarchpy.user_interface import *
from quarchpy.device.scanDevices import *
from quarchpy.device import quarchQPS, quarchDevice

from quarchpy.connection_specific.connection_QPS import QpsInterface

from quarchpy.qps.qpsFuncs import isQpsRunning

from quarchpy.disk_test.testLine import testLine
from quarchpy.disk_test import driveTestConfig
from quarchpy.disk_test.dtsGlobals import dtsGlobals
from quarchpy.disk_test.dtsComms import DTSCommms
from quarchpy.disk_test.hostInformation import HostInformation

# Import zero conf only if available
try:
    import zeroconf
    from zeroconf import ServiceInfo, Zeroconf

    zeroConfAvail = True
except:
    logging.warning("Please install zeroconf using 'pip install zeroconf'")
    zeroConfAvail = False

myHostInfo = HostInformation()
comms = DTSCommms()
ignoredChoices = ["choiceResponse::rescan"]

def printToBackend(text=""):
    printText(text=text, terminalWidth=80,fillLine=True)

def printProgressBar(iteration, total):
    iteration = float(iteration)
    total = float(total)
    progressBar(iteration,total, fullWidth=80)


def sendLogMessage (logTime, messageType, messageText, messageSource, messageData = None, uId = ""):
    if ("TEST_LOG" in driveTestConfig.testCallbacks):
        driveTestConfig.testCallbacks["TEST_LOG"](uId, logTime, messageType, messageText, messageSource, messageData)

def executeAndCheckCommand(myDevice, command):
    # Run the command
    result = myDevice.sendCommand(command)

    # Log the command data
    sendLogMessage(time.time(), "debug", "Quarch Command: " + command + " - Response: " + result,
                   os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name,
                   {"debugLevel": 1, "textDetails": "Executing command on module"}, uId="");

    # Verify that the command executed as expected
    if (result == "OK"):
        return True
    else:
        sendLogMessage(time.time(), "error", "Failed to execute Torridon command",
                       os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name, uId="");
        return False


'''
Stores a given string in the test resources dictionary
'''
def storeResourceString(resourceName, resourceValue):
    driveTestConfig.testResources[resourceName] = resourceValue


"""
Checking the user's cmd is with admin privelages
"""
def isUserAdmin():
    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            # If == 1, user is running from elevated cmd prompt
            # printText(ctypes.windll.shell32.IsUserAnAdmin() == 1)
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
        except:
            traceback.print_exc()
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % (os.name,))


'''
Adds a newly defined quarch module to use during the test and stores it as a resource to use later
connection="USB:QTL1743" or "REST:192.168.1.12<7>"
moduleName="myModule1" (unique string to identify the resource later)
'''
def specifyQuarchModule(moduleName, interFaceType="PY", powerOnDevice=True):
    # allow use to find device, then connect to it
    connection = None

    if "PY" in interFaceType:
        connection = chooseQuarchModule(moduleName)
    elif "QPS" in interFaceType:
        connection = chooseQuarchModuleQPS(moduleName)

    if connection is None:
        printText("No item selected, test aborted. Waiting for new test start..\n")
        return 0

    # If this is an array controller sub module
    strPos = connection.find('<')
    if (strPos != -1):
        logging.debug(connection + " : " + moduleName)

        # Get the array part
        arrayConnection = connection[0:strPos]
        # Get the sub module nubmber
        arrayPosition = connection[strPos + 1:]
        arrayPosition = arrayPosition.strip(' >')

        # Create the array controller connection
        try :
            myQuarchDevice = quarchDevice(arrayConnection)
        except Exception as e:
            # If the connection to device failed, rescan for actual devices
            connection = None
            comms.sendMsgToGUI(toSend="stopTest")
            printText("Could not establish connection to root device. Test aborted")
            return 0

        # Promote connection to array type
        myArray = quarchArray(myQuarchDevice)
        # Get access to the sub-device
        mySubDevice = myArray.getSubDevice(arrayPosition)
        moduleResponse = mySubDevice.sendCommand("*TST?")

        # Test the connection
        if (moduleResponse != "OK"):
            notifyTestLogEvent(time.time(), "error", "Quarch module not ready",
                               os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name,
                               {"textDetails": "Module responded: " + moduleResponse})
        else:
            # Add the item to the test resources dictionary
            driveTestConfig.testResources[moduleName] = mySubDevice

    elif "QPS" in interFaceType:

        # Splitting string 'USB::QTL1999-01-001=5v' into connection and output mode
        connection, outputModeValue = connection.split("=")

        # Creating QPS connection with device  --  Uses GUI TCP
        myQuarchDevice = quarchDevice(connection, ConType="QPS:" + dtsGlobals.GUI_TCP_IP + ":9822")

        # Create the device connection, as a QPS connected device
        myQpsDevice = quarchQPS(myQuarchDevice)
        myQpsDevice.openConnection()

        # Add the item to the test resources dictionary
        driveTestConfig.testResources[moduleName] = myQpsDevice

        # Making an auto-power up -- Could be changed to specify whether it is to be powered up or not.
        if powerOnDevice:
            powerOnDrive(myQpsDevice, outputMode=outputModeValue)

    else:
        # Create the device connection
        myQuarchDevice = None

        try :
            myQuarchDevice = quarchDevice(connection)
        except Exception as e:
            # If the connection to device failed, rescan for actual devices
            connection = None
            comms.sendMsgToGUI(toSend="stopTest")
            printText("Error while connecting to specified device, test aborted")
            return 0

        # Test the connection
        moduleResponse = myQuarchDevice.sendCommand("*TST?")
        if (moduleResponse is None or moduleResponse == ""):
            notifyTestLogEvent(time.time(), "error", "Quarch module did not respond",
                               os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name)
            return
        elif (moduleResponse != "OK"):
            notifyTestLogEvent(time.time(), "warning", "Quarch module did not pass self test",
                               os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name,
                               {"textDetails": "Module responded: " + moduleResponse})

        # Add the item to the test resources dictionary
        driveTestConfig.testResources[moduleName] = myQuarchDevice

        # Making an auto-power up -- Could be changed to specify whether it is to be powered up or not.
        if powerOnDevice:
            powerOnDrive(myQuarchDevice)


def powerOnDrive(myQuarchDevice, outputMode=None):
    if outputMode is not None:
        myQuarchDevice.sendCommand("conf:out:mode " + outputMode)
        myQuarchDevice.sendCommand("conf out 12v pull on")

    # printText(myQuarchDevice.sendCommand("run:pow?"))
    # printText(myQuarchDevice.sendCommand("sig:12v:volt?"))
    myQuarchDevice.sendCommand("sig 12v volt 12000")
    powerStatus = myQuarchDevice.sendCommand("run pow?")
    # hd will reply with off if no power
    counter = 0
    while "on" not in str(powerStatus).lower() and counter < 50:
        if "plugged" in str(powerStatus).lower():
            return
        myQuarchDevice.sendCommand("run:pow up")
        time.sleep(0.2)
        counter += 1
        powerStatus = myQuarchDevice.sendCommand("run:pow?")


def chooseQuarchModuleQPS(moduleName, myQps=None):

    dir = os.path.dirname(os.path.realpath(__file__))

    if not isQpsRunning(dtsGlobals.GUI_TCP_IP):
        comms.sendMsgToGUI("QuarchDTS::StartQPS::" + str(dir), None)

    dtsGlobals.choiceResponse = None

    while True:
        try:  # moved this line here
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_sock.connect((dtsGlobals.GUI_TCP_IP, 9822))  # no longer throws error
            send_sock.close()
            break
        except socket.error:
            time.sleep(1)

    myQps = QpsInterface(host=dtsGlobals.GUI_TCP_IP)

    status = myQps.sendCmdVerbose("$qis status")
    while "Not Connected" in status:
        status = myQps.sendCmdVerbose("$qis status")
        time.sleep(0.2)

    # Small pause for QIS to start finding devices
    time.sleep(3)

    # Display and choose module from found modules
    qpsDeviceList = myQps.getDeviceList()

    # specify the module selection header
    comms.sendMsgToGUI("QuarchDTS::header<QPS>::Choose a Quarch module to connect to", None)

    content = " "
    content = content.join(qpsDeviceList)
    if "No Devices Found" in content:
        # python logic!
        printText("No Quarch modules currently detected", fillLine=True, terminalWidth=80)
    else:
        for quarchModule in qpsDeviceList:
            # Skip rest modules as we can't stream over rest
            if "rest" in quarchModule:
                continue
            connectionWithoutConType = quarchModule[quarchModule.rindex(":") + 1:]
            # Sending in the form : tcp::QTL1995-05-006
            comms.newNotifyChoiceOption("qpsmodule", quarchModule.replace("::",":"),
                                        connectionWithoutConType)  # outputMode=outputModeValue )

    # wait for next response from java
    comms.sendMsgToGUI("QuarchDTS::end-of-data", None)

    while dtsGlobals.choiceResponse is None and dtsGlobals.continueTest is True:
        time.sleep(0.25)

    # order should be choiceResponse::xyz
    choice = bytes.decode(dtsGlobals.choiceResponse)
    selection = choice.replace("\r\n","").split("::", 2)
    if "rescan" not in selection: #rescan is the only responce we dont want printed at the moment. If others are needed make a global list.
        logging.debug("Response from module selection was : " + choice)
        # printText("Response from module selection was : " + selection[1], fillLine=True, terminalWidth=80)


    if "choice-abort" in choice:
        return None
    elif "rescan" in choice:
        return chooseQuarchModuleQPS(moduleName, myQps)

    # Obtain output from the quarchModule selection
    selection[1] = selection[1].replace(":", "::")
    logging.debug("Selection1 is now " + selection[1])

    # Resetting the device prior to any commands being sent
    myQps.sendCmdVerbose("selection[1] conf:def:state")

    outMode = myQps.sendCmdVerbose(selection[1] + " conf:out:mode?")
    logging.debug("Out mode for selection was " + outMode)
    if "DISABLED" in outMode:
        comms.sendMsgToGUI("QuarchDTS::header::Choose a Quarch module to connect to", None)
        selection[1] = selection[1].replace("::", ":")
        # printText("changed selection1 back to : " + selection[1] + " for the cmd send")
        connectionWithoutConType = selection[1][selection[1].rindex(":") + 1:]
        comms.newNotifyChoiceOption("qpsmodule", selection[1].replace("::",":"), connectionWithoutConType, outputMode=outMode)
        # small wait to guarantee the frontend deals with parse +  list add before display appears
        time.sleep(0.5)
        comms.sendMsgToGUI("QuarchDTS::end-of-data::true", None)
        while dtsGlobals.choiceResponse is None and dtsGlobals.continueTest is True:
            time.sleep(0.25)

        choice = bytes.decode(dtsGlobals.choiceResponse)
        if "choice-abort" in choice:
            return None
        elif "rescan" in choice:
            return chooseQuarchModuleQPS(moduleName, myQps)

        outModeSelection = str(dtsGlobals.choiceResponse).split("::")
        outMode = outModeSelection[2]
        logging.debug(outMode)
        # It's easier to hardcode the 2 results, than to attempt a parse for different systems
        if "5V" in outMode:
            outMode = "5V"
        if "3v3" in outMode:
            outMode = "3v3"

    # Closing the connection to QPS
    myQps.client.close()

    selection[1] = selection[1].replace("::", ":")
    selection = selection[1]

    # if user does not select an item, we abort
    retVal = selection.strip() + "=" + outMode
    # print("returning value  " + retVal)
    return retVal


def chooseQuarchModule(moduleName, ipAddressLookup=None):
    dtsGlobals.choiceResponse = None

    # scan for quarch devices
    # favourite only False - Allow all connections to be present
    scanDictionary = scanDevices(favouriteOnly=False, ipAddressLookup=ipAddressLookup)

    # printText(scanDictionary)

    # Reset the variable so it's not searched for unless specified during same run of program.
    ipAddressLookup=None

    # specify the module selection header
    comms.sendMsgToGUI("QuarchDTS::header<PY>::Choose a Quarch module to connect to", None)

    # Print the provided list of devices with a numbered prefix
    for connection in scanDictionary:
        # need to replace before and after send
        # connection = connection.replace("::", ":")
        # comms.notifyChoiceOption(connection, scanDictionary[connection])
        comms.newNotifyChoiceOption("module", connection, scanDictionary[connection])
    if not scanDictionary:
        # python logic!
        printText("No Quarch modules currently detected")

    # wait for next response from java
    comms.sendMsgToGUI("QuarchDTS::end-of-data", None)

    while dtsGlobals.choiceResponse is None and dtsGlobals.continueTest is True:
        time.sleep(0.25)

    choice = bytes.decode(dtsGlobals.choiceResponse)
    selection = choice.split("::")
    # order should be choiceResponse::xyz
    selection = selection[1]
    selection = selection.replace(":", "::")
    if "rescan" not in selection: #rescan is the only responce we dont want printed at the moment. If others are needed make a global list.
        logging.debug("Response from module selection was : " + choice)
        # printText("Response from module selection was : " + selection, fillLine=True, terminalWidth=80)

    # if user does not select an item, we abort
    if "choice-abort" in selection:
        return None
    elif "rescan" in selection:
        if "==" in selection:
            ipAddressLookup = selection[selection.index("==") + 2:]
        return chooseQuarchModule(moduleName, ipAddressLookup)
    else:
        return selection.strip()

'''
Parses and executes all the tests specified within the given CSV file
testCallbacks=Dictionary of callback function for the tests
filePath=Full path to CSV file containing the tests
'''
def executeCsvTestFile(testCallbacks, filePath, delimitor="\t"):
    # Open the test file for parsing
    with open(filePath, 'r') as scriptFile:
        # Iterate through each line in the file
        for fileLine in scriptFile:
            # Comment lines
            if (fileLine.find("#") == 0):
                # Ignore file comment lines
                continue
            # Config line - for setting up modules and test elements
            elif (fileLine.find("Config") == 0):
                # Split the line into sections
                lineSections = fileLine.split(delimitor)
                # Get the module that the setup function is in
                moduleName = lineSections[1]
                # Get the name of the setup function
                testName = lineSections[2]

                # Build up the paramenter string for the python function call
                funcParams = ""
                for x in range(3, len(lineSections)):
                    # Skip any params that have no data (CSV file can generate empty params here)
                    if (len(lineSections[x].strip()) > 0):
                        funcParams = funcParams + lineSections[x].strip() + ","
                # Strip the last comma off the end
                funcParams = funcParams.strip(',')

                # Parse the string into a dictionary of parameters
                parsedArgs = dict(e.split('=') for e in funcParams.split(','))
                modulePointer = sys.modules[moduleName]
                # Call the function, using module.function(parameters)
                getattr(modulePointer, testName)(**parsedArgs)
            # Standard test line - for running a defined test
            elif (fileLine.find("Test") == 0):
                # Split the line into sections
                lineSections = fileLine.split(delimitor)
                # Get the module that the setup function is in
                moduleName = lineSections[1]
                # Get the name of the setup function
                testName = lineSections[2]

                # Build up the paramenter string for the python function call
                funcParams = ""
                for x in range(3, len(lineSections)):
                    # Skip any params that have no data (CSV file can generate empty params here)
                    if (len(lineSections[x].strip()) > 0):
                        funcParams = funcParams + lineSections[x].strip() + ","
                # Strip the last comma off the end
                funcParams = funcParams.strip(',')

                # Parse the string into a dictionary of parameters
                parsedArgs = dict(e.split('=') for e in funcParams.split(','))

                # Get the module pointer for the required test module
                modulePointer = sys.modules[moduleName]
                # Call the function, using module.function(parameters)
                getattr(modulePointer, testName)(**parsedArgs)
            # Skip line - used to mark test for temporary bypass
            elif (fileLine.find("Skip") == 0):
                continue
            # Ignore blank lines
            elif (len(fileLine.strip()) == 0):
                continue
            # Undefined line type
            else:
                # Split the line into sections
                lineSections = fileLine.split(delimitor)
                # Log the error of the unknown line type
                driveTestConfig.testCallbacks["TEST_LOG"](time.time(), "error",
                                                          "Unknown test line type: " + lineSections[0],
                                                          os.path.basename(
                                                              __file__) + " - " + sys._getframe().f_code.co_name)


'''
Adds a newly defined disk drive to use during the test
driveId="PCI:0:00.0"
driveName="myDrive1"
'''
def specifyDriveById(driveId, driveName):
    # Add the item to the test resources dictionary
    driveTestConfig.testResources[driveName] = driveId


'''
Callback function allowing tests to request a specific 'test resource' item
This could be a quarch module connection, setup string or any other object.
These resources are created during the 'Config' phase

resourceName=Name of the resource to return
'''
def getTestResource(resourceName):
    if (resourceName in driveTestConfig.testResources):
        return driveTestConfig.testResources[resourceName]
    else:
        notifyTestLogEvent(time.time(), "error", "Unknown resource item requested:" + resourceName,
                           os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name,
                           {"textDetails": "The given resource name was not found"})
        return None


'''
Callback function allowing tests to store a specific 'test resource' item
This could be a quarch module connection, setup string or any other object.
These resources are created during the 'Config' phase

resourceName = Unique name of resource
resourceValue = Value for resource
'''
def setTestResource(resourceName, resourceValue):
    driveTestConfig.testResources[resourceName] = resourceValue


def resetTestResources():
    # python booleanness logic - if true there's something here
    if driveTestConfig.testResources:
        driveTestConfig.testResources.clear()

    # resetting test variable
    dtsGlobals.continueTest = True
    dtsGlobals.validVersion = True
    dtsGlobals.choiceResponse = None


'''
Callback: Run when a test invokes UTILS_VISUALSLEEP.  This allows user feedback when a delay function is required. Specified
delay time is in seconds
'''
def checkDriveState(driveObject, deviceState, waitTime):
    # DeviceState 0 : Wait for device to be cleared from list
    # DeviceState 1 : Wait for device to appear in list

    start = time.time()
    loop = 0
    end = time.time() - start
    toFind = ""
    # if deviceState is 0:
    #     printText ("looking for device to be off")
    # if deviceState is 1:
    #     printText ("Looking for device to be detected")

    while (end < float(waitTime)):
        end = time.time() - start
        # Should be the only time that we don't want to check lane speeds
        if driveTestConfig.testCallbacks["TEST_GETDISKSTATUS"]("", driveObject, deviceState, checkLanes=False):
            # printText("device new state after " + str(end) + " seconds" )
            return

        time.sleep(0.1)
        loop += 1
        if loop == 5:
            loop = 0
            comms.sendMsgToGUI("testing>")


def visualSleep(delayTime):
    # Print header for delay
    # printText("Delay:" + str(delayTime) + "S:", end="")
    # Tick through each second
    for x in range(0, int(delayTime)):
        time.sleep(1)
        # printText(".", end="")
        # Send msg every second ( 5 seconds allow for disconnect and reconnect + continue test )
        if x % 1 == 0:
            # sending across a message to show it's still alive
            comms.sendMsgToGUI("testing>")
    # Force a new line
    # printText("")


'''
Callback: Run whenever a TEST_LOG event ocurrs, allowing the script to direct the various forms
of output from tests to one or more locations (terminal, results database and similar)
'''
logFilePath = os.path.join(os.getcwd(), "LogFile" + str(datetime.now()).replace(':', '_') + ".txt")


def notifyTestLogEvent(timeStamp, logType, logText, logSource, logDetails=None):
    # Build up log string
    logString = datetime.utcfromtimestamp(timeStamp).strftime(
        '%Y-%m-%d %H:%M:%S') + "\t" + logType + "\t" + logText + "\t" + logSource
    # Append details
    if (logDetails != None):
        for k, v in logDetails.items():
            logString = logString + "\t" + k + "=" + str(v)
    # printText to terminal, skipping debug if not required
    # if (not (driveTestConfig.logDebugMessagesOnTerminal == False and logType == 'debug')):
    # printText(logString)
    # Write to log file, skipping debug if not required
    if (not (driveTestConfig.logDebugMessagesInFile == False and logType == 'debug')):
        with open(logFilePath, 'a') as logFile:
            logFile.write(logString + "\n")


'''
Callback: Run when a test invokes TEST_GETDISKSTATUS (Check the status of the drive).  This can use lspci or
be expanded to use any form of internal test tool
'''
def DiskStatusCheck(uniqueID, driveId, expectedState, checkLanes=True):
    # PCIE drive type
    if "PCIE" in str(driveId).upper() and driveId.index('PCIE:') == 0:
        # Get pcieMappingMode resource if set
        # Check to see if the pcieMappingMode resource string is set
        mappingMode = getTestResource("pcieMappingMode")
        if (mappingMode == None):
            mappingMode = False

        # Get the PCIe address
        pcieAddress = driveId[5:]
        driveState = myHostInfo.isDevicePresent(pcieAddress, mappingMode, "pcie")

        # If drive should be plugged, verify the speed and link width
        if (expectedState):
            if driveState:
                # Moving this so it's not checked on every search for device
                if checkLanes:
                    return myHostInfo.verifyDriveStats(uniqueID, pcieAddress, mappingMode)
                # printText("device was discovered - PASS")
                return True
            else:
                # printText("device was not discovered - FAIL")
                return False
        else:
            if (driveState == False):
                # printText("device was undiscovered - PASS")
                return True
            else:
                # printText("device was discovered - FAIL")
                return False

        return driveState
        # PCIE drive type
    elif "SAS" in str(driveId).upper() and driveId.index('SAS:') == 0:
        # Get pcieMappingMode resource if set
        # Check to see if the pcieMappingMode resource string is set

        mappingMode = getTestResource("pcieMappingMode")
        if (mappingMode == None):
            mappingMode = False

        sasDriveName = driveId[4:]
        driveState = myHostInfo.isDevicePresent(sasDriveName, mappingMode, "sas")

        # If drive should be plugged, verify the speed and link width
        if (expectedState):  # if true, device is plugged and should be found
            if driveState:
                # printText("device was discovered - PASS")
                return True
            else:
                # printText("device was not discovered - FAIL")
                return False
        else:
            if (driveState == False):
                # printText("device was undiscovered - PASS")
                return True
            else:
                # printText("device was discovered - FAIL")
                return False

        return driveState
    # Unknown device type
    else:
        notifyTestLogEvent(time.time(), "error", "Unknown drive type: " + driveId,
                           os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name,
                           {"textDetails": "Unable to check status of the drive"})
        return False


# CurrentTest = "starting"
# def alivePulse():
#     counter = 0
#     quarchidentifier = "QuarchDTS"
#     separator = "::"
#     current_time = time.time()
#
#     while True:
#         # QuarchDTS::currentTest::1
#         quarchstringtosend = quarchidentifier + separator + CurrentTest + separator + str(counter)
#
#         # printText("time is " + str(time.time() - current_time))
#
#         if (time.time() - current_time) > 1:
#             # send item to gui and reset function variables
#
#             try:
#                 sendMsgToGUI(quarchstringtosend)
#                 counter += 1
#             except Exception as e:
#                 printText("server not up")
#                 printText(e)
#                 pass
#             current_time = time.time()
#
#         # as to not clutter cpu
#         time.sleep(.1)
'''
Callback: Run whenever a TEST_LOG event ocurrs, allowing the script to direct the various forms
of output from tests to one or more locations (terminal, results database and similar)

This version logs to a remote TCP server
'''
def notifyTestLogEventXml(uniqueId, timeStamp, logType, logText, logSource, logDetails=None):
    if uniqueId == "" or uniqueId is None:
        # quick check in place just to ensure the unique id of an object is not sent incorrectly
        uniqueId = " "

    # Build main XML structure
    xmlObject = cElementTree.Element("object")
    cElementTree.SubElement(xmlObject, "uniqueID").text = uniqueId
    cElementTree.SubElement(xmlObject, "timestamp").text = datetime.utcfromtimestamp(timeStamp).strftime(
        '%Y-%m-%d %H:%M:%S')
    cElementTree.SubElement(xmlObject, "logType").text = logType
    cElementTree.SubElement(xmlObject, "text").text = logText
    cElementTree.SubElement(xmlObject, "messageSource").text = logSource
    # Add details dictionary if present
    if (logDetails != None):
        xmlDetails = cElementTree.SubElement(xmlObject, "logDetails")
        for k, v in logDetails.items():
            xmlEntry = cElementTree.SubElement(xmlDetails, "entry")
            cElementTree.SubElement(xmlEntry, "key").text = str(k)
            cElementTree.SubElement(xmlEntry, "value").text = str(v)

    xmlstr = str(cElementTree.tostring(xmlObject), "UTF-8").replace("\n", "")
    # Send to GUI server
    comms.sendMsgToGUI(xmlstr)


'''
Tries to get the local/network IP address of the server
'''


def getLocalIpAddress(first=True):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if IP == "127.0.0.1" and first is True:
            s.close()
            getLocalIpAddress(first=False)

    except:
        IP = None
    finally:
        s.close()
    return IP


'''
Activates a remote server at the given port number.  This function will not return until the server connection is closed

This is intended for use with a remote client (generally running a compliance test script).  This server takes in XML format command requests and executes local
test functions based on this.
'''
def attemptRestart(conn, sock, reason=None):
    if reason is None:
        printText("Java connection closed, attempting to recover ")
    else:
        printText(reason)
    conn.close()
    sock.close()
    # time.sleep(1)
    resetTestResources()
    ActivateRemoteServer(localHost=False)


def ActivateRemoteServer(portNumber=9742, localHost=False):
    # Creating the callbacks for future use
    driveTestConfig.testCallbacks = {"TEST_LOG": notifyTestLogEventXml,
                                     "TEST_GETDISKSTATUS": DiskStatusCheck,
                                     "UTILS_VISUALSLEEP": visualSleep,
                                     "TEST_GETRESOURCE": getTestResource,
                                     "TEST_SETRESOURCE": setTestResource,
                                     "TEST_NEWSLEEP": checkDriveState}

    TCP_PORT = portNumber
    portNumber = 1024
    BUFFER_SIZE = 4096
    mDnsInfo = None
    conn = None

    serverName = None
    # Get the sensible server name
    if (serverName is None):
        try:
            serverName = socket.gethostname()
        except:
            serverName = "no-name-server"

    try:
        # Setup and open the socket for connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Making the socket allow connections from any connection available...?
        # sock.bind((TCP_IP, TCP_PORT))
        sock.bind(('', TCP_PORT))
        sock.listen(1)
        printText("----Remote Server Activated----")
        TCP_IP = '127.0.0.1'
        if not localHost:
            # Conditional strings
            TCP_IP = '{address}'.format(address="127.0.0.1" if getLocalIpAddress() is None else getLocalIpAddress())
        printText("\tServer IP: " + str(TCP_IP))

        # Activates mDNS registration for the server, so it can be located remotely
        if (zeroConfAvail):
            try:
                # Register the service
                mDnsIp = TCP_IP
                mDnsDesc = {'version': '1.0', 'server-name': serverName}
                mDnsInfo = ServiceInfo("_http._tcp.local.", "quarchCS._http._tcp.local.", socket.inet_aton(mDnsIp),
                                       TCP_PORT, 0, 0, mDnsDesc)
                zeroConf = Zeroconf()
                zeroConf.register_service(mDnsInfo)

                # Print registration results
                printText("----mDNS Registered----")
                printText("\tServer Name: " + serverName)
            except:
                printText("mDNS error, Service not registered")
        else:
            zeroConf = None

        # Wait for a connection
        # sock.setblocking(0)
        conn, addr = sock.accept()
        printText("----Remote Server connection opened from: " + str(addr))

        # layout = :<'x.x.x.x',xx>
        item = str(addr).split('\'')
        dtsGlobals.GUI_TCP_IP = item[1]

        # Checking to see Quarchpy and QCS are valid together - Exit if not.
        if not checkCompatibility(comms):
            # This return will jump to finally block
            return

        continueScript = True
        try:
            # Loop while the server is to be active
            while continueScript:
                # Get data from the connection
                data = conn.recv(BUFFER_SIZE)
                if not data: pass

                data = data.replace(str.encode("\r\n"), b"")
                # printText("Data Received = " + bytes.decode(data))

                commandParser(conn,sock,data)


        except KeyboardInterrupt:
            printText("---Remote server shutdown request, user CTRL-C received")
    except ConnectionResetError:
        attemptRestart(conn, sock)
    except Exception as ex:
        printText("----Remote server process exited with an exception")
        printText(ex)
        # traceback.print_tb(ex.__traceback__)
    finally:
        # processObject.terminate()
        # processObject.join()
        if conn is not None:
            conn.close()
        # sock.shutdown()
        sock.close()
        printText("----Remote server shutdown complete")

def commandParser(conn, sock, data):
    if (len(data) == 0):
        # 0 data length means socket was closed by java
        attemptRestart(conn, sock)

    if "Alive?" in bytes.decode(data):
        # Java poll to ensure responsiveness
        toSend = str.encode("ok >")
        conn.sendall(toSend + b"\n")
        return

    if "disconnect" in bytes.decode(data):
        # Java poll to ensure responsiveness
        toSend = str.encode("ok >")
        conn.sendall(toSend + b"\n")
        attemptRestart(conn, sock, "User Closed GUI. Server Restart.")

    try:
        # parse command passed
        myobj = testLine()

        xmlRoot = cElementTree.fromstring(bytes.decode(data))
        myobj.initFromXml(xmlRoot)

        # Get the module pointer for the required test module
        if myobj.moduleName == "driveTestCore":
            modulePointer = sys.modules[__name__]
        elif myobj.moduleName == "hostInformation":
            modulePointer = myHostInfo
        else:
            modulePointer = importlib.import_module("." + myobj.moduleName,
                                                    "quarchpy.disk_test")  # should disk_test be removed from this to allow tests to access all parts of QPy (UI, QIS etc)

        # printText(dtsGlobals.GUI_TCP_IP)
        # printText(bytes.decode(data))

        # Call the requested function, using module.function(parameters)
        getattr(modulePointer, myobj.testName)(**myobj.paramList)

        # printText("Sending Data : ok >")
        finishedString = "ok >"
        conn.sendall(str.encode(finishedString) + b"\n")

    except ValueError as err:
        traceback.print_tb(err.__traceback__)
        printText("ERROR - Bad remote command format")

    except AttributeError as e:
        printText("Hit an attribute error, restarting")
        printText(e)
        printText(AttributeError)
        attemptRestart(conn, sock)
    except ConnectionRefusedError as err:
        printText("Could not send response to Java, aborting")
        attemptRestart(conn, sock)
    except Exception as e:
        printText(e)
        printText("ERROR - Unexpected failure in command parser")
        raise

def checkCompatibility(comms):
    # Send GUI the quarchpy version
    comms.sendMsgToGUI("QuarchPy Version: " + pkg_resources.get_distribution("quarchpy").version)
    # First check is to see if QCS accepts the quarchpy version sent
    if not dtsGlobals.validVersion:
        printText(pkg_resources.get_distribution("quarchpy").version)
        printText("Quarchpy version too low for this QCS version. Please upgrade Quarchpy.")
        return False
    # Second check is to see if the QCS version is accepted by this quarchpy
    if not dtsGlobals.QCSVersionValid:
        printText("QCS version too low for this Quarchpy version. Please upgrade QCS.")
        return False

    printText("Compatible QCS and quarchpy")
    return True

def setUpLogging(logLevel):
    levels={
    "CRITICAL" : 50,
    "ERROR" : 40,
    "WARNING" : 30,
    "INFO" : 20,
    "DEBUG" : 10,
    }

    logging.basicConfig(level=levels.get(str(logLevel).upper()))


def main(argstring):
    import argparse

    # Handle expected command line arguments here using a flexible parsing system
    parser = argparse.ArgumentParser(description='QCS parameters')
    parser.add_argument('-l', '--logLevel',
                        help='Logging level sets the base level of what is output. Defaults to warning and above',
                        choices=["debug", "info", "warning"], default="warning", type=str.lower)
    args = parser.parse_args(argstring)

    setUpLogging(args.logLevel)

    printText("\n################################################################################")
    printText("                                   Welcome to                                 ")
    printText("                               Quarch Technology's                            ")
    printText("                             Quarch Compliance Suite                          ")
    printText("                            Quarchpy Version : " + pkg_resources.get_distribution("quarchpy").version)
    printText("################################################################################\n")



    if (isUserAdmin() is False):
        printText("Quarch Compliance Suite must be run from an elevated command prompt.")
        printText("Please restart with administrator privileges")
        sys.exit()

    ActivateRemoteServer()


if __name__ == "__main__":
    main(sys.argv[1:])
