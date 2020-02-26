#!/usr/bin/python3
import pathlib
import shutil
import sys

try:
    from .__id__ import ID
except ImportError:
    src = pathlib.Path(__file__).parents[1].joinpath("__id__.py")
    dst = pathlib.Path(__file__).parent.joinpath("__id__.py")
    shutil.copyfile(src, dst)
    from __id__ import ID


def main():
    try:
        app = __import__(f"{ID}.main", fromlist=["main"])
    except ImportError:
        import main as app
    app.main()


if __name__ == '__main__':
    main()
