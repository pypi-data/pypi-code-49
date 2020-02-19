# -*- coding: utf-8 -*-
#
from __future__ import print_function

import os
import subprocess
import textwrap
import tokenize
from io import StringIO

from .rendering import render


def get_kernel():
    return os.path.basename(os.environ["_"])


def print_html(code, tmp_dir=None, tmp_file="out.html", print_output=False):
    html_data = render(code, formatting="html", print_output=print_output)
    if not tmp_dir:
        tmp_dir = os.path.join(
            "../..", "doc", "auto_examples", os.path.basename(os.getcwd())
        )

    if os.path.exists(tmp_dir):
        # building the doc with sphinx-gallery
        with open(os.path.join(tmp_dir, tmp_file), "wt") as fh:
            fh.write(html_data)
    else:
        kernel = get_kernel()
        if kernel == "python" or "ipython":
            # running from a terminal or ipython
            render(code)
        else:
            if kernel == "jupyter":
                # running from jupyter
                from IPython.display import display, HTML
                from pygments.formatters import HtmlFormatter

                display(
                    HTML(
                        """
                <style>
                {pygments_css}
                </style>
                """.format(
                            pygments_css=HtmlFormatter().get_style_defs(".highlight")
                        )
                    )
                )
                display(HTML(html_data))


def make_png(code, filename="tmp"):
    with open(filename, "w") as f:
        f.write(code)
    render(filename, "{}.png".format(filename))
    os.remove(filename)


def show_png(filename="tmp"):
    import matplotlib.pyplot as plt

    image = plt.imread("{}.png".format(filename))
    plt.figure()
    plt.imshow(image)
    plt.axis("off")
    plt.tight_layout()
    import warnings

    warnings.simplefilter("error", UserWarning)
    try:
        plt.show()
    except UserWarning:
        pass


def build_example_png(code, filename="tmp"):
    make_png(code, filename=filename)
    show_png(filename=filename)
    os.remove("{}.png".format(filename))


def _add_raw_code(s, raw_code, newline=True):
    if newline:
        nl = "\n"
    else:
        nl = ""
    s += nl + raw_code
    return s


def _comment(s, style="short", newline=False):
    if newline:
        nl = "\n"
    else:
        nl = ""
    if style == "short":
        if len(s) > 80:
            s = "\n".join(textwrap.wrap(s))
            return _comment(s, style="long", newline=newline)
        else:
            return nl + r"// " + s
    elif style == "long":
        return nl + r"/*  " + s + r" */"


def _is_string(obj):
    return isinstance(obj, str)


def _is_list(obj):
    return isinstance(obj, list)


def _is_tuple(obj):
    return isinstance(obj, tuple)


def _is_complex(obj):
    return isinstance(obj, complex)


def _get_getdp_exe():
    macos_getdp_location = "/Applications/Getdp.app/Contents/MacOS/getdp"
    return macos_getdp_location if os.path.isfile(macos_getdp_location) else "getdp"


def py2getdplist(l):
    return "{" + ",".join([str(_) for _ in l]) + "}"


def get_getdp_major_version(getdp_exe=_get_getdp_exe()):
    out = (
        subprocess.check_output([getdp_exe, "--version"], stderr=subprocess.STDOUT)
        .strip()
        .decode("utf8")
    )
    ex = out.split(".")
    return int(ex[0])


def make_args(glist, sep=","):
    sep = sep + " "
    if isinstance(glist, list):
        if len(glist) == 1:
            glist = str(glist[0])
        else:
            glist = sep.join([str(g) for g in glist])
            glist = "{" + glist + "}"
    return str(glist)


def replace_formula(str_in, to_replace, replacement):
    str_in = "".join(str_in.split())
    str_in = str_in.replace("{", "").replace("}", "")
    to_replace = ["".join(_.split()) for _ in to_replace]
    to_replace = [_.replace("{", "").replace("}", "") for _ in to_replace]
    tok = [
        token[1]
        for token in tokenize.generate_tokens(StringIO(str_in).readline)
        if token[1]
    ]

    for rold, rnew in zip(to_replace, replacement):
        for i, t in enumerate(tok):
            if t == rold:
                tok[i] = rnew
    return "".join(tok)
