# -*- coding: utf-8 -*-

"""Console script for exo."""
import sys

import click

from exo import __author__
from exo import __version__

from pyfiglet import Figlet

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--version', is_flag=True, help="print current version")
def main(version):
    """
    exo is a collection of command-line utilities for Yeast Epigenome Project

    List of available utilities:

    \b
        calculate-contrast  : calculates & reports a contrast threshold from tagPileUP CDT for generating heatmaps.
        makeheatmap         : generates a heatmap from tagPileUP CDT and contrast-threshold files.
        mergeheatmaps       : Combines two heatmaps into a single heatmap.
        makecomposite       : generates a composite from sample and control tagPileUP CDT tabular files.
        motifcomposite      : generates a composite from strand separated tagPileUP CDT tabular file.
        fourcolor           : generates a fourcolor plot from Fasta file.
        bedtoucsc           : converts sacCer3_cegr bedfiles to UCSC specifications.
        totaltagorder       : sorts the tagPileUP CDT in descending order of (row-wise) totaltags.
        remove-overlapping-motifs : scans and removes motifs overlapping within an exclusion window.
        processbedgraph     : converts genomeCovergeBed output to standard ucsc bedGraph.

    To learn how to use any utility, use -h (ex: make-heatmap -h).
    The utilities prompt you for missing options, incase you forget. Hit enter to activate prompt.
    """
    if version:
        click.echo(__version__)
    else:
        f = Figlet(font='larry3d')
        click.echo(f.renderText('yeast epigenome project !'))
        click.echo("Author: " + __author__ + "\nVersion: " + __version__)
        click.echo("Usage: exo --help \n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
