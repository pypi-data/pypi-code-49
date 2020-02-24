import os

from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

# Ctrl c will quit aplication. Async threads can terminated only with os.exit(0)
@bindings.add('c-q')
@bindings.add('c-c')
def _(event):
    print("\r\nQuitting (CTRL+C or CTRL+Q)")
    quit()


def quit():
    os._exit(0)
