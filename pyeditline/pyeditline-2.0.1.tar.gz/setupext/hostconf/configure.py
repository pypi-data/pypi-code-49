#!/usr/bin/python3
"""
Tools for emulating autoconf's inspection abilities in pure (ok, almost) python.

"""

import sys
import os
import sysconfig
import tempfile
import shutil
import subprocess

from pprint import PrettyPrinter

from distutils.errors import DistutilsExecError, CompileError, LinkError
from distutils.ccompiler import new_compiler
from distutils.sysconfig import customize_compiler

import hostconf.backport
from hostconf.config_errors import ConfigureSystemHeaderFileError


class Configure(object):
    """Base class for common support aspects of the configuration process.

    Args:
        name: the name of the configuration instance
        compiler:  specify which compiler to use  (default: distutils)
        tmpdir:  specify a temp-dir to use
        verbose: explain the process as it goes
        dry_run: do not actually do the testing (default: False)
        debug:   engage debug infra (default: False)

    Notes:
        Harvests `distutils` heavily to setup the tooling infra.

    """

    def __init__(self,
                 name='hostconf',
                 compiler=None,
                 tmpdir=None,
                 verbose=0,
                 dry_run=0,
                 debug=False):

        # basic catalogues
        self.cache = {}
        self.config = {}
        self.macros = []  # list of tuples (MACRO, value)
        self.includes = []
        self.include_dirs = []
        self.libraries = []

        # manage arguments
        self.name = name
        self.debug = debug
        self.log = None
        self.ostream = sys.stdout

        if tmpdir is None:
            self.tdir = tempfile.mkdtemp(prefix=name + '_')
        else:
            self.tdir = os.path.join(tmpdir, name)
            if not os.path.isdir(self.tdir):
                os.makedirs(self.tdir)

        # create a log file
        self.log = open(os.path.join(self.tdir, 'config_' + name + '.log'), 'w')

        # initialize our  indexer
        self.conf_idx = 0

        # None - init, False - during, True - Done
        self._checked_stdc = None

        # create the compiler infra
        self.compiler = compiler
        if self.compiler is None:
            self.compiler = new_compiler(verbose=verbose, dry_run=dry_run)
            customize_compiler(self.compiler)

        # add the Python stuff
        self.compiler.include_dirs += [sysconfig.get_config_var('INCLUDEPY')]

        # hook in my spawner
        self._spawn = self.compiler.spawn
        self.compiler.spawn = self.spawn


    def __del__(self):
        """Destructor must tidy up a few things specifically."""
        if self.log:
            self.log.close()

        if not self.debug:
            shutil.rmtree(self.tdir)


    def dump(self):
        """Print out a detailled state of the instance.

        """
        ppt = PrettyPrinter(indent=4)
        print("Configure.config:", file=self.ostream)
        ppt.pprint(self.config)
        print("Configure.cache:", file=self.ostream)
        ppt.pprint(self.cache)
        print("Configure.macros:", file=self.ostream)
        ppt.pprint(self.macros)
        print("Configure.includes:", file=self.ostream)
        ppt.pprint(self.includes)
        print("Configure.include_dirs:", file=self.ostream)
        ppt.pprint(self.include_dirs)
        print("Configure.libraries:", file=self.ostream)
        ppt.pprint(self.libraries)


    @staticmethod
    def _cache_tag(prefix, tag):
        """Create a cache tag name"""
        tag = tag.replace('/', '_')
        tag = tag.replace('.', '_')
        tag = tag.replace(' ', '_')
        return prefix + tag


    @staticmethod
    def _config_tag(prefix, tag):
        """Create a config tag name"""
        tag = tag.replace('.', '_')
        tag = tag.replace('/', '_')
        tag = tag.replace(' ', '_')
        return prefix + tag.upper()


    def generate_config_log(self, config_log):
        """Write out a similar log file format to the config.log

        Args:
            config_log: name of file to create

        """

        fd = open(config_log, 'w')

        fd.write('## ---------------- ##\n')
        fd.write('## Cache variables. ##\n')
        fd.write('## ---------------- ##\n')
        fd.write('\n')

        for key in sorted(self.cache.keys()):
            fd.write('{}={}\n'.format(key, self.cache[key]))

        fd.write('\n')
        fd.write('## ----------------- ##\n')
        fd.write('## Output variables. ##\n')
        fd.write('## ----------------- ##\n')
        fd.write('\n')

        fd.write("LIBS='{}'\n".format(' -l'.join(self.libraries)))

        fd.write('\n')
        fd.write('## ----------- ##\n')
        fd.write('## confdefs.h. ##\n')
        fd.write('## ----------- ##\n')
        fd.write('\n')

        for mname, value in self.macros:
            if value is None:
                value = 1
            fd.write('#define {} {}\n'.format(mname, value))

        # done
        fd.close()


    def generate_config_h(self, config_h, config_h_in):
        """Generate a config.h format file based on the config.h.in template.

        Args:
            config_h:    output filename
            config_h_in: input/template filename

        """

        print("Creating {} from {} ...".format(config_h, config_h_in),
              file=self.ostream)

        # grab the files
        fdin = open(config_h_in, 'r')
        fd = open(config_h, 'w')

        # emulate the extra header
        fd.write('/* config.h.  Generated from config.h.in by pyconfigure.  */'
                 + os.linesep)

        # iterate through the file
        for line in fdin.readlines():

            # migrate uninteresting stuff
            if not line.startswith('#'):
                fd.write(line)
                continue

            # handle uninteresting cpp tokens
            if 'undef' not in line:
                fd.write(line)
                continue

            # chop it up
            pptag, tag = line.rsplit(maxsplit=1)

            # handle easy undefs
            if tag not in self.config:
                fd.write('/* ' + pptag + ' ' + tag + ' */\n')
                continue

            # grab the value
            value = self.config[tag]

            # change undef -> define without modifying whitespace
            pptag = pptag.replace('undef', 'define')

            # finish it up
            fd.write('{} {} {}'.format(pptag, tag, value) + os.linesep)

        # mop up
        fdin.close()
        fd.close()


    def spawn(self, cmd_args):
        """Run a given command and collect information.

        Args:
            cmd_args: list of command-line parameters

        Returns:
            Nothing

        Raises:
            DistutilsExecError -- indicating the problem

        """

        # run it as a subprocess to collect the output
        try:
            self.log.write(' '.join(cmd_args) + os.linesep)
            rv = subprocess.run(
                cmd_args,
                timeout=5,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            rv.check_returncode()
        except subprocess.TimeoutExpired as te_err:
            self.log.write("process timeout ({:d}s) error".format(
                te_err.timeout) + os.linesep)
            self.log.write("stdout output:" + os.linesep)
            self.log.write(str(te_err.output))
            if hasattr(cp_err, 'stderr'):
                self.log.write("stderr output:" + os.linesep)
                self.log.write(str(te_err.stderr))
            raise DistutilsExecError("command %r timed-out." % cmd_args)

        except subprocess.CalledProcessError as cp_err:
            self.log.write("process error: ({:d})".format(cp_err.returncode) +
                           os.linesep)
            if cp_err.output != b'':
                errstrs = cp_err.output.decode('utf-8').split('\n')
                self.log.write("stdout output:" + os.linesep)
                for estr in errstrs:
                    self.log.write(estr + os.linesep)
            if hasattr(cp_err, 'stderr') and cp_err.stderr != b'':
                errstrs = cp_err.stderr.decode('utf-8').split('\n')
                self.log.write("stderr output:" + os.linesep)
                for estr in errstrs:
                    self.log.write(estr + os.linesep)
            raise DistutilsExecError(cp_err)

        # success
        return


    def _conftest_file(self,
                       pre_main=None,
                       main=None,
                       add_config=False,
                       macros=None,
                       header=None,
                       includes=None,
                       include_dirs=None):
        """Create a file and build out the contents for a test.

        Args:
            pre_main:   lines of code to place before main()
            main:       lines of code to place in main()
            add_config: populate the known configuration macros and includes
            macros:     extra macros to define
            header:     primary header file to include
            includes: list of headers to add after the system headers
            include_dirs:  directories to add to the build path

        Returns:
            Filename of the prepared file.

        """

        if includes is None:
            includes = []
        if include_dirs is None:
            include_dirs = []
        if macros is None:
            macros = []

        # need to make these atomic, just in case parallel stuff
        curid = self.conf_idx
        self.conf_idx += 1
        fname = 'conftest_{:03d}'.format(curid)

        # create the file
        fname = os.path.join(self.tdir, fname + '.c')

        # eventually, get the have_* stuff
        conftext = []

        # setup the defs
        if add_config:
            conftext += ['#define {} {}'.format(t, v) for t, v in self.macros]
        conftext += ['#define {} {}'.format(t, v) for t, v in macros]

        # setup the headers
        if add_config:
            conftext += ['#include "%s"' % incl for incl in self.includes]
        conftext += ['#include "%s"' % incl for incl in includes]

        # put the main header after the others
        if header is not None:
            conftext += ['#include "%s"' % header]

        # add in the precode
        if pre_main is not None:
            conftext += pre_main

        # setup the body
        conftext += ['int main(void) {']

        # add in the main code
        if main is not None:
            for line in main:
                conftext.append('    ' + line)

        # close the body
        conftext += ['    return 0;', '}']

        # log it
        for line in conftext:
            self.log.write('| ' + line + os.linesep)

        # create and fill the file
        with open(fname, "w") as outfile:
            outfile.write(os.linesep.join(conftext))

        # just pass back the relative name
        return fname


    def package_info(self, name, version, release, bugreport=None, url=None):
        """Create package information similar to autoconf.

        Args:
            name:        name of package
            version:     version string
            release:     release string
            bugreport:   email address to send bug info
            url:         URL for further info

        Returns:
            Nothing.

        """

        self.add_macro('PACKAGE_NAME', name, quoted=True)
        self.add_macro(
            'PACKAGE_TARNAME', '-'.join([name, release]), quoted=True)
        self.add_macro('PACKAGE_VERSION', version, quoted=True)
        self.add_macro('PACKAGE_STRING', ' '.join([name, version]), quoted=True)
        self.add_macro('PACKAGE_BUGREPORT', bugreport or '', quoted=True)
        self.add_macro('PACKAGE_URL', url or '', quoted=True)
        self.add_macro('PACKAGE', '-'.join([name, release]), quoted=True)
        self.add_macro('VERSION', version, quoted=True)

        # this is not really valid, but should be there
        self.config['LT_OBJDIR'] = '".libs/"'


    def check_msg(self, item, item_in=None, extra=None):
        """Common messaging routine to create autoconf style output.

        Args:
            item:   name of item
            item_in:  component it is inside
            extra:   additional text

        Returns:
            Nothing

        """
        # format the banner
        msg = "checking for " + item
        if item_in is not None:
            msg = msg + " in " + item_in
        if extra is not None:
            msg += ' ' + extra
        msg += " ... "

        # log it
        self.log.write(os.linesep)
        self.log.write('#' * 60 + os.linesep)
        self.log.write(msg + os.linesep)
        self.log.write('#' * len(msg) + os.linesep)

        # print to the terminal without a line ending
        print(msg, end='', file=self.ostream)


    def check_msg_result(self, msg):
        """Common message result in a similar format to autoconf.

        Args:
            msg:  message to display

        Returns:
            Nothing

        """
        logmsg = "result: " + msg
        self.log.write(os.linesep)
        self.log.write('#' * len(logmsg) + os.linesep)
        self.log.write(logmsg + os.linesep)
        self.log.write('#' * 60 + os.linesep * 2)

        print(msg, file=self.ostream)


    def add_macro(self, macro, macro_value, config_value=None, quoted=False):
        """Add a C-Pre-Procesor macro or define to the catalogue.

        Args:
            macro:        name of the macro
            macro_value:  value to assign
            config_value: value to add to the 'config' catalogue if
                          different from macro_value
            quoted:       put the `macro_value` into double-quotes

        Returns:
            Nothing

        """
        if quoted:
            macro_value = '"' + macro_value + '"'
        self.macros.append((macro, macro_value))
        if config_value is None:
            config_value = macro_value
        else:
            if quoted:
                config_value = '"' + config_value + '"'
        self.config[macro] = config_value


    def check_stdc(self):
        """Run a set of very basic checks on the most common items.

        This will update the various catalogues with the results of checking
        the basic C infrastructure files

        """

        # mark that we are "in" check_stdc
        self._checked_stdc = False

        # check ansi headers
        oks = self.check_headers(
            ['stdlib.h', 'stdarg.h', 'string.h', 'float.h'])
        if False not in oks:
            self.add_macro('STDC_HEADERS', 1)

        pre_main = self._get_stdc_header_defs()

        # look for a set of basic headers
        self.check_headers(
            [
                'sys/types.h', 'sys/stat.h', 'stdlib.h', 'string.h', 'memory.h',
                'strings.h', 'inttypes.h', 'stdint.h', 'unistd.h'
            ],
            macros=self.macros,
            pre_main=pre_main)

        # flag that the std checks are done
        self._checked_stdc = True


    def _get_stdc_header_defs(self):
        """Generate a common set of header file and macro exclusions for
        `standard-c` type usage.
        """
        pre_main_text = '''
        #include <stdio.h>
        #ifdef HAVE_SYS_TYPES_H
        # include <sys/types.h>
        #endif
        #ifdef HAVE_SYS_STAT_H
        # include <sys/stat.h>
        #endif
        #ifdef STDC_HEADERS
        # include <stdlib.h>
        # include <stddef.h>
        #else
        # ifdef HAVE_STDLIB_H
        #  include <stdlib.h>
        # endif
        #endif
        #ifdef HAVE_STRING_H
        # if !defined STDC_HEADERS && defined HAVE_MEMORY_H
        #  include <memory.h>
        # endif
        # include <string.h>
        #endif
        #ifdef HAVE_STRINGS_H
        # include <strings.h>
        #endif
        #ifdef HAVE_INTTYPES_H
        # include <inttypes.h>
        #endif
        #ifdef HAVE_STDINT_H
        # include <stdint.h>
        #endif
        #ifdef HAVE_UNISTD_H
        # include <unistd.h>
        #endif
        '''
        pre_main = []
        for line in pre_main_text.split(os.linesep):
            pre_main.append(line.strip())
        return pre_main


    def _check_compile(self,
                       main=None,
                       pre_main=None,
                       add_config=False,
                       macros=None,
                       includes=None,
                       include_dirs=None):
        """Compile a file incorporating the given parameters.

        Args:
            main:       lines of code to place in main()
            pre_main:   lines of code to place before main()
            add_config: populate the known configuration macros and includes
            macros:     extra macros to define
            includes: list of headers to add after the system headers
            include_dirs:  directories to add to the build path

        Returns:
            boolean -- True on successful compile

        """

        # just setup the file
        ctfname = self._conftest_file(
            macros=macros,
            includes=includes,
            add_config=add_config,
            pre_main=pre_main,
            main=main)

        # try to compile it
        try:
            _ = self.compiler.compile(
                [ctfname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(ctfname)
            )
        except CompileError:
            return False

        return True

    def _check_run(self,
                   main=None,
                   pre_main=None,
                   macros=None,
                   includes=None,
                   include_dirs=None,
                   library_dirs=None):
        """Compile, link and RUN a file incorporating the given parameters.

        Args:
            main:       lines of code to place in main()
            pre_main:   lines of code to place before main()
            add_config: populate the known configuration macros and includes
            macros:     extra macros to define
            includes: list of headers to add after the system headers
            include_dirs:  directories to add to the build path

        Returns:
            boolean -- True on successful run

        """

        # just setup the file
        ctfname = self._conftest_file(
            macros=macros, includes=includes, pre_main=pre_main, main=main)

        # try to compile it
        try:
            objects = self.compiler.compile(
                [ctfname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(ctfname),
            )
        except CompileError:
            return False

        # test file
        exe_file = os.path.basename(ctfname.replace('.c', ''))

        # now try to link it...
        try:
            self.compiler.link_executable(
                objects,
                exe_file,
                output_dir=os.path.dirname(ctfname),
                library_dirs=library_dirs)
        except LinkError:
            return False

        # run it
        try:
            self.spawn([os.path.join(self.tdir, exe_file)])
        except DistutilsExecError:
            return False

        # success...
        return True


    def check_python(self):
        """Verify that we can actually build something to bind to Python."""

        #SHLIBS = "-lpthread -ldl  -lutil"
        #PY_LDFLAGS = "-Wl,-Bsymbolic-functions -Wl,-z,relro"
        #OPT = "-DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes"
        #CONFINCLUDEPY = "/usr/include/python3.5m"
        #DESTLIB = "/usr/lib/python3.5"
        #BLDLIBRARY = "-lpython3.5m"

        #BLDSHARED = "x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1
        #                                  -Wl,-Bsymbolic-functions
        #                                  -Wl,-Bsymbolic-functions
        #                                  -Wl,-z,relro"
        raise NotImplementedError


    def _check_tool(self, tool, tool_args=None):
        """Verify that a given tool is available on the command-line.

        Args:
            tool:  name of the tool
            tool_args: optional arguments for the tool

        Returns:
            boolean -- True if the tool is present
            int     -- return code from the execution

        """
        rv = None

        if tool_args is None:
            tool_args = ['--garbage']

        try:
            rv = subprocess.run(
                [tool] + tool_args,
                timeout=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        except FileNotFoundError:
            # tool is not available
            return False, rv
        except PermissionError:
            # found something but it is not executable
            return False, rv
        except subprocess.TimeoutExpired:
            # ran it and it wedged
            return False, rv
        except subprocess.CalledProcessError:
            # ran it and it failed, but got an exit code
            return True, rv

        # all good
        return True, rv


    def check_tool(self, tool, tool_args=None, verbose=True):
        """Try to locate a tool.

        Args:
            tool:  name of the tool
            tool_args: optional arguments for the tool
            verbose: add detail to the output

        Returns:
            boolean -- True if the tool is present

        """

        # setup the message
        if verbose:
            self.check_msg(tool, extra="tool")

        # snoop it
        ok, _ = self._check_tool(tool=tool, tool_args=tool_args)

        if ok:
            if verbose:
                self.check_msg_result(tool)
            return True

        if verbose:
            self.check_msg_result('unavailable')
        return False


    def check_headers(self,
                      headers,
                      includes=None,
                      include_dirs=None,
                      macros=None,
                      pre_main=None):
        """Check for the presence and usability of a set of headers.

        Args:
            headers:    list of header file names to check
            includes: list of headers to add after the system headers
            include_dirs:  directories to add to the build path
            macros:     extra macros to define
            pre_main:   lines of code to place before main()

        Returns:
            listof booleans -- True indicates the the successful inspection
                               of that particular header file.

        Notes:
            Equivalent to AC_CHECK_HEADERS

        """
        results = []

        for header in headers:
            rv = self.check_header(
                header,
                includes=includes,
                include_dirs=include_dirs,
                macros=macros,
                pre_main=pre_main)
            results.append(rv)

        return results


    def check_header(self,
                     header,
                     includes=None,
                     include_dirs=None,
                     macros=None,
                     pre_main=None,
                     add_config=False):
        """Check for the presence and usability of a set of headers.

        Args:
            headers:    list of header file names to check
            includes: list of headers to add after the system headers
            include_dirs:  directories to add to the build path
            macros:     extra macros to define
            pre_main:   lines of code to place before main()
            add_to_catalogue:  optional - add to defaults

        Returns:
            boolean -- True indicates the the successful inspection
                       of that particular header file.

        Notes:
            Equivalent to AC_CHECK_HEADER

        """

        # hook to be sure we do the std stuff first
        if not self._checked_stdc and self._checked_stdc is None:
            self.check_stdc()

        # setup the message
        self.check_msg(header)

        # determine the tags
        cache_tag = self._cache_tag('ac_cv_header_', header)
        config_tag = self._config_tag('HAVE_', header)
        cache_loc = 'cached'

        # check the sysconfig
        #rv = sysconfig.get_config_var(config_tag)
        rv = False
        if rv:
            self.macros.append((config_tag, 1))
            self.includes.append(header)
            self.config[config_tag] = rv
            self.cache[cache_tag] = 'yes'
            cache_loc = 'sysconfig'

        # cache check
        if cache_tag in self.cache and self.cache[cache_tag] == 'yes':
            self.check_msg_result(self.cache[cache_tag] +
                                  ' ({})'.format(cache_loc))
            return True

        # assume the worst
        self.cache[cache_tag] = 'no'

        # create the conftest file
        fname = self._conftest_file(
            header=header, includes=includes, macros=macros,
            pre_main=pre_main, add_config=add_config)

        # try to compile it
        try:
            _ = self.compiler.compile(
                [fname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(fname)
            )
        except CompileError:
            self.check_msg_result('no')
            return False

        # inventory
        self.macros.append((config_tag, 1))
        self.includes.append(header)
        self.config[config_tag] = 1

        # cache update
        self.cache[cache_tag] = 'yes'

        # done
        self.check_msg_result('yes')
        return True


    def check_lib(self,
                  funcname,
                  library=None,
                  includes=None,
                  include_dirs=None,
                  libraries=None,
                  library_dirs=None,
                  msg_add_libs=False):
        """Check for the presence and usability of a function in a library.

        Args:
            funcname:     name of function to check in a library
            library:      optional specific library to include
            includes:     optional list of headers to add after the
                          system headers
            include_dirs: optional directories to add to the build path
            libraries:    optional list of libraries to add to the link command
            library_dirs: optional directories to add to the linker path
            msg_add_libs: optional report which libraries are being added to
                          the output

        Returns:
            listof booleans -- True indicates the the successful inspection
                               of that particular header file.

        Notes:
            Equivalent to AC_CHECK_LIB

        """

        # hook to be sure we do the std stuff first
        if not self._checked_stdc and self._checked_stdc is None:
            self.check_stdc()

        # adjust arguments
        if includes is None:
            includes = []
        if include_dirs is None:
            include_dirs = []
        if libraries is None:
            libraries = []
        if library_dirs is None:
            library_dirs = []

        # create a local list and remove the empty string
        #  as it will screw up the cmdline
        local_libs = [x for x in libraries if x != '']

        # handle the case where we're looking in the 'standar libraries'
        if library is None:
            libmsg = 'stdlibs'
            dashl = ''
        else:
            dashl = '-l' + library
            local_libs.insert(0, library)
            libmsg = dashl

        # provide a bit of extra info on the lib linking
        if msg_add_libs:
            for exlib in libraries:
                if exlib != '':
                    libmsg += ' -l' + exlib

        self.check_msg(funcname, item_in=libmsg)

        # determine the tags
        cache_tag = self._cache_tag('ac_cv_func_', funcname)
        config_tag = self._config_tag('HAVE_', funcname)

        # check the sysconfig
        rv = sysconfig.get_config_var(config_tag)
        if rv:
            self.add_macro(config_tag, 1, rv)
            self.cache[cache_tag] = 'yes'

        # cache check
        if cache_tag in self.cache and self.cache[cache_tag] == 'yes':
            self.check_msg_result(self.cache[cache_tag] + ' (cached)')
            return True

        # assume the worst
        self.cache[cache_tag] = 'no'

        # create the conftest file
        fname = self._conftest_file(
            includes=includes,
            pre_main=['char {}(void);'.format(funcname)],
            main=['    {}();'.format(funcname)])
        # the declaration is as it is because of -Wstrict-prototypes

        # try to compile it
        try:
            objects = self.compiler.compile(
                [fname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(fname)
            )
        except CompileError:
            print('no', file=self.ostream)
            return False

        # link it
        try:
            self.compiler.link_executable(
                objects,
                os.path.basename(fname.replace('.c', '')),
                output_dir=os.path.dirname(fname),
                libraries=local_libs,
                library_dirs=library_dirs)
        except (LinkError, TypeError):
            self.check_msg_result('no')
            return False

        # add the new library only if it is not there
        if library is not None and library not in self.libraries:
            self.libraries.append(library)

        # inventory
        self.config[config_tag] = 1
        if library is not None and library != '':
            lib_tag = self._config_tag('HAVE_LIB', library)
            self.config[lib_tag] = 1

        # update the cache
        self.cache[cache_tag] = 'yes'

        self.check_msg_result('yes')
        return True


    def check_lib_link(self,
                       funcname,
                       library,
                       includes=None,
                       include_dirs=None,
                       libraries=None,
                       library_dirs=None):
        """Verify which extra libraries are needed to link the given lib

        Args:
            funcname:     name of function to check in a library
            library:      optional specific library to include
            includes:     optional list of headers to add after the
                          system headers
            include_dirs: optional directories to add to the build path
            libraries:    optional list of libraries to add to the link command
            library_dirs: optional directories to add to the linker path

        Returns:
            list of libs - libraries needed to link the function and lib.
                         - May return `None` when all linking fails

        Notes:
            This has no specific autoconf counterpart.

        """

        # need this to be a list
        if libraries is None:
            libraries = []

        # add the case where the library needs nothing
        if '' not in libraries:
            libraries.insert(0, '')

        # remember the pre-state
        save_libs = self.libraries

        # check each library in turn
        for testlib in libraries:

            # reset the list of libraries
            self.libraries = []

            # check the library by itself
            if self.check_lib(
                    funcname,
                    library,
                    libraries=[testlib],
                    includes=includes,
                    include_dirs=include_dirs,
                    library_dirs=library_dirs,
                    msg_add_libs=True):
                return [testlib]

        # full restore
        self.libraries = save_libs

        # hmm. nothing worked
        return None


    def check_decl(self,
                   decl,
                   header,
                   includes=None,
                   include_dirs=None,
                   main=None):
        """Verify a declaration is available in a header file.

        Args:
            decl:         name of function to check in a library
            header:       header file to inspect
            includes:     optional list of headers to add after the
                          system headers
            include_dirs: optional directories to add to the build path
            main:         optional extra code lines for the main() function

        Returns:
            boolean -- True if the declaration is available.

        Notes:
            Equivalent to AC_CHECK_DECL.

        """

        # hook to be sure we do the std stuff first
        if not self._checked_stdc and self._checked_stdc is None:
            self.check_stdc()

        # setup the message
        self.check_msg(decl, header)

        # cache check
        cache_tag = self._cache_tag('ac_cv_func_', decl)
        if cache_tag in self.cache and self.cache[cache_tag] == 'yes':
            self.check_msg_result(self.cache[cache_tag] + ' (cached)')
            return True

        # assume the worst
        self.cache[cache_tag] = 'no'

        if main is None:
            main = [
                '#ifndef {0}'.format(decl), '#ifdef __cplusplus',
                '  (void) {0};'.format(decl), '#else',
                '  (void) {0};'.format(decl), '#endif', '#endif'
            ]

        # create the conftest file
        fname = self._conftest_file(header=header, includes=includes, main=main)

        # try to compile it
        try:
            _ = self.compiler.compile(
                [fname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(fname)
            )
        except CompileError:
            self.check_msg_result('no')
            return False

        # inventory
        tag = self._config_tag('HAVE_DECL_', decl)
        self.add_macro(tag, 1)

        # update the cache
        self.cache[cache_tag] = 'yes'

        # done
        self.check_msg_result('yes')
        return True


    def _check_common(self,
                      main,
                      cache_tag,
                      config_tag,
                      msg,
                      msg_in=None,
                      msg_extra=None,
                      add_config=False,
                      includes=None,
                      include_dirs=None):
        """Common code for generic checks

        Args:
            main:         lines of code to put in main()
            cache_tag:    string used in the cache catalogue
            config_tag:   string used in the config catalogue
            msg:          string message for console display
            msg_in:       optional text for checking inside something else
            msg_extra:    optional extra text for display
            add_config:   populate the known configuration macros and includes
            includes:     optional list of headers to add after the
                          system headers
            include_dirs: optional directories to add to the build path

        Returns:
            boolean:  True if available.

        """

        # hook to be sure we do the std stuff first
        if not self._checked_stdc and self._checked_stdc is None:
            self.check_stdc()

        if includes is None:
            includes = []
        if include_dirs is None:
            include_dirs = []

        # setup the message
        self.check_msg(msg, msg_in, msg_extra)

        # cache check
        if cache_tag in self.cache and self.cache[cache_tag] == 'yes':
            self.check_msg_result(self.cache[cache_tag] + ' (cached)')
            return True

        # assume the worst
        self.cache[cache_tag] = 'no'

        # create the conftest file
        fname = self._conftest_file(
            includes=includes, add_config=add_config, main=main)

        # try to compile it
        try:
            _ = self.compiler.compile(
                [fname],
                include_dirs=include_dirs
                #output_dir=os.path.dirname(fname)
            )
        except CompileError:
            self.check_msg_result('no')
            return False

        # inventory
        self.add_macro(config_tag, 1)
        self.cache[cache_tag] = 'yes'

        # done
        self.check_msg_result('yes')
        return True


    def check_type(self, type_name, includes=None, include_dirs=None):
        """Inspect the system to see if it supports a specific C/C++ type-name

        Args:
            type_name:    C type-name to check for
            includes:     optional - headers to add after the system headers
            include_dirs: optional - directories to add to the build path

        Returns:
            boolean:  True if available.

        Notes:
            Emulate AC_CHECK_TYPES

        """
        cache_tag = self._cache_tag('ac_cv_type_', type_name)
        config_tag = self._config_tag('HAVE_', type_name)
        main = ['if (sizeof ({})) {{'.format(type_name), '    return 0;', '}']
        return self._check_common(
            main,
            cache_tag,
            config_tag,
            add_config=True,
            msg=type_name,
            includes=includes,
            include_dirs=include_dirs)


    def check_member(self,
                     type_name,
                     member_name,
                     includes=None,
                     include_dirs=None):
        """Inspect the system to see if it supports a specific C/C++ type-name

        Args:
            type_name:    C/C++ type name or struct name
            member_name:  structure member-name to check
            includes:     optional - headers to add after the system headers
            include_dirs: optional - directories to add to the build path

        Returns:
            boolean:  True if available.

        Notes:
            Emulate AC_CHECK_MEMBER

        """
        cache_tag = self._cache_tag('ac_cv_type_',
                                    type_name + '_' + member_name)
        config_tag = self._config_tag('HAVE_', type_name + '_' + member_name)
        main = [
            'static {} ac_aggr;'.format(type_name),
            'if (ac_aggr.{}) {{'.format(member_name), '    return 0;', '}'
        ]

        # bail if we don't even have the type
        ok = self.check_type(
            type_name, includes=includes, include_dirs=include_dirs)
        if not ok:
            return False

        # ok, see if the member is valid
        return self._check_common(
            main,
            cache_tag,
            config_tag,
            add_config=True,
            msg=member_name,
            msg_in=type_name,
            includes=includes,
            include_dirs=include_dirs)


    def check_use_system_extensions(self):
        """Verify if the system uses standard system-extension definitions

        Args:
            None

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_USE_SYSTEM_EXTENSIONS

        """

        # setup the message
        self.check_msg('system extensions')

        pre_main = self._get_stdc_header_defs()

        ok = self._check_compile(
            macros=self.macros,
            pre_main=['#define __EXTENSIONS__ 1'] + pre_main)
        if ok:
            self.check_msg_result('yes')
            self.add_macro('__EXTENSIONS__', 1)
            self.add_macro('_ALL_SOURCE', 1)
            self.add_macro('_GNU_SOURCE', 1)
            self.add_macro('_POSIX_PTHREAD_SEMANTICS', 1)
            self.add_macro('_TANDEM_SOURCE', 1)
        else:
            self.check_msg_result('no')

        return ok


    def check_header_dirent(self):
        """Inspect headers available which implement `dirent`.

        Args:
            None

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_HEADER_DIRENT

        """
        for header in ['dirent.h', 'sys/ndir.h', 'sys/dir.h', 'ndir.h']:
            ok = self.check_decl(
                'DIR',
                header,
                includes=['sys/types.h'],
                main=['if ((DIR *) 0) {', '   return 0;', '}'])
            if ok:
                tag = self._config_tag('HAVE_', header)
                self.add_macro(tag, 1)
                return True
        return False


    def check_header_sys_wait(self):
        """Inspect the system's availability of sys/wait.h

        Args:
            None.

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_HEADER_SYS_WAIT

        """
        return self.check_header('sys/wait.h', includes=['sys/types.h'])


    def check_type_signal(self):
        """Inspect the system usage and type of `signal`.

        Args:
            None.

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_TYPE_SIGNAL

        """
        cache_tag = self._cache_tag('ac_cv_type_', 'signal')

        # check the sysconfig
        rv = sysconfig.get_config_var('RETSIGTYPE')
        if rv:
            self.cache[cache_tag] = 'void'
            self.add_macro('RETSIGTYPE', 'void')
            return True

        # estimate it
        ok = self.check_header('sys/signal.h', includes=['sys/types.h'])
        if ok:
            self.cache[cache_tag] = 'void'
            self.add_macro('RETSIGTYPE', 'void')
        return ok

    #AC_C_CONST


    def check_type_pid_t(self):
        """Inspect the system type name for `pid_t`.

        Args:
            None.

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_TYPE_PID_T

        """
        rv = sysconfig.get_config_var('SIZEOF_PID_T')
        if rv:
            self.add_macro('HAVE_PID_T', rv)
            return True
        return self.check_type('pid_t')


    def check_type_size_t(self):
        """Inspect the system type name for `size_t`.

        Args:
            None.

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_TYPE_SIZE_T

        """
        rv = sysconfig.get_config_var('SIZEOF_SSIZE_T')
        if rv:
            self.add_macro('HAVE_SIZE_T', rv)
            return True
        return self.check_type('size_t')

    #AC_FUNC_CLOSEDIR_VOID

    def check_func_fork(self, fcn='fork'):
        """Inspect the system for unix `fork` function.

        Args:
            fcn:  supply the 'fork' function name (default: fork)

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_FUNC_FORK

        """
        rv = False

        # got to have this to work
        if not self.check_type_pid_t():
            return rv

        self.check_msg(fcn)

        # setup the tags
        havef = self._config_tag('HAVE_', fcn)
        chf = self._cache_tag('ac_cv_func_', fcn)
        have_wf = self._config_tag('HAVE_WORKING_', fcn)
        chwf = chf + '_working'

        # python check this already?
        ok = sysconfig.get_config_var(havef)
        if ok:
            self.add_macro(havef, 1)
            self.cache[chf] = 'yes'
            rv = True
        else:
            # ok, see if it is there
            ok = self.check_lib(fcn)
            if ok:
                self.add_macro(havef, 1)
                self.cache[chf] = 'yes'
                rv = True

        # check for it working...
        ok = sysconfig.get_config_var(have_wf)
        if ok:
            self.add_macro(have_wf, 1)
            self.cache[chwf] = 'yes'
            rv = True
        else:
            # assuming this for now...
            self.add_macro(have_wf, 1)
            self.cache[chwf] = 'yes'
            rv = True

        # update banner
        if rv:
            self.check_msg_result('yes')
        else:
            self.check_msg_result('no')

        return rv


    def check_func_vfork(self):
        """Inspect the system for unix `vfork` function.

        Args:
            None.

        Returns:
            boolean:  True if available.

        Notes:
            Emulates AC_FUNC_VFORK

        """
        # setup the defs
        self.check_header('vfork.h')

        # check the function
        return self.check_func_fork(fcn='vfork')

    #AC_PROG_GCC_TRADITIONAL

    def check_func_stat(self):
        """Check for the availability of `stat()`

        Args:
            None

        Returns:
            Boolean:  True if available

        Notes:
            Emulate AC_FUNC_STAT

        """
        self.check_header('sys/stat.h')
        return self.check_lib('stat')

    def check_func_lstat(self):
        """Check for the availability of `lstat()`

        Args:
            None

        Returns:
            Boolean:  True if available

        Notes:
            Emulate AC_FUNC_LSTAT

        """
        # do we have it
        ok = self.check_lib('lstat')
        if not ok:
            return False

        # should check if it does proper dereferencing
        self.check_msg('whether lstat correctly handles trailing slash')

        # test files
        testfile = os.path.join(self.tdir, 'conftest_lstat.file')
        symfile = testfile.replace('.file', '.sym')

        # tidy up
        try:
            os.unlink(testfile)
        except FileNotFoundError:
            pass
        try:
            os.unlink(symfile)
        except FileNotFoundError:
            pass

        # lastly, run it...
        try:
            # make a basic file
            with open(testfile, 'w') as tfd:
                tfd.write('garbage' + os.linesep)

            # setup the framework
            os.symlink(testfile, symfile)

        except NotImplementedError:
            self.log.write("failed to create symlink for test: " + symfile)
            return False

        # compile and run
        ok = self._check_run(
            main=[
                'struct stat sbuf;',
                'return lstat ("{}/", &sbuf) == 0;'.format(symfile)
            ],
            includes=self.includes)

        if not ok:
            self.check_msg_result('no')
            return False

        # setup the macro for the special functionality
        self.add_macro('LSTAT_FOLLOWS_SLASHED_SYMLINK', 1)
        self.check_msg_result('yes')
        return True


    def check_getpw_r__posix(self):
        """Check if `getpw*_R()` routines are POSIX-like.

        Args:
            None

        Returns:
            Boolean:  True if available

        Notes:
            Emulates AC_FUNC_GETPW_R_POSIX

        """
        self.check_msg('getpw*_r are posix like')

        ok = self._check_compile(
            includes=['stdlib.h', 'sys/types.h', 'pwd.h'],
            add_config=True,
            main=[
                'getpwnam_r(NULL, NULL, NULL, (size_t)0, NULL);',
                'getpwuid_r((uid_t)0, NULL, NULL, (size_t)0, NULL);'
            ])

        if not ok:
            self.check_msg_result('no')
            return False

        self.check_msg_result('yes')
        self.add_macro('HAVE_GETPW_R_POSIX', 1)
        return True


    def check_getpw_r__draft(self):
        """Check if `getpw*_R()` routines are POSIX-draft-like.

        Args:
            None

        Returns:
            Boolean:  True if available

        Notes:
            Emulates AC_FUNC_GETPW_R_DRAFT

        """
        self.check_msg('getpw*_r are draft like')

        ok = self._check_compile(
            includes=['stdlib.h', 'sys/types.h', 'pwd.h'],
            add_config=True,
            main=[
                'getpwnam_r(NULL, NULL, NULL, (size_t)0);',
                'getpwuid_r((uid_t)0, NULL, NULL, (size_t)0);'
            ])

        if not ok:
            self.check_msg_result('no')
            return False

        self.check_msg_result('yes')
        self.add_macro('HAVE_GETPW_R_DRAFT', 1)
        return True


def check_system():
    """Run the system inspection to create config.h"""
    # setup the configurator
    ctool = Configure('conf_edit', debug=True, tmpdir='/tmp/conf_test')
    ctool.package_info('libedit', '3.1', '20180321')

    # early items...
    ctool.check_stdc()
    ctool.check_use_system_extensions()

    # check for the necessary system header files
    ctool.check_headers([
        'fcntl.h', 'limits.h', 'malloc.h', 'stdlib.h', 'string.h',
        'sys/ioctl.h', 'sys/param.h', 'unistd.h', 'sys/cdefs.h', 'dlfcn.h',
        'inttypes.h'
    ])

    # some uncommon headers
    ctool.check_header_dirent()
    ctool.check_header_sys_wait()

    # figure out which terminal lib we have
    for testlib in ['tinfo', 'ncurses', 'ncursesw', 'curses', 'termcap']:
        ok = ctool.check_lib('tgetent', testlib)
        if ok:
            break

    # check for terminal headers
    term_headers = ['curses.h', 'ncurses.h', 'termcap.h']
    oks = ctool.check_headers(term_headers)
    if True not in oks:
        raise ConfigureSystemHeaderFileError(term_headers)

    # must have termios.h
    ok = ctool.check_header('termios.h')
    if not ok:
        raise ConfigureSystemHeaderFileError(['termios.h'])

    # must have term.h
    ctool.check_header('term.h')

    #AC_C_CONST
    ctool.check_type_pid_t()
    ctool.check_type_size_t()
    ctool.check_type('u_int32_t')

    #AC_FUNC_CLOSEDIR_VOID
    ctool.check_func_fork()
    ctool.check_func_vfork()
    #AC_PROG_GCC_TRADITIONAL
    ctool.check_type_signal()
    #AC_FUNC_STAT

    # check for bsd/string.h -- mainly for linux
    ok = ctool.check_header('bsd/string.h')
    if ok:
        ctool.check_lib('strlcpy', 'bsd')

    # check a bunch of standard-ish functions
    fcns = [
        'endpwent', 'isascii', 'memchr', 'memset', 're_comp', 'regcomp',
        'strcasecmp', 'strchr', 'strcspn', 'strdup', 'strerror', 'strrchr',
        'strstr', 'strtol', 'issetugid', 'wcsdup', 'strlcpy', 'strlcat',
        'getline', 'vis', 'strvis', 'unvis', 'strunvis', '__secure_getenv',
        'secure_getenv'
    ]
    for fcn in fcns:
        ctool.check_lib(fcn, libraries=ctool.libraries)

    ctool.check_func_lstat()

    # these probably should be local
    ctool.check_getpw_r__posix()
    ctool.check_getpw_r__draft()

    #print("exlibs3:", exlibs)
    #print("libs3:", ctool.libraries)

    ctool.dump()

    # looks good - add the extra libraries if any
    #clib['libraries'] += ctool.libraries

    # locate the config template and output
    #config_h = os.path.join(self.build_temp, self.libedit_dir, 'config.h')
    #config_h_in = os.path.join(self.libedit_dir, 'config.h.in')
    config_h = '/tmp/config.h'
    config_h_in = '/home/mjn/work/python/pe-test/src/libedit/config.h.in'

    # barf out the config.h file from config.h.in
    ctool.generate_config_h(config_h, config_h_in)
    ctool.generate_config_log(config_h.replace('.h', '.log'))

    # done
    return ctool


if __name__ == '__main__':
    check_system()
