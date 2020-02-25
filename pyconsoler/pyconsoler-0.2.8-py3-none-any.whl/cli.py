import logging
from pyconsoler import const
from pyconsoler.const import COLOR_ERROR
from pyconsoler.output import _out, bordered_text, prt

_LOGGER = logging.getLogger(__name__)


def main():
    itms = dir(const)
    for itm in itms:
        if itm.startswith("COLOR"):
            _out(f"This is color: {itm}", color=getattr(const, itm))

    print("")

    prt(bordered_text("This is bordered text"))

    prt(bordered_text(f"Bordered text in COLOR_ERROR"),color=COLOR_ERROR)

if __name__ == "__main__":
    main()
