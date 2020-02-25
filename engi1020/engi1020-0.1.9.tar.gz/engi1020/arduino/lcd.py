lcd_instance = None

def get_lcd():
    """Get static reference to LCD display."""

    global lcd_instance

    if lcd_instance is None:
        from . import arduino, rgb_lcd

        lcd_instance = rgb_lcd.rgb_lcd(arduino().connection)
        lcd_instance.setRGB(255, 255, 255)

    return lcd_instance

def clear():
    """Clear all text from the LCD screen and reset the cursor to the
    top-left corner of the screen.
    """
 
    get_lcd().clear()

def move_cursor(row, col):
    """Move the cursor to a specific location.

    Parameters:
      row (int):       Row on the LCD screen (range: [0, 1])
      col (int):       Column on the LCD screen (range: [0, 15])
    """
    get_lcd().moveCursor(col, row)

def print(value):
    """Print a value to the LCD screen.

    Parameters:
      value:    Any value, of any type.
    """
    get_lcd().printString(str(value))

def hsv(hue, saturation, value):
    """Change the LCD background colour by HSV value.

    Parameters:
      hue (float):           colour (between 0 and 1)
      saturation (float):    vibrance (between 0 and 1)
      value (int):           brightness (between 0 and 255)
    """
    import colorsys
    red, green, blue = colorsys.hsv_to_rgb(hue, saturation, value)
    rgb(red, green, blue)

def rgb(red, green, blue):
    """Change the LCD background colour by RGB value.

    Parameters:
      red (int):             amount of red to display (0–255)
      green (int):           amount of green to display (0–255)
      blue (int):            amount of blue to display (0–255)
    """
    get_lcd().setRGB(red, green, blue)
