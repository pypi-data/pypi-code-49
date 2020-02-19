#!/usr/bin/env python
import os

from pygments import highlight
from pygments.formatters import HtmlFormatter, Terminal256Formatter

from .prolexer import CustomLexer
from .prostyle import ProStyle


def render(
    pro_filename,
    out_filename=None,
    font_size=22,
    formatting="terminal",
    print_output=True,
):
    if os.path.isfile(pro_filename):
        cmd = "pygmentize -O full,line_numbers=False,style=prostyle,font_name='Ubuntu Mono',font_size={} -l pro".format(
            font_size
        )
        if out_filename:
            cmd += " -o {}".format(out_filename)
        cmd += " {}".format(pro_filename)
        os.system(cmd)
    else:
        if formatting == "terminal":
            formatter = Terminal256Formatter(style=ProStyle)
        elif formatting == "html":
            formatter = HtmlFormatter(style=ProStyle)
        else:
            raise Exception("Wrong formatting, choose between html and terminal")
        highlighted_code = highlight(pro_filename, CustomLexer(), formatter)

        if print_output:
            print(highlighted_code)
        return highlighted_code
