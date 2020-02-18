# MIT License
#
# Copyright (c) 2018 Antoine Busque
# Copyright (c) 2018-2020 Philippe Proulx
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import json
import operator
import os.path
import random
import sys
import unicodedata
import pkg_resources
import qngng
import enum
import re


@enum.unique
class _Gender(enum.Enum):
    MALE = 1
    FEMALE = 2


class _PartialName:
    def __init__(self, name, gender=None):
        self._name = name
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender


class _FullName:
    def __init__(self, name, surname, gender):
        self._name = name
        self._surname = surname
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def gender(self):
        return self._gender


def _cat_file_to_objs(cat_filename, create_obj_func):
    path = os.path.join('cats', cat_filename) + '.json'
    path = pkg_resources.resource_filename(__name__, path)

    with open(path) as f:
        entries = json.load(f)

    objs = []

    for entry in entries:
        name = entry.get('name')
        surname = entry.get('surname')
        objs.append(create_obj_func(name, surname))

    return objs


def _random_std_fullname(gender):
    name_objs = []

    if gender is None or gender == _Gender.MALE:
        name_objs += _cat_file_to_objs('std-names-m',
                                       lambda n, s: _PartialName(n, _Gender.MALE))

    if gender is None or gender == _Gender.FEMALE:
        name_objs += _cat_file_to_objs('std-names-f',
                                       lambda n, s: _PartialName(n, _Gender.FEMALE))

    surname_objs = _cat_file_to_objs('std-surnames',
                                     lambda n, s: _PartialName(s))
    rand_name_obj = random.choice(name_objs)
    rand_surname_obj = random.choice(surname_objs)
    return _FullName(rand_name_obj.name, rand_surname_obj.name,
                     rand_name_obj.gender)


def _random_cat_fullname(cat_name, gender):
    assert(cat_name != 'std')

    base_cats = {
        'uda': ['uda-actors', 'uda-hosts', 'uda-singers'],
        'uda-actors': ['uda-actors'],
        'uda-hosts': ['uda-hosts'],
        'uda-singers': ['uda-singers'],
    }[cat_name]

    objs = []

    for base_cat in base_cats:
        if gender is None or gender == _Gender.MALE:
            objs += _cat_file_to_objs(base_cat + '-m',
                                      lambda n, s: _FullName(n, s, _Gender.MALE))

        if gender is None or gender == _Gender.FEMALE:
            objs += _cat_file_to_objs(base_cat + '-f',
                                      lambda n, s: _FullName(n, s, _Gender.FEMALE))

    return random.choice(objs)


class _CliError(Exception):
    pass


def _parse_args():
    parser = argparse.ArgumentParser(description=qngng.__description__)
    parser.add_argument('--gender', '-g', choices=['male', 'female'],
                        help='Print a male or female name')
    parser.add_argument('--male', '-m', action='store_true',
                        help='Shorthand for `--gender=male`')
    parser.add_argument('--female', '-f', action='store_true',
                        help='Shorthand for `--gender=female`')
    parser.add_argument('--snake-case', '-s', action='store_true',
                        help='Print name in `snake_case` format')
    parser.add_argument('--kebab-case', '-k', action='store_true',
                        help='Print name in `kebab-case` format')
    parser.add_argument('--camel-case', '-C', action='store_true',
                        help='Print name in `camelCase` format')
    parser.add_argument('--cap-camel-case', action='store_true',
                        help='Print name in `CapitalizedCamelCase` format')
    parser.add_argument('--cat', '-c', action='append',
                        help='Category name')
    args = parser.parse_args()

    if sum([0 if args.gender is None else 1, args.male, args.female]) > 1:
        raise _CliError('Cannot specify more than one option amongst `--gender`, `--male`, and `--female`.')

    if args.male:
        args.gender = 'male'

    if args.female:
        args.gender = 'female'

    if args.gender == 'male':
        args.gender = _Gender.MALE
    elif args.gender == 'female':
        args.gender = _Gender.FEMALE

    if sum([args.kebab_case, args.snake_case, args.camel_case, args.cap_camel_case]) > 1:
        raise _CliError('Cannot specify more than one option amongst `--snake-case`, `--kebab-case`, `--camel-case`, and `--cap-camel-case`.')

    args.fmt = _Format.DEFAULT

    if args.snake_case:
        args.fmt = _Format.SNAKE
    elif args.kebab_case:
        args.fmt = _Format.KEBAB
    elif args.camel_case:
        args.fmt = _Format.CAMEL
    elif args.cap_camel_case:
        args.fmt = _Format.CAP_CAMEL

    valid_cats = {
        'std',
        'uda',
        'uda-actors',
        'uda-hosts',
        'uda-singers',
    }

    if args.cat is None:
        args.cat = ['std']

    for cat in args.cat:
        if cat not in valid_cats:
            raise _CliError('Unknown category `{}`.'.format(cat))

    return args


def _strip_diacritics(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')


def _normalize_name(name, sep, lower=True):
    name = _strip_diacritics(name)

    if lower:
        name = name.lower()

    return re.sub(r'[^a-zA-Z0-9_]', sep, name)


@enum.unique
class _Format(enum.Enum):
    DEFAULT = 0
    SNAKE = 1
    KEBAB = 2
    CAMEL = 3
    CAP_CAMEL = 4


def _format_name(fullname, fmt=_Format.DEFAULT):
    if fmt == _Format.DEFAULT:
        string = '{} {}'.format(fullname.name, fullname.surname)
    elif fmt == _Format.SNAKE:
        name = _normalize_name(fullname.name, '_')
        surname = _normalize_name(fullname.surname, '_')
        string = '{}_{}'.format(name, surname)
    elif fmt == _Format.KEBAB:
        name = _normalize_name(fullname.name, '-')
        surname = _normalize_name(fullname.surname, '-')
        string = '{}-{}'.format(name, surname)
    elif fmt == _Format.CAMEL or fmt == _Format.CAP_CAMEL:
        name = _normalize_name(fullname.name, '', False)
        surname = _normalize_name(fullname.surname, '', False)
        string = '{}{}'.format(name, surname)

        if fmt == _Format.CAMEL:
            string = string[0].lower() + string[1:]

    return string


def _run(args):
    rand_fullnames = []

    for cat in args.cat:
        if cat == 'std':
            rand_fullnames.append(_random_std_fullname(args.gender))
        else:
            rand_fullnames.append(_random_cat_fullname(cat, args.gender))

    rand_fullname = random.choice(rand_fullnames)
    print(_format_name(rand_fullname, args.fmt))


def _main():
    try:
        _run(_parse_args())
    except Exception as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
