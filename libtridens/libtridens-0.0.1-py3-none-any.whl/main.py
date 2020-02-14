"""
pasteurize: automatic conversion of Python 3 code to clean 2/3 code
===================================================================

``pasteurize`` attempts to convert existing Python 3 code into source-compatible
Python 2 and 3 code.

Use it like this on Python 3 code:

  $ pasteurize --verbose mypython3script.py

This removes any Py3-only syntax (e.g. new metaclasses) and adds these
import lines:

    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    from __future__ import unicode_literals
    from future import standard_library
    standard_library.install_hooks()
    from builtins import *

To write changes to the files, use the -w flag.

It also adds any other wrappers needed for Py2/3 compatibility.

Note that separate stages are not available (or needed) when converting from
Python 3 with ``pasteurize`` as they are when converting from Python 2 with
``futurize``.

The --all-imports option forces adding all ``__future__`` imports,
``builtins`` imports, and standard library aliases, even if they don't
seem necessary for the current state of each module. (This can simplify
testing, and can reduce the need to think about Py2 compatibility when editing
the code further.)

"""

from __future__ import (print_function, unicode_literals)

import sys
import logging
import optparse
from lib2to3.main import main, warn, StdoutRefactoringTool
from lib2to3 import refactor

from .fixes import get_fixers
from . import fixes as fx

__version__ = '0.0.1'


exclude = set([  # these either don't work or are turned off by default
                 'libpasteurize.fixes.fix_bitlength',  
                 'libpasteurize.fixes.fix_bool',    
                 'libpasteurize.fixes.fix_bytes',   
                 'libpasteurize.fixes.fix_classdecorator',  
                 'libpasteurize.fixes.fix_collections',
                 'libpasteurize.fixes.fix_dctsetcomp',  
                 'libpasteurize.fixes.fix_except',   
                 'libpasteurize.fixes.fix_features',  
                 'libpasteurize.fixes.fix_funcattrs',
                 'libpasteurize.fixes.fix_input',
                 'libpasteurize.fixes.fix_int',
                 'libpasteurize.fixes.fix_intern',
                 'libpasteurize.fixes.fix_itertools',
                 'libpasteurize.fixes.fix_memoryview',
                 'libpasteurize.fixes.fix_metaclass',  
                 'libpasteurize.fixes.fix_methodattrs',  
                 'libpasteurize.fixes.fix_next',   
                 'libpasteurize.fixes.fix_numliterals',   
                 'libpasteurize.fixes.fix_open',   
                 'libpasteurize.fixes.fix_print',  
                 'libpasteurize.fixes.fix_raise_',   
                 'libpasteurize.fixes.fix_range',  
                 'libpasteurize.fixes.fix_reduce',
                 'libpasteurize.fixes.fix_setliteral',
                 'libpasteurize.fixes.fix_str',
                 'libpasteurize.fixes.fix_super',  
                 'libpasteurize.fixes.fix_unittest',
                 'libpasteurize.fixes.fix_with',
                ])


def name_handler(fix, avail_fixes):
    # Infer the full module name for the fixer.
    # First ensure that no names clash (e.g.
    # lib2to3.fixes.fix_blah and libtridens.libpasteurize.fixes.fix_blah):
    found = [f for f in avail_fixes
                if f.endswith('fix_{0}'.format(fix))]
    if len(found) > 1:
        print("Ambiguous fixer name. Choose a fully qualified "
                "module name instead from these:\n" +
                "\n".join("  " + myf for myf in found),
                file=sys.stderr)
        return None
    elif len(found) == 0:
        print("Unknown fixer. Use --list-fixes or -l for a list.",
                file=sys.stderr)
        return None
    else:
        return found[0]


def main(args=None):
    """Main program.

    Returns a suggested exit status (0, 1, 2).
    """
    # Set up option parser
    parser = optparse.OptionParser(usage="pasteurize [options] file|dir ...")
    parser.add_option("-V", "--version", action="store_true",
                      help="Report the version number of pasteurize")
    parser.add_option("-a", "--all-imports", action="store_true",
                      help="Adds all __future__ and future imports to each module")
    parser.add_option("-f", "--fix", action="append", default=[],
                      help="Each FIX specifies a transformation; default: all")
    parser.add_option("-j", "--processes", action="store", default=1,
                      type="int", help="Run 2to3 concurrently")
    parser.add_option("-x", "--nofix", action="append", default=[],
                      help="Prevent a fixer from being run.")
    parser.add_option("-l", "--list-fixes", action="store_true",
                      help="List available transformations")
    # parser.add_option("-p", "--print-function", action="store_true",
    #                   help="Modify the grammar so that print() is a function")
    parser.add_option("-v", "--verbose", action="store_true",
                      help="More verbose logging")
    parser.add_option("--no-diffs", action="store_true",
                      help="Don't show diffs of the refactoring")
    parser.add_option("-w", "--write", action="store_true",
                      help="Write back modified files")
    parser.add_option("-n", "--nobackups", action="store_true", default=False,
                      help="Don't write backups for modified files.")
    parser.add_option("-i", "--install", action="store", type="str")
    parser.add_option("-u", "--uninstall", action="store", type="str")

    # Parse command line arguments
    refactor_stdin = False
    flags = {}
    options, args = parser.parse_args(args)
    fixer_pkg = 'libtridens.libpasteurize.fixes'
    flags["print_function"] = True

    # when installing/uninstalling fixers:
    if options.install:
        fx.install_fixer(options.install)
        return 0
    elif options.uninstall:
        fx.uninstall_fixer(options.uninstall)
        return 0

    # set available fixers as ones that are excluded by default
    # plus those that are excluded at runtime by the user
    if options.nofix:
        for a in options.nofix:
            # we assume that a full name for fixer would be sth like blah.fix_blahhh_blahhh
            # and we assume that when there is no dot before the `fix` keyword we are dealing with
            # a full name
            if '.fix_' in a:
                exclude.add(a)
            else:
                # otherwise we need to infer the full name from available fixers
                full_name = name_handler(a, get_fixers(fx, exclude=exclude))
                if full_name:
                    exclude.add(full_name)
    
    # after the excluded fixers are updated, get the list that will be used:
    avail_fixes = get_fixers(fx, exclude=exclude)

    if not options.write and options.no_diffs:
        warn("not writing files and not printing diffs; that's not very useful")
    if not options.write and options.nobackups:
        parser.error("Can't use -n without -w")
    if options.version:
        print(__version__)
        return 0
    if options.list_fixes:
        print("Available transformations for the -f/--fix option:")
        for fixname in sorted(avail_fixes):
            print(fixname)
        if not args:
            return 0
    if not args:
        print("At least one file or directory argument required.",
              file=sys.stderr)
        print("Use --help to show usage.", file=sys.stderr)
        return 2
    if "-" in args:
        refactor_stdin = True
        if options.write:
            print("Can't write to stdin.", file=sys.stderr)
            return 2

    # Set up logging handler
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format='%(name)s: %(message)s', level=level)

    explicit = set()
    if options.fix:
        all_present = False
        for fix in options.fix:
            if fix == 'all':
                all_present = True
            else:
                if ".fix_" in fix:
                    explicit.add(fix)
                else:
                    full_name = name_handler(fix, avail_fixes)
                    if full_name:
                        explicit.add(full_name)
        if len(explicit & exclude) > 0:
            print("Conflicting usage: the following fixers have been "
                  "simultaneously requested and disallowed:\n" +
                  "\n".join("  " + myf for myf in (explicit & exclude)),
                  file=sys.stderr)
            return 2
        requested = avail_fixes.union(explicit) if all_present else explicit
    else:
        requested = avail_fixes.union(explicit)

    fixer_names = requested

    # Initialize the refactoring tool
    rt = StdoutRefactoringTool(sorted(fixer_names), flags, set(),
                               options.nobackups, not options.no_diffs)

    # Refactor all files and directories passed as arguments
    if not rt.errors:
        if refactor_stdin:
            rt.refactor_stdin()
        else:
            try:
                rt.refactor(args, options.write, None,
                            options.processes)
            except refactor.MultiprocessingUnsupported:
                assert options.processes > 1
                print("Sorry, -j isn't " \
                      "supported on this platform.", file=sys.stderr)
                return 1
        rt.summarize()

    # Return error status (0 if rt.errors is zero)
    return int(bool(rt.errors))
