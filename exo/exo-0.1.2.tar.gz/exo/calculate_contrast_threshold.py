# -*- coding: utf-8 -*-

"""Console script for exo."""
import errno
import math
import sys

import click

import numpy as np

# Adapted Java treeview image compression algorithm


def rebin(a, new_shape):
    M, N = a.shape
    m, n = new_shape
    if m >= M:
        # repeat rows in data matrix
        a = np.repeat(a, math.ceil(float(m) / M), axis=0)

    M, N = a.shape
    m, n = new_shape

    row_delete_num = M % m
    col_delete_num = N % n

    np.random.seed(seed=0)

    if row_delete_num > 0:
        # select deleted rows with equal intervals
        row_delete = np.linspace(0, M - 1, num=row_delete_num, dtype=int)
        # sort the random selected deleted row ids
        row_delete = np.sort(row_delete)
        row_delete_plus1 = row_delete[1:-1] + \
            1  # get deleted rows plus position
        # get deleted rows plus position (top +1; end -1)
        row_delete_plus1 = np.append(
            np.append(row_delete[0] + 1, row_delete_plus1), row_delete[-1] - 1)
        # put the info of deleted rows into the next rows by mean
        a[row_delete_plus1, :] = (
            a[row_delete, :] + a[row_delete_plus1, :]) / 2
        a = np.delete(a, row_delete, axis=0)  # random remove rows

    if col_delete_num > 0:
        # select deleted cols with equal intervals
        col_delete = np.linspace(0, N - 1, num=col_delete_num, dtype=int)
        # sort the random selected deleted col ids
        col_delete = np.sort(col_delete)
        col_delete_plus1 = col_delete[1:-1] + \
            1  # get deleted cols plus position
        # get deleted cols plus position (top +1; end -1)
        col_delete_plus1 = np.append(
            np.append(col_delete[0] + 1, col_delete_plus1), col_delete[-1] - 1)
        # put the info of deleted cols into the next cols by mean
        a[:, col_delete_plus1] = (
            a[:, col_delete] + a[:, col_delete_plus1]) / 2
        a = np.delete(a, col_delete, axis=1)  # random remove columns

    M, N = a.shape

    # compare the heatmap matrix
    a_compress = a.reshape((m, int(M / m), n, int(N / n))).mean(3).mean(1)
    return np.array(a_compress)


def calculate_threshold(input_file, threshold_type, threshold_value, header, start_col, row_num, col_num, min_upper_lim):
    data0 = []
    with open(input_file, 'r') as data:
        if header:
            data.readline()

        for rec in data:
            tmp = [(x.strip()) for x in rec.split('\t')]
            data0.append(tmp[start_col:])
        data0 = np.array(data0, dtype=float)

    if row_num == -999:
        row_num = data0.shape[0]
    if col_num == -999:
        col_num = data0.shape[1]

    # rebin data0
    if row_num < data0.shape[0] and col_num < data0.shape[1]:
        data0 = rebin(data0, (row_num, col_num))
    elif row_num < data0.shape[0]:
        data0 = rebin(data0, (row_num, data0.shape[1]))
    elif col_num < data0.shape[1]:
        data0 = rebin(data0, (data0.shape[0], col_num))

    if threshold_type == 'quantile':
        # Calculate contrast limits here
        rows, cols = np.nonzero(data0)
        upper_lim = np.percentile(data0[rows, cols], threshold_value)
        lower_lim = 0

        # Setting an absolute threshold to a minimum,
        # in cases the 95th percentile contrast is <= user defined min_upper_lim
        if threshold_value > 0.0:
            click.echo(
                "\nCalculated constrast UPPER LIMIT using quantile: {}".format(upper_lim))
            click.echo("Assigned LOWER LIMIT: {}".format(lower_lim))
            if upper_lim <= min_upper_lim:
                click.echo(
                    "UPPER LIMIT <= min-upper-limit ; Setting Max contrast to min_upper_lim")
                upper_lim = min_upper_lim
    else:
        # Set absolute constrast here.
        upper_lim = threshold_value
        lower_lim = 0

    # Generate the output file.
    outfile = open('calcThreshold.txt', 'w')
    outfile.write("upper_threshold:{}\nlower_threshold:{}\nrow_num:{}\ncol_num:{}\nheader:{}\nstart_col:{}".format(
        upper_lim, lower_lim, row_num, col_num, header, start_col))
    click.echo('\ncontrast_upper_threshold:' + str(upper_lim))
    click.echo('contrast_lower_threshold:' + str(lower_lim))
    outfile.flush()
    outfile.close()
    click.echo('.' * 50 + '\n')


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(options_metavar='<options>', context_settings=CONTEXT_SETTINGS)
@click.argument('tagpileup-cdt', type=click.Path(exists=True, resolve_path=True, file_okay=True, dir_okay=False,))
@click.option('-hh', '--has-header', metavar="<string>", type=click.BOOL, default='T', prompt=True, show_default='True', help='has headers ?')
@click.option('-ct', '--threshold-type', type=click.Choice(['quantile', 'absolute'], case_sensitive=False), prompt=True, default='quantile')
@click.option('-cv', '--threshold-value', metavar="<float>", default=90.0, prompt=True, show_default="quantile:90.0", help="Takes values >=0")
@click.option('-m', '--min-upper-limit', metavar="<float>", default=5.0, prompt=True, show_default='5.0', help='Minimum upper limit')
@click.option('-s', '--start_col', metavar="<int>", default=2, prompt=True, show_default='2', help='Start column')
@click.option('-r', '--row_num', metavar="<int>", default=700, prompt=True, show_default='700', help='Height of the plot')
@click.option('-c', '--col_num', metavar="<int>", default=300, prompt=True, show_default='300', help='Width of the plot')
def cli(min_upper_limit, tagpileup_cdt, has_header, start_col, row_num, col_num, threshold_type, threshold_value):
    """
    Calculates a contrast threshold from the CDT file generated by tagpileup. The calculated values are reported ina text file which can then used to set a uniform contrast for multiple heatmaps generated downstream.

    \b
    For example if your trying to create multiple heatmaps with dimensions (Width x Height)px = (300 x 700)px.
    Use width (col_num) = 300, height(row_num) = 700.

    """
    click.echo('\n' + '.' * 50)
    click.echo('Contrast threshold Type: %s' % threshold_type)
    click.echo('Contrast threshold Value: %s' % threshold_value)
    click.echo('Has Header: %s' % has_header)
    click.echo('Start column: %s' % start_col)
    click.echo('Height (pixels): %s' % row_num)
    click.echo('Width (pixels):%s' % col_num)
    click.echo('Min Upper Limit (used only with quantile):%s' %
               min_upper_limit)

    if threshold_value <= 0:
        click.echo('\n Invalid threshold value')
        sys.exit(errno.EINVAL)
    else:
        calculate_threshold(tagpileup_cdt, threshold_type, threshold_value,
                            has_header, start_col, row_num, col_num, min_upper_limit)
    return 0
