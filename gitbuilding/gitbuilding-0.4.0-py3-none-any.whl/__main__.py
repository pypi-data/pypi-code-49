#!/usr/bin/env python

'''The entrypoint of GitBuilding'''

import argparse
import os
import codecs
from colorama import Fore, Style
import pkg_resources
import gitbuilding as gb

def main():
    '''This is what runs if you run `gitbuilding` from the terminal'''

    parser = argparse.ArgumentParser(description='Run git building to build your documentation',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--version", action="store_true", dest="version",
                        help="Print version information.")
    subparsers = parser.add_subparsers(help='Available commands', metavar="<command>",
                                       dest='command')
    parser_build = subparsers.add_parser('build', help='Build documentation')
    parser_build.add_argument("-O", "--OutputDir", action="store", dest="outDir",
                              type=str, help="Set output directory")
    parser_new = subparsers.add_parser('new', help='New gitbuilding project')
    parser_serve = subparsers.add_parser('serve', help='Start local server to view documentation')
    parser_serve.add_argument("--dev", action="store_true", dest="dev",
                              help="Use npm dev server for live editor. Beware, here be dragons!")
    parser_html = subparsers.add_parser('build-html', help='Build static HTML site')
    parser_html.add_argument("-B", "--BuildDir", action="store", dest="buildDir", type=str,
                             help="Set gitbuilding output directoru to be converted to html (default: Output)")
    parser_help = subparsers.add_parser('help', help="Run 'help <command>' for detailed help")
    parser_help.add_argument('h_command', metavar='<command>', nargs='?', type=str,
                             help="Command to show help for")
    args = parser.parse_args()

    if args.version:
        print(pkg_resources.get_distribution("gitbuilding").version)
        return None

    if os.path.isfile('buildconf.yaml'):
        conf = 'buildconf.yaml'
    else:
        conf = None

    if args.command == 'build':
        doc = gb.Documentation(conf, args.outDir)
        doc.buildall()

    elif args.command == 'new':
        if os.listdir('.') == []:
            newdir = '.'
        else:
            ans = input('This directory is not empty. Build to new sub-dir? [y/N]: ')
            if ans in ('y', 'Y'):
                newdir = input('Enter subdir name: ')
                if not os.path.split(newdir)[0] == '':
                    print('\n\ngitbuilding new only supports creating a single subdirectory'
                          ' to the current folder, not nested directories or full paths\n\n')
                    return None
                if os.path.exists(newdir):
                    print(f"\n\nCannot create directory '{newdir}', as it already exists\n\n")
                    return None
                try:
                    os.mkdir(newdir)
                except:
                    print(f"\n\nFailed to create directory '{newdir}'\n\n")
                    return None
            else:
                if ans not in ('n', 'N', ''):
                    print('Invalid response.')
                return None
        # writing default/empty project

        #CONFIG FILE
        with codecs.open(os.path.join(newdir, 'buildconf.yaml'), "w", "utf-8") as file:
            file.write(gb.empty.emptyconfig())

        #OVERVIEW FILE
        with codecs.open(os.path.join(newdir, 'landing.md'), "w", "utf-8") as file:
            file.write(gb.empty.emptylanding())

        #TESTPAGES
        for n, page in enumerate(['testpage1.md', 'testpage2.md']):
            with codecs.open(os.path.join(newdir, page), "w", "utf-8") as file:
                file.write(gb.empty.testpage(f"Test Page {n+1}"))

        #PARTS LIST
        with codecs.open(os.path.join(newdir, 'Parts.yaml'), "w", "utf-8") as file:
            file.write(gb.empty.basicparts())

        #IMAGE DIRECTORY
        os.mkdir(os.path.join(newdir, 'images'))

    elif args.command == 'serve':

        gbs = gb.GBServer(conf, dev=args.dev)
        if args.dev:
            print(Fore.RED+
                  '\n\n   WARNING! You are using the gitbuilding dev server.\nHere be dragons!\n\n'+
                  Style.RESET_ALL)
            from flask_cors import CORS
            CORS(gbs)
        gbs.run()

    elif args.command == 'build-html':
        gb.html_build(conf, build_dir=args.buildDir)

    elif args.command == 'help':
        if args.h_command is None:
            parser.print_help()
        elif args.h_command == 'build':
            print(f"""\n`build` will build the documentation in the current folder,
make sure the current folder is a valid gitbuilding project.\n""")
            print(parser_build.format_help())
        elif args.h_command == 'build-html':
            print(f"""\n`build-html` will turn creat a static html webstite using the
build files produced from 'gitbuilding build'\n""")
            print(parser_html.format_help())
        elif args.h_command == 'serve':
            print(f"""\n`serve` will create a local webserver to view your built
documentation rendered in HTML. You must run `build` before
running serve.\n""")
            print(parser_serve.format_help())
        elif args.h_command == 'new':
            print(f"""\n`new` will create an empty gitbuilding project in the
current folder if empty. If the current folder is not
empty it will ask for a subfolder name for the project\n""")
            print(parser_new.format_help())
        else:
            print(f'Invalid gitbuilding command {args.h_command}\n\n')
            parser.print_help()
    else:
        print(f'Invalid gitbuilding command {args.command}')
    return None

if __name__ == '__main__':
    main()
