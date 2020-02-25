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

from nr.databind.core import ObjectMapper
from nr.databind.json import JsonModule
from typing import Optional, BinaryIO
from wpx.providers import IImageProvider
from wpx.setwp import SetWallpaperOptions, set_wallpaper
import argparse
import logging
import os
import sys
import yaml

logger = logging.getLogger(__name__)
mapper = ObjectMapper(JsonModule())


def save_to(filename: str, src: BinaryIO, chunk_size: int = 1024*16):
  """ Saves the contents from *src* to the specified *filename*. """

  with open(filename, 'wb') as dst:
    while True:
      chunk = src.read(chunk_size)
      dst.write(chunk)
      if not chunk:
        break


def get_argument_parser(prog: Optional[str]):
  parser = argparse.ArgumentParser(prog=prog)
  parser.add_argument('provider', help='The name of the image provider.')
  parser.add_argument('config', nargs='?', help='Inline JSON configuration of the provider.')
  parser.add_argument('-d', '--directory', help='The output directory.')
  parser.add_argument('--overwrite', action='store_true', help='Overwrite output file(s).')
  parser.add_argument('--daily', action='store_true', help='Get the daily image.')
  parser.add_argument('--random', action='store_true', help='Get a random image.')
  parser.add_argument('--set-desktop', action='store_true', help='Set as desktop wallpaper.')
  parser.add_argument('--set-login', action='store_true', help='Set as login wallpaper.')
  return parser


def main(argv=None, prog=None):
  logging.basicConfig(format='%(message)s', level=logging.INFO)

  parser = get_argument_parser(prog)
  args = parser.parse_args(argv)

  if not args.daily and not args.random:
    parser.error('no action specified, try --daily or --random')

  if args.directory:
    os.chdir(args.directory)

  payload = {'type': args.provider}
  payload.update(yaml.safe_load(args.config or '{}'))
  provider = mapper.deserialize(payload, IImageProvider)

  try:
    if args.daily:
      image = provider.get_daily_image()
    elif args.random:
      image = provider.get_random_image()
  except NotImplementedError:
    parser.error('{}: unsupported operation'.format(args.provider))

  if args.overwrite or not os.path.isfile(image.filename):
    with image.open() as src:
      save_to(image.filename, src)
  else:
    logging.info('note: "%s" already exists', image.filename)

  # Print the absolute path to the saved file so that scripts can get it.
  print(os.path.abspath(image.filename))

  if args.set_desktop or args.set_login:
    options = SetWallpaperOptions(image.filename,
      desktop=args.set_desktop, login=args.set_login)
    try:
      set_wallpaper(options)
    except NotImplementedError:
      print('error: setting wallpaper is not supported on this system.',
            file=sys.stderr)


_entry_main = lambda: exit(main())

if __name__ == '__main__':
  _entry_main()
