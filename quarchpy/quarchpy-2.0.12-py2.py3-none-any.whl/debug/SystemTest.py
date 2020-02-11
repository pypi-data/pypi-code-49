from quarchpy import *
from quarchpy.device import *
import pkg_resources
from pkg_resources import parse_version, get_distribution
import os
import platform
import time
import sys
import subprocess

# TODO: Move this code to a seperate system_test function so it can be called from other places.  Only argument handling should be done in main
def main (args=None):
    """
    Main function to allow the system test to be called direct from the command line
    
    """

    print("")
    print("SYSTEM INFORMATION")
    print("------------------")
    print("OS Name : " + os.name)
    print("Platform System : " + platform.system())
    print("Platfrom : " + platform.platform())
    if "nt" in os.name: print ("Platform Architecture : " + platform.architecture()[0])
    print("Platform Release :  " + platform.release())

    try:
        print("Quarchpy Version : " + pkg_resources.get_distribution("quarchpy").version)
    except:
        print("Unable to detect Quarchpy version")

    try:
        print("Python Version : " + sys.version)
    except:
        print("Unable to detect Python version")

    try:
        print("QIS version number: " + get_QIS_version())
    except:
        print("Unable to detect QIS version")

	#TODO print java version and jfx, should work for open java and openJFX
    try:
        javaVersion = bytes(subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)).decode()
        print("Java Version:"+ str(javaVersion))
    except:
        print("Unable to detect java version"
              "If Java is not installed then QIS and QPS will run")


	
	# Scan for all quarch devices on the system
    print("")
    print("DEVICE COMMUNICATION TEST")
    print("-------------------------")
    print("")
    deviceList = scanDevices('all', favouriteOnly=False)
    print("Devices visible:\r\n" +str(deviceList))
    print("")
    moduleStr = userSelectDevice(deviceList, nice=True)
    if moduleStr == "quit":
        return 0
    print("Selected module is: "+moduleStr)
    # Create a device using the module connection string
    myDevice = quarchDevice(moduleStr)
    QuarchSimpleIdentify(myDevice)

    # Close the module before exiting the script
    myDevice.closeConnection()



def QuarchSimpleIdentify(device1):
    """
    Prints basic identification test data on the specified module, compatible with all Quarch devices

    Parameters
    ----------
    device1 : quarchDevice
        Open connection to a quarch device
        
    """
    # Print the module name
    print("MODULE IDENTIFY TEST")
    print("--------------------")
    print("")
    print("Module Name:"),
    print(device1.sendCommand("hello?"))
    print("")
    # Print the module identify and version information
    print("Module Identity Information:")
    print(device1.sendCommand("*idn?"))




def get_QIS_version():
    """
    Returns the version of QIS.  This is the version of QIS currenty running on the local system if one exists.
    Otherwise the local version within quarchpy will be exectued and its version returned.

    Returns
    -------
    version : str
        String representation of the QIS version number
        
    """

    qis_version = ""
    my_close_qis = False
    if isQpsRunning() == False:
        my_close_qis = True
        startLocalQis()
        
    myQis = qisInterface()
    qis_version = myQis.sendAndReceiveCmd(cmd="$version")
    if "No Target Device Specified" in qis_version:
        qis_version = myQis.sendAndReceiveCmd(cmd="$help").split("\r\n")[0]
    if my_close_qis:
        myQis.sendAndReceiveCmd(cmd = "$shutdown")
    return qis_version


if __name__ == "__main__":
    main()