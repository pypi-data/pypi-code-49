motor_instance = None

def get_motor(pin):
    """Get static reference to servo motor.

    Parameters:
      pint (int):       Digital connection port (range: [2, 8])
    """

    global motor_instance

    if motor_instance is None:
        from . import arduino, servo

        motor_instance = servo.Servo(pin, arduino().connection)

    return motor_instance

def move(pin, angle):
    """Move servo motor to given angle (in degrees)

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])
      angle (int):      Final servo position (range: [0 180])
    """

    get_motor(pin).write(angle)
    from time import sleep
    sleep(0.5)

def read(pin):
    """Check position of servo motor

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])

    Returns:         Servo motor position (0–180).
    """

    return get_motor(pin).read()
    
