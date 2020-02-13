#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2008-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>
# Copyright 2013 by Elena Grandi <elena.valhalla@gmail.com>
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
"""
Generate example PDF documents for pdfposter.

This generates four PDF-files, with two sides each: A4, A5, A6 and DIN lang.

These pages are later used creating images for examples.
"""

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2008-2020 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"

import os

from reportlab.lib.units import mm
from reportlab.lib.colors import black, pink, lightblue
from reportlab.lib.pagesizes import A4, A5, A6, portrait, landscape
from reportlab.pdfgen.canvas import Canvas
from reportlab import rl_config
rl_config.invariant = 1  # produce identical PDFs with same timestamp info

DIN_LANG = landscape((A4[0], A4[1] / 3))


def draw_numbers(canvas, numbers, size, margin, rows, cols):
    step_x = (size[0] - margin*2) / cols
    step_y = (size[1] - margin*2) / rows
    for i, n in enumerate(numbers):
        canvas.drawCentredString(
            margin + step_x / 2 + step_x * (i % cols),
            # font-size 72 -> offset -36
            margin-36 + step_y / 2 + (rows - 1 - i // cols) * step_y, n)


def drawPage(canv, size, text1, text2, margin, color):
    numbers = ['1', '2', '3', '4', '5', '6']
    # draw the numbers
    canv.setFont("Helvetica", 72)
    canv.setStrokeColor(black)
    canv.setFillColor(black)
    # two lines of text
    canv.drawCentredString(size[0] / 2, size[1] / 2, text1)
    canv.drawCentredString(size[0] / 2, size[1] / 2 - 72, text2)
    canv.setFillColor(color)
    draw_numbers(canv, numbers, size, margin, 3, 2)
    # draw the border
    width, height = size
    canv.rect(margin, margin, width - margin * 2,
              height - margin * 2, fill=0, stroke=1)
    canv.showPage()


def genFile(filename, size, text, margin=10*mm):
    canv = Canvas(filename, pagesize=size)
    drawPage(canv, size, text, "front", margin, lightblue)
    drawPage(canv, size, text, "back", margin, pink)
    # save the pdf file
    canv.save()


def genTestFiles(output_directory):
    for name, size in (
            ('a4', A4),
            ('a5', A5),
            ('a6', A6),
            ('din-lang', DIN_LANG)):
        for orientation in (portrait, landscape):
            genFile(os.path.join(
                output_directory,
                "pages-%s-%s.pdf" % (name, orientation.__name__)),
                    size=orientation(size),
                    text=name.upper())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-O', '--output-directory', default=".")
    args = parser.parse_args()
    genTestFiles(args.output_directory)
