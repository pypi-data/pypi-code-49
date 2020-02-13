#
# Copyright 2008-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of flyer-composer.
#
# flyer-composer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# flyer-composer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with flyer-composer. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2008-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"

import os
import sys
import argparse

import pytest

from flyer_composer import cli, __version__

ArgParserError = argparse.ArgumentTypeError


def test_help(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli.run(['foobar', '--help'])
    assert excinfo.value.code == 0
    out, err = capsys.readouterr()
    assert "positional arguments" in out


def test_help_media_names(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli.run(['foobar', '--help-media-names'])
    assert excinfo.value.code == 0
    out, err = capsys.readouterr()
    assert "media and distance names" in out
    assert "a2 a3 a4" in out


def test_version(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli.run(['foobar', '--version'])
    assert excinfo.value.code == 0
    out, err = capsys.readouterr()
    assert len(out.splitlines()) == 1
    progname = os.path.basename(sys.argv[0])
    assert out.strip() == ('%s %s' % (progname, __version__))


def test_without_options(monkeypatch):

    def mockmain(infilename, outfilename, **args):
        assert infilename == 'in.pdf'
        assert outfilename == 'out.pdf'

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)
    cli.run(['in.pdf', 'out.pdf'])


def test_corrupt_pdf(monkeypatch):

    def mockerror(self, msg):
        pass

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr('argparse.ArgumentParser.error', mockerror)
    cli.run([__file__, 'out.pdf'])


def test_can_parse_mediasize(monkeypatch):

    def mockmain(infilename, outfilename, media_size, **args):
        assert media_size['unit'] == 'a5'
        assert media_size['units_x'] == 3
        assert media_size['units_y'] == 4

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)
    cli.run(['in.pdf', '-m3x4a5', 'out.pdf'])


def test_can_parse_flyersize(monkeypatch):

    def mockmain(infilename, outfilename, flyer_size, **args):
        assert flyer_size['unit'] == 'a5'
        assert flyer_size['units_x'] == 3
        assert flyer_size['units_y'] == 4

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)
    cli.run(['in.pdf', '-f3x4a5', 'out.pdf'])


def test_flyersize_defaults_to_mediasize(monkeypatch):

    def mockmain(infilename, outfilename, flyer_size, media_size, **args):
        assert flyer_size == media_size
        assert flyer_size['unit'] == 'a5'
        assert flyer_size['units_x'] == 3
        assert flyer_size['units_y'] == 4

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)
    cli.run(['in.pdf', '-m3x4a5', 'out.pdf'])


def test_flyersize_and_mediasize_given(monkeypatch):

    def mockmain(infilename, outfilename, flyer_size, media_size, **args):
        assert media_size['unit'] == 'a5'
        assert media_size['units_x'] == 3
        assert media_size['units_y'] == 4

        assert flyer_size['unit'] == 'dinlang'
        assert flyer_size['units_x'] == 23
        assert flyer_size['units_y'] == 42

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)
    cli.run(['in.pdf', '-m3x4a5', '-f23x42dinla', 'out.pdf'])


page_numbers =(
    ("-F1", None, 0, None),
    ("-F1", "-B1", 0, 0),
    ("-F1", "-B42", 0, 41),
    # bound check is done in main, thus test wrong numbers
    ("-F0", None, -1, None),
    ("-F-1", None, -2, None),
    ("-F0", "-B0", -1, -1),
    )
@pytest.mark.parametrize(
    "page_numbers", page_numbers,
    ids=["".join(filter(None, e[:2])) for e in page_numbers])
def test_page_numbers(monkeypatch, page_numbers):

    def mockmain(infilename, outfilename, front_page, back_page, **args):
        assert front_page == front_expected
        assert back_page == back_expected

    # 'main' is imported into `cli`, need to monkeypath there
    monkeypatch.setattr(cli, 'main', mockmain)

    front_spec, back_spec, front_expected, back_expected = page_numbers
    args = [a for a in (front_spec, back_spec) if a]
    EXPECTED = 0 ; cli.run(['in.pdf', 'out.pdf', *args])
