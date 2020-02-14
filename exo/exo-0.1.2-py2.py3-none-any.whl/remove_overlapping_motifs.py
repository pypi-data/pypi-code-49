#!/usr/bin/python
from __future__ import division

import click

import pandas as pd
# import pprint


def removeRepeats(dataFrame):

    sortedData = dataFrame
    excludeList = []

    # choosing motifs based on p-values per chromosome
    for i in sortedData['#chr'].unique():
        chrData = sortedData.loc[sortedData['#chr'] == i]
        # print chrData[0:3]
        mdp = chrData['midpoint'].tolist()
        # pprint.pprint(mdp)

        # iterating through each motif to pick the least p-value
        for j in range(0, len(mdp)):
            # print mdp[j]

            if len(chrData.index[chrData['midpoint'] == mdp[j]].tolist()) > 1:
                print("Found Same Midpoints : {} {}".format(mdp[j], len(
                    chrData.index[chrData['midpoint'] == mdp[j]].tolist())))
                # print len(chrData.index[chrData['midpoint'] == mdp[j]].tolist())
                first = chrData.index[chrData['midpoint'] == mdp[j]].tolist()[
                    0]
                second = chrData.index[chrData['midpoint'] == mdp[j]].tolist()[
                    1]
                pv1 = chrData.loc[first]['p-value']
                pv2 = chrData.loc[first]['p-value']

                # excluding the greater p-value after comparison
                if pv1 <= pv2:
                    # print " IF pv1: {}, pv2 :{}".format(pv1,pv2)
                    excludeList.append(second)
                else:
                    # print "ELSE pv1: {}, pv2 :{}".format(pv1,pv2)
                    excludeList.append(first)

    print("\nRemoved in Repeats : {} ,\nindex : {}\n".format(
        len(excludeList), excludeList))
    dataFrame = dataFrame.drop(excludeList)
    # print dataFrame
    return dataFrame


def removeRegions(dataFrame, er, out):
    """
    removes the regions from the dataFrame which have overlaps and within
    exclusion region by choosing the lowest p-value
    """
    midpoints = []  # to store midpoints

    # finding midpoints
    for index, row in dataFrame.iterrows():
        midpoints.append((row['start'] + row['end']) // 2)

    # adding another column called midpoints
    dataFrame['midpoint'] = midpoints

    # sort based on chromosome and then by midpoints
    sData = dataFrame.sort_values(
        by=['midpoint', 'p-value'], kind='mergesort')
    excludeList = []  # list of indexes that needs to be removed
    # print sData
    # print "\n"

    # removing the motifs that are called on the different strand
    sortedData = removeRepeats(sData)

    # choosing motifs based on p-values per chromosome
    for i in sortedData['#chr'].unique():
        chrData = sortedData.loc[sortedData['#chr'] == i]
        # print chrData[0:3]
        mdp = chrData['midpoint'].tolist()
        # pprint.pprint(mdp)
        print("processing chromosome : {} ".format(i))

        # iterating through each motif to pick the least p-value
        for j in range(0, len(mdp)):
            # print mdp[j]

            # retrieve the index that will later be removed or retained
            index1 = chrData.index[chrData['midpoint'] == mdp[j]].tolist()[
                0]
            # print index1

            excludeZone = range(0, mdp[j] + er)  # create a boundary region
            pv1 = chrData.loc[index1]['p-value']  # retrieve the pvalue

            # if the index is not excluded from any previous comparisons
            if index1 not in excludeList:
                for k in range(j + 1, len(mdp)):
                    # print "\t {}".format(mdp[k])
                    # retrieve the next line index
                    index2 = chrData.index[chrData['midpoint'] == mdp[k]].tolist()[
                        0]
                    # print "\t {}".format(index2)

                    # checking if the next line is in the exclusionZone
                    if mdp[k] in excludeZone:
                        # retrieve the p-value for comparison
                        pv2 = chrData.loc[index2]['p-value']

                        # excluding the greater p-value after comparison
                        if pv1 <= pv2:
                            # pprint.pprint(" IF pv1: {}, pv2 :{}".format(pv1,pv2))
                            excludeList.append(index2)
                            # pprint.pprint(list(chrData.loc[index2]))
                        else:
                            # pprint.pprint("ELSE pv1: {}, pv2 :{}".format(pv1,pv2))
                            excludeList.append(index1)
                            # pprint.pprint(list(chrData.loc[index1]))
            # else:
                # print "IN EXCLUDE LIST : {}".format(index1)
    print("\nRemoved : {} ,\nindex : {}\n".format(
        len(excludeList), excludeList))
    sData = sortedData.drop(excludeList)
    sortedData = sData.sort_values(by=['#chr', 'rank'], kind='mergesort')
    # print sortedData
    sortedData = sortedData.drop(['midpoint'], axis=1)
    print("Final Shape of the data : {}".format(sortedData.shape))
    sortedData.to_csv(out, sep='\t', header=False, index=False)
    # return excludeList


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('bedfile', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-ew', '--exclude-window', metavar="<int>", type=int, default='100', prompt=True, show_default='100', help='Exclusion window for motif p-value comparison')
@click.option('-o', '--out', metavar="<string>", default='dedupRegions.bed', prompt=True, show_default='dedupRegions.bed', help='output filename')
def cli(bedfile, exclude_window, out):
    """
    For each motif region in the bedfile, scans for overlapping motifs with an exclusion window (in bp) centered at the region midpoint. Between two motifs, retains the motif with lowest p-value and discards the other.
    """
    click.echo('\n' + '.' * 50)

    # reading the fimo text file
    Fdata = pd.read_csv(bedfile, sep="\t", index_col=False, names=[
                        '#chr', 'start', 'end', 'rank', 'p-value', 'strand'])

    Fdata = Fdata.sort_values(by=['#chr', 'p-value'], kind='mergesort')
    click.echo("Motif data Shape : {}".format(Fdata.shape))
    removeRegions(Fdata, exclude_window, out)

    click.echo('\n' + '.' * 50)
