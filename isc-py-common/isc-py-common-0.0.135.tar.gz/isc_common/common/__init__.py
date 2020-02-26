from typing import Text


def getOrElse(default, value):
    if value:
        return value
    else:
        return default


def blinkString(text, blink=True, color="black", bold=False) -> Text:
    if blink:
        res = f'<div class="blink"><strong><font color="{color}"</font>{text}</strong></div>'
    else:
        res = f'<div><strong><font color="{color}"</font>{text}</strong></div>'

    if bold:
        return f'<b>{res}</b>'
    else:
        return res
