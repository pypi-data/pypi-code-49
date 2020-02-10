# Copyright: (C) 2010-2019 Alex Clark and Pillow contributors
# License: PIL Software License

import os
import sys
from distutils.ccompiler import CCompiler
from multiprocessing import Pool, cpu_count

try:
    MAX_PROCS = int(os.environ.get("MAX_CONCURRENCY", min(4, cpu_count())))
except NotImplementedError:
    MAX_PROCS = None


# hideous monkeypatching.  but. but. but.
def _mp_compile_one(tp):
    (self, obj, build, cc_args, extra_postargs, pp_opts) = tp
    try:
        src, ext = build[obj]
    except KeyError:
        return
    self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
    return


def _mp_compile(
    self,
    sources,
    output_dir=None,
    macros=None,
    include_dirs=None,
    debug=0,
    extra_preargs=None,
    extra_postargs=None,
    depends=None,
):
    """Compile one or more source files.

    see distutils.ccompiler.CCompiler.compile for comments.
    """
    # A concrete compiler class can either override this method
    # entirely or implement _compile().

    macros, objects, extra_postargs, pp_opts, build = self._setup_compile(
        output_dir, macros, include_dirs, sources, depends, extra_postargs
    )
    cc_args = self._get_cc_args(pp_opts, debug, extra_preargs)

    pool = Pool(MAX_PROCS)
    try:
        print("Building using %d processes" % pool._processes)
    except Exception:
        pass
    arr = [(self, obj, build, cc_args, extra_postargs, pp_opts) for obj in objects]
    pool.map_async(_mp_compile_one, arr)
    pool.close()
    pool.join()
    # Return *all* object filenames, not just the ones we just built.
    return objects


def install():

    fl_win = sys.platform.startswith("win")
    fl_cygwin = sys.platform.startswith("cygwin")

    if fl_win or fl_cygwin:
        # Windows barfs on multiprocessing installs
        print("Single threaded build for Windows")
        return

    if MAX_PROCS != 1:
        # explicitly don't enable if environment says 1 processor
        try:
            # bug, only enable if we can make a Pool. see issue #790 and
            # https://stackoverflow.com/questions/6033599/oserror-38-errno-38-with-multiprocessing
            Pool(2)
            CCompiler.compile = _mp_compile
        except Exception as msg:
            print("Exception installing mp_compile, proceeding without: %s" % msg)
    else:
        print(
            "Single threaded build, not installing mp_compile: %s processes" % MAX_PROCS
        )
