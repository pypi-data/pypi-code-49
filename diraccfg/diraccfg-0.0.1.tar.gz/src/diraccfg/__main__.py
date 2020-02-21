from __future__ import absolute_import
from __future__ import print_function

import argparse
import json
import os
import sys
import re

from .cfg import CFG


def parseArgs():
  parser = argparse.ArgumentParser(description='Parser for DIRAC cfg files')
  subparsers = parser.add_subparsers(help='Actions to run with the ')

  parserJson = subparsers.add_parser('as-json', help='Dump the entire configuration as JSON')
  parserJson.add_argument('cfgfile')
  parserJson.set_defaults(func=lambda a: dumpAsJson(a.cfgfile))

  parserSort = subparsers.add_parser(
      'sort-versions',
      help='Read JSON from stdin and prints JSON list of sorted version numbers'
  )
  parserSort.add_argument('--allow-pre-releases', action='store_true')
  parserSort.set_defaults(func=lambda a: sortVersions(a.allow_pre_releases))

  args = parser.parse_args()
  args.func(args)
  # Explicitly exit to make testing easier
  sys.exit(0)


def dumpAsJson(cfgFilename):
  if not os.path.isfile(cfgFilename):
    sys.stderr.write('ERROR: %s does not exist\n' % cfgFilename)
    sys.exit(1)
  res = CFG().loadFromFile(cfgFilename)
  print(json.dumps(res.getAsDict()))


def sortVersions(allow_pre_releases=False):
  try:
    objs = json.loads(sys.stdin.read())
  except getattr(json, 'JSONDecodeError', ValueError):
    sys.stderr.write('ERROR: Failed to parse standard input as JSON\n')
    sys.exit(3)

  parsedVersions = {}
  for obj in objs:
    match = re.match(r"^v(?P<major>\d+)r(?P<minor>\d+)(?:p(?P<patch>\d+))?(?:-pre(?P<pre>\d+))?$", obj)
    if match:
      v = match.groupdict()
      if not allow_pre_releases and v['pre']:
        continue
      if v['pre'] is None:
        v['pre'] = sys.maxsize
      v = {k: 0 if v is None else int(v) for k, v in v.items()}
      parsedVersions[obj] = (v['major'], v['minor'], v['patch'], v['pre'])
    elif obj not in ('integration', 'devel', 'master'):
      sys.stderr.write('WARN: Unexpected version string %r\n' % obj)

  print(json.dumps(sorted(parsedVersions, key=parsedVersions.get, reverse=True)))


if __name__ == '__main__':
  parseArgs()   # pragma: no cover
