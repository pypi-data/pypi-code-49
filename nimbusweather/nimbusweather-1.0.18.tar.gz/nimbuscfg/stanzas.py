#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com> and
#                            Matthew Wall
#
#    See the file LICENSE.txt for your full rights.
#
"""Utilities for managing the config file"""

config_stanzas = {
    'AcuRite':
        """
        [AcuRite]
            # This section is for AcuRite weather stations.

            # The station model, e.g., 'AcuRite 01025' or 'AcuRite 02032C'
            model = 'AcuRite 01035'
        """,

    'CC3000':
        """
        [CC3000]
            # This section is for RainWise MarkIII weather stations and CC3000 logger.

            # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
            port = /dev/ttyUSB0

            # The station model, e.g., CC3000 or CC3000R
            model = CC3000
        """,

    'FineOffsetUSB':
        """
        [FineOffsetUSB]
            # This section is for the Fine Offset series of weather stations.

            # The station model, e.g., WH1080, WS1090, WS2080, WH3081
            model = WS2080

            # How often to poll the station for data, in seconds
            polling_interval = 60
        """,

    'Simulator':
        """
        [Simulator]
            # This section is for the nimbus weather station simulator

            # The time (in seconds) between LOOP packets.
            loop_interval = 2.5

            # The simulator mode can be either 'simulator' or 'generator'.
            # Real-time simulator. Sleep between each LOOP packet.
            mode = simulator

            # Generator.  Emit LOOP packets as fast as possible (useful for testing).
            #mode = generator

            # The start time. If not specified, the default is to use the present time.
            #start = 2011-01-01 00:00
        """,

    'TE923':
        """
        [TE923]
            # This section is for the Hideki TE923 series of weather stations.

            # The station model, e.g., 'Meade TE923W' or 'TFA Nexus'
            model = TE923

            # The default configuration associates the channel 1 sensor with outTemp
            # and outHumidity.  To change this, or to associate other channels with
            # specific columns in the database schema, use the following maps.
            [[sensor_map]]
                # Map the remote sensors to columns in the database schema.
                outTemp =     t_1
                outHumidity = h_1
                extraTemp1 =  t_2
                extraHumid1 = h_2
                extraTemp2 =  t_3
                extraHumid2 = h_3
                extraTemp3 =  t_4
                # WARNING: the following are not in the default schema
                extraHumid3 = h_4
                extraTemp4 =  t_5
                extraHumid4 = h_5

            [[battery_map]]
                txBatteryStatus =      batteryUV
                windBatteryStatus =    batteryWind
                rainBatteryStatus =    batteryRain
                outTempBatteryStatus = battery1
                # WARNING: the following are not in the default schema
                extraBatteryStatus1 =  battery2
                extraBatteryStatus2 =  battery3
                extraBatteryStatus3 =  battery4
                extraBatteryStatus4 =  battery5
        """,

    'Ultimeter':
        """
        [Ultimeter]
            # This section is for the PeetBros Ultimeter series of weather stations.

            # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
            port = /dev/ttyUSB0

            # The station model, e.g., Ultimeter 2000, Ultimeter 100
            model = Ultimeter
        """,

    'Vantage':
        """
        [Vantage]
            # This section is for the Davis Vantage series of weather stations.

            # Connection type: serial or ethernet
            #  serial (the classic VantagePro)
            #  ethernet (the WeatherLinkIP)
            type = serial

            # If the connection type is serial, a port must be specified:
            #   Debian, Ubuntu, Redhat, Fedora, and SuSE:
            #     /dev/ttyUSB0 is a common USB port name
            #     /dev/ttyS0   is a common serial port name
            #   BSD:
            #     /dev/cuaU0   is a common serial port name
            port = /dev/ttyUSB0

            # If the connection type is ethernet, an IP Address/hostname is required:
            host = 1.2.3.4

            ######################################################
            # The rest of this section rarely needs any attention.
            # You can safely leave it "as is."
            ######################################################

            # Serial baud rate (usually 19200)
            baudrate = 19200

            # TCP port (when using the WeatherLinkIP)
            tcp_port = 22222

            # TCP send delay (when using the WeatherLinkIP):
            tcp_send_delay = 1

            # The id of your ISS station (usually 1)
            iss_id = 1

            # How long to wait for a response from the station before giving up (in
            # seconds; must be greater than 2)
            timeout = 5

            # How long to wait before trying again (in seconds)
            wait_before_retry = 1.2

            # How many times to try before giving up:
            max_tries = 4
        """,

    'WMR100':
    """
       [WMR100]
            # This section is for the Oregon Scientific WMR100

            # The station model, e.g., WMR100, WMR100N, WMRS200
            model = WMR100

            # How long a wind record can be used to calculate wind chill (in seconds)
            stale_wind = 30
        """,

    'WMR200':
        """
        [WMR200]
            # This section is for the Oregon Scientific WMR200

            # The station model, e.g., WMR200, WMR200A, Radio Shack W200
            model = WMR200
        """,

    'WMR9x8':
        """
        [WMR9x8]
            # This section is for the Oregon Scientific WMR918/968

            # Connection type. For now, 'serial' is the only option.
            type = serial

            # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
            port = /dev/ttyUSB0

            # The station model, e.g., WMR918, Radio Shack 63-1016
            model = WMR968
        """,

    'WS1':
        """
        [WS1]
            # This section is for the ADS WS1 series of weather stations.

            # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
            port = /dev/ttyUSB0
        """,

    'WS23xx':
        """
        [WS23xx]
            # This section is for the La Crosse WS-2300 series of weather stations.

            # Serial port such as /dev/ttyS0, /dev/ttyUSB0, or /dev/cuaU0
            port = /dev/ttyUSB0

            # The station model, e.g., 'LaCrosse WS2317' or 'TFA Primus'
            model = LaCrosse WS23xx
        """,

    'WS28xx':
        """
        [WS28xx]
            # This section is for the La Crosse WS-2800 series of weather stations.

            # Radio frequency to use between USB transceiver and console: US or EU
            # US uses 915 MHz, EU uses 868.3 MHz.  Default is US.
            transceiver_frequency = US

            # The station model, e.g., 'LaCrosse C86234' or 'TFA Primus'
            model = LaCrosse WS28xx
        """
}
