#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################

"""Migrate a v1 database to v2

Usage:
  %(prog)s [-v ... | --verbose ...] [--prefix=<path>][-f|--force]
           <database_identifier>
  %(prog)s (--help | -h)
  %(prog)s (--version | -V)


Options:
  -h, --help                 Show this screen
  -V, --version              Show version
  -v, --verbose              Increases the output verbosity level
  -p, --prefix=<path>        Path where the prefix is contained [default: .]
"""

import os
import sys
import copy

from docopt import docopt

from ..version import __version__

from ..database import Database, Storage as DBStorage
from ..protocoltemplate import ProtocolTemplate, Storage as PTStorage
from ..utils import setup_logging


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    prog = os.path.basename(sys.argv[0])
    completions = dict(prog=prog, version=__version__)
    args = docopt(
        __doc__ % completions,
        argv=argv,
        options_first=True,
        version="v%s" % __version__,
    )

    logger = setup_logging(args["--verbose"], __name__, __name__)

    prefix = args["--prefix"] if args["--prefix"] is not None else "."
    if not os.path.exists(prefix):
        logger.error("Prefix not found at: '%s'", prefix)
        return 1

    database_identifier = args["<database_identifier>"]

    database = Database(prefix, database_identifier)

    if not database.valid:
        logger.error("Invalid database: '%s'", "\n".join(database.errors))
        return 1

    if database.schema_version != 1:
        logger.error("Can't migrate database is not v1")
        return 1

    db_name, db_version = database_identifier.split("/")
    new_db_name = f"{db_name}/{int(db_version) + 1}"

    db_storage = DBStorage(prefix, new_db_name)
    if db_storage.exists():
        logger.error(f"Database already exists: {new_db_name}")
        return 1

    database_json = copy.deepcopy(database.data)
    database_json["schema_version"] = 2
    database_json["protocols"] = []

    for protocol in database.protocols:
        sets = database.sets(protocol)
        set_list = []
        views = {}
        for _, set_ in sets.items():
            views[set_["name"]] = {
                "view": set_["view"],
                "parameters": set_.get("parameters", {}),
            }

            for key in ["template", "view", "parameters"]:
                if key in set_:
                    set_.pop(key)
            set_list.append(set_)

        template = {"schema_version": 1, "sets": set_list}

        pt_name = f"{protocol}/1"
        pt_storage = PTStorage(prefix, pt_name)

        if pt_storage.exists():
            logger.info(f"Protocol template already exists: {pt_name}")
        else:
            protocol_template = ProtocolTemplate(prefix, template)
            if not protocol_template.valid:
                logger.error(
                    "Invalid protocol created:", "\n".join(protocol_template.errors)
                )
                return 1
            else:
                protocol_template.write(pt_storage)

        protocol_entry = {"name": protocol, "template": pt_name, "views": views}

        database_json["protocols"].append(protocol_entry)

    new_database = Database(prefix, database_json)
    if not new_database.valid:
        logger.error("Invalid database created:", "\n".join(new_database.errors))
        return 1
    else:
        new_database.code = database.code
        new_database.description = (
            database.description if database.description is not None else ""
        )
        new_database.write(db_storage)


if __name__ == "__main__":
    main()
