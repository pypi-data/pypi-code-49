from gbrpi.electronics.gpio_device import GPIODevice


class LedRing(GPIODevice):
    def on(self):
        """
        turns on this led ring
        """
        self.set_power(255)

    def off(self):
        """
        turns off this led ring
        """
        self.set_power(0)
