#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com> and
#                            Matthew Wall
#
#    See the file LICENSE.txt for your full rights.
#
"""Utilities for managing the config file"""

from nimbusdrivers import get_driver_info


def prompt_for_info():
    print "Specify latitude in decimal degrees, negative for south."
    lat = prompt_with_limits("latitude", -90, 90)
    print "Specify longitude in decimal degrees, negative for west."
    lon = prompt_with_limits("longitude", -180, 180)

    return {'latitude': lat,
            'longitude': lon}


def prompt_with_limits(prompt, low_limit=None, high_limit=None):
    """Ask the user for an input with an optional default value. The
    returned value must lie between optional upper and lower bounds.

    prompt: A string to be used for a prompt.

    default: A default value. If the user simply hits <enter>, this
    is the value returned. Optional.

    low_limit: The value must be equal to or greater than this value.
    Optional.

    high_limit: The value must be less than or equal to this value.
    Optional.
    """
    msg = "%s: " % prompt
    value = None
    while not value:
        value = raw_input(msg).strip()
        if value:
            try:
                v = float(value)
                if (low_limit is not None and v < low_limit) or \
                        (high_limit is not None and v > high_limit):
                    value = None
            except (ValueError, TypeError):
                value = None

    return value


def prompt_with_options(prompt, default=None, options=None):
    """Ask the user for an input with an optional default value.

    prompt: A string to be used for a prompt.

    default: A default value. If the user simply hits <enter>, this
    is the value returned. Optional.

    options: A list of possible choices. The returned value must be in
    this list. Optional."""

    msg = "%s [%s]: " % (prompt, default) if default is not None else "%s: " % prompt
    value = None
    while value is None:
        value = raw_input(msg).strip()
        if value:
            if options and value not in options:
                value = None
        elif default is not None:
            value = default

    return value


def prompt_for_driver_settings(driver_name):
    """Let the driver prompt for any required settings."""
    return driver_prompts[driver_name]()


def prompt_for_wunderground():
    ans = None

    while ans is None:
        msg = "configure weather underground? [y]: "
        ans = raw_input(msg).strip()

        if ans == "n" or ans == "N":
            return {}

        if ans and ans != "y" and ans != "Y":
            ans = None

    station = None

    while not station:
        msg = "station ID: "
        station = raw_input(msg).strip()

    password = None

    while not password:
        msg = "password: "
        password = raw_input(msg).strip()

    return {'station': station,
            'password': password}


def prompt_for_weather_services():
    _dict = dict()
    _dict['Wunderground'] = prompt_for_wunderground()
    return _dict


def prompt_for_driver():
    """Get the information about each driver, return as a dictionary."""

    info = get_driver_info()
    keys = sorted(info)
    dflt_idx = None
    print "Installed nimbusdrivers include:"
    for i, d in enumerate(keys):
        print " %2d) %-15s %-25s %s" % (i, info[d].get('driver_name', '?'),
                                        "(%s)" % d, info[d].get('status', ''))
    msg = "choose a driver: "
    ans = None
    while ans is None:
        ans = raw_input(msg).strip()
        if not ans:
            ans = dflt_idx
        try:
            idx = int(ans)
            if not 0 <= idx < len(keys):
                ans = None
        except (ValueError, TypeError):
            ans = None
    return info[keys[idx]]


def vantage_prompt():
    settings = dict()
    print "Specify the hardware interface, either 'serial' or 'ethernet'."
    print "If the station is connected by serial, USB, or serial-to-USB"
    print "adapter, specify serial.  Specify ethernet for stations with"
    print "WeatherLinkIP interface."
    settings['type'] = prompt_with_options('type', 'serial', ['serial', 'ethernet'])
    if settings['type'] == 'serial':
        print "Specify a port for stations with a serial interface, for"
        print "example /dev/ttyUSB0 or /dev/ttyS0."
        settings['port'] = prompt_with_options('port', '/dev/ttyUSB0')
    else:
        print "Specify the IP address (e.g., 192.168.0.10) or hostname"
        print "(e.g., console or console.example.com) for stations with"
        print "an ethernet interface."
        settings['host'] = prompt_with_options('host')
    return settings


def no_prompt():
    return {}


def serial_port_prompt():
    print "Specify the serial port on which the station is connected, for"
    print "example /dev/ttyUSB0 or /dev/ttyS0."
    port = prompt_with_options('port', '/dev/ttyUSB0')
    return {'port': port}


def ws28xx_prompt():
    print "Specify the frequency used between the station and the"
    print "transceiver, either 'US' (915 MHz) or 'EU' (868.3 MHz)."
    freq = prompt_with_options('frequency', 'US', ['US', 'EU'])
    return {'transceiver_frequency': freq}


driver_prompts = {
    'AcuRite': no_prompt,
    'Vantage': vantage_prompt,
    'Simulator': no_prompt,
    'CC3000': serial_port_prompt,
    'FineOffsetUSB': no_prompt,
    'TE923': no_prompt,
    'Ultimeter': serial_port_prompt,
    'WMR100': no_prompt,
    'WMR200': no_prompt,
    'WMR9x8': serial_port_prompt,
    'WS1': serial_port_prompt,
    'WS23xx': serial_port_prompt,
    'WS28xx': ws28xx_prompt,
}
