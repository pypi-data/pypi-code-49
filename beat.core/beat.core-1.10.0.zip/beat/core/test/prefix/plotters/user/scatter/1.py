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


import six
import numpy
import itertools

# Make sure we won't require an X11 connection
import matplotlib

matplotlib.use("Agg")  # noqa need to happen before further imports

from matplotlib.figure import Figure
import matplotlib.pyplot as pyplot


class Plotter:
    def setup(self, parameters):

        self.xlabel = parameters["xlabel"]
        self.xaxis_multiplier = parameters["xaxis_multiplier"]
        self.xaxis_log = parameters["xaxis_log"]
        self.ylabel = parameters["ylabel"]
        self.yaxis_multiplier = parameters["yaxis_multiplier"]
        self.yaxis_log = parameters["yaxis_log"]
        self.title = parameters["title"]
        self.line_attributes = parameters["line_attributes"].split("&")
        self.legend = parameters["legend"].split("&")
        self.grid = parameters["grid"]
        self.mimetype = parameters["mimetype"]

        return True

    def process(self, inputs):

        # Creates the image to return
        fig = Figure()
        ax = fig.add_subplot(111)

        if not isinstance(inputs, (list, tuple)):
            inputs = [inputs]
        if not isinstance(self.legend, (list, tuple)):
            self.legend = [self.legend]
        if not isinstance(self.line_attributes, (list, tuple)):
            self.line_attributes = [self.line_attributes]

        try:
            Z = itertools.izip
        except AttributeError:
            Z = zip

        C = itertools.cycle

        for input, attributes, label in Z(
            inputs, C(self.line_attributes), C(self.legend)
        ):

            # Massages the input data
            final_data = numpy.array([(k.x, k.y) for k in input.data])
            x = final_data[:, 0]
            y = final_data[:, 1]
            x *= self.xaxis_multiplier
            y *= self.yaxis_multiplier

            args = (x, y)
            if attributes:
                args = args + (attributes,)
            kwargs = {}
            if label:
                kwargs["label"] = label

            # Plots
            ax.plot(*args, **kwargs)

        # Sets plot attributes
        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        ax.grid(self.grid)
        if self.xaxis_log:
            ax.set_xscale("log")
        if self.yaxis_log:
            ax.set_yscale("log")
        if any(self.legend):
            ax.legend()

        # Returns the image
        if six.PY2:
            sio = six.StringIO()
        else:
            sio = six.BytesIO()

        if self.mimetype == "image/png":
            pyplot.savefig(sio, format="png")
        elif self.mimetype == "image/jpeg":
            pyplot.savefig(sio, format="jpeg")
        elif self.mimetype == "application/pdf":
            from matplotlib.backends.backend_pdf import FigureCanvasPdf

            canvas = FigureCanvasPdf(fig)
            canvas.print_figure(sio)

        return sio.getvalue()
