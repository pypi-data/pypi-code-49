"""
@ Stefanie Fiedler 2020
@ Alexander Teubert 2020
Version vom 18.02.2020

for Hochschule Anhalt, University of Applied Sciences
in coorperation with axxeo GmbH
"""

from EasyModbusSilaaCooling.modbusClient import ModbusClient as MBC
from HeliosEthernetSilaaCooling.Helios_HexConverter import str2duohex, duohex2str
from HeliosEthernetSilaaCooling.Helios_Errors import errortable, warningtable, infotable
import re
from logging import debug, info, warning, error, critical, basicConfig, DEBUG, INFO, WARNING, ERROR, CRITICAL

"""
set-up the logger module by using the basicConfig - method
level - level of severity, on which the logger starts writing output, might be changed between:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
filename - name of the logfile, ending on .log
filemode - possible modes:
    w - write, overwrites existing file
    a - append, standard mode, appends on existing log file
format - sets the standard format for the logged string
"""

basicConfig(
    level=INFO,
    filename="/home/pi/Log-Datei/Helios_Ethernet.log",
    filemode="a",
    format="%(asctime)s: %(name)s - %(levelname)s - %(message)s")

class COM():
    """
    Implementation of a Modbus TCP/IP-Client to access read and writeable attributes of a Helios KWL Device
    """

    def __init__(self, ip = "192.168.40.40", port = 502):

        if isinstance(ip, str): self.__ip = ip
        else:
            error("The ip-adress should be given as a string!")
            return "Wrong input!"

        if isinstance(port, int): self.__port = port
        else:
            error("Please check your input! The tcp-port should be given as an integer!")
            return "Wrong input!"

        self.__timeout = 2
        self.__device_id = 180

        """
        setup for the Modbus-Connection
        """

        self.modbusclient = MBC(self.__ip, self.__port)
        self.modbusclient.unitidentifier = self.__device_id
        self.modbusclient.timeout = self.__timeout
        self.modbusclient.connect()

        info("Connecting to the client for the first time!")
        debug("Setting date-format to dd.mm.yyyy and operation-mode to automatic to test the connection")

        """
        set date-format to dd.mm.yyyy
        """

        self.modbusclient.write_multiple_registers(0, str2duohex("v00052=mm.dd.yyyy"))

        info("Modbus client succesfully running!")


    def exit(self):
        self.modbusclient.close()
        info("Modbus client succesfully stopped!")


    def set_operation_mode(self, mode):
        """
        sets the operation mode to on (1) or off(0)
        """

        debug("Checking values of setting operation mode...")
        if (mode in (0,1)):
            debug("Setting operation mode...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00101=" + str(mode)) )
            info("Operation mode was set succesfully!")
        else:
            error("Please check the validicity of your input values! (operation mode)")
            return "Wrong input!"


    def read_operation_mode(self):
        """
        reads operation mode from slave (0=off; 1=on)
        """

        debug("Reading operation mode...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00101"))
        operation_state = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]
        info("Operation mode was succesfully read!")
        return int(operation_state)


    def read_temp(self):
        """
        reads several temperature values from slave and returns them as a list of float-values
        """

        """
        read outdoor-air-temperature (variable v00104) / Aussenluft
        """
        debug("Reads the sensor for the outdoor-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00104"))
        outTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read supplied-air-temperature (variable v00105) / Zuluft
        """
        debug("Reads the sensor for the supplied-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00105"))
        suppTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read exhaust-air-temperature (variable v00106) / Fortluft
        """
        debug("Reads the sensor for the exhaust-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00106"))
        exhaustTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read extract-air-temperature (variable v00107) / Abluft
        """
        debug("Reads the sensor for the extract-air-temperature...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00107"))
        extractTemp = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        info("Successfully read all temperature sensors!")
        return float(outTemp), float(suppTemp), float(exhaustTemp), float(extractTemp)


    def read_date(self):
        """
        outputs the slaves time and date
        """

        """
        read system-clock (variable v00005)
        """
        debug("Reads the system-clock...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00005"))
        time = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]

        """
        read system-date (variable v00004)
        """
        debug("Reads the system-date...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00004"))
        date = duohex2str(self.modbusclient.read_holdingregisters(0,9))[7:]

        info("Successfully read time and date!")
        return time, date


    def set_date(self, time, date):
        """
        sets the slave time and date
        """

        """
        sets the slave date / v00004
        by using a regular expression, we check if the date-format is correct
        """

        debug("Checking if the given date matches the pattern...")
        #filtert das Datumsformat, nach Monaten mit 31 und 30 Tagen und Februar
        if re.compile("[0][1-9].[0][13578].[0-2][0-9][0-9][0-9]|\
[0][1-9].[1][02].[0-2][0-9][0-9][0-9]|\
[1-2][0-9].[0][13578].[0-2][0-9][0-9][0-9]|\
[1-2][0-9].[1][02].[0-2][0-9][0-9][0-9]|\
[3][0-1].[0][13578].[0-2][0-9][0-9][0-9]|\
[3][0-1].[1][02].[0-2][0-9][0-9][0-9]|\
[0][1-9].[0][469].[0-2][0-9][0-9][0-9]|\
[0][1-9].[1][1].[0-2][0-9][0-9][0-9]|\
[1-2][0-9].[0][469].[0-2][0-9][0-9][0-9]|\
[1-2][0-9].[1][1].[0-2][0-9][0-9][0-9]|\
[3][0].[0][469].[0-2][0-9][0-9][0-9]|\
[3][0].[1][1].[0-2][0-9][0-9][0-9]|\
[0][1-9].[0][2].[0-2][0-9][0-9][0-9]|\
[1-2][0-9].[0][2].[0-2][0-9][0-9][0-9]").fullmatch(date):
            debug("Setting the slaves date...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00004="+date))
            info("Successfully set the date!")

        else:
            error("Please check your date format! It should be dd.mm.yyyy")
            return "Wrong format of date!"

        """
        sets the slave time / v00005
        by using a regular expression, we check if the time-format is correct
        """
        debug("Checking if the given date matches the pattern...")
        if re.compile("[01][0-9]:[0-5][0-9]:[0-5][0-9]|[2][0-3]:[0-5][0-9]:[0-5][0-9]").fullmatch(time):
            debug("Setting the slaves time...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00005="+time))
            info("Successfully set the time!")

        else:
            error("Please check your time format! It should be hh:mm:ss")
            return "Wrong format of time!"


    def read_management_state(self):
        """
        outputs the state of the humidity, carbon-dioxide and voc-management
        """

        """
        read humidity management-state (variable v00033)
        """
        debug("Reading the humidity management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00033") )
        humidity_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read carbon-dioxide management-state (variable v00037)
        """
        debug("Reading the carbon-dioxide management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00037") )
        carbon_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read voc management-state (variable v00040)
        """
        debug("Reading the voc management state...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00040") )
        voc_state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        info("Successfully read all management states from the slave!")
        return int(humidity_state), int(carbon_state), int(voc_state)

    def read_management_opt(self):
        """
        outputs the defined optimum value for the humidity, carbon-dioxide and voc-management
        """

        """
        read optimum humidity level in percent (variable v00034)
        """
        debug("Reading the optimum humidity level in percent...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00034"))
        humidity_val = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]

        """
        read optimum carbon-dioxide concentration in ppm (variable v00038)
        """
        debug("Reading the optimum carbon-dioxide concentration in ppm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00038") )
        carbon_val = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        """
        read optimum voc concentration in ppm (variable v00041)
        """
        debug("Reading the optimum voc concentration in ppm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00041") )
        voc_val = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        info("Successfully set all optimal values for the air quality-sensors!")
        return int(humidity_val), int(carbon_val), int(voc_val)

    def set_management_state(self, state_humidity, state_carbon, state_voc):
        """
        writes the state of the humidity, carbon-dioxide and voc-management
        """
        debug("Checking legimaticy of the input values...")
        state_humidity = int(state_humidity)
        state_carbon = int(state_carbon)
        state_voc = int(state_voc)
        if (state_humidity >= 0 and state_humidity <= 2):
            """
            write humidity management-state (variable v00033)
            """
            debug("Setting the state on the humidity management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00033="+ str(state_humidity)) )
        else:
            return "Wrong input!"
            error("Wrong Input! (state_humidity)")
        if (state_carbon >= 0 and state_carbon <= 2):

            """
            write carbon-dioxide management-state (variable v00037)
            """
            debug("Setting the state on the carbon-dioxide management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00037="+ str(state_carbon)) )
        else:
            return "Wrong input!2"
            error("Wrong input! (state_carbon)")
        if (state_voc >= 0 and state_voc <= 2):

            """
            write voc management-state (variable v00040)
            """
            debug("Setting the state on the voc management...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00040="+ str(state_voc)) )

            info("Successfully wrote all optimal values to the slave")

        else:
            error("Please check the validicity of your input values! (state_voc)")
            return "Invalid input values!"

    def set_management_opt(self, opt_humidity, opt_carbon, opt_voc):
        """
        sets the optimum value for the humidity, carbon-dioxide and voc-management
        """
        debug("Checking legimaticy of the input values...")
        opt_humidity = int(opt_humidity)
        opt_carbon = int(opt_carbon)
        opt_voc = int(opt_voc)
        if(opt_humidity >= 20 and opt_humidity <= 80):
            """
            set the optimum percentage of air-humidity /  between 20% and 80% (variable v00034)
            """
            debug("Setting the optimal level of air-humidity...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00034="+ str(opt_humidity)))
        else:
            error("Please check the validicity of your input values! (opt_humidity)")
            return "Invalid input values"

        if(opt_carbon >= 300 and opt_carbon <= 2000):
            """
            set the optimum concentration of carbon-dioxide / between 300 and 2000 ppm (variable v00038)
            """
            debug("Setting the optimal concentration of carbon-dioxide...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00038="+ str(opt_carbon)))
        else:
            error("Please check the validicity of your input values! (opt_carbon)")
            return "Invalid input values!"
        if(opt_voc >= 300 and opt_voc <= 2000):
            """
            set the optimum concentration of voc / between 300 and 2000 ppm (variable v00041)
            """
            debug("Setting the optimal concetration of voc...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00041="+ str(opt_voc)))
            info("Successfully wrote optimal value for voc to the slave")

        else:
            error("Please check the validicity of your input values! (opt_voc)")
            return "Invalid input values!"


    def read_state_preheater(self, *preheater):
        """
        sets/ reads the state of the preheater / 0 = off, 1 = on (variable v00024)
        """
        debug("Checking input to determine, if to read or set the state of the slaves preheater...")
        try:
            if isinstance(preheater[0], int) & (preheater[0] in (0,1)):
                debug("Setting state of preheater...")
                self.modbusclient.write_multiple_registers(0, str2duohex("v00024="+ str(preheater[0])) )
                info("Successfully wrote state to the preheater!")

        except IndexError:
            debug("Reading state of preheater...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00024"))
            state = duohex2str(self.modbusclient.read_holdingregisters(0,5))[7:]
            info("Successfully read state of the preheater!")
            return state

    def read_fan_level(self):
        """
        read fan level in percents (variable v00103)
        """
        debug("Reading fan level in percents...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00103") )
        level = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
        info("Successfully read fan level in percents!")
        return int(level)

    def read_fan_rpm(self):
        """
        read the revolutions per minute for the supply fan (variable v00348)
        """
        debug("Reading supply fans rpm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00348") )
        supply = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        """
        read the revolutions per minute for the extraction fan (variable v00349)
        """
        debug("Reading extraction fans rpm...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00349") )
        extraction = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]

        info("Successfully read the rpm of extraction and suppply fan!")
        return int(supply), int(extraction)

    def read_fan_stage(self):
        """
        reads fan stage / 0-4 (variable v00102)
        """
        debug("Reading fan stage...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v00102") )
        stage = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
        info("Successfully read fan stage level!")
        return int(stage)

    def set_fan_stage(self, stage):
        """
        sets the state for the supply and  extraction fans / stages 0-4
        """
        debug("Checking the input values for the supply and extraction fans stages...")
        if (isinstance(stage, int)) & (stage in (0,1,2,3,4)):
            """
            sets the stage for the supply fan (variable v00102)
            """
            debug("Setting the fan stage...")
            self.modbusclient.write_multiple_registers(0, str2duohex("v00102="+ str(stage)) )
            info("Successfully set the supply fans stage!")

        else:
            error("Please check the validicity of your input values! stage")
            return("Invalid input values!")

    def read_state(self):
        """
        receive error messages from the Helios Slave
        """

        string = ""

        """
        read errors as integer values / v01123
        """
        debug("Requesting error codes from the slave...")
        try:
            self.modbusclient.write_multiple_registers(0, str2duohex("v01123") )
            string = duohex2str(self.modbusclient.read_holdingregisters(0,8))[7:]
            info("Successfully read error message from the slave!")
            return errortable(int(string)), "error"

        except KeyError:
            """
            read warnings as integer values / v01124
            """
            debug("Requesting warning codes from the slave...")
            try:
                self.modbusclient.write_multiple_registers(0, str2duohex("v01124") )
                string = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
                info("Successfully read warnings from the slave!")
                return warningtable(int(string)), "warning"

            except KeyError:
                """
                read informations on the state of the KWL EC 170 W / v01125
                """
                debug("Requesting information codes on the state of the slave...")
                try:
                    self.modbusclient.write_multiple_registers(0, str2duohex("v01125") )
                    string = duohex2str(self.modbusclient.read_holdingregisters(0,6))[7:]
                    info("Successfully informations from the slave!")
                    return infotable(int(string)), "state"

                except KeyError:
                    return "There are no callable errors, alerts or informations!"

    def clear_state(self):
        """
        clears the memory of the error register
        """
        debug("Clearing the error register...")
        self.modbusclient.write_multiple_registers(0, str2duohex("v02015=1") )
        info("Successfully cleared the memory of the error register!")
