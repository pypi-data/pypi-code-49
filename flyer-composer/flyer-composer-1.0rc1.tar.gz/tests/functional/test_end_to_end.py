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

import pytest
import os, sys

from flyer_composer import cli
import PyPDF2

A5_LANDSCAPE = os.path.join(os.path.dirname(__file__), "..", "..",
                            "examples", "pages-a5-landscape.pdf")


def get_page_texts(filename):
    with open(filename, 'rb') as fh:
        reader = PyPDF2.PdfFileReader(fh)
        return [reader.getPage(num).extractText()
                for num in range(reader.getNumPages())]


def get_num_flyers(page_texts):
    nums = []
    #import pdb ; pdb.set_trace()
    for pt in page_texts:
        pt = pt.split()
        nums.append(pt.count("front") + pt.count("back"))
    return nums


def test_without_options(tmpdir):
    outname = str(tmpdir.join('out.pdf'))
    cli.run([A5_LANDSCAPE, outname])
    # default media-size is 1x1a4 and default flyer-size is media-size
    page_texts = get_page_texts(outname)
    assert len(page_texts) == 1
    assert get_num_flyers(page_texts)[0] == 1


def test_mediasize(tmpdir):
    outname = str(tmpdir.join('out.pdf'))
    cli.run([A5_LANDSCAPE, '-m3x4a5', outname])
    # default flyer-size is media-size, so this is one flyer
    page_texts = get_page_texts(outname)
    assert len(page_texts) == 1
    assert get_num_flyers(page_texts)[0] == 1


def test_flyersize_a5(tmpdir):
    outname = str(tmpdir.join('out.pdf'))
    cli.run([A5_LANDSCAPE, '-fa5', outname])
    # default media-size is 1x1a4, so this will be 2 flyers
    page_texts = get_page_texts(outname)
    assert len(page_texts) == 1
    assert get_num_flyers(page_texts)[0] == 2


def test_flyersize_a6(tmpdir):
    outname = str(tmpdir.join('out.pdf'))
    cli.run([A5_LANDSCAPE, '-fa6', outname])
    # default media-size is 1x1a4, so this will be 4 flyers
    page_texts = get_page_texts(outname)
    assert len(page_texts) == 1
    assert get_num_flyers(page_texts)[0] == 4


def test_flyersize_and_mediasize(tmpdir):
    outname = str(tmpdir.join('out.pdf'))
    cli.run([A5_LANDSCAPE, '-mA5', '-fa6', outname])
    # this will be 2 flyers
    page_texts = get_page_texts(outname)
    assert len(page_texts) == 1
    assert get_num_flyers(page_texts)[0] == 2
