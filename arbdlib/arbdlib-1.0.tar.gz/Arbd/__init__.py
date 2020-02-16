from pyfirmata import ArduinoNano, util
import time
import serial

class arbd1:
    @staticmethod
    def getPorts():
        ports = list(serial.tools.list_ports.comports())
        portList = []
        for p in ports:
            portList.append(str(p))
        return portList

    def __init__(self,COM):
        self.temp = None
        self.humidity = None
        self.board = ArduinoNano(COM)
        self.iterator = util.Iterator(self.board)
        self.iterator.start()
        # RGB PINS
        self.board.get_pin('d:9:p')
        self.board.get_pin('d:10:p')
        self.board.get_pin('d:11:p')
        # BUZZER PIN
        self.board.get_pin('d:6:p')
        # Navigation Switches
        self.board.get_pin('a:1:o')
        # Potentiometer
        self.board.get_pin('a:6:o')
        # LDR
        self.board.get_pin('a:7:o')
        # Charlieplexed LEDs
        self.board.get_pin('a:2:o')
        self.board.get_pin('a:3:o')
        self.board.get_pin('a:4:o')
        # delays
        self.potentiometer_delay = 0.1
        self.ldr_delay = 0.1
        self.dht_delay = 0.1
        self.navigation_switches_delay = 0.01
        print('*** CONNECTION ESTABLISHED ***')
    # Enter one or zero to turn off and turn on Rgb led
    def rgb_digital(self, r, g, b):
        self.board.digital[9].write(g)
        self.board.digital[10].write(b)
        self.board.digital[11].write(r)

    # takes value from 0.0 to 1.0
    def rgb_analog(self, r, g, b):
        self.board.digital[9].write(g)
        self.board.digital[10].write(b)
        self.board.digital[11].write(r)

    # takes value from 0.0 to 1.0
    def buzzer(self, value):
        self.board.digital[6].write(value)

    # Navigation Switch
    '''Return Values
    UP => 1
    DOWN => 2
    LEFT => 3
    Right => 4
    Center => 5
    
    '''

    def navigationSwitchesClickTest(self):
        time.sleep(0.5)
        prevValue = self.board.analog[1].read()
        while (1):
            time.sleep(0.1)
            value = self.board.analog[1].read()
            if (value < prevValue + 0.02 and value > prevValue - 0.02):
                pass

            elif value >= 0 and value < 0.01:
                print("Up Pressed")
            elif value >= 0.79 and value < 0.81:
                print("Down Pressed")
            elif value >= 0.47 and value < 0.52:
                print("Left Pressed")
            elif value >= 0.745 and value < 0.755:
                print("Right Pressed")
            elif value >= 0.655 and value < 0.675:
                print("Center Pressed")
            prevValue = value

    def navigation_switches(self):
        ret_val = 0
        time.sleep(self.navigation_switches_delay)
        value = self.board.analog[1].read()
        if 0 <= value < 0.01:
            ret_val = 1
        elif 0.79 <= value < 0.81:
            ret_val = 2
        elif 0.47 <= value < 0.52:
            ret_val = 3
        elif value >= 0.745 and value < 0.755:
            ret_val = 4
        elif value >= 0.655 and value < 0.675:
            ret_val = 5
        return ret_val

    # Return value from 0.0 to 1.0
    def potentiometer(self):
        
        time.sleep(self.potentiometer_delay)
        value = self.board.analog[6].read()
        return value

    # Return value from 0.0 to 1.0
    def ldr(self):
        time.sleep(self.ldr_delay)
        value = self.board.analog[7].read()
        return value

    def charlieplexing(self, A2='Z', A3='Z', A4='L', A5='H'):
        # https://arbd1.hatchnhack.com/arbd1-peripherals/multiplexing/charlieplexing
        # Z is for high impedance or Input
        # H = HIGH PIN
        # L = LOW PIN
        LED = 0
        cmd = 0x01  # Command for Charlieplexing as it was made in firmata.ino file
        if A2 == 'Z' and A3 == 'Z' and A4 == 'L' and A5 == 'H':
            LED = 1
        elif A2 == 'Z' and A3 == 'L' and A4 == 'Z' and A5 == 'H':
            LED = 2
        elif A2 == 'L' and A3 == 'Z' and A4 == 'Z' and A5 == 'H':
            LED = 3
        elif A2 == 'Z' and A3 == 'L' and A4 == 'H' and A5 == 'Z':
            LED = 4
        elif A2 == 'L' and A3 == 'Z' and A4 == 'H' and A5 == 'Z':
            LED = 5
        elif A2 == 'Z' and A3 == 'Z' and A4 == 'H' and A5 == 'L':
            LED = 6
        elif A2 == 'L' and A3 == 'H' and A4 == 'Z' and A5 == 'Z':
            LED = 7
        elif A2 == 'Z' and A3 == 'H' and A4 == 'Z' and A5 == 'L':
            LED = 8
        elif A2 == 'Z' and A3 == 'H' and A4 == 'L' and A5 == 'Z':
            LED = 9
        elif A2 == 'H' and A3 == 'Z' and A4 == 'Z' and A5 == 'L':
            LED = 10
        elif A2 == 'H' and A3 == 'Z' and A4 == 'L' and A5 == 'Z':
            LED = 11
        elif A2 == 'H' and A3 == 'L' and A4 == 'Z' and A5 == 'Z':
            LED = 12
        data = [LED]
        self.board.send_sysex(cmd, data)

    def charlieplexing_pov(self):
        while 1:
            for x in range(1, 13):
                self.board.send_sysex(0x01, [x])

    def dht11(self):  # Function to fetch temp and humidity value
        # Returns Nothing
        def get_dht(*args, **kwargs):  # Returns DHT value
            # print(args)
            # print util.two_byte_iter_to_str(args)
            # print(kwargs)
            self.humidity = args[0]
            self.temp = args[1]

        self.board.add_cmd_handler(0x02, get_dht)  # Command mentioned in firmata.ino
        self.board.send_sysex(0x02, [])  # Command send to ARBD1
        time.sleep(self.dht_delay)

    def temp_and_humidity(self):
        self.dht11()
        return [self.temp, self.humidity]




