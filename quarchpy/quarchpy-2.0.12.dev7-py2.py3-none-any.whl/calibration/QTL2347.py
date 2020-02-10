'''
Quarch Power Module Calibration Functions
Written for Python 3.6 64 bit

M Dearman April 2019
'''

'''
Calibration Flow
    Connect to PPM
    Connect to Keithley
    step through a set of values and get ADC vs Reference Value
    evaluate results vs defined limits

'''

#Imports QuarchPy library, providing the functions needed to use Quarch modules
#from quarchpy import quarchDevice #, scanDevices

# Import other libraries used in the examples
from functools import reduce
#from quarchpy.calibration import *
from quarchpy.calibration.deviceHelpers import returnMeasurement
import quarchpy.calibration.calibrationConfig
import types
from time import sleep,time
from math import ceil
from quarchpy.calibration.PowerModuleCalibration import *
import threading
from quarchpy.user_interface import *
from quarchpy.user_interface import logSimpleResult
from quarchpy.device.device import *

def setBit(hexString,bit):
    newVal = int(hexString,16) | 2**bit
    return '0x{:04x}'.format(newVal)

def clearBit(hexString,bit):
    mask = ((2**16)-1 - (2**bit))
    newVal = int(hexString,16) & mask
    return '0x{:04x}'.format(newVal)

def parseFixtureData(response,start,length):

    # split the multiline response into a list
    response = response.splitlines()
    result = ""
    # for each line
    for line in response:
        # remove 0x, swap bytes
        line = line[4:6] + line[2:4]
        # convert 4 char Hex to 16 bit binary string
        line = "{0:016b}".format(int(line,16))
        # concatenate all the strings
        result += line
    # pick out the section we want
    result = int(result[start:(start+length)],2)
    # convert two's compliment
    if (result >= 2**(length-1)):
        result -= 2**length
    return result


def getFixtureData(device,channel):
    #hold measurement
    response = device.sendCommand("read 0x0000")
    device.sendCommand("write 0x0000" + setBit(response,3))
    #read measurement
    data = device.sendCommand("read 0x1000 to 0x1007")
    #release measurement
    response = device.sendCommand("read 0x0000")
    device.sendCommand("write 0x000" + clearBit(response,3))

    if (channel == "3V3 VOLT"):
        return parseFixtureData(data,0,16)
    elif (channel == "3V3 CUR"):
        return parseFixtureData(data,16,25)
    elif (channel == "12V VOLT"):
        return parseFixtureData(data,41,16)
    elif (channel == "12V CUR"):
        return parseFixtureData(data,57,25)
    elif (channel == "3V3_AUX VOLT"):
        return parseFixtureData(data,82,16)
    elif (channel == "3V3_AUX CUR"):
        return parseFixtureData(data,98,20)

class QTL2347 (PowerModule):

    CALIBRATION_MODE_ADDR               = '0xA100'
    CALIBRATION_CONTROL_ADDR            = '0xA101'      
    V3_3_LOW_MULTIPLIER_ADDR            = '0xA103'
    V3_3_LOW_OFFSET_ADDR                = '0xA104'
    V3_3_HIGH_MULTIPLIER_ADDR           = '0xA105'
    V3_3_HIGH_OFFSET_ADDR               = '0xA106'
    V3_3_VOLT_MULTIPLIER_ADDR           = '0xA107'
    V3_3_VOLT_OFFSET_ADDR               = '0xA108'
    V3_3_LEAKAGE_MULTIPLIER_ADDR        = '0xA109'
    V12_LOW_MULTIPLIER_ADDR             = '0xA10A'
    V12_LOW_OFFSET_ADDR                 = '0xA10B'
    V12_HIGH_MULTIPLIER_ADDR            = '0xA10C'
    V12_HIGH_OFFSET_ADDR                = '0xA10D'
    V12_VOLT_MULTIPLIER_ADDR            = '0xA10E'
    V12_VOLT_OFFSET_ADDR                = '0xA10F'
    V12_LEAKAGE_MULTIPLIER_ADDR         = '0xA110'
    V3_3_AUX_MULTIPLIER_ADDR            = '0xA111'
    V3_3_AUX_OFFSET_ADDR                = '0xA112'
    V3_3_AUX_VOLT_MULTIPLIER_ADDR       = '0xA113'
    V3_3_AUX_VOLT_OFFSET_ADDR           = '0xA114'
    V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR    = '0xA115'

    def specific_requirements(self):
        #func to declare any aditional requiremtns needed before cal/ver this specific device. For example switchbox for an HDPPM
        pass

    def open_module(self):

        # set unit into calibration mode
        self.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0xaa55")
        self.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0x55aa")

    def clear_calibration(self):

        # set unit into calibration mode
        self.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0xaa55")
        self.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0x55aa")

        # clear all calibration registers
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_OFFSET_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_MULTIPLIER_ADDR + " 0x0000")
        self.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")
        
        # write 0xaa55 to register 0xf012 to tell module it is calibrated
        #self.dut.sendAndVerifyCommand("write 0xf012 0xaa55")
        
    def write_calibration(self):

        # write the calibration registers
        # erase the tag memory
        self.dut.sendCommand("write 0xa200 0x0020")
        # TODO: should check for completion here...
        # wait for 2 seconds for erase to complete
        printText("Erasing TAG memory..")
        sleep(2.0)
        # write the tag memory
        printText("Programming TAG memory...")
        self.dut.sendCommand("write 0xa200 0x0040")        


    def close_module(self):

        #TODO: No point in reseting the DUT as that does not reset the fixture
        ## reset the module
        #printText("");
        #printText("resetting the device...")
        #printText("");
        ##self = QTL2347(self.dut.resetDevice())
        #self.dut.resetDevice(40)
        #response = self.dut.sendCommand("*idn?")
        pass

    class QTL2347Calibration (Calibration):

        def __init__(self): 
            super().__init__()

        def init_cal(self,voltage):

            # TODO: No Power control at the moment
            # power up
            #self.powerModule.dut.sendAndVerifyCommand("power up")

            # check averaging and set to max
            if (self.powerModule.dut.sendCommand("rec:ave?").find("32k") != 0):
                self.powerModule.dut.sendAndVerifyCommand("rec:ave 32k")

            # set module into calibration mode (again?)
            self.powerModule.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0xaa55")   # will not verify
            self.powerModule.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0x55aa")   # will not verify

            #Reset Keithley
            self.powerModule.load.reset()

            # TODO: No Switchbox at the moment
            ##Set switchbox to correct channel
            #if voltage.upper() == "12V":
            #    mySwitchbox.sendAndVerifyCommand("connect 12v")
            #elif voltage.upper() == "5V":
            #    mySwitchbox.sendAndVerifyCommand("connect 5v")
            #else:
            #    raise ValueError("Invalid voltage specified")

            # TODO: Temperature verification removed

        def meas_12v_volt(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:volt:12v?")

            ## returnMeasurement() returns [value,units] we only need the value, which is actually ADC levels * 2^shift
            #return int(response[0])
            result = getFixtureData(self.powerModule.dut,"12V VOLT")
            return result

        def meas_12v_cur(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:cur 12v?")
            #return float(response[0])*1000

            result = getFixtureData(self.powerModule.dut,"12V CUR")
            return result

        def meas_3v3_volt(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:volt:3v3?")

            ## returnMeasurement() returns [value,units] we only need the value, which is actually ADC levels * 2^shift
            #return int(response[0])

            result = getFixtureData(self.powerModule.dut,"3V3 VOLT")
            return result

        def meas_3v3_cur(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:cur 3v3?")
            #return float(response[0])*1000

            result = getFixtureData(self.powerModule.dut,"3V3 CUR")
            return result

        def meas_3v3_aux_volt(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:volt:3v3_aux?")

            ## returnMeasurement() returns [value,units] we only need the value, which is actually ADC levels * 2^shift
            #return int(response[0])

            result = getFixtureData(self.powerModule.dut,"3V3_AUX VOLT")
            return result

        def meas_3v3_aux_cur(self):

            #response = returnMeasurement(self.powerModule.dut,"meas:cur 3v3_aux?")
            #return float(response[0])*1000

            result = getFixtureData(self.powerModule.dut,"3V3_AUX CUR")
            return result

        # check connections to host power and load
        def checkLoadVoltage(self,voltage,tolerance):

            self.powerModule.load.setReferenceCurrent(0)
            result = self.powerModule.load.measureLoadVoltage()*1000    # *1000 because we use mV but keithley uses volts
            # check result is in required range
            if (result >= voltage-tolerance) and (result <= voltage+tolerance):
                return True
            else:
                return False

        def finish_cal(self):

            #turn off load
            #self.powerModule.load.setReferenceCurrent(0)
            self.powerModule.load.disable()

            # turn dut to autoranging
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F0")

        def report(self,action,data):

            report = []

            # check errors and generate report
            report.append('\n')

            if action == "calibrate":
               report.append("\t" + '{0:>11}'.format('Reference ')+ self.units + '   ' + '{0:>10}'.format('Raw Value ')+ self.units + '   ' + '{0:>10}'.format('Result ')+ self.units + '   ' + '{0:>10}'.format('Error ')+ self.units + '   ' + '{0:>13}'.format('+/-(Abs Error,% Error)') + ' ' + '{0:>10}'.format('Pass'))
            elif action == "verify":
                report.append("\t" + '{0:>11}'.format('Reference ')+ self.units + '   ' + '{0:>10}'.format('Result ')+ self.units + '   ' + '{0:>10}'.format('Error ')+ self.units + '   ' + '{0:>13}'.format('+/-(Abs Error,% Error)') + '   ' + '{0:>10}'.format('Pass'))

            report.append("==================================================================================================")

            # zero worst case error vars
            worstAbsError = 0
            worstRelError = 0
            worstRef = None
            overallResult = True

            # for each calibration reference
            for thisLine in data:
                reference = thisLine[1]
                ppmValue = thisLine[0]

                # for calibration, replace value with calibrated result
                if action =="calibrate":
                    calibratedValue = self.getResult(ppmValue)
                # otherwise just use ppmValue directly
                else:
                    calibratedValue = ppmValue

                # work out errors
                (actError,errorSign,absError,relError,result) = getError(reference,calibratedValue,self.absErrorLimit,self.relErrorLimit)

                # compare/replace with running worst case
                if absError >= worstAbsError:
                    if relError >= worstRelError:
                        worstAbsError = absError
                        worstRelError = relError
                        worstCase = errorSign + "(" + str(absError) + self.units + "," + "{:.3f}".format(relError) + "%) @ " + '{:.3f}'.format(reference) + self.units

                # update overall pass/fail
                if result != True:
                    overallResult = False

                #generate report
                passfail = lambda x: "Pass" if x else "Fail"
                if action == "calibrate":
                    report.append("\t" + '{:>11.3f}'.format(reference) + '     ' + '{:>10.1f}'.format(ppmValue) + '     ' + '{:>10.1f}'.format(calibratedValue) + '     ' + "{:>10.3f}".format(actError) + '     ' + '{0:>16}'.format(errorSign + "(" + str(absError) + self.units + "," + "{:.3f}".format(relError) + "%)") + '     ' + '{0:>10}'.format(passfail(result)))
                elif action == "verify":
                    report.append("\t" + '{:>11.3f}'.format(reference) + '     ' + '{:>10.1f}'.format(ppmValue) + '     ' + "{:>10.3f}".format(actError) + '     ' + '{0:>16}'.format(errorSign + "(" + str(absError) + self.units + "," + "{:.3f}".format(relError) + "%)") + '     ' + '{0:>10}'.format(passfail(result)))

            report.append("==================================================================================================")
            report.append('\n')

            if action == "calibrate":
                report.append("Calculated Multiplier: " + str(self.multiplier.originalValue()) + ", Calculated Offset: " + str(self.offset.originalValue()))
                report.append("Stored Multiplier: " + str(self.multiplier.storedValue()) + ", Stored Offset: " + str(self.offset.storedValue()))
                report.append("Multiplier Register: " + self.multiplier.hexString(4) + ", Offset Register: " + self.offset.hexString(4))

            return {"result":overallResult,"worst case":worstCase,"report":('\n'.join(report)), "calObj": self}
        #"absErrorLimit":self.absErrorLimit, "relErrorLimit": self.relErrorLimit, "units": self.units, "unitTemp": self.unitTemp

    class QTL2347_12V_VoltageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1
            self.relErrorLimit = 1
            self.test_min = 40
            self.test_max = 14400
            self.test_steps = 20
            self.units = "mV"
            self.scaling = 4
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12v")

            # set module into calibration mode (again?)
            self.powerModule.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0xaa55")   # will not verify
            self.powerModule.dut.sendCommand("write " + QTL2347.CALIBRATION_MODE_ADDR + " 0x55aa")   # will not verify
            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 12V Voltage
            showDialog(title="Setup 12V Voltage Calibration",message="\aPlease connect the load to the 12v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 12v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_12v_volt()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 12v voltage", result)

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 12v voltage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_VOLT_MULTIPLIER_ADDR)
            # get 12v voltage offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_VOLT_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 12v voltage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 12v voltage offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_VOLT_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_12V_LeakageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 50                 # 1% of 5000 uA
            self.relErrorLimit = 0                  #
            self.test_min = 1000                    # 1000mV
            self.test_max = 14400                   # 14.4V
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 1
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = False               # offset is not stored, don't care
            self.offset_int_width = 16               # offset is not stored, don't care
            self.offset_frac_width = 16              # offset is not stored, don't care
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12v")

            #set manual range, full averaging, low current mode
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F5")
            # clear the multiplier register by setting it to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")

            # Ask user to setup 12V Leakage
            showDialog(title="Setup 12V Leakage Calibration",message="\aPlease connect the load to the 12v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 12v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            # negate result because in this case the load is providing the power, not sinking it
            return -load_meas_cur(self.powerModule.load)

        def readVal(self):

            return load_get_volt(self.powerModule.load)

        def setCoefficients(self):

            # we don't apply the leakage calibration here because it provides uA leakage results and the current calibration uses raw ADC values
            # instead we will use it to correct the current calibration and apply it later

            #result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            #logSimpleResult("Set 12v leakage to device", result)
            pass

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 12v leakage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR)
            return coefficients

        def writeCoefficients(self,coefficents):

            # write 12v leakage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR + " " + coefficents["multiplier"])

    class QTL2347_12V_LowCurrentCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2      # 2uA
            self.relErrorLimit = 2      # 2%
            self.test_min = 10      # 10uA
            self.test_max = 85000   # 85mA
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 32
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12v")

            #set manual range, full averaging, 12v low current mode, 3v3 all off (so we can detect we're connected to the wrong channel
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F4")
            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 12V Current
            showDialog(title="Setup 12V Current Calibration",message="\aPlease connect host power and load to the 12v channel")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connect Host Power",message="\aPlease connect host power and load to the 12v channel on the fixture")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            # read device voltage and add leakage current to the reference
            voltage =  super().meas_12v_volt()
            leakage = voltage*self.powerModule.calibrations["12V"]["Leakage"].multiplier.originalValue() + self.powerModule.calibrations["12V"]["Leakage"].offset.originalValue()
            return load_meas_cur(self.powerModule.load) + leakage

        def readVal(self):

            return super().meas_12v_cur()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 12v Low Current", result)

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 12v low current multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_LOW_MULTIPLIER_ADDR)
            # get 12v low current offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_LOW_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 12v low current multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 12v low current offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LOW_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_12V_HighCurrentCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2000   # 2mA
            self.relErrorLimit = 1      # 1%
            self.test_min = 1000    # 1mA
            self.test_max = 4000000 # 4A
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 2048
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12v")

            #set manual range, full averaging, 12v high current mode, 3v3 all off (so we can detect we're connected to the wrong channel
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F8")
            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 12V Current
            showDialog(title="Setup 12V Current Calibration",message="\aPlease connect host power and load to the 12v channel")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connect Host Power",message="\aPlease connect host power and load to the 12v channel on the fixture")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            # read device voltage and add leakage current to the reference
            voltage =  super().meas_12v_volt()
            leakage = voltage*self.powerModule.calibrations["12V"]["Leakage"].multiplier.originalValue() + self.powerModule.calibrations["12V"]["Leakage"].offset.originalValue()
            return load_meas_cur(self.powerModule.load) + leakage

        def readVal(self):

            return super().meas_12v_cur()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 12v high current", result)

            # once we've completed low and high current we can set leakage on the fixture
            result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_LEAKAGE_MULTIPLIER_ADDR + " " + self.powerModule.calibrations["12V"]["Leakage"].multiplier.hexString(4))

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 12v high current multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_HIGH_MULTIPLIER_ADDR)
            # get 12v high current offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V12_HIGH_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 12v high current multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 12v high current offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V12_HIGH_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_3V3_VoltageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1
            self.relErrorLimit = 1
            self.test_min = 40
            self.test_max = 14400
            self.test_steps = 20
            self.units = "mV"
            self.scaling = 4
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3v3")

            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 3V3 Current
            showDialog(title="Setup 3.3V Voltage Calibration",message="\aPlease connect the load to the 3.3v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_volt()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 3.3v voltage", result)

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3v3 voltage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_VOLT_MULTIPLIER_ADDR)
            # get 3v3 voltage offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_VOLT_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 3v3 voltage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 3v3 voltage offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_VOLT_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_3V3_LeakageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 50                 # 1% of 5000 uA
            self.relErrorLimit = 0                  #
            self.test_min = 1000                    # 1000mV
            self.test_max = 14400                   # 14.4V
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 1
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = False               # offset is not stored, don't care
            self.offset_int_width = 16               # offset is not stored, don't care
            self.offset_frac_width = 16              # offset is not stored, don't care
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3v3")

            #set manual range, full averaging, low current mode
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F5")
            # clear the multiplier register by setting it to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")

            # Ask user to setup 3V3 Leakage
            showDialog(title="Setup 3.3V Leakage Calibration",message="\aPlease connect the load to the 3.3v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            # negate result because in this case the load is providing the power, not sinking it
            return -load_meas_cur(self.powerModule.load)

        def readVal(self):

            return load_get_volt(self.powerModule.load)

        def setCoefficients(self):

            # we don't apply the leakage calibration here because it provides uA leakage results and the current calibration uses raw ADC values
            # instead we will use it to correct the current calibration and apply it later

            #result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            #logSimpleResult("Set 3.3v leakage to device", result)
            pass

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3.3v leakage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR)
            return coefficients

        def writeCoefficients(self,coefficents):

            # write 3.3v leakage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR + " " + coefficents["multiplier"])

    class QTL2347_3V3_LowCurrentCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2
            self.relErrorLimit = 2
            self.test_min = 10
            self.test_max = 85000
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 32
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3v3")

            #set manual range, full averaging, 3.3v low current mode, 12v all off (so we can detect we're connected to the wrong channel
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F1")
            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 3.3V Current
            showDialog(title="Setup 12V Current Calibration",message="\aPlease connect host power and load to the 3.3v channel")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connect Host Power",message="\aPlease connect host power and load to the 3.3v channel on the fixture")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            # read device voltage and add leakage current to the reference
            voltage =  super().meas_3v3_volt()
            leakage = voltage*self.powerModule.calibrations["3.3V"]["Leakage"].multiplier.originalValue() + self.powerModule.calibrations["3.3V"]["Leakage"].offset.originalValue()
            return load_meas_cur(self.powerModule.load) + leakage

        def readVal(self):

            return super().meas_3v3_cur()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 3.3v low current", result)
        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3.3v low current multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_LOW_MULTIPLIER_ADDR)
            # get 3.3v low current offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_LOW_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 3.3v low current multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 3.3v low current offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LOW_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_3V3_HighCurrentCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2000
            self.relErrorLimit = 1
            self.test_min = 1000
            self.test_max = 4000000
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 2048
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3v3")

            #set manual range, full averaging, 3.3v high current mode, 12v all off (so we can detect we're connected to the wrong channel
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F2")
            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 3.3V Current
            showDialog(title="Setup 12V Current Calibration",message="\aPlease connect host power and load to the 3.3v channel")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connect Host Power",message="\aPlease connect host power and load to the 3.3v channel on the fixture")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            # read device voltage and add leakage current to the reference
            voltage =  super().meas_3v3_volt()
            leakage = voltage*self.powerModule.calibrations["3.3V"]["Leakage"].multiplier.originalValue() + self.powerModule.calibrations["3.3V"]["Leakage"].offset.originalValue()
            return load_meas_cur(self.powerModule.load) + leakage

        def readVal(self):

            return super().meas_3v3_cur()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 3.3v high current", result)

            # once we've completed low and high current we can set leakage on the fixture
            result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_LEAKAGE_MULTIPLIER_ADDR + " " + self.powerModule.calibrations["3.3V"]["Leakage"].multiplier.hexString(4))

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3v3 high current multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_HIGH_MULTIPLIER_ADDR)
            # get 3v3 high current offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_HIGH_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 3v3 high current multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 3v3 high current offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_HIGH_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_3V3_AUX_VoltageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1
            self.relErrorLimit = 1
            self.test_min = 40
            self.test_max = 14400
            self.test_steps = 20
            self.units = "mV"
            self.scaling = 4
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3_AUX")

            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 3.3V Aux Voltage
            showDialog(title="Setup 3.3V Aux Voltage Calibration",message="\aPlease connect the load to the 3.3v Aux channel and disconnect host power")

            # Disconnect Host Power and check its gone
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Aux Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_aux_volt()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 3.3v voltage", result)

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3v3 voltage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_AUX_VOLT_MULTIPLIER_ADDR)
            # get 3v3 voltage offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_AUX_VOLT_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 3v3 voltage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 3v3 voltage offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_VOLT_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_3V3_AUX_LeakageCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 50                 # 1% of 5000 uA
            self.relErrorLimit = 0                  #
            self.test_min = 1000                    # 1000mV
            self.test_max = 14400                   # 14.4V
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 1
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = False               # offset is not stored, don't care
            self.offset_int_width = 16               # offset is not stored, don't care
            self.offset_frac_width = 16              # offset is not stored, don't care
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3_AUX")

            #set manual range, full averaging, low current mode
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.CALIBRATION_CONTROL_ADDR + " 0x00F5")
            # clear the multiplier register by setting it to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR + " 0x0000")

            # Ask user to setup 12V Leakage
            showDialog(title="Setup 3.3V Leakage Calibration",message="\aPlease connect the load to the 3.3v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            # negate result because in this case the load is providing the power, not sinking it
            return -load_meas_cur(self.powerModule.load)

        def readVal(self):

            return load_get_volt(self.powerModule.load)

        def setCoefficients(self):

            # we don't apply the leakage calibration here because it provides uA leakage results and the current calibration uses raw ADC values
            # instead we will use it to correct the current calibration and apply it later

            #result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            #logSimpleResult("Set 3.3v Aux leakage to device", result)
            pass

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3.3v Aux leakage multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR)
            return coefficients

        def writeCoefficients(self,coefficents):

            # write 3.3v Aux leakage multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR + " " + coefficents["multiplier"])

    class QTL2347_3V3_AUX_CurrentCalibration (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2
            self.relErrorLimit = 2
            self.test_min = 100     # 100uA
            self.test_max = 400000  # 400mA
            self.test_steps = 20
            self.units = "uA"
            self.scaling = 64
            self.multiplier_signed = False
            self.multiplier_int_width = 1
            self.multiplier_frac_width = 16
            self.offset_signed = True
            self.offset_int_width = 10
            self.offset_frac_width = 6
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3_AUX")

            # clear the multiplier and offset registers by setting them to zero
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_MULTIPLIER_ADDR + " 0x0000")
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_OFFSET_ADDR + " 0x0000")

            # Ask user to setup 3.3V Current
            showDialog(title="Setup 3.3V Aux Current Calibration",message="\aPlease connect host power and load to the 3.3v Aux channel")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connect Host Power",message="\aPlease connect host power and load to the 3.3v Aux channel on the fixture")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            # read device voltage and add leakage current to the reference
            voltage =  super().meas_3v3_aux_volt()
            leakage = voltage*self.powerModule.calibrations["3.3V Aux"]["Leakage"].multiplier.originalValue() + self.powerModule.calibrations["3.3V Aux"]["Leakage"].offset.originalValue()
            return load_meas_cur(self.powerModule.load) + leakage

        def readVal(self):

            return super().meas_3v3_aux_cur()

        def setCoefficients(self):

            result1 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_MULTIPLIER_ADDR + " " + self.multiplier.hexString(4))
            result2 = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_OFFSET_ADDR + " " + self.offset.hexString(4))
            if result1 and result2:
                result = True
            else:
                result = False
            logSimpleResult("Set 3.3v Aux low current", result)

            # once we've completed low and high current we can set leakage on the fixture
            result = self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_LEAKAGE_MULTIPLIER_ADDR + " " + self.powerModule.calibrations["3.3V Aux"]["Leakage"].multiplier.hexString(4))

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("calibrate",data)

        def readCoefficients(self):

            coefficients = {}
            # get 3v3 low current multiplier
            coefficients["multiplier"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_AUX_MULTIPLIER_ADDR)
            # get 3v3 low current offset
            coefficients["offset"] = self.powerModule.dut.sendCommand("read " + QTL2347.V3_3_AUX_OFFSET_ADDR)
            return coefficients

        def writeCoefficients(self,coefficients):

            # write 3v3 low current multiplier
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_MULTIPLIER_ADDR + " " + coefficients["multiplier"])
            # write 3v3 low current offset
            self.powerModule.dut.sendAndVerifyCommand("write " + QTL2347.V3_3_AUX_OFFSET_ADDR + " " + coefficients["offset"])

    class QTL2347_12V_VoltageVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1      # 1mV
            self.relErrorLimit = 1      # 1% tolerance
            self.test_min = 40          # 40mV
            self.test_max = 14400       # 14.4V
            self.test_steps = 20
            self.units = "mV"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12V")

            # Ask user to setup 12V Voltage
            showDialog(title="Setup 12V Voltage Verification",message="\aPlease connect the load to the 12v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 12v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_12v_volt()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_12V_LowCurrentVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2      # 2uA
            self.relErrorLimit = 2      # 2% tolerance
            self.test_min = 100         # 100uA
            self.test_max = 1000        # 1mA
            self.test_steps = 20
            self.units = "uA"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12V")

            # Ask user to setup 12V Current
            showDialog(title="Setup 12V Current Verification",message="\aPlease connect the load to the 12v channel and connect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connnect Host Power",message="\aPlease connect host power to the fixture on the 12v Channel")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            return load_meas_cur(self.powerModule.load)

        def readVal(self):

            return super().meas_12v_cur()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_12V_HighCurrentVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2000       # 2mA
            self.relErrorLimit = 1          # 1% tolerance
            self.test_min = 1000            # 1mA
            self.test_max = 4000000         # 4A
            self.test_steps = 20
            self.units = "uA"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("12v")

            # Ask user to setup 12V Current
            showDialog(title="Setup 12V Current Verification",message="\aPlease connect the load to the 12v channel and connect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connnect Host Power",message="\aPlease connect host power to the fixture on the 12v Channel")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            return load_meas_cur(self.powerModule.load)

        def readVal(self):

            return super().meas_12v_cur()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_3V3_VoltageVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1      # 1mV
            self.relErrorLimit = 1      # 1%
            self.test_min = 40          # 40mV
            self.test_max = 6000        # 6V
            self.test_steps = 20
            self.units = "mV"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3")

            # Ask user to setup 3V3 Voltage
            showDialog(title="Setup 3.3V Voltage Verification",message="\aPlease connect the load to the 3.3v channel and disconnect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_volt()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_3V3_LowCurrentVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2      # 2uA
            self.relErrorLimit = 2      # 2%
            self.test_min = 100         # 100uA
            self.test_max = 1000        # 1mA
            self.test_steps = 20
            self.units = "uA"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3")

            # Ask user to setup 3V3 Voltage
            showDialog(title="Setup 3.3V Current Verification",message="\aPlease connect the load to the 3.3v channel and connect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connnect Host Power",message="\aPlease connect host power to the fixture on the 3.3v Channel")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            return load_meas_cur(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_cur()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_3V3_HighCurrentVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2000       # 2mA
            self.relErrorLimit = 1          # 1% tolerance
            self.test_min = 1000            # 1mA
            self.test_max = 4000000         # 4A
            self.test_steps = 20
            self.units = "uA"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3")

            # Ask user to setup 3V3 Voltage
            showDialog(title="Setup 3.3V Current Verification",message="\aPlease connect the load to the 3.3v channel and connect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connnect Host Power",message="\aPlease connect host power to the fixture on the 3.3v Channel")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            return load_meas_cur(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_cur()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_3V3_AUX_VoltageVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 1      # 1mV
            self.relErrorLimit = 1      # 1%
            self.test_min = 40          # 40mV
            self.test_max = 14400       # 14.4V
            self.test_steps = 20
            self.units = "mV"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3_AUX")

            # Ask user to setup 3V3 Voltage
            showDialog(title="Setup 3.3V Aux Voltage Verification",message="\aPlease connect the load to the 3.3v Aux channel and disconnect host power")

            # Check Host Power is disconnected
            while (super().checkLoadVoltage(500,500) != True):
                showDialog(title="Disconnnect Host Power",message="\aPlease disconnect host power from the fixture on the 3.3v Aux Channel")

        def setRef(self,value):

            return load_set_volt(self.powerModule.load,value)

        def readRef(self):

            return load_meas_volt(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_aux_volt()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)

    class QTL2347_3V3_AUX_CurrentVerification (QTL2347Calibration):

        def __init__(self,powerModule):

            self.powerModule = powerModule
            self.absErrorLimit = 2      # 2uA
            self.relErrorLimit = 2      # 2%
            self.test_min = 100         # 100uA
            self.test_max = 400000      # 400mA
            self.test_steps = 20
            self.units = "uA"
            self.unitTemp = self.powerModule.dut.sendCommand('meas:temp unit?')
            self.v5Temp = self.powerModule.dut.sendCommand('meas:temp 5v?')
            self.v12Temp = self.powerModule.dut.sendCommand('meas:temp 12v?')

        def init(self):

            super().init_cal("3V3_AUX")

            # Ask user to setup 3V3 Voltage
            showDialog(title="Setup 3.3V Aux Current Verification",message="\aPlease connect the load to the 3.3v Aux channel and connect host power")

            # Check Host Power is present
            while (super().checkLoadVoltage(12000,1000) != True):
                showDialog(title="Connnect Host Power",message="\aPlease connect host power to the fixture on the 3.3v Aux Channel")

        def setRef(self,value):

            load_set_cur(self.powerModule.load,value)

        def readRef(self):

            return load_meas_cur(self.powerModule.load)

        def readVal(self):

            return super().meas_3v3_aux_cur()

        def finish(self):

            super().finish_cal()

        def report(self,data):

            return super().report("verify",data)



    def __init__(self,dut):

        # set the name of this module
        self.name = "PCIe x16 Power Measurement Fixture"
        self.dut = dut

        self.calibrations = {}
        # populate 12V channel with calibrations
        self.calibrations["12V"] = {
            "Voltage":self.QTL2347_12V_VoltageCalibration(self),
            "Leakage":self.QTL2347_12V_LeakageCalibration(self),
            "Low Current":self.QTL2347_12V_LowCurrentCalibration(self),
            "High Current":self.QTL2347_12V_HighCurrentCalibration(self)
            }
        # populate 3V3 channel with calibrations
        self.calibrations["3.3V"] = {
            "Voltage":self.QTL2347_3V3_VoltageCalibration(self),
            "Leakage":self.QTL2347_3V3_LeakageCalibration(self),
            "Low Current":self.QTL2347_3V3_LowCurrentCalibration(self),
            "High Current":self.QTL2347_3V3_HighCurrentCalibration(self)
            }
        # populate 3V3_AUX channel with calibrations
        self.calibrations["3.3V Aux"] = {
            "Voltage":self.QTL2347_3V3_AUX_VoltageCalibration(self),
            "Leakage":self.QTL2347_3V3_AUX_LeakageCalibration(self),
            "Current":self.QTL2347_3V3_AUX_CurrentCalibration(self)
            }

        self.verifications = {}
        # populate 12V channel with verifications
        self.verifications["12V"] = {
            "Voltage":self.QTL2347_12V_VoltageVerification(self),
            "Low Current":self.QTL2347_12V_LowCurrentVerification(self),
            "High Current":self.QTL2347_12V_HighCurrentVerification(self)
            }
        # populate 3V3 channel with verifications
        self.verifications["3.3V"] = {
            "Voltage":self.QTL2347_3V3_VoltageVerification(self),
            "Low Current":self.QTL2347_3V3_LowCurrentVerification(self),
            "High Current":self.QTL2347_3V3_HighCurrentVerification(self)
            }
        # populate 3V3 channel with verifications
        self.verifications["3.3V Aux"] = {
            "Voltage":self.QTL2347_3V3_AUX_VoltageVerification(self),
            "Current":self.QTL2347_3V3_AUX_CurrentVerification(self)
            }

if __name__== "__main__":
    main()

