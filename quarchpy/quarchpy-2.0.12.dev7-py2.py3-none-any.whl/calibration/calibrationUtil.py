#!/usr/bin/env python
'''
This example runs the calibration process for a HD PPM
It products a calibrated PPM and a calibration file for later use

########### VERSION HISTORY ###########

05/04/2019 - Andy Norrie     - First Version

########### INSTRUCTIONS ###########

1- Connect the PPM on LAN and power up
2- Connect the Keithley 2460 until on LAN, power up and check its IP address
3- Connect the calibration switch unit to the output ports of the PPM and Keithley

####################################
'''

# Global resources
from time import sleep,time
import datetime
import logging,os
import sys

# Quarch device control
from quarchpy.device import *

# Calibration control
#from quarchpy.calibration import *
from quarchpy.calibration.keithley_2460_control import *
from quarchpy.calibration.calibration_classes import *
from quarchpy.calibration.HDPowerModule import *
from quarchpy.calibration.QTL2347 import *
from quarchpy.calibration.calibrationConfig import *
# UI functions
from quarchpy.user_interface import *

# Performs a standard calibration of the PPM
def runCalibration (instrAddress=None, calPath=None, ppmAddress=None, logLevel="warning", calAction=None, userMode="testcenter", extra_args=None):

    try:
        # Display the app title to the user
        printText("********************************************************")
        printText("          Quarch Technology Calibration System")
        printText("             (C) 2019, All rights reserved")
        printText("                          V" + quarchpy.calibration.calCodeVersion)
        printText("********************************************************")
        printText("")

        # Process parameters
        calPath = get_check_valid_calPath(calPath)
        setup_logging(logLevel)

        # Creates the calibration header information object for this test run
        calHeader = CalibrationHeaderInformation()
        # Store the current cal header as a resource that can be accessed later
        calibrationResources["CalHeader"] = calHeader
        calibrationResources["user_mode"] = userMode
        while True:
            # If no address specified, the user must select the module to calibrate
            if (calAction != None and 'select' in calAction) or (ppmAddress == None):
                calAction, ppmAddress = select_module(calAction, ppmAddress)
            # Connect to the module
            while True:
                try:
                    printText("Selected Module: " + ppmAddress)
                    myPpmDevice = quarchDevice(ppmAddress)
                    break
                except:
                    printText("Failed to connect to "+str(ppmAddress))
                    calAction, ppmAddress = select_module(calAction,ppmAddress)

            serialNumber = myPpmDevice.sendCommand("*SERIAL?")
            success = False
            # Identify and create a power module object
            if ('1944' in serialNumber):
                # create HD Power Module Object
                dut = HDPowerModule(myPpmDevice)
                success = True
            elif ('2312' in serialNumber):
                # this is a Power Analysis Module, we need to detect the fixture
                fixtureId = myPpmDevice.sendCommand("read 0xA401")
                if ('2347' in fixtureId):
                    dut = QTL2347(myPpmDevice)
                    success = True
            if (success == False):
                raise ValueError("ERROR - Serial number not recogised as a valid power module")
            # TODO: check what device is being calibrated and call appropriate populateCalHeader for that device.
            # populate device information in to the cal header
            populateCalHeader_HdPpm(calHeader, dut.dut, calAction)
            # populate system information in to the cal header
            populateCalHeader_System(calHeader)
            storeDeviceInfo(serial=calHeader.quarchEnclosureSerial, idn=calHeader.idnStr)

            # create calibration File Name
            # if its a x6, append the port number
            if 'QTL1995' in calHeader.quarchEnclosureSerial.upper():
                calFilename = calHeader.quarchEnclosureSerial + "-" + calHeader.quarchEnclosurePosition
            else:
                calFilename = calHeader.quarchEnclosureSerial
            # keep track of overall pass/fail status, this is set false if we fail a test. it should only be set back to true
            # here, or if the user initiates another test.
            calHeader.result = True
            # If no calibration action is selected, request one

            if (calAction == None):
                calAction = show_action_menu(calAction)
            if (calAction == 'quit'):
                if userMode == "testcenter":
                    return calHeader
                else:
                    sys.exit(0)
            elif ('calibrate' in calAction) or ('verify' in calAction):
                # If no calibration instrument is provided, request it
                while (True):
                    if (instrAddress == None):
                        instrAddress = userSelectCalInstrument(scanFilterStr="Keithley 2460", nice=True)
                    try:
                        # Connect to the calibration instrument
                        myCalInstrument = keithley2460(instrAddress)
                        # Open the connection
                        myCalInstrument.openConnection()
                        populateCalHeader_Keithley(calHeader, myCalInstrument)
                        break
                    # In fail, allow the user to try again with a new selection
                    except:
                        printText("Unable to communicate with selected instrument!")
                        printText("")
                        instrAddress = None
                calHeader, myCalInstrument, report = cal_or_ver(calAction, calFilename, calHeader, calPath,
                                                                dut, myCalInstrument)


            # End of Loop
            # if we've done a calibrate, always verify next

            myPpmDevice.closeConnection()
            if 'calibrate' in calAction:
                if report:
                    calAction = 'verify'
                else:
                    printText("Not verifying this module because calibration failed")
                    calAction = "quit"
            # if we're in testcenter, always exit before selecting a new module
            elif userMode == "testcenter":
                calAction = "quit"
            elif 'select' in calAction:
                pass
            else:
                calAction = None

    except Exception as thisException:
        try:
            myCalInstrument.setLoadCurrent(0)
            myCalInstrument.closeConnection()
        # Handle case where exception may have been thrown before instrument was set up
        except:
            pass
        logging.error(thisException)

        raise thisException


def select_module(calAction, ppmAddress):
    # Request user to select the (QTL1999) PPM to calibrate
    ppmAddress = userSelectDevice(scanFilterStr=["QTL1999", "QTL1995", "QTL1944", "QTL2312"], nice=True,
                                  message="Select device for calibration")
    if (ppmAddress.lower() == 'quit'):
        printText("User Quit Program")
        sys.exit(0)
    if (calAction != None and 'select' in calAction):
        calAction = None
    return calAction, ppmAddress


def setup_logging(logLevel):
    # check log file is present or writeable
    numeric_level = getattr(logging, logLevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)



def get_check_valid_calPath(calPath):
    inputOK = False
    while inputOK is False:
        if (calPath is None):
            calPath = os.path.expanduser("~")
            calPath = requestDialog("Enter Report Path",
                                    "Enter the desired save path for the calibration report. Leave blank to defaut to [" + calPath + "] :",
                                    desiredType="path", defaultUserInput=os.path.expanduser("~"))

        if (os.path.isdir(calPath) == False):
            printText("Supplied calibration path is invalid: " + calPath)
            inputOK = False
            calPath = None
        else:
            inputOK = True
    return calPath


def cal_or_ver(calAction, calFilename, calHeader, calPath, dut, myCalInstrument):
    # Creates the calibration header information object for this test run
    # calHeader = CalibrationHeaderInformation()
    # Store the current cal header as a resource that can be accessed later

    calHeader.calibrationType = calAction
    # check self test
    # TODO : check status here

    dut.specific_requirements()
    # open report for writing
    fileName = calPath + "\\" + calFilename + "_" + datetime.datetime.now().strftime(
        "%d-%m-%y_%H-%M" + "-" + calAction + ".txt")
    printText("")
    printText("Report file: " + fileName)
    reportFile = open(fileName, "a+")
    reportFile.write(calHeader.toReportText())
    if getCalibrationResource("runtimecheckskipped") is True:
        tempString="Module temperature not guaranteed to be stable."
    elif getCalibrationResource("runtimecheckskipped") is False:
        tempString="Module temperature is stable."
    reportFile.write(tempString)
    
    # If a calibration is requested
    if ('calibrate' in calAction):
        retTupple = dut.calibrate(myCalInstrument, reportFile, calHeader)
        title = "Calibration "
    elif ('verify' in calAction):
        retTupple = dut.verify(myCalInstrument, reportFile, calHeader)
        title = "Verification "

    report = retTupple[0]
    calHeader = retTupple[1]
    formatFinalReport(reportFile)

    if report is True:
        result = "Passed"

    else:
        result = "Failed"
        calHeader.result = False

    printText("\n====================\n" + title + result + "\n====================")
    printText("More information at : " + fileName + "\n\n")
    reportFile.write("\n====================\n" + title + result + "\n====================")

    # Close all instruments
    myCalInstrument.closeConnection()
    reportFile.close()
    return calHeader, myCalInstrument, report


def show_action_menu(calAction):
    actionList = []
    actionList.append(["Calibrate","Calibrate the power module"])
    actionList.append(["Verify","Verify existing calibration on the power module"])
    actionList.append(["Select","Select a different power module"])
    actionList.append(["Quit","Quit"])
    calAction = listSelection("Select an action", "Please select an action to perform", actionList, nice=True, tableHeaders=["Option", "Description"], indexReq=True)
    return calAction[1].lower()


# Returns a resource from the previous calibration. This is the mechanism for getting results and similar back to
# a higher level automated script.
def getCalibrationResource (resourceName):
    try:
        return calibrationResources[resourceName]
    except Exception as e:
        printText("Failed to get calibration resource : " +str(resourceName))
        printText("Exception : " + str(e))
        return None



def formatFinalReport(reportFile):
    with open(reportFile.name, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        overview = []
        for line in lines:
            if not line.__contains__("worst case:"):
                f.write(line)
            else:
                overview.append(line)
        for i in overview:
            f.write(i)

def getFailuresFromReport(reportFile):
    with open(reportFile.name, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        listOfFailures = []
        for line in lines:
            if line.__contains__("worst case:") and line.__contains__("False"):
                listOfFailures.append(line)
    listOfFailures = ''.join(listOfFailures)
    return listOfFailures;



def main(argstring):
    import argparse
    # Handle expected command line arguments here using a flexible parsing system
    parser = argparse.ArgumentParser(description='Calibration utility parameters')
    parser.add_argument('-a', '--action', help='Calibration action to perform', choices=['calibrate', 'verify'], type=str.lower)
    parser.add_argument('-m', '--module', help='IP Address or netBIOS name of power module to calibrate', type=str.lower)
    parser.add_argument('-i', '--instr', help='IP Address or netBIOS name of calibration instrument', type=str.lower)
    parser.add_argument('-p', '--path', help='Path to store calibration logs', type=str.lower)
    parser.add_argument('-l', '--logging', help='Level of logging to report', choices=['warning', 'error', 'debug'], type=str.lower,default='warning')
    parser.add_argument('-u', '--userMode', help='User mode',choices=['console','testcenter'], type=str.lower,default='console')
    args, extra_args = parser.parse_known_args(argstring)
    
    # Create a user interface object
    thisInterface = User_interface(args.userMode)

    # Call the main calibration function, passing the provided arguments
    runCalibration(instrAddress=args.instr, calPath=args.path, ppmAddress=args.module, logLevel=args.logging, calAction=args.action, userMode=args.userMode, extra_args=extra_args)

#Command to run from terminal.
#python -m quarchpy.calibration -mUSB:QTL1999-01-002 -acalibrate -i192.168.1.210 -pC:\\Users\\sboon\\Desktop
if __name__ == "__main__":
    #main(['-musb::QTL1999-02-001','-acalibrate','-i192.168.1.137'])
    #main(['-mTCP:192.168.1.214', '-acalibrate'])
    main (sys.argv[1:])
    #main (sys.argv)