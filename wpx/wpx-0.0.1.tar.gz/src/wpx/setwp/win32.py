# -*- coding: utf8 -*-
# Copyright (c) 2020 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from wpx.setwp import SetWallpaperOptions
import ctypes
import logging
import os

# See https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfoa
SPI_SETDESKWALLPAPER = 0x0014


def set_wallpaper(options: SetWallpaperOptions):
  if options.desktop:
    cs = ctypes.c_buffer(os.path.abspath(options.path).encode())
    ok = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, cs, 0)
    if not ok:
      raise RuntimeError('Desktop wallpaper could not be set.')
  if options.login:
    logging.warning('setting the login wallpaper is not supported on windows')
