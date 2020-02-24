import time, threading, random
try:
    import smbus
    VIRTUALIZE = False
except:
    print("pysmbus not found.")
    print("Configuration will default to Virtualizing.")
    VIRTUALIZE = True
    
class MPU_6050(object):

    """
    I2C MPU_6050

    """

    GRAVITIY_MS2 = 9.80665
    address = None
    bus = None
    ACCEL_SCALE_MODIFIER_2G = 16384.0
    ACCEL_SCALE_MODIFIER_4G = 8192.0
    ACCEL_SCALE_MODIFIER_8G = 4096.0
    ACCEL_SCALE_MODIFIER_16G = 2048.0
    GYRO_SCALE_MODIFIER_250DEG = 131.0
    GYRO_SCALE_MODIFIER_500DEG = 65.5
    GYRO_SCALE_MODIFIER_1000DEG = 32.8
    GYRO_SCALE_MODIFIER_2000DEG = 16.4
    ACCEL_RANGE_2G = 0x00
    ACCEL_RANGE_4G = 0x08
    ACCEL_RANGE_8G = 0x10
    ACCEL_RANGE_16G = 0x18
    GYRO_RANGE_250DEG = 0x00
    GYRO_RANGE_500DEG = 0x08
    GYRO_RANGE_1000DEG = 0x10
    GYRO_RANGE_2000DEG = 0x18
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C
    TEMP_OUT0 = 0x41
    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B
    
    ACCEL_XOUT0 = 0x43
    ACCEL_YOUT0 = 0x45
    ACCEL_ZOUT0 = 0x47

    GYRO_XOUT0 = 0x3B
    GYRO_YOUT0 = 0x3D
    GYRO_ZOUT0 = 0x3F

    def __init__(self, address=0x68, bus=1, sleep=0.5):
        """
        address = MPU_6080 Address - Default to MPU6060 default address
        bus = Smbus for I2C - Default to 1
        sleep = Refresher/Updater sleep time - Default 0.5 seconds
        """

        super().__init__()
        self.error = False
        self.Gyro = Gyro()
        self.Remote = None
        self.Accelerometer = Accelerometer()
        if VIRTUALIZE == False:
            self.address = address
            self.def_bus = bus
            self.bus = smbus.SMBus(bus)
            self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)
        self.updater_sleep = sleep
        threading.Thread(target=self.__z_Underground__, daemon=True).start()

    def read_i2c(self, reg):
        if VIRTUALIZE:
            return 0
        high = self.bus.read_byte_data(self.address, reg)
        low = self.bus.read_byte_data(self.address, reg + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    @property
    def temp(self):
        if VIRTUALIZE:
            return 20.0
        raw_temp = self.read_i2c(self.TEMP_OUT0)
        actual_temp = (raw_temp / 340.0) + 36.53

        return actual_temp

    def set_accelerometer(self, accel_range):
        if VIRTUALIZE:
            return None
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, 0x00)
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, accel_range)

    def read_accel_range(self, raw = False):
        if VIRTUALIZE:
            return 2
        raw_data = self.bus.read_byte_data(self.address, self.ACCEL_CONFIG)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == self.ACCEL_RANGE_2G:
                return 2
            elif raw_data == self.ACCEL_RANGE_4G:
                return 4
            elif raw_data == self.ACCEL_RANGE_8G:
                return 8
            elif raw_data == self.ACCEL_RANGE_16G:
                return 16
            else:
                return -1

    @property
    def accelerometer_data(self, g = False):
        if VIRTUALIZE:
            return (random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200))
        x = self.read_i2c(self.ACCEL_XOUT0)
        y = self.read_i2c(self.ACCEL_YOUT0)
        z = self.read_i2c(self.ACCEL_ZOUT0)

        accel_scale_modifier = None
        accel_range = self.read_accel_range(True)

        if accel_range == self.ACCEL_RANGE_2G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G
        elif accel_range == self.ACCEL_RANGE_4G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_4G
        elif accel_range == self.ACCEL_RANGE_8G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_8G
        elif accel_range == self.ACCEL_RANGE_16G:
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_16G
        else:
            print("Error")
            accel_scale_modifier = self.ACCEL_SCALE_MODIFIER_2G

        x = x / accel_scale_modifier
        y = y / accel_scale_modifier
        z = z / accel_scale_modifier

        if g is True:
            return (x, y, z)
        elif g is False:
            return (x * self.GRAVITIY_MS2, y * self.GRAVITIY_MS2, z * self.GRAVITIY_MS2)

    def set_gyro(self, gyro_range):
        if VIRTUALIZE:
            return None
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, 0x00)
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, gyro_range)

    def read_gyro_range(self, raw = False):
        if VIRTUALIZE:
            return 250
        raw_data = self.bus.read_byte_data(self.address, self.GYRO_CONFIG)

        if raw is True:
            return raw_data
        elif raw is False:
            if raw_data == self.GYRO_RANGE_250DEG:
                return 250
            elif raw_data == self.GYRO_RANGE_500DEG:
                return 500
            elif raw_data == self.GYRO_RANGE_1000DEG:
                return 1000
            elif raw_data == self.GYRO_RANGE_2000DEG:
                return 2000
            else:
                return -1

    @property
    def Gyro_data(self):
        if VIRTUALIZE:
            return (random.randint(-200, 200), random.randint(-200, 200), random.randint(-200, 200))
        x = self.read_i2c(self.GYRO_XOUT0)
        y = self.read_i2c(self.GYRO_YOUT0)
        z = self.read_i2c(self.GYRO_ZOUT0)

        gyro_scale_modifier = None
        gyro_range = self.read_gyro_range(True)

        if gyro_range == self.GYRO_RANGE_250DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG
        elif gyro_range == self.GYRO_RANGE_500DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_500DEG
        elif gyro_range == self.GYRO_RANGE_1000DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_1000DEG
        elif gyro_range == self.GYRO_RANGE_2000DEG:
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_2000DEG
        else:
            print("Unkown range - gyro_scale_modifier set to self.GYRO_SCALE_MODIFIER_250DEG")
            gyro_scale_modifier = self.GYRO_SCALE_MODIFIER_250DEG

        x = x / gyro_scale_modifier
        y = y / gyro_scale_modifier
        z = z / gyro_scale_modifier

        return (x, y, z)
    
    def reconnect(self):
        for i in range(10):
            try:
                print("Reconnecting:", i, "/", 10)
                time.sleep(2)
                self.bus = smbus.SMBus(self.def_bus)
                self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)
                print("Reconnected")
                return
            except:
                pass
        raise ConnectionError("Connection Error: Did module get disconnected?")
        

    def __z_Underground__(self):
        while True:
            try:
                self.error = False
                if VIRTUALIZE == False:
                    self.Gyro.Update(self.Gyro_data)
                    self.Accelerometer.Update(self.accelerometer_data)
                if self.Remote:
                    if self.Remote.TYPE == "SENDER":
                        data = {}
                        data['g_x'] = self.Gyro.x.value
                        data['g_y'] = self.Gyro.y.value
                        data['g_z'] = self.Gyro.z.value

                        data['a_x'] = self.Accelerometer.x.value
                        data['a_y'] = self.Accelerometer.y.value
                        data['a_z'] = self.Accelerometer.z.value

                        self.Remote.data = data
                    else:
                        data = self.Remote.data
                        self.Gyro.x.value = data['g_x']
                        self.Gyro.y.value = data['g_y']
                        self.Gyro.z.value = data['g_z']

                        self.Accelerometer.x.value = data['a_x'] 
                        self.Accelerometer.y.value = data['a_y']
                        self.Accelerometer.z.value = data['a_z']
                time.sleep(self.updater_sleep)
            except Exception as e:
                self.error = True
                if VIRTUALIZE == False:
                    self.reconnect()
                else:
                    print(e)
                    raise ConnectionError("Couldn't reconnect to remote.")




class Gyro(object):
    
    def __init__(self):
        super().__init__()
        self.x = Axis("Gyro_X")
        self.y = Axis("Gyro_Y")
        self.z = Axis("Gyro_Z")

    def set_offset(self):
        self.x.offset = self.x.value*-1
        self.y.offset = self.y.value*-1
        self.z.offset = self.z.value*-1

    def Update(self, vals):
        x_val, y_val, z_val = vals
        self.x.value = x_val
        self.y.value = y_val
        self.z.value = z_val

class Accelerometer(object):

    def __init__(self):
        super().__init__()
        self.x = Axis("Acc_X")
        self.y = Axis("Acc_Y")
        self.z = Axis("Acc_Z")

    def Update(self, vals):
        x_val, y_val, z_val = vals
        self.x.value = x_val
        self.y.value = y_val
        self.z.value = z_val


class Axis(object):

    def __init__(self, name):
        super().__init__()
        self.value = 0
        self.name = name
        self.offset = 0
        self.do_emulate = False

    @property
    def offset_value(self):
        return self.value + self.offset

    def Emulate(self, max_step=0.5, sleep=1, max_value=180):
        if self.do_emulate == False:
            self.do_emulate = True
            threading.Thread(target=self.__z_Underground__, daemon=True, args=[max_step, sleep, max_value]).start()
        else:
            self.do_emulate = False

    def __z_Underground__(self, max_step, sleep, max_value):
        direction = 1
        while self.do_emulate:
            self.value += (random.randint(0, max_step*100)/100) * direction
            self.value = round(self.value, 4)
            if random.randint(0, 4) == 3 or abs(self.value) >= max_value:
                direction = direction * -1
            time.sleep(sleep)
