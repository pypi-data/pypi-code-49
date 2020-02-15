import sys
import os
import stat
import fnmatch
import functools
import io
import pkgutil
import time
import mimetypes
from logging import getLogger, basicConfig, INFO, DEBUG
import click
from jinja2 import Environment
from .version import VERSION

log = getLogger(__name__)


@click.version_option(version=VERSION, prog_name="dirindex")
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


def set_verbose(flag):
    fmt = '%(asctime)s %(levelname)s %(message)s'
    if flag:
        basicConfig(level=DEBUG, format=fmt)
    else:
        basicConfig(level=INFO, format=fmt)


_cli_option = [
    click.option("--verbose/--no-verbose"),
]


def multi_options(decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco


def cli_option(func):
    @functools.wraps(func)
    def wrap(verbose, *args, **kwargs):
        set_verbose(verbose)
        return func(*args, **kwargs)
    return multi_options(_cli_option)(wrap)


def pattern_filter(target, pattern, hide):
    log.debug("pfilter: target=%s, pattern=%s, hide=%s", target, pattern, hide)
    rms = []
    if hide:
        for h in hide:
            for rm in filter(lambda f: fnmatch.fnmatch(f, h), target):
                log.debug("remove(hide %s): %s", h, rm)
                rms.append(rm)
    if pattern:
        for p in pattern:
            for rm in filter(lambda f: not fnmatch.fnmatch(f, p), target):
                log.debug("remove(pattern %s): %s", p, rm)
                rms.append(rm)
    for rm in rms:
        target.remove(rm)
    return target


def fileopen(dir, fn, mode="w"):
    if fn == "-":
        if mode == "w":
            return sys.stdout
        else:
            return sys.stdin
    if dir:
        return open(os.path.join(dir, fn), mode)
    return open(fn, mode)


def mkent(fullpath, basedir):
    rel = os.path.relpath(fullpath, basedir)
    guess_type = mimetypes.guess_type(os.path.basename(fullpath))
    res = {
        "name": rel,
        "fullpath": fullpath,
        "abspath": os.path.abspath(fullpath),
        "stat": os.stat(fullpath),
    }
    if guess_type[0] is not None:
        res["content_type"] = guess_type[0]
    if guess_type[1] is not None:
        res["content_encoding"] = guess_type[1]
    return res


def openresource(filename, resource_base="templates"):
    log.debug("filename: %s", filename)
    if filename == "-":
        return sys.stdin
    elif os.path.exists(filename):
        return fileopen(None, filename, "r")
    return io.StringIO(pkgutil.get_data(__package__, os.path.join(resource_base, filename)).decode("utf-8"))


@cli.command()
@cli_option
@click.option("--template", type=str)
@click.option("--dry/--no-dry", default=False, show_default=True)
@click.option("--recursive/--no-recursive", default=False, show_default=True)
@click.option("--single/--no-single", default=False, show_default=True)
@click.option("--pattern", type=str, default=["*"], show_default=True, multiple=True)
@click.option("--hide", type=str, default=None, show_default=True, multiple=True)
@click.option("--filename", default="index.html", show_default=True)
@click.argument("directory", type=click.Path(dir_okay=True, exists=True))
def make(template, directory, dry, recursive, single, filename, pattern, hide):
    env = Environment(keep_trailing_newline=True)
    env.filters['strftime'] = lambda a, b: time.strftime(b, time.localtime(a))
    env.filters['filemode'] = stat.filemode
    with openresource(template, "templates") as tfp:
        tmpl = env.from_string(tfp.read())
    args = {
        "root": directory,
        "dir": [], "file": [],
    }
    if recursive and single:
        # output single file
        for root, dirs, files in os.walk(directory):
            dirs = pattern_filter(dirs, pattern, hide)
            files = pattern_filter(files, pattern, hide)
            for d in dirs:
                args["dir"].append(mkent(os.path.join(root, d), directory))
            for f in files:
                args["file"].append(mkent(os.path.join(root, f), directory))
        log.debug("output %s / %s arg=%s", directory, filename, args)
        if not dry:
            with fileopen(directory, filename, "w") as ofp:
                ofp.write(tmpl.render(**args))
    elif recursive:
        # output to each directory
        for root, dirs, files in os.walk(directory):
            args = {
                "root": root,
                "dir": [], "file": [],
            }
            dirs = pattern_filter(dirs, pattern, hide)
            files = pattern_filter(files, pattern, hide)
            for d in dirs:
                args["dir"].append(mkent(os.path.join(root, d), root))
            for f in files:
                args["file"].append(mkent(os.path.join(root, f), root))
            log.debug("output %s / %s args=%s", root, filename, args)
            if not dry:
                with fileopen(root, filename, "w") as ofp:
                    ofp.write(tmpl.render(**args))
    else:
        # single directory
        files = os.listdir(directory)
        files = pattern_filter(files, pattern, hide)
        for f in files:
            ent = mkent(os.path.join(directory, f), directory)
            if stat.S_ISDIR(ent["stat"].st_mode):
                args["dir"].append(ent)
            else:
                args["file"].append(ent)
        log.debug("output %s / %s args=%s", directory, filename, args)
        if not dry:
            with fileopen(directory, filename, "w") as ofp:
                ofp.write(tmpl.render(**args))


@cli.command()
@cli_option
@click.argument("name", type=str)
def read_resource(name):
    log.info("read resource %s", name)
    with openresource(name, "templates") as ifp:
        print(ifp.read())


if __name__ == "__main__":
    cli()
