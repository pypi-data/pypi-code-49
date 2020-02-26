import pigpio as pg


class GPIODevice:
    """
    a GPIO single port device connection

    :param port: the GPIO port
    :param pi: optional, a pigpio pi, if not given the constructor will create a new one
    """
    def __init__(self, port: int, pi=None):
        if pi is None:
            pi = pg.pi()
            pass
        self.pi = pi
        self.port = port

    def set_power(self, power: int):
        """
        sets the pwm dutycycle of this device

        :param power: the power [0 - 255]
        """
        self.pi.set_PWM_dutycycle(self.port, power)

    def get_power(self) -> int:
        """
        gets the pwm dutycycle of this device

        :return: the pwm dutycycle [0 - 255]
        """
        return self.pi.get_PWM_dutycycle(self.port)
