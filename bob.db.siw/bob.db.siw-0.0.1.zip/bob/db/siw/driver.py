"""SIW - a mobile face presentation attack database with real-world
variations
"""

import os
import sys
import pkg_resources
from bob.db.base.driver import Interface as BaseInterface
from bob.io.base import create_directories_safe
import re
from .common import siw_file_metadata


def dumplist(args):
    """Dumps lists of files based on your criteria"""

    from .query import Database

    db = Database()

    r = db.objects(purposes=args.purpose, groups=args.group)

    output = sys.stdout
    if args.selftest:
        from bob.db.base.utils import null

        output = null()

    for f in r:
        output.write(
            "%s\n" % f.make_path(directory=args.directory, extension=args.extension)
        )

    return 0


def checkfiles(args):
    """Checks existence of files based on your criteria"""

    from .query import Database

    db = Database()

    r = db.objects()

    # go through all files, check if they are available on the filesystem
    good = []
    bad = []
    for f in r:
        if os.path.exists(f.make_path(args.directory, args.extension)):
            good.append(f)
        else:
            bad.append(f)

    # report
    output = sys.stdout
    if args.selftest:
        from bob.db.base.utils import null

        output = null()

    if bad:
        for f in bad:
            output.write(
                'Cannot find file "%s"\n' % f.make_path(args.directory, args.extension)
            )
        output.write(
            '%d files (out of %d) were not found at "%s"\n'
            % (len(bad), len(r), args.directory)
        )

    return 0


def pad_list(folder, files, bf, pa):
    create_directories_safe(folder)
    bf = re.compile(bf)
    pa = re.compile(pa)
    bf_files = filter(bf.search, files)
    pa_files = filter(pa.search, files)
    for name, lines in [("for_real.lst", bf_files), ("for_attack.lst", pa_files)]:
        with open(os.path.join(folder, name), "w") as f:
            for line in lines:
                path = line.strip()
                client_id, attack_type = siw_file_metadata(path)[:2]
                if name == "for_real.lst":
                    f.write("{0} {1}\n".format(path, client_id))
                else:
                    f.write("{0} {1} {2}\n".format(path, client_id, attack_type))


def pad_protocols(out_folder, files_map):
    for grp, (files, bf, pa) in files_map.items():
        pad_list(os.path.join(out_folder, grp), files, bf, pa)


def create(args):
    "Creates the PAD file lists of the dataset."

    out_folder = args.output_dir

    # list all files
    files = {"train": [], "dev": [], "eval": []}
    for grp, filelist in files.items():
        with open(
            pkg_resources.resource_filename(__name__, f"lists/{grp}_files.lst")
        ) as f:
            filelist.extend([l.strip() for l in f.readlines()])

    # create protocols
    root = pkg_resources.resource_filename(__name__, "lists")

    # protocol 1 is all files except first 60 frames is used in training
    bf = ".*/live/.*"
    pa = ".*/spoof/.*"
    out_folder = os.path.join(root, "Protocol_1")
    files_map = {
        "train": ([p + "_60" for p in files["train"]], bf, pa),
        "dev": (files["dev"], bf, pa),
        "eval": (files["eval"], bf, pa),
    }
    pad_protocols(out_folder, files_map)

    # protocol 2 is 4 folds of display attacks (print attacks are excluded)
    for medium in range(1, 5):
        out_folder = os.path.join(root, f"Protocol_2_{medium}")
        # fmt: off
        files_map = {
            "train": (files["train"], f".*/live/.*", f".*/spoof/.*/.*-.*-3-[^{medium}]-.*"),
            "dev": (files["dev"], f".*/live/.*", f".*/spoof/.*/.*-.*-3-[^{medium}]-.*"),
            "eval": (files["eval"], f".*/live/.*", f".*/spoof/.*/.*-.*-3-{medium}-.*"),
        }
        # fmt: on
        pad_protocols(out_folder, files_map)

    # protocol 3 is to train on print and test on display and vice-versa
    for type_id in (2, 3):
        out_folder = os.path.join(root, f"Protocol_3_{type_id-1}")
        # fmt: off
        files_map = {
            "train": (files["train"], f".*/live/.*", f".*/spoof/.*/.*-.*-{type_id}-.*-.*"),
            "dev": (files["dev"], f".*/live/.*", f".*/spoof/.*/.*-.*-{type_id}-.*-.*"),
            "eval": (files["eval"], f".*/live/.*", f".*/spoof/.*/.*-.*-[^{type_id}]-.*-.*"),
        }
        # fmt: on
        pad_protocols(out_folder, files_map)


class Interface(BaseInterface):
    def name(self):
        return "siw"

    def version(self):
        return pkg_resources.require("bob.db.%s" % self.name())[0].version

    def files(self):
        return ()

    def type(self):
        return "text"

    def add_commands(self, parser):

        from . import __doc__ as docs

        subparsers = self.setup_parser(parser, "SIW database", docs)

        import argparse

        # the "dumplist" action
        parser = subparsers.add_parser("dumplist", help=dumplist.__doc__)
        parser.add_argument(
            "-d",
            "--directory",
            default="",
            help="if given, this path will be prepended to every entry " "returned.",
        )
        parser.add_argument(
            "-e",
            "--extension",
            default="",
            help="if given, this extension will be appended to every entry "
            "returned.",
        )
        parser.add_argument(
            "-u",
            "--purpose",
            help="if given, this value will limit the "
            "output files to those designed for the given purposes.",
            choices=("enroll", "probe", ""),
        )
        parser.add_argument(
            "-g",
            "--group",
            help="if given, this value will limit the output files to those "
            "belonging to a particular protocolar group.",
            choices=("dev", "eval", "world", ""),
        )
        parser.add_argument(
            "--self-test", dest="selftest", action="store_true", help=argparse.SUPPRESS
        )
        parser.set_defaults(func=dumplist)  # action

        # the "checkfiles" action
        parser = subparsers.add_parser("checkfiles", help=checkfiles.__doc__)
        parser.add_argument(
            "-l",
            "--list-directory",
            required=True,
            help="The directory which contains the file lists.",
        )
        parser.add_argument(
            "-d",
            "--directory",
            dest="directory",
            default="",
            help="if given, this path will be prepended to every entry " "returned.",
        )
        parser.add_argument(
            "-e",
            "--extension",
            dest="extension",
            default="",
            help="if given, this extension will be appended to every entry "
            "returned.",
        )
        parser.add_argument(
            "--self-test", dest="selftest", action="store_true", help=argparse.SUPPRESS
        )
        parser.set_defaults(func=checkfiles)  # action

        # the "create" action
        parser = subparsers.add_parser("create", help=create.__doc__)
        default_output = pkg_resources.resource_filename(__name__, "lists")
        parser.add_argument(
            "-o",
            "--output-dir",
            default=default_output,
            help="The directory where the new list files will be saved into.",
        )
        parser.set_defaults(func=create)  # action
