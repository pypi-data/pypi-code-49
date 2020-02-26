#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


import imghdr

import nose.tools

from ..plotter import Plotter

from . import prefix


def test_default():
    p = Plotter(prefix, data=None)
    nose.tools.assert_false(p.valid)


def test_scatter():
    for i in range(1, 3):
        yield scatter, f"user/scatter/{i}"


def scatter(plotter_name):
    p = Plotter(prefix, plotter_name)
    nose.tools.assert_true(p.valid, "\n  * %s" % "\n  * ".join(p.errors))


def do_plot(mimetype, plotter_name):

    p = Plotter(prefix, plotter_name)
    nose.tools.assert_true(p.valid)

    runnable = p.runner()
    nose.tools.assert_false(runnable.ready)
    runnable.setup(
        {
            "xlabel": "Temperature in C",
            "ylabel": "Icecream Sales in $",
            "title": "Temperature versus icecream sales",
            "mimetype": mimetype,
        }
    )
    nose.tools.assert_true(runnable.ready)

    # now produce the plot
    data = p.dataformat.type(
        data=[
            # temperature in C against icecream sales day-by-day
            {"x": 11.9, "y": 185},
            {"x": 14.2, "y": 215},
            {"x": 15.2, "y": 332},
            {"x": 16.4, "y": 325},
            {"x": 17.2, "y": 408},
            {"x": 18.1, "y": 421},
            {"x": 19.4, "y": 412},
            {"x": 18.5, "y": 406},
            {"x": 22.1, "y": 522},
            {"x": 22.6, "y": 445},
            {"x": 23.4, "y": 544},
            {"x": 25.1, "y": 614},
        ]
    )

    return runnable.process(data)


def test_plot_image():
    for i in range(1, 3):
        for image_type in ["png", "jpeg"]:
            yield plot_image, f"user/scatter/{i}", image_type


def plot_image(plotter_name, image_type):
    fig = do_plot(f"image/{image_type}", plotter_name)
    nose.tools.eq_(imghdr.what(f"test.{image_type}", fig), image_type)


def test_plot_pdf():
    for i in range(1, 3):
        yield plot_pdf, f"user/scatter/{i}"


def plot_pdf(plotter_name):
    fig = do_plot("application/pdf", plotter_name)
    nose.tools.assert_true(fig.startswith(b"%PDF"))


def test_plot_many_lines():
    for i in range(1, 3):
        yield plot_many_lines, f"user/scatter/{i}"


def plot_many_lines(plotter_name):
    p = Plotter(prefix, plotter_name)
    nose.tools.assert_true(p.valid)

    data1 = p.dataformat.type(
        data=[
            # temperature in C against icecream sales day-by-day
            {"x": 0, "y": 0},
            {"x": 1, "y": 1},
            {"x": 2, "y": 2},
            {"x": 3, "y": 3},
            {"x": 4, "y": 4},
            {"x": 5, "y": 5},
            {"x": 6, "y": 6},
            {"x": 7, "y": 7},
            {"x": 8, "y": 8},
            {"x": 9, "y": 9},
        ]
    )

    data2 = p.dataformat.type(
        data=[
            # temperature in C against icecream sales day-by-day
            {"x": 0, "y": 1},
            {"x": 1, "y": 3},
            {"x": 2, "y": 5},
            {"x": 3, "y": 7},
            {"x": 4, "y": 9},
            {"x": 5, "y": 11},
            {"x": 6, "y": 13},
            {"x": 7, "y": 15},
            {"x": 8, "y": 17},
            {"x": 9, "y": 19},
        ]
    )

    runnable = p.runner()
    nose.tools.assert_false(runnable.ready)
    runnable.setup(
        {
            "title": "Test plot",
            "grid": True,
            "legend": "&".join(
                ["Dashed red line with cross", "Blue circles with line"]
            ),
            "line_attributes": "&".join(["r+--", "bo-"]),
            "mimetype": "image/png",
        }
    )
    nose.tools.assert_true(runnable.ready)

    fig = runnable.process([data1, data2])
    nose.tools.eq_(imghdr.what("test.png", fig), "png")
