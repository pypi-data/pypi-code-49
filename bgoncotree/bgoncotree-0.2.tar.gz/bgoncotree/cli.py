import logging
import json

import click

from bgoncotree.exceptions import BGOncoTreeError
from bgoncotree.main import BGOncoTree

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

logger = logging.getLogger("bgoncotree")


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option("--verbose", "-v", is_flag=True, default=False)
def cli(verbose):
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG if verbose else logging.WARNING,
    )
    if not verbose:
        logging.getLogger("bgdata").setLevel(logging.WARNING)


@cli.command(short_help="Find descendents of a particular node")
@click.option("--node", "-n", "name", help="Node to start the search from. Default root")
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    default=False,
    help="Use json format for the output",
)
@click.option("--file", default=None, type=click.Path(exists=True), help="Use a specific file")
@click.option("--limit", default=None, type=int, help="Limit descendents to show")
def descendants(name, as_json, file, limit):
    tree = BGOncoTree(file)
    node = tree.find(name)
    if as_json:
        print(json.dumps(node.to_json(limit=limit), indent=4))
    else:
        for n, level in tree.iter_from(node):
            if limit is None or level < limit:
                print(" " * 3 * level + "|- {} ({})".format(n.name, n.id))


@cli.command(short_help="Find ancestors of a particular node")
@click.option("--node", "-n", "name", help="Node to start the search from. Default root")
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    default=False,
    help="Use json format for the output",
)
@click.option("--file", default=None, type=click.Path(exists=True), help="Use a specific file")
@click.option("--limit", default=None, type=int, help="Limit descendents to show")
def ancestors(name, as_json, file, limit):
    tree = BGOncoTree(file)
    node = tree.find(name)
    if as_json:
        print(json.dumps(node.to_json(descending=False, limit=limit), indent=4))
    else:
        for n, level in tree.iter_from(node, descending=False):
            if limit is None or level < limit:
                print(" " * 3 * level + "|- {} ({})".format(n.name, n.id))


@cli.command(short_help="Search for all nodes containing a particular substring")
@click.argument("name", metavar="<NAME>")
@click.option("--file", default=None, type=click.Path(exists=True), help="Use a specific file")
def search(name, file):
    tree = BGOncoTree(file)
    for node in tree.search(name):
        print(node)


@cli.command(short_help="Validate a tree file")
@click.argument("file", type=click.Path(exists=True), metavar="<FILE>")
def validate(file):
    """Validate a tree created from <FILE>"""
    try:
        BGOncoTree(file)
    except BGOncoTreeError as e:
        print("Invalid tree. Reason {}".format(e))
    else:
        print("Valid tree")
