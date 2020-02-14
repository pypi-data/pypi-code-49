#!/usr/bin/python
import click

import pandas as pd


def sortData(sense, out):
    """
    Function to read, calculate total tag count, sort data based on the total tag count and finally create the new CDT tabular files for Heatmaps.
    """

    # reading the sense Heatmap frequencies
    sdata = pd.read_csv(sense, sep="\t")

    # creating a combined dataframe to find total tag count.
    combined = sdata
    combined['sum'] = combined[combined.columns[2:]].sum(
        axis=1)  # summing each row

    # sort in the descending order of the sum for each row.
    combinedSort = combined.sort_values(
        by='sum', ascending=False, na_position='first')

    print(combinedSort[0:10])
    # removing the sum column after sorting, so that data can be written into new tabular file.
    data = combinedSort.drop(['sum'], axis=1)

    # basic DEBUG
    # print combinedSort[0:10]
    # print combinedSort['sum']
    # print combinedSort.columns
    # print str(sdata.loc[42].sum() + adata.loc[42].sum())
    # print combinedSort.index

    data.to_csv(out, sep='\t', header=True, index=False)


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('tagpileup-cdt', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-o', '--out', metavar="<string>", default='totalTagSorted.tabular', prompt=True, show_default='totalTagSorted.tabular', help='output filename')
def cli(tagpileup_cdt, out):
    """
    Sorts the tagpileup heatmap frequency matrix based on totalTagCount.
    Output file is a sorted tabular file.

    """
    click.echo('\n' + '.' * 50)
    # creating the totaltag sorted tabular
    sortData(tagpileup_cdt, out)
    click.echo('\n' + '.' * 50)
