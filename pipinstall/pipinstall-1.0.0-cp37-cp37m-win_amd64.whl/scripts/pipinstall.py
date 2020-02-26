from __future__ import print_function
import subprocess

__version__ = '1.0.0'
__author__ = 'Gaming32'

def main(uninstall=False):
    import argparse
    parser = argparse.ArgumentParser()

    def check_version(version):
        if args.no2 and version.startswith(' -2.'):
            return False
        elif args.no3 and version.startswith(' -3.'):
            return False
        elif args.no32 and version.endswith('-32'):
            return False
        elif args.no64 and version.endswith('-64'):
            return False
        return True

    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('packages', metavar='PACKAGE', nargs='+',
        help='packages to install; pip is automatically added to this unless --no-pip-update is specified')
    parser.add_argument('-u', '--uninstall', dest='uninstall', action='store_true',
        help='switch to uninstall mode; ignored if using pipuninstall')
    parser.add_argument('-v', '--verbose', dest='verbose', action='count', default=0,
        help='verbose; -v displays commands before they are run; -vv also displays discovered python versions and arguments passed to python; more times are passed to pip')
    parser.add_argument('-q', '--quiet', dest='quiet', action='count', default=0,
        help='Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels).')
    parser.add_argument('-no2', dest='no2', action='store_true', help='don\'t install on python 2 versions')
    parser.add_argument('-no3', dest='no3', action='store_true', help='don\'t install on python 3 versions')
    parser.add_argument('-no32', dest='no32', action='store_true', help='don\'t install on 32-bit python versions')
    parser.add_argument('-no64', dest='no64', action='store_true', help='don\'t install on 64-bit python versions')
    parser.add_argument('--no-pip-update', dest='do_pip_update', action='store_false', help='don\'t install pip, and don\' update pip')
    parser.add_argument('--no-user', dest='do_user', action='store_false', help='don\'t pass --user to pip')
    parser.add_argument('--no-upgrade', dest='do_upgrade', action='store_false', help='don\'t pass --upgrade to pip')
    parser.add_argument('--pre', dest='pre', action='store_true',
        help='Include pre-release and development versions. By default, pip only finds stable versions.')
    parser.add_argument('--force-reinstall', dest='do_reinstall', action='store_true',
        help='Reinstall all packages even if they are already up-to-date.')
    parser.add_argument('--warn-script-location', dest='do_no_warn_script_location', action='store_false',
        help='don\'t pass --no-warn-script-location to pip; this is passed by default because only one python version is usually on PATH')
    parser.add_argument('--dry', dest='dry', action='store_true', help='don\'t run pip, just display verbose information')

    args = parser.parse_args()

    uninstall = (uninstall or args.uninstall)
    installcmd = 'un'*uninstall + 'install'
    pythonargs = ['-m', 'pip', installcmd]
    if args.do_user:
        pythonargs.append('--user')
    if args.do_upgrade:
        pythonargs.append('--upgrade')
    if args.pre:
        pythonargs.append('--pre')
    if args.do_reinstall:
        pythonargs.append('--force-reinstall')
    if args.do_no_warn_script_location:
        pythonargs.append('--no-warn-script-location')
    if args.quiet:
        pythonargs.append('-' + 'q'*args.quiet)
    if args.verbose > 2:
        pythonargs.append('-' + 'v'*(args.verbose-2))
    if args.do_pip_update:
        pythonargs.append('pip')
    pythonargs.extend(args.packages)

    if args.verbose >= 2:
        print('Arguments passed to python:', *pythonargs)
    if args.verbose >= 1:
        print('Args to run:', *['py', '-0'])
    process = subprocess.run(['py', '-0'], capture_output=True, text=True)
    pyvers = [x[2:] for x in process.stdout.split('\n')[1:] if check_version(x)]
    if args.verbose >= 2:
        print('Discovered python versions:', *pyvers)

    if args.dry: return

    for version in pyvers:
        print('Installing on version', version)
        command = ['py', '-'+version] + pythonargs
        if args.verbose >= 1:
            print('Args to run:', *command)
        returncode = subprocess.call(command)
        if returncode:
            print('An error occured with the python version', version, '(The packages may have still been installed, though)')
    print('Done.')

if __name__ == '__main__': main()