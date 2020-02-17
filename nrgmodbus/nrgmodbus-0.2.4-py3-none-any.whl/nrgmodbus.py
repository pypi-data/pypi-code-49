#!/bin/usr/python


class ipackaccess(object):
    """
    class for handling modbus connections to iPackACCESS

    parameters
                  ip : string, ip address or domain name of zx lidar
                port : int, port for modbus access (default 502)
                unit : int, slave number on bus (default 1)   
        logger_model : int, finished good number of connected Symphonie
            (default 8206)
    """
    def __init__(self, ip='', port=502, logger_model=8206, unit=1, connect=False):
        self.ip = ip
        self.logger_model = logger_model
        self.port = port
        self.unit = unit
        self.hard_init_registers()
        self.e = ''
        if connect == True:
            self.connect()


    def hard_init_registers(self):
        """
        set registers for all available data manually
        each is an array
         0 = register address
         1 = number of registers
        """
        # system information
        self.hr_signed_num_ex = [0, 2]
        self.hr_unsigned_num_ex = [2, 2]
        self.hr_unsigned_16_num_ex = [4, 1]
        self.hr_site_number = [5, 2]
        self.hr_logger_sn = [7, 2]
        self.hr_logger_model = [9, 1]
        self.hr_logger_ver = [10, 2]
        self.hr_logger_fw = [12, 2]
        self.hr_ipack_sn = [14, 2]
        self.hr_ipack_model = [16, 1]
        self.hr_ipack_ver = [17, 2]
        self.hr_ipack_fw = [19, 2]
        # real-time data
        self.hr_rt_year = [1500, 1]
        self.hr_rt_month = [1501, 1]
        self.hr_rt_day = [1502, 1]
        self.hr_rt_hour = [1503, 1]
        self.hr_rt_minute = [1504, 1]
        self.hr_rt_second = [1505, 1]
        self.hr_rt_channel_readings = [1506, 52]
        # statistical time data
        self.hr_sta_year = [2500, 1]
        self.hr_sta_month = [2501, 1]
        self.hr_sta_day = [2502, 1]
        self.hr_sta_hour = [2503, 1]
        self.hr_sta_minute = [2504, 1]
        self.hr_sta_second = [2505, 1]
        # statistical channel data]
        self.hr_sta_ch1_avg = [2506, 2]
        self.hr_sta_ch1_sd = [2508, 2]
        self.hr_sta_ch1_max = [2510, 2]
        self.hr_sta_ch1_min = [2512, 2]
        self.hr_sta_ch1_gust = [2514, 2]
        self.hr_sta_ch2_avg = [2516, 2]
        self.hr_sta_ch2_sd = [2518, 2]
        self.hr_sta_ch2_max = [2520, 2]
        self.hr_sta_ch2_min = [2522, 2]
        self.hr_sta_ch2_gust = [2524, 2]     
        self.hr_sta_ch3_avg = [2526, 2]
        self.hr_sta_ch3_sd = [2528, 2]
        self.hr_sta_ch3_max = [2530, 2]
        self.hr_sta_ch3_min = [2532, 2]
        self.hr_sta_ch3_gust = [2534, 2]  
        self.hr_sta_ch4_avg = [2536, 2]
        self.hr_sta_ch4_sd = [2538, 2]
        self.hr_sta_ch4_max = [2540, 2]
        self.hr_sta_ch4_min = [2542, 2]
        self.hr_sta_ch4_gust = [2544, 2]
        self.hr_sta_ch5_avg = [2546, 2]
        self.hr_sta_ch5_sd = [2548, 2]
        self.hr_sta_ch5_max = [2550, 2]
        self.hr_sta_ch5_min = [2552, 2]
        self.hr_sta_ch5_gust = [2554, 2]
        self.hr_sta_ch6_avg = [2556, 2]
        self.hr_sta_ch6_sd = [2558, 2]
        self.hr_sta_ch6_max = [2560, 2]
        self.hr_sta_ch6_min = [2562, 2]
        self.hr_sta_ch6_gust = [2564, 2]
        self.hr_sta_ch7_avg = [2566, 2]
        self.hr_sta_ch7_sd = [2568, 2]
        self.hr_sta_ch7_max = [2570, 2]
        self.hr_sta_ch7_min = [2572, 2]
        self.hr_sta_ch7_gust = [2574, 2]
        self.hr_sta_ch8_avg = [2576, 2]
        self.hr_sta_ch8_sd = [2578, 2]
        self.hr_sta_ch8_max = [2580, 2]
        self.hr_sta_ch8_min = [2582, 2]
        self.hr_sta_ch8_gust = [2584, 2]
        self.hr_sta_ch9_avg = [2586, 2]
        self.hr_sta_ch9_sd = [2588, 2]
        self.hr_sta_ch9_max = [2590, 2]
        self.hr_sta_ch9_min = [2592, 2]
        self.hr_sta_ch9_gust = [2594, 2]
        self.hr_sta_ch10_avg = [2596, 2]
        self.hr_sta_ch10_sd = [2598, 2]
        self.hr_sta_ch10_max = [2600, 2]
        self.hr_sta_ch10_min = [2602, 2]
        self.hr_sta_ch10_gust = [2604, 2]
        self.hr_sta_ch11_avg = [2606, 2]
        self.hr_sta_ch11_sd = [2608, 2]
        self.hr_sta_ch11_max = [2610, 2]
        self.hr_sta_ch11_min = [2612, 2]
        self.hr_sta_ch11_gust = [2614, 2]
        self.hr_sta_ch12_avg = [2616, 2]
        self.hr_sta_ch12_sd = [2618, 2]
        self.hr_sta_ch12_max = [2620, 2]
        self.hr_sta_ch12_min = [2622, 2]
        self.hr_sta_ch12_gust = [2624, 2]
        self.hr_sta_ch13_avg = [2626, 2]
        self.hr_sta_ch13_sd = [2628, 2]
        self.hr_sta_ch13_max = [2630, 2]
        self.hr_sta_ch13_min = [2632, 2]
        self.hr_sta_ch14_avg = [2634, 2]
        self.hr_sta_ch14_sd = [2636, 2]
        self.hr_sta_ch14_max = [2638, 2]
        self.hr_sta_ch14_min = [2640, 2]
        self.hr_sta_ch15_avg = [2642, 2]
        self.hr_sta_ch15_sd = [2644, 2]
        self.hr_sta_ch15_max = [2646, 2]
        self.hr_sta_ch15_min = [2648, 2]
        self.hr_sta_ch16_avg = [2650, 2]
        self.hr_sta_ch16_sd = [2652, 2]
        self.hr_sta_ch16_max = [2654, 2]
        self.hr_sta_ch16_min = [2656, 2]
        self.hr_sta_ch17_avg = [2658, 2]
        self.hr_sta_ch17_sd = [2660, 2]
        self.hr_sta_ch17_max = [2662, 2]
        self.hr_sta_ch17_min = [2664, 2]
        self.hr_sta_ch18_avg = [2666, 2]
        self.hr_sta_ch18_sd = [2668, 2]
        self.hr_sta_ch18_max = [2670, 2]
        self.hr_sta_ch18_min = [2672, 2]
        self.hr_sta_ch19_avg = [2674, 2]
        self.hr_sta_ch19_sd = [2676, 2]
        self.hr_sta_ch19_max = [2678, 2]
        self.hr_sta_ch19_min = [2680, 2]
        self.hr_sta_ch20_avg = [2682, 2]
        self.hr_sta_ch20_sd = [2684, 2]
        self.hr_sta_ch20_max = [2686, 2]
        self.hr_sta_ch20_min = [2688, 2]
        self.hr_sta_ch21_avg = [2690, 2]
        self.hr_sta_ch21_sd = [2692, 2]
        self.hr_sta_ch21_max = [2694, 2]
        self.hr_sta_ch21_min = [2696, 2]
        self.hr_sta_ch22_avg = [2698, 2]
        self.hr_sta_ch22_sd = [2700, 2]
        self.hr_sta_ch22_max = [2702, 2]
        self.hr_sta_ch22_min = [2704, 2]
        self.hr_sta_ch23_avg = [2706, 2]
        self.hr_sta_ch23_sd = [2708, 2]
        self.hr_sta_ch23_max = [2710, 2]
        self.hr_sta_ch23_min = [2712, 2]
        self.hr_sta_ch24_avg = [2714, 2]
        self.hr_sta_ch24_sd = [2716, 2]
        self.hr_sta_ch24_max = [2718, 2]
        self.hr_sta_ch24_min = [2720, 2]
        self.hr_sta_ch25_avg = [2722, 2]
        self.hr_sta_ch25_sd = [2724, 2]
        self.hr_sta_ch25_max = [2726, 2]
        self.hr_sta_ch25_min = [2728, 2]
        self.hr_sta_ch26_avg = [2730, 2]
        self.hr_sta_ch26_sd = [2732, 2]
        self.hr_sta_ch26_max = [2734, 2]
        self.hr_sta_ch26_min = [2736, 2]
        # diagnostic data
        self.hr_diag_year = [3000, 1]
        self.hr_diag_month = [3001, 1]
        self.hr_diag_day = [3002, 1]
        self.hr_diag_hour = [3003, 1]
        self.hr_diag_minute = [3004, 1]
        self.hr_diag_second = [3005, 1]
        self.hr_diag_temp = [3006, 2]
        self.hr_diag_12v_bat = [3008, 2]
        self.hr_diag_12v_cur = [3010, 2]
        self.hr_diag_2v_bat = [3012, 2]
        self.hr_diag_5v_cur = [3014, 2]
        self.hr_diag_sd_inst = [3016, 1]
        self.hr_diag_sd_free = [3017, 2]
        self.hr_diag_sd_used = [3019, 2]


    def connect(self):
        """
        initialize self.ip, self.port, self.unit
        """
        from pymodbus.client.sync import ModbusTcpClient as ModbusClient

        self.client = ModbusClient(host=self.ip,port=self.port,unit=self.unit)
        print("Connecting to {0}... \t\t".format(self.ip), end="", flush=True)
        try:
            self.client.connect()
            if self.client.is_socket_open() == True:
                print("[OK]")
            else:
                self.client.connect()
                if self.client.is_socket_open != True:
                    raise ValueError('Could Not Connect to {0}'.format(self.ip))
        except Exception as e:
            self.e = e
            print("[FAILED]")
            print(self.e)
            

    def disconnect(self):
        print("Disconnecting from {0}... \t\t".format(self.ip), end="", flush=True)
        try:
            self.client.close()
            print("[OK]")
        except Exception as e:
            print("[ERROR]")
            print(e)


    def poll(self, interval=4, reconnect=True, 
             stat=True, rt=True, serial=False,
             diag=False, config=False,
             db='', save_to_db=False,
             echo=False):
        """
        regularly poll registers

        parameters : (default value)
              interval : seconds to wait between polls (4)
             reconnect : automatically reconnect on failure (True)
                  stat : poll statistical registers (True)
                    rt : poll real time registers (True)
                serial : poll serial registers (False)
                  diag : poll diagnostic registers (False)
                config : poll config registers (False)
                    db : sqlite3 db to save to ('')
            save_to_db : save to db? (False)
                  echo : print some data to console (False)

        returns register values as individual and packages arrays
        """
        from time import time, sleep
        i=0
        # set up database connection if save_to_db == True
        while True:
            poll_time = time()
            i += 1
            if self.e != '':
                if reconnect == True:
                    self.connect()
                else:
                    return "Disconnected from {0}, reconnect disabled".format(self.ip)
                self.e = ''

            if stat == True:
                self.return_stat_readings()
            if rt == True:
                self.return_rt_data_readings()
            if serial == True:
                self.return_rt_serial_readings()
            if diag == True:
                self.return_diag_readings()
            if config == True:
                self.return_config()

            if save_to_db == True:
                # do the db things
                pass

            if echo == True:
                if rt == True:
                    print("{0}\t{1}\t{2}\t{3}".format(i,self.date_time,self.rt_ch1,self.rt_ch13))
                else:
                    print("Poll # {0}".format(i))

            while time() < poll_time + interval:
                sleep(0.01)



    def return_diag_readings(self):
        """
        returns data from diagnostic registers
        """
        self.diag_year = self.read_single_register(self.hr_diag_year)
        self.diag_month = self.read_single_register(self.hr_diag_month)
        self.diag_day = self.read_single_register(self.hr_diag_day)
        self.diag_hour = self.read_single_register(self.hr_diag_hour)
        self.diag_minute = self.read_single_register(self.hr_diag_minute)
        self.diag_second = self.read_single_register(self.hr_diag_second)
        self.diag_temp = self.read_single_register(self.hr_diag_temp)
        self.diag_12v_bat = self.read_single_register(self.hr_diag_12v_bat)
        self.diag_12v_cur = self.read_single_register(self.hr_diag_12v_cur)
        self.diag_2v_bat = self.read_single_register(self.hr_diag_2v_bat)
        self.diag_5v_cur = self.read_single_register(self.hr_diag_5v_cur)
        self.diag_sd_inst = self.read_single_register(self.hr_diag_sd_inst)
        self.diag_sd_free = self.read_single_register(self.hr_diag_sd_free)
        self.diag_sd_used = self.read_single_register(self.hr_diag_sd_used)


    def return_rt(self):
        self.rt_year = self.read_single_register(self.hr_rt_year)
        self.rt_month = self.read_single_register(self.hr_rt_month)
        self.rt_day = self.read_single_register(self.hr_rt_day)
        self.rt_hour = self.read_single_register(self.hr_rt_hour)
        self.rt_minute = self.read_single_register(self.hr_rt_minute)
        self.rt_second = self.read_single_register(self.hr_rt_second)
        self.time = ":".join(map(str, [self.rt_hour,self.rt_minute,self.rt_second]))
        self.date = "-".join(map(str, [self.rt_year,self.rt_month,self.rt_day]))
        self.date_time = " ".join([self.date,self.time])


    def return_rt_data_readings(self):
        """
        returns real time data from all channels
        """
        self.return_rt()
        self.rt_ch1 = self.read_single_register([self.hr_rt_channel_readings[0]+0,2])
        self.rt_ch2 = self.read_single_register([self.hr_rt_channel_readings[0]+2,2])
        self.rt_ch3 = self.read_single_register([self.hr_rt_channel_readings[0]+4,2])
        self.rt_ch4 = self.read_single_register([self.hr_rt_channel_readings[0]+6,2])
        self.rt_ch5 = self.read_single_register([self.hr_rt_channel_readings[0]+8,2])
        self.rt_ch6 = self.read_single_register([self.hr_rt_channel_readings[0]+10,2])
        self.rt_ch7 = self.read_single_register([self.hr_rt_channel_readings[0]+12,2])
        self.rt_ch8 = self.read_single_register([self.hr_rt_channel_readings[0]+14,2])
        self.rt_ch9 = self.read_single_register([self.hr_rt_channel_readings[0]+16,2])
        self.rt_ch10 = self.read_single_register([self.hr_rt_channel_readings[0]+18,2])
        self.rt_ch11 = self.read_single_register([self.hr_rt_channel_readings[0]+20,2])
        self.rt_ch12 = self.read_single_register([self.hr_rt_channel_readings[0]+22,2])
        self.rt_ch13 = self.read_single_register([self.hr_rt_channel_readings[0]+24,2])
        self.rt_ch14 = self.read_single_register([self.hr_rt_channel_readings[0]+26,2])
        self.rt_ch15 = self.read_single_register([self.hr_rt_channel_readings[0]+28,2])
        self.rt_ch16 = self.read_single_register([self.hr_rt_channel_readings[0]+30,2])
        self.rt_ch17 = self.read_single_register([self.hr_rt_channel_readings[0]+32,2])
        self.rt_ch18 = self.read_single_register([self.hr_rt_channel_readings[0]+34,2])
        self.rt_ch19 = self.read_single_register([self.hr_rt_channel_readings[0]+36,2])
        self.rt_ch20 = self.read_single_register([self.hr_rt_channel_readings[0]+38,2])
        self.rt_ch21 = self.read_single_register([self.hr_rt_channel_readings[0]+40,2])
        self.rt_ch22 = self.read_single_register([self.hr_rt_channel_readings[0]+42,2])
        self.rt_ch23 = self.read_single_register([self.hr_rt_channel_readings[0]+44,2])
        self.rt_ch24 = self.read_single_register([self.hr_rt_channel_readings[0]+46,2])
        self.rt_ch25 = self.read_single_register([self.hr_rt_channel_readings[0]+48,2])
        self.rt_ch26 = self.read_single_register([self.hr_rt_channel_readings[0]+50,2])
        self.rt_ch_all = [self.date_time,
                          self.rt_ch1, self.rt_ch2, self.rt_ch3, self.rt_ch4, self.rt_ch5,
                          self.rt_ch6, self.rt_ch7, self.rt_ch8, self.rt_ch9, self.rt_ch10,
                          self.rt_ch11, self.rt_ch12, self.rt_ch13, self.rt_ch14, self.rt_ch15,
                          self.rt_ch16, self.rt_ch17, self.rt_ch18, self.rt_ch19, self.rt_ch20,
                          self.rt_ch21, self.rt_ch22, self.rt_ch23, self.rt_ch24, self.rt_ch25]


    def return_rt_serial_readings(self):
        """
        returns real time data from all channels
        """
        self.rt_ch26 = self.read_single_register([self.hr_rt_channel_readings[0]+52,2])
        self.rt_ch27 = self.read_single_register([self.hr_rt_channel_readings[0]+54,2])
        self.rt_ch28 = self.read_single_register([self.hr_rt_channel_readings[0]+56,2])
        self.rt_ch29 = self.read_single_register([self.hr_rt_channel_readings[0]+58,2])
        self.rt_ch30 = self.read_single_register([self.hr_rt_channel_readings[0]+60,2])


    def return_stat_readings(self):
        """
        poll statistical registers
        """
        pass


    def return_config(self):
        """
        returns data from config registers
        """
        pass


    def read_registers(self, list_of_registers_to_read):
        """
        returns array of converted values
        """
        return_values = []
        for reg in list_of_registers_to_read:
            try:
                return_values.append(self.read_single_register(reg))
            except:
                return_values.append(9999)
        return return_values


    def read_single_register(self, register):
        """
        wrapper for pymodbus, returns single value
        """       
        import struct
        try:
            rr = self.client.read_holding_registers(register[0], register[1], unit=1)
            if register[1] == 2:
                raw = struct.pack('>HH', rr.registers[0], rr.registers[1])
                flo = struct.unpack('>f', raw)[0]
            elif register[1] > 2:
                flo = []
                for i in range(0,register[1],2):
                    raw = struct.pack('>HH', rr.registers[0], rr.registers[1])
                    temp = struct.unpack('>f', raw)[0]
                    flo.append(temp)
            else:
                flo = rr.registers[0]
            #values = rr.registers
            return flo
        except Exception as e:
            self.e = e
            return 9999


