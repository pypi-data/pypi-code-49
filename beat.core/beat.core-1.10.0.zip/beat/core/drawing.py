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


"""
=======
drawing
=======

Utilities for drawing toolchains and experiments
"""


def text_color(c):
    """Calculates if text must be black/white for a given color background

    The technique deployed in this function calculates the perceptive luminance
    for a given color and then choses a black or white color depending on that
    value.

    Parameters:

      c (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.


    Returns:

      str: Either ``#000000`` (black) or ``#ffffff`` (white) depending on which
        better text color would go with the given color.
    """

    c = int(c[1:3], 16), int(c[3:5], 16), int(c[5:], 16)
    a = 1 - (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]) / 255
    if a < 0.5:
        return "#000000"
    else:
        return "#ffffff"


def lighten_color(n):
    """Lightens the given color

    Parameters:

      c (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.


    Returns:

      str: The hexadecimal representation of the lightened color.
    """

    c = int(n[1:3], 16), int(n[3:5], 16), int(n[5:], 16)
    c = [k + 120 for k in c]
    c = map(lambda k: k if k <= 0xFF else 0xFF, c)
    return "#%02x%02x%02x" % tuple(c)


def create_port_table(type, names, color):
    """Creates an HTML table with the defined port names


    Parameters:

      type (str): The type of port - maybe set to 'input', 'output' or 'result'

      names (str): A set of strings that define the contents of each port

      color (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.

    Returns

      str: A string containing the HTML representation for the table,
        compatible with GraphViz.
    """

    retval = '<td><table border="0" cellspacing="5" bgcolor="%s">' % lighten_color(
        color
    )
    for n in names:
        port = 'port="%s_%s" ' % (type, n) if n.find("<") < 0 else ""  # results
        retval += (
            '<tr><td %sbgcolor="%s" border="1"><font color="%s">%s</font></td></tr>'
            % (port, color, text_color(color), n)
        )
    retval += "</table></td>"
    return retval


def create_layout_ports_table(color, input_names=[], output_names=[]):
    """Creates an HTML table with the defined input & output port names


    Parameters:

      input_names (str): A set of strings that define the contents of each
        input port

      output_names (str): A set of strings that define the contents of each
        output port

      color (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.

    Returns

      str: A string containing the HTML representation for the table,
        compatible with GraphViz.
    """

    retval = '<td><table border="0" bgcolor="%s">' % lighten_color(color)
    num_rows = max(len(input_names), len(output_names))
    width = 200 if len(input_names) == 0 or len(output_names) == 0 else 100
    for x in range(0, num_rows):
        retval += "<tr>"
        if len(input_names) > x:
            n = input_names[x]
            port = 'port="input_%s" ' % n if n.find("<") < 0 else ""  # results
            retval += (
                '<td %sbgcolor="%s" border="1" fixedsize="true" width="%s" height="20"><font color="%s">%s</font></td>'
                % (port, color, width, text_color(color), x)
            )
        if len(output_names) > x:
            n = output_names[x]
            port = 'port="output_%s" ' % n if n.find("<") < 0 else ""  # results
            retval += (
                '<td %sbgcolor="%s" border="1" fixedsize="true" width="%s" height="20"><font color="%s">%s</font></td>'
                % (port, color, width, text_color(color), x)
            )
        retval += "</tr>"
    retval += "</table></td>"
    return retval


def make_label(inputs, name, outputs, color):
    """Creates an HTML Table representing the label for a given block

    Parameters:

      inputs (:py:class:`list`): A list of input names which represent all
        inputs for this block

      name (str): The name of the block

      outputs (:py:class:`list`): A list of output names which represent all
        outputs for this block

      color (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.


    Returns

      str: A string containing the HTML representation for the table,
        compatible with GraphViz.
    """

    light_color = lighten_color(color)
    retval = '<<table border="0" cellspacing="0" bgcolor="%s"><tr>' % light_color
    if inputs:
        retval += create_port_table("input", inputs, color)
    retval += '<td><font color="%s">%s</font></td>' % (text_color(light_color), name)
    if outputs:
        retval += create_port_table("output", outputs, color)
    retval += "</tr></table>>"
    return retval


def make_layout_label(inputs, name, outputs, color):
    """Creates an HTML Table representing the label for a given block

    Parameters:

      inputs (:py:class:`list`): A list of input names which represent all
        inputs for this block

      name (str): The name of the block

      outputs (:py:class:`list`): A list of output names which represent all
        outputs for this block

      color (str): A color definition in the format ``#rrggbb``, in which each
        color channel is represented by 2-digit hexadecimal number ranging from
        0x0 to 0xff.


    Returns

      str: A string containing the HTML representation for the table,
        compatible with GraphViz.
    """

    light_color = lighten_color(color)
    retval = '<<table border="0" bgcolor="%s">%s<tr>' % (
        light_color,
        '<tr><td><font color="%s">%s</font></td></tr>'
        % (text_color(light_color), name),
    )
    retval += create_layout_ports_table(color, inputs or [], outputs or [])
    retval += "</tr></table>>"
    return retval
