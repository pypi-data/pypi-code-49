'''
Implements a cross platform system for scanning and querying system resources.

########### VERSION HISTORY ###########

06/05/2019 - Andy Norrie    - First version

####################################
'''

import subprocess
import platform
import time
import os
import re
import sys
import ctypes
from abc import ABC, abstractmethod
import logging
from quarchpy.user_interface import *
from quarchpy.disk_test import driveTestConfig
from quarchpy.disk_test.dtsGlobals import dtsGlobals
from quarchpy.disk_test.dtsComms import DTSCommms
#from quarchpy.disk_test.driveTestCore import myGlobals
#from quarchpy.disk_test.driveTestCore import notifyChoiceOption, sendMsgToGUI, checkChoiceResponse, setChoiceResponse

# to make input function back compatible with Python 2.x
if hasattr(__builtins__, 'raw_input'):
    input = raw_input


# defining this here means we will never have to differentiate
if platform.system() == 'Windows':
    from quarchpy.disk_test.lspci import WindowsLSPCI as lspci
    from quarchpy.disk_test.sasFuncs import WindowsSAS as sasDET

else:
    from quarchpy.disk_test.lspci import LinuxLSPCI as lspci
    from quarchpy.disk_test.sasFuncs import LinuxSAS as sasDET



class HostInformation:
    # creating new (private) class instance
    __mylspci = lspci()
    __mySAS = sasDET()
    internalResults = {}

    def _init_(self):
        pass

    '''
    Lists physical drives on the system, returning them in the form "{drive-type:identifier=drive description}"
    '''
    def list_physical_drives(self, drive_type, search_params=None):
        filter_drives = True

        # Get any additional parameters for the search
        if search_params is not None:
            if "filter_drives" in search_params:
                filter_drives = search_params["filter_drives"]

        user_devices = {}

        # PCIE devices are returned with an identifier number as the PCIe slot ID
        if drive_type.lower() == "pcie":

            pcie_scan_data = self.__mylspci.getPcieDeviceList()
            # Loop through PCIe results, pick only those matching the class code of a storage controller ([01xx]
            for pcie_name, pcie_device in pcie_scan_data.items():
                if "[01" in pcie_device["class"]:
                    # Add the device address and description to the dictionary
                    user_devices["pcie:" + pcie_device["slot"]] = pcie_device
                    # user_devices["pcie:" + pcie_device["slot"]] = pcie_device["vendor"] + ", " + pcie_device["device"]

            return user_devices

        elif drive_type.lower() == "sas":

            sas_scan_data = self.__mySAS.getSasDeviceList()

            for sas_name, sas_device in sas_scan_data.items():

                # windows interpretation
                if "description" in sas_device:
                    # windows version of sas
                    if "Disk drive" in sas_device["description"]:
                        # Add the device address and description to the dictionary
                        # user_devices["SAS:" + sas_device["name"]] = sas_device["model"] + ", " + sas_device["size"]
                        user_devices["SAS:" + sas_device["name"]] = sas_device

                # linux interpretation
                elif "type" in sas_device:
                    # linux version of sas
                    if "disk" in sas_device["type"].lower():
                        # Add the device address and description to the dictionary
                        # user_devices["SAS:" + sas_device["Conn_Type"]] = sas_device["vendor"] + " " + sas_device["model"] + ", " + sas_device["size"]
                        user_devices["SAS:/dev/" + sas_device["name"]] = sas_device

                elif "Disk_Type" in sas_device:
                    # linux version of sas
                    if "disk" in sas_device["Disk_Type"].lower():
                        # Add the device address and description to the dictionary
                        # user_devices["SAS:" + sas_device["Conn_Type"]] = sas_device["vendor"] + " " + sas_device["model"] + ", " + sas_device["size"]
                        user_devices["SAS:" + sas_device["name"]] = sas_device

            return user_devices

    '''
    Returns a dictionary of status elements for the given device.
    '''
    def get_device_status(self, device_id):
        # If a PCIe device
        if device_id.find("pcie") == 0:
            # Get the status of the PCIe device and return it
            return self.__mylspci.getPcieDeviceDetailedInfo(devicesToScan=device_id)
        else:
            # currently would be in form sas:nameofDrive
            return self.__mySAS.getSasDeviceDetailedInfo(devicesToScan=device_id)

    '''
    Verifies that the PCIe link stats are the same now as they were at the start of the test

    driveId=ID string of the drive to test
    '''
    def verifyDriveStats(self, uniqueID, driveId, mappingMode):
        if "pcie" in str(driveId).lower():
            # Get the expected stats
            expectedSpeed = self.internalResults[driveId + "_linkSpeed"]
            expectedWidth = self.internalResults[driveId + "_linkWidth"]

            # Get the current stats
            linkSpeed, linkWidth = self.__mylspci.getPcieLinkStatus(driveId, mappingMode)

            # if the speed and width is the same
            if (linkSpeed == expectedSpeed and linkWidth == expectedWidth):
                # Log a test success
                driveTestConfig.testCallbacks["TEST_LOG"](uniqueID, time.time(), "testResult",
                                                          "Drive link speed/width was maintained " + driveId,
                                                          os.path.basename(
                                                              __file__) + " - " + sys._getframe().f_code.co_name,
                                                          {"testResult": True})
                return True;
            # Else log a test failure
            else:
                changeDetails = "Was: " + expectedSpeed + "/" + expectedWidth + " Now: " + linkSpeed + "/" + linkWidth
                driveTestConfig.testCallbacks["TEST_LOG"](uniqueID, time.time(), "testResult",
                                                          "Drive link speed/width was NOT maintained for: " + driveId,
                                                          os.path.basename(
                                                              __file__) + " - " + sys._getframe().f_code.co_name,
                                                          {"testResult": False, "textDetails": changeDetails})
                return False
        else:
            driveTestConfig.testCallbacks["TEST_LOG"](uniqueID, time.time(), "testResult",
                                                      "Drive still ID'd - No record of speeds for : " + driveId,
                                                      os.path.basename(
                                                          __file__) + " - " + sys._getframe().f_code.co_name,
                                                      {"testResult": True, "textDetails": "No change"})
            return True

    '''
    Checks if the given device string is visible on the bus
    '''
    def isDevicePresent(self, deviceStr, mappingMode, driveType):
        cwd = os.getcwd()
        os.chdir( os.path.dirname(__file__))
        # Get current device list
        if "pcie" in str(driveType).lower():
            deviceList = self.__mylspci.getPcieDevices(mappingMode)
            if str(deviceStr).startswith("pcie"):
                deviceStr = deviceStr[5:]
        elif "sas" in str(driveType).lower():
            deviceList = self.__mySAS.getSasDeviceList()
            if not str(deviceStr).startswith("sas"):
                deviceStr = "SAS:" + deviceStr

            if "\\" in deviceStr and "." in deviceStr:
                deviceStr = deviceStr.replace("\\", "").replace(".","").replace("SAS:","")

        # printText(deviceStr)
        # printText(deviceList)

        os.chdir(cwd)

        # Loop through devices and see if our module is there
        for devStr in deviceList:
            if platform.system() == 'Windows':
                if str(deviceStr).strip() in str(devStr).strip():
                    return True
            else:
                # devStr = sdc            deviceStr = SAS:/dev/sdc
                if "sas" in deviceStr.lower():
                    # printText("looking for " + str(devStr).strip() + " in " + str(deviceStr).strip())
                    if str(devStr).strip() in str(deviceStr).strip():
                        return True
                else :
                    # printText("looking for " + str(deviceStr).strip() + " in " + str(devStr).strip())
                    if str(deviceStr).strip() in str(devStr).strip():
                        return True

        return False


    def storeInitialDriveStats(self, driveId, linkSpeed, linkWidth):
        self.internalResults[driveId + "_linkSpeed"] = linkSpeed
        self.internalResults[driveId + "_linkWidth"] = linkWidth

    def getDriveList(self, mappingMode):
        cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        # Get current device list
        deviceList = self.__mylspci.getPcieDevices(mappingMode)
        deviceList += self.__mySAS.getSasDeviceList()
        # printText(deviceList)
        os.chdir(cwd)
        return deviceList

    '''
        Checks if the specified device exists in the list
        '''
    def devicePresentInList(self, deviceList, deviceStr):
        for pciStr in deviceList:
            if deviceStr in pciStr:
                return True
        return False

    '''
    Prompts the user to view the list of PCIe devices and select the one to work with
    Console, QCS
    '''
    def pickPcieTarget(self, resourceName, drive_type):

        comms = DTSCommms()

        dtsGlobals.choiceResponse = None

        # Check to see if the pcieMappingMode resource string is set
        mappingMode = driveTestConfig.testCallbacks["TEST_GETRESOURCE"]("pcieMappingMode")
        if (mappingMode == None):
            mappingMode = False

        # Get the current devices
        deviceStr = "NO_DEVICE_STRING"
        # deviceList = self.__mylspci.getPcieDevices(mappingMode)

        # specify the module selection header
        comms.sendMsgToGUI("QuarchDTS::header<DRIVE>::Choose a Drive to test", None)

        if "all" in drive_type:
            deviceDictSas = self.list_physical_drives("sas")
            deviceDictPcie = self.list_physical_drives("pcie")

            if not deviceDictSas and not deviceDictPcie:
                # python logic!
                printText("ERROR - No devices found to display")

            # Sending both of the dictionaries
            # PCIE / SAS have different implementation to send, but same way of dealing with response
            self.sendChoiceObjects(comms, deviceDictSas, "sas")
            self.sendChoiceObjects(comms, deviceDictPcie, "pcie")


        else:
            deviceDict = self.list_physical_drives(drive_type)

            if not deviceDict:
                # python logic!
                printText("ERROR - No devices found to display")

            self.sendChoiceObjects(comms, deviceDict, drive_type)

        # Ask for selection -- Send as individual as to allow infinite wait for response
        comms.sendMsgToGUI("QuarchDTS::end-of-data", None)  # wait for response from java

        while dtsGlobals.choiceResponse is None and dtsGlobals.continueTest is True:
            time.sleep(0.25)

        if (dtsGlobals.choiceResponse is None):
            return 0

        # choice response back should be.. choiceResponse::KEY

        choice = bytes.decode(dtsGlobals.choiceResponse)
        # printText("choice from user was : " + choice)

        # changing the dict dependant on the response.
        if "all" in drive_type:
            if "sas" in choice.lower():
                deviceDict = deviceDictSas
            if "pcie" in choice.lower():
                deviceDict = deviceDictPcie

        selection = choice.split("::")
        # order should be choiceResponse::xyz
        selection = selection[1]
        if "rescan" not in selection:  # rescan is the only responce we dont want printed at the moment. If others are needed make a global list.
            printText("Response from drive selection was : " + selection.replace("\n","").replace("\r", ""), fillLine=True, terminalWidth=80)
        logging.debug("Response from drive selection was : " + choice)
        # exit on 'choice-abort' or if user stopped tests
        if "choice-abort" in selection or dtsGlobals.continueTest is False:
            printText("No item selected, test aborted. Waiting for new test start..\n")
            return 0
        elif "rescan" in selection:
            return self.pickPcieTarget(resourceName, drive_type)

        # Validate selection
        found = False
        # need to change to string compare

        for key, value in deviceDict.items():
            if selection.strip() == key:
                deviceStr = key
                found = True
                break

        if not found:
            return 0

        # Get and store the initial link status of the selected device
        if selection.lower().find("pcie") == 0:
            linkSpeed, linkWidth = self.__mylspci.getPcieLinkStatus(deviceStr, mappingMode)
            self.storeInitialDriveStats(deviceStr, linkSpeed, linkWidth)
            # Log the selection
            driveTestConfig.testCallbacks["TEST_LOG"](None, time.time(), "debug",
                                                  "Device Selected: " + "PCIE:" + deviceStr + " - Speed:" + linkSpeed + ", Width:" + linkWidth,
                                                  os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name)
            # driveTestConfig.testCallbacks["TEST_LOG"](uId, logTime, messageType, messageText, messageSource, messageData)
            # Store the device selection in the test resources
            driveTestConfig.testCallbacks["TEST_SETRESOURCE"](resourceName, "PCIE:" + deviceStr)

        if selection.find("SAS") == 0:
            #linkSpeed, linkWidth = self.__mylspci.getPcieLinkStatus(deviceStr, mappingMode)
            #self.storeInitialDriveStats(deviceStr, linkSpeed, linkWidth)
            # Log the selection
            driveTestConfig.testCallbacks["TEST_LOG"](None, time.time(), "debug",
                                                  "Device Selected: " + deviceStr, # + " - Speed:" + linkSpeed + ", Width:" + linkWidth,
                                                  os.path.basename(__file__) + " - " + sys._getframe().f_code.co_name)
            # driveTestConfig.testCallbacks["TEST_LOG"](uId, logTime, messageType, messageText, messageSource, messageData)
            # Store the device selection in the test resources
            driveTestConfig.testCallbacks["TEST_SETRESOURCE"](resourceName, deviceStr)




    '''
    Checks if the script is runnin under admin permissions
    '''
    def checkAdmin(self):
        if self.__mylspci.is_admin_mode() == False:
            logging.critical("Not in Admin mode\nExiting Program")
            quit()


    def sendChoiceObjects(self, comms, deviceDict, drive_type):
        for key, value in deviceDict.items():
            # printText("Key = " + key)
            # printText("Value = " + str(value))
            # is send across in format QuarchDTS::Key=Value
            try:
                #comms.notifyChoiceOption(key, value)
                comms.newNotifyChoiceOption("drive", key, value, drive_type)
            except Exception as e:
                printText(e)

    def getPcieLinkStatus(self, deviceStr, mappingMode):
       return self.__mylspci.getPcieLinkStatus(deviceStr, mappingMode)
