import pyautogui as ag
from time import sleep

__version__ = "0.4.0-beta.1"


class Cursor(object):
    def to(self, x, y):
        ag.moveTo(x, y)

    def click(self):
        ag.click()

    @property
    def position(self):
        return ag.position()

    def drag_to(self, x, y, speed=0.1, button="left"):
        ag.dragTo(x, y, speed, button=button)

    def drag_rel(self, x, y, speed=0.1, button="left"):
        ag.dragRel(x, y, speed, button=button)


class Keyboard(object):
    def press(self, key, times=1):
        for x in range(0, times):
            ag.press(key)
        return self

    def write(self, text):
        ag.typewrite(text)
        return self

    def writeline(self, text):
        ag.typewrite(text)
        self.enter()
        return self

    def tab(self, times=1):
        self.press("tab")
        return self

    def enter(self, times=1):
        self.press("enter", times)
        return self

    def pagedown(self, times=1):
        self.press("pagedown", times)
        return self

    def pageup(self, times=1):
        self.press("pageup", times)
        return self

    def esc(self, times=1):
        self.press("esc", times)
        return self

    def ctrl(self, key):
        ag.hotkey("ctrl", key)
        return self

    def f(self, number, times=1):
        self.press(f"f{number}", times)
        return self

    def down(self, times=1):
        self.press("down", times)
        return self

    def up(self, times=1):
        self.press("up", times)
        return self

    def right(self, times=1):
        self.press("right", times)
        return self

    def left(self, times=1):
        self.press("left", times)
        return self

    def delete(self, times=1):
        self.press("delete", times)
        return self

    def add(self, times=1):
        self.press("add", times)
        return self

    def subtract(self, times=1):
        self.press("subtract", times)
        return self

    def multiply(self, times=1):
        self.press("multiply", times)
        return self

    def divide(self, times=1):
        self.press("divide", times)
        return self


class MsgBox(object):
    @classmethod
    def confirm(cls, msg):
        return ag.confirm(msg)

    @classmethod
    def alert(cls, msg):
        return ag.alert(msg)

    @classmethod
    def input(cls, msg, title="", default=None):
        return ag.prompt(text=msg, title=title, default=default)


class Automator(object):
    def __init__(self):
        self.cursor = self.cr = Cursor()
        self.keyboard = self.kb = Keyboard()
        self.msgbox = self.mb = MsgBox()
        self.failsafe = True

    @property
    def failsafe(self):
        return ag.FAILSAFE

    @failsafe.setter
    def failsafe(self, value):
        ag.FAILSAFE = value

    @property
    def throttle(self):
        return ag.PAUSE

    @throttle.setter
    def throttle(self, value):
        ag.PAUSE = float(value)

    def request_throttle(self):
        speed = input("  Throttle input (0.1-2.0): ")
        self.throttle = float(speed)

    def pause(self, seconds):
        sleep(seconds)

    def locate_image(self, image_file, region=None):
        return list(ag.locateAllOnScreen(image_file, region=region))

    def image_visible(self, image_file, region=None):
        return len(list(self.locate_image(image_file, region=region)))

    def run(self, macro, *args, **kwargs):
        macro(self, *args, *kwargs)


Automater = Automator
