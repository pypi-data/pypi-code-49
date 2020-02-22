from time import strftime, localtime

import colored

__all__ = ["styles"]


class Styles:
    __slots__ = ["_styles", "default", "timestring", "timestampCodes"]

    def __init__(self):
        self._styles = {}
        self.timestring = "%d %b %H:%M:%S"
        self.timestampCodes = colored.fg("magenta")

    def create(self, name, *, fg = None, bg = None, attr = None):
        """Create a custom style"""
        name = name.lower()
        codes = ""
        if fg is not None:
            codes += colored.fg(fg)
        if bg is not None:
            codes += colored.bg(bg)
        if attr is not None:
            codes += colored.attr(attr)
        self._styles[name] = codes

    def format(self, message, *, style="default", showtime=False):
        """Format a message in the requested style"""
        style = style.lower()
        if style not in self._styles:
            raise ValueError(f"Unknown style: {style}")
        formatted = ""
        if showtime:
            formatted += self._timestamp()
        formatted = self._styles.get(style, "") + message + colored.attr("reset")
        return formatted

    def print(self, *args, **kwargs):
        """Print a message in the requested style"""
        print(self.format(*args, **kwargs))

    def _timestamp(self):
        """Color styling for terminal messages"""
        t = localtime()
        return self.timestampCodes + strftime(f"{self.timestring} | ", t) + colored.attr("reset")

    def __getattr__(self, name):
        name = name.lower()
        if name not in self._styles:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")
        return lambda message: self.print(message, style=name)

    def __str__(self):
        return "styles: " + (" ".join(self.format(level, style=level) for level in self._styles.keys()))


styles = Styles()
