"""CLI for Arduino API wrapper.
"""

import click

from . import *


@click.group()
def cli():
    pass

@cli.group()
def analog():
    """Commands to interact with analog pins."""
    pass

@analog.command('read')
@click.argument('pin', type=int)
def aread(pin):
    """Read a value from an analog pin."""
    print(analog_read(pin))

@cli.group()
def digital():
    """Commands to interact with digital pins."""
    pass

@digital.command('read')
@click.argument('pin', type=int)
def dread(pin):
    """Read a value from a digital pin."""
    print(digital_read(pin))


lcd_instance = None

def get_lcd():
    global lcd_instance

    if lcd_instance is None:
        from . import rgb_lcd
        lcd_instance = rgb_lcd.rgb_lcd(arduino().connection)
        lcd_instance.setRGB(255, 255, 255)

    return lcd_instance


@cli.group()
def lcd():
    """Commands to interact with an RGB LCD screen."""

@lcd.command('print')
@click.argument('message')
def lcd_print_message(message):
    lcd_clear()
    lcd_print(message)

@lcd.command()
@click.argument('hue', type=int)
@click.argument('saturation', type=float, default=1)
@click.argument('value', type=float, default=1)
def hsv(hue, saturation, value):
    """Set LCD background colour by hue, saturation and value."""
    lcd_hsv(hue / 360, saturation, value)

@lcd.command()
@click.argument('red', type=int)
@click.argument('green', type=int)
@click.argument('blue', type=int)
def rgb(red, green, blue):
    lcd_rgb(red, green, blue)
