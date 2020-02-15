from typing import Text


def getOrElse(default, value):
    if value:
        return value
    else:
        return default


def blinkString(text, blink=True, color="black") -> Text:
    if blink:
        return f'<div class="blink"><strong><font color="{color}"</font>${text}</strong></div>'
    else:
        return text
