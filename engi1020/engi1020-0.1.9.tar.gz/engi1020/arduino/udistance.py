udistance_instance = None

def get_udistance(pin):
    """Get static reference to ultrasonic distance sensor.

    Parameters:
      pint (int):       Digital connection port (range: [2, 8])
    """

    global udistance_instance

    if udistance_instance is None:
        from . import arduino, ultrasonic

        udistance_instance = ultrasonic.Ultrasonic(pin, arduino().connection)

    return udistance_instance

def get_distance(pin):
    """Find sensed distance in cm

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])
    """

    return get_udistance(pin).get_distance()
