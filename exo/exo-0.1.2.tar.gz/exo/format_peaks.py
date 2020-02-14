#!/usr/bin/python
from __future__ import division

from collections import OrderedDict

import click

import pandas as pd


def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('bedfile', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-ew', '--expand-window', metavar="<int>", type=int, default='0', prompt=True, show_default='0', help='Expand Peak Region')
@click.option('-o', '--out', metavar="<string>", default='formated.bed', prompt=True, show_default='formated.bed', help='output filename')
def cli(bedfile, expand_window, out):
    """
    Converts chromosome numbers in bedfile to UCSC specifications.
    Removes 2-micron and chrM regions.

    \b
    Can expand regions to certain bp if needed.
    expands from the midpoint of the regions in both directions
    Currently supports sacCer3_cegr bedfiles

    """
    click.echo('\n' + '.' * 50)

    data = []  # used to store the file contents as a list of lists
    filecontents = []
    header = []  # contains 2-microns and other wrongly formated lines

    # reading the genomeCoverageBed output file
    openfile = open(bedfile, 'r').readlines()

    # reading each line and converting the chromosome numbers to ROMAN equivalents
    for line in openfile:
        if line.startswith("chr"):
            temp = line.strip().split("\t")

            if temp[0][3:] != '2-micron':
                # checking the strand information
                if int(expand_window) > 0:
                    #  checking if it is chrM
                    if temp[0][3:] != 'M':
                        # getting the chr number and converting to romans
                        romanValue = write_roman(int(temp[0][3:]))
                        temp[0] = "chr" + str(romanValue)

                        # calculating the new start and end
                        mid = int((int(temp[1]) + int(temp[2])) // 2)
                        ns = mid - int(expand_window)
                        ne = mid + int(expand_window)

                        temp[1] = ns
                        temp[2] = ne

                        filecontents.append(temp)
                    else:
                        filecontents.append(temp)
                else:
                    #  checking if it is chrM
                    if temp[0][3:] != 'M':
                        # getting the chr number and converting to romans
                        romanValue = write_roman(int(temp[0][3:]))
                        temp[0] = "chr" + str(romanValue)
                        filecontents.append(temp)
                    else:
                        filecontents.append(temp)

            # removing 2-microns, which is not recognized by the UCSC browser
            else:
                if line.startswith("2-micron") is False:
                    header.append(line)

    data = pd.DataFrame(filecontents)
    print(data[0:10])
    data.to_csv(out, sep='\t', header=False, index=False)
    click.echo('\n' + '.' * 50)
