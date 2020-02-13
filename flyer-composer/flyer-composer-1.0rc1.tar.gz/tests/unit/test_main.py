#!/usr/bin/env python3
#
# Copyright 2012-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>
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
__copyright__ = "Copyright 2012-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"

import os
import pytest
import py.path
import PyPDF2.pdf

from flyer_composer import main, Box

PAGE_PATTERNS = [(p, o)
                 for p in ("a4", "a5", "a6", "a7")
                 for o in ("landscape", "portrait")]

EXAMPLES_DIR = py.path.local(os.path.dirname(__file__)).join(
    "..", "..", "examples")

INPUT_SIZES = ["a4", "a5", "a6"]

EXPECTED_1 = {
    # insize, flyersize -> scale
    ("a4", "a4"): (1.00,),
    ("a4", "a5"): (0.70,),
    ("a4", "a6"): (0.50,),
    ("a4", "a7"): (0.35,),

    ("a5", "a4"): (1.41,),
    ("a5", "a5"): (1.00,),
    ("a5", "a6"): (0.70,),
    ("a5", "a7"): (0.50,),

    ("a6", "a4"): (2.00,),
    ("a6", "a5"): (1.41,),
    ("a6", "a6"): (1.00,),
    ("a6", "a7"): (0.70,),
    }

EXPECTED_2 = {
    # flyersize, mediasize -> num pages, …
    ("a4", "a4"): (1, False),
    ("a5", "a4"): (2, True),
    ("a6", "a4"): (4, False),
    ("a7", "a4"): (8, True),

    ("a5", "a5"): (1, False),
    ("a6", "a5"): (2, True),
    ("a7", "a5"): (4, False),

    ("a6", "a6"): (1, False),
    ("a7", "a6"): (2, True),
    }


@pytest.fixture
def _collect_page_params(monkeypatch):

    def rotate(self):
        rotated.append(True)
        bR(self)

    def mergeScaledTranslatedPage(self, page2, scale, tx, ty, expand=False):
        added_pages.append((scale, tx, ty))
        mSTP(self, page2=page2, scale=scale, tx=tx, ty=ty, expand=expand)

    bR = Box.rotate
    mSTP = PyPDF2.pdf.PageObject.mergeScaledTranslatedPage
    monkeypatch.setattr("flyer_composer.Box.rotate", rotate)
    monkeypatch.setattr(
        "PyPDF2.pdf.PageObject.mergeScaledTranslatedPage",
        mergeScaledTranslatedPage)

    added_pages = []
    rotated = []
    return added_pages, rotated


@pytest.mark.parametrize(
    "flyerspec", sorted(EXPECTED_2.keys()),
    ids=["as-%s-on-%s" % e for e in sorted(EXPECTED_2.keys())])
@pytest.mark.parametrize("orientation", ["landscape", "portrait"])
@pytest.mark.parametrize("insize", INPUT_SIZES)
def test_main(tmpdir, _collect_page_params, insize, flyerspec, orientation):
    inspec = (insize, orientation)
    flyersize, mediasize = flyerspec
    infilename = str(EXAMPLES_DIR / ("pages-%s-%s.pdf" % inspec))
    outfilename = str(tmpdir / ("out-%s-%s.pdf" % inspec))
    main(infilename, outfilename, flyersize, mediasize)

    added_pages, rotated = _collect_page_params
    scale = EXPECTED_1[insize, flyersize][0]
    num_pages, rotate = EXPECTED_2[flyersize, mediasize]

    assert len(added_pages) == num_pages
    # flyerbox in decide_num_cols_rows()
    num_rotations = int(rotate)
    # inbox in decide_scale() implies mediabox in flyerize()
    num_rotations += 2 * int(rotate != (orientation == "landscape"))
    assert len(rotated) == num_rotations
    for p in added_pages:
        assert abs(p[0] - scale) < 0.1
    assert os.path.exists(outfilename)


@pytest.mark.parametrize("orientation", ["landscape", "portrait"])
def test_main_dinlang(tmpdir, _collect_page_params, orientation):
    flyersize = "dinlang"
    infilename = str(EXAMPLES_DIR / ("pages-din-lang-%s.pdf" % orientation))
    outfilename = str(tmpdir / ("out-din-lang-%s.pdf" % orientation))
    main(infilename, outfilename, flyersize, "a4")

    added_pages, rotated = _collect_page_params
    assert len(added_pages) == 3
    if orientation == "landscape":
        assert len(rotated) == 0
    else:
        assert len(rotated) == 1 + 1
    for p in added_pages:
        assert abs(p[0] - 1) < 0.1
    assert os.path.exists(outfilename)


def test_main_two_inputs(tmpdir, _collect_page_params):
    insize_1 = "a4"
    insize_2 = "a5"
    flyersize = "a6"
    mediasize = "a4"
    infilename_1 = str(EXAMPLES_DIR / ("pages-%s-landscape.pdf" % insize_1))
    infilename_2 = str(EXAMPLES_DIR / ("pages-%s-portrait.pdf" % insize_2))
    outfilename = str(tmpdir / "out-twofiles.pdf")

    main(infilename_1, outfilename, flyersize, mediasize,
         front_page=1, back_page=0, infilename_back=infilename_2)

    added_pages, rotated = _collect_page_params
    # 2x for A4 inbox landscape != flyerbox portrait
    # 0x for A5 portrait
    assert len(rotated) == 2

    assert os.path.exists(outfilename)
    assert len(added_pages) == 8
    # front
    scale = EXPECTED_1[insize_1, flyersize][0]
    for p in added_pages[:4]:
        assert abs(p[0] - scale) < 0.01
    # back
    scale = EXPECTED_1[insize_2, flyersize][0]
    for p in added_pages[4:]:
        assert abs(p[0] - scale) < 0.01
