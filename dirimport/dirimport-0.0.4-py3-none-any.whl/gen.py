import os
import sys
import types
import difflib
import importlib
from jinja2 import Template
from logging import getLogger

log = getLogger(__name__)

tmpl = Template("""
{%- for d in dirs %}
from . import {{d}}  # noqa
{%- endfor %}
{%- for f in files %}
from .{{f}} import *  # noqa
{%- endfor %}
""")


def dig(dirname):
    resd = {}
    resf = []
    for f in sorted(os.listdir(dirname)):
        if f.startswith("_") or f.startswith("."):
            continue
        fpath = os.path.join(dirname, f)
        if os.path.isdir(fpath):
            x = dig(fpath)
            if len(x[0]) == 0 and len(x[1]) == 0:
                continue
            resd[f] = x
        elif os.path.isfile(fpath) and f.endswith(".py"):
            resf.append(f[:-3])
    return resd, resf


def generate(data, basename, filename="__init__.py"):
    dirs, files = data
    ofn = os.path.join(basename, filename)
    with open(ofn, "w") as ofp:
        print(tmpl.render(dirs=dirs.keys(), files=files).strip(), file=ofp)
    for k, v in dirs.items():
        generate(v, os.path.join(basename, k), filename)


def diff(data, basename, filename="__init__.py"):
    dirs, files = data
    ofn = os.path.join(basename, filename)
    if os.path.exists(ofn):
        orig = list(filter(lambda f: f != "", map(
            lambda f: f.strip(), open(ofn).readlines())))
    else:
        orig = []
    newtxt = tmpl.render(dirs=dirs.keys(), files=files)
    newdata = list(filter(lambda f: f.strip() != "", newtxt.split("\n")))
    res = list(difflib.unified_diff(orig, newdata,
                                    fromfile=ofn + ".orig", tofile=ofn))
    for k, v in dirs.items():
        res.extend(diff(v, os.path.join(basename, k), filename))
    return res


def clear(basename, filename="__init__.py"):
    for root, dirs, files in os.walk(basename):
        if filename in files:
            os.unlink(os.path.join(root, filename))


def importdata(data, basename, rootdir="."):
    dirs, files = data
    res = types.ModuleType(basename)
    sys.path.insert(0, rootdir)
    log.debug("path %s", rootdir)
    for f in files:
        # from .f import *
        log.debug("loading(f) %s %s", basename, f)
        tmp = importlib.import_module(basename + "." + f)
        log.debug("loaded: %s, file=%s", tmp, tmp.__file__)
        for v in dir(tmp):
            if v.startswith("_"):
                continue
            if hasattr(res, v):
                log.info("duplicate symbol %s %s %s", basename, f, v)
                continue
            obj = getattr(tmp, v)
            log.debug("set attribute: %s.%s = %s", res, v, obj)
            setattr(res, v, obj)
    sys.path.pop(0)
    for k, v in dirs.items():
        log.debug("loading(d) %s %s %s", basename, k, v)
        setattr(res, k, importdata(v, basename + "." + k, rootdir))
    return res


def importall(basename):
    data = dig(basename)
    log.debug("dig %s: %s", basename, data)
    return importdata(data, os.path.basename(basename), os.path.dirname(basename))
