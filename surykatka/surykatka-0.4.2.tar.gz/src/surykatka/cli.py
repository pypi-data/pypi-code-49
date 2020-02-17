# Copyright (C) 2019  Nexedi SA and Contributors.
#                     Romain Courteaud <romain@nexedi.com>
#
# This program is free software: you can Use, Study, Modify and Redistribute
# it under the terms of the GNU General Public License version 3, or (at your
# option) any later version, as published by the Free Software Foundation.
#
# You can also Link and Combine this program with other software covered by
# the terms of any of the Free Software licenses or any of the Open Source
# Initiative approved licenses and Convey the resulting work. Corresponding
# source of such a combination shall include the source code for all other
# software used.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See COPYING file for full licensing terms.
# See https://www.nexedi.com/licensing for rationale and options.

import click
import sys
from .bot import create_bot


@click.command(short_help="Runs surykatka bot.")
@click.option(
    "--run",
    "-r",
    help="The bot operation mode to run.",
    show_default=True,
    default="status",
    type=click.Choice(["crawl", "status"]),
)
@click.option(
    "--sqlite", "-s", help="The path of the sqlite DB. (default: :memory:)"
)
@click.option("--nameserver", "-n", help="The IP of the DNS server.")
@click.option("--url", "-u", help="The url to check.")
@click.option("--domain", "-d", help="The domain to check.")
@click.option("--timeout", "-t", help="The timeout value.")
@click.option(
    "--configuration", "-f", help="The path of the configuration file."
)
@click.option(
    "--reload/--no-reload",
    default=False,
    help="Reload the configuration file between each crawl.",
    show_default=True,
)
@click.option(
    "--output",
    "-o",
    help="The status output format.",
    type=click.Choice(["plain", "json"]),
    default="plain",
    show_default=True,
)
def runSurykatka(
    run,
    sqlite,
    nameserver,
    url,
    domain,
    timeout,
    configuration,
    reload,
    output,
):

    mapping = {}
    if url:
        mapping["URL"] = url
        mapping["DOMAIN"] = ""
    if domain:
        mapping["DOMAIN"] = domain
        if not url:
            mapping["URL"] = ""
    if timeout:
        mapping["TIMEOUT"] = timeout
    if sqlite:
        mapping["SQLITE"] = sqlite
    if nameserver:
        mapping["NAMESERVER"] = nameserver
    if reload:
        mapping["RELOAD"] = str(reload)
    mapping["FORMAT"] = output
    bot = create_bot(cfgfile=configuration, mapping=mapping)
    return bot.run(run)


if __name__ == "__main__":
    sys.exit(runSurykatka())
