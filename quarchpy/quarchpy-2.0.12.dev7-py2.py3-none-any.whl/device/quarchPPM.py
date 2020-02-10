from .device import quarchDevice

class quarchPPM(quarchDevice):
    def __init__(self, originObj):

        self.connectionObj = originObj.connectionObj
        self.ConString = originObj.ConString
        self.ConType = originObj.ConType
        numb_colons = self.ConString.count(":")
        if numb_colons == 1:
            self.ConString = self.ConString.replace(':', '::')
 
    def startStream(self, fileName='streamData.txt', fileMaxMB=2000, streamName ='Stream With No Name', streamAverage = None, releaseOnData = False, separator=" "):
        return self.connectionObj.qis.startStream(self.ConString, fileName, fileMaxMB, streamName, streamAverage, releaseOnData, separator)

    def streamRunningStatus(self):
        return self.connectionObj.qis.streamRunningStatus(self.ConString)

    def streamBufferStatus(self):
        return self.connectionObj.qis.streamBufferStatus(self.ConString)

    def streamInterrupt(self):
        return self.connectionObj.qis.streamInterrupt()

    def waitStop(self):
        return self.connectionObj.qis.waitStop()

    def streamResampleMode(self, streamCom):
        if streamCom.lower() == "off" or streamCom[0:-2].isdigit():
            return self.connectionObj.qis.sendAndReceiveCmd(cmd = "stream mode resample " + streamCom.lower(), device = self.ConString)
        else:
            return "Invalid resampling argument. Valid options are: off, [x]ms or [x]us."

    def stopStream(self):
        return self.connectionObj.qis.stopStream(self.ConString)

    '''
    Function to check the output state of the module and prompt to select an output mode if not set already
    '''
    def setupPowerOutput(myModule):
        # Output mode is set automatically on HD modules using an HD fixture, otherwise we will chose 5V mode for this example
        if "DISABLED" in myModule.sendCommand("config:output Mode?"):
            try:
                drive_voltage = raw_input(
                    "\n Either using an HD without an intelligent fixture or an XLC.\n \n>>> Please select a voltage [3V3, 5V]: ") or "3V3" or "5V"
            except NameError:
                drive_voltage = input(
                    "\n Either using an HD without an intelligent fixture or an XLC.\n \n>>> Please select a voltage [3V3, 5V]: ") or "3V3" or "5V"

            myModule.sendCommand("config:output:mode:" + drive_voltage)

        # Check the state of the module and power up if necessary
        powerState = myModule.sendCommand("run power?")
        # If outputs are off
        if "OFF" in powerState:
            # Power Up
            print("\n Turning the outputs on:"), myModule.sendCommand("run:power up"), "!"

