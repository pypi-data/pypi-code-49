#!/usr/bin/env python
#
# exporting_tsv.py - Export data to a TSV file.
#
# Author: Paul McCarthy <pauldmccarthy@gmail.com>
#
"""This module provides the :func:`exportTSV` function, which exports the data
contained in a :class:`.DataTable` to a TSV file.
"""


import functools as ft
import os.path   as op
import              os
import              logging

import numpy            as np
import pandas           as pd
import pandas.api.types as pdtypes

from . import util
from . import custom


log = logging.getLogger(__name__)


TSV_SEP = '\t'
"""Default separator string to use in TSV-style output files."""


NUM_ROWS = 10000
"""Default number of rows to export at a time by :func:`exportTSV` - the
default value for its ``numRows`` argument.
"""


@custom.exporter('tsv')
def exportTSV(dtable,
              outfile,
              idcol,
              colnames,
              sep=None,
              missingValues=None,
              dateFormat=None,
              timeFormat=None,
              formatters=None,
              numRows=None,
              nonNumericFile=None,
              **kwargs):
    """Export data to a TSV-style file.

    This may be parallelised by row - chunks of ``numRows`` rows will be
    saved to separate temporary output files in parallel, and then concatenated
    afterwards to produce the final output file.

    :arg dtable:         :class:`.DataTable` containing the data

    :arg outfile:        File to output to

    :arg idcol:          Name to use for the subject ID column

    :arg colnames:       Dict containing ``{oldcol : newcol}`` mappings

    :arg sep:            Separator character to use. Defaults to
                         :attr:`TSV_SEP`

    :arg missingValues:  String to use for missing/NA values. Defaults to the
                         empty string.

    :arg dateFormat:     Name of formatter to use for date columns.

    :arg timeFormat:     Name of formatter to use for time columns.

    :arg formatters:     Dict of ``{ [vid|column] : formatter }`` mappings,
                         specifying custom formatters to use for specific
                         variables.

    :arg numRows:        Number of rows to write at a time. Defaults to
                         :attr:`NUM_ROWS`.

    :arg nonNumericFile: If provided, non-numeric columns (after formatting)
                         are saved to this file instead of to ``outfile``
    """

    if sep           is None: sep           = TSV_SEP
    if missingValues is None: missingValues = ''
    if dateFormat    is None: dateFormat    = 'default'
    if timeFormat    is None: timeFormat    = 'default'
    if formatters    is None: formatters    = {}
    if numRows       is None: numRows       = NUM_ROWS

    # We're going to output each chunk of
    # subjects to a separate file (in
    # parallel), and then cat the files
    # together afterwards
    index      = dtable.index
    nchunks    = int(np.ceil(len(index) / numRows))
    idxchunks  = [index[i:i + numRows] for i in
                  range(0, len(index), numRows)]
    subtables  = [dtable.subtable(rows=c) for c in idxchunks]
    outfiles   = ['{}_{}'.format(outfile, i) for i in range(nchunks)]

    if nonNumericFile is not None:
        nnfiles = ['{}_{}'.format(nonNumericFile, i) for i in range(nchunks)]
    else:
        nnfiles = [None] * nchunks

    # write each chunk in parallel
    args = zip(subtables,
               outfiles,
               nnfiles,
               [True] + [False] * (nchunks - 1),
               range(nchunks))
    func = ft.partial(writeDataFrame,
                      idcol=idcol,
                      colnames=colnames,
                      sep=sep,
                      missingValues=missingValues,
                      dateFormat=dateFormat,
                      timeFormat=timeFormat,
                      formatters=formatters)

    with dtable.pool() as pool:
        pool.starmap(func, args)

    # concatenate the chunks to
    # form the final output file
    if len(outfiles) == 1:
        os.rename(outfiles[0], outfile)
    else:
        util.cat(outfiles, outfile)

    if nonNumericFile is not None and all([op.exists(f) for f in nnfiles]):
        if len(nnfiles) == 1:
            os.rename(nnfiles[0], nonNumericFile)
        else:
            util.cat(nnfiles, nonNumericFile)

    # remove intermediate files
    for f in outfiles + nnfiles:
        if f is not None and op.exists(f):
            os.remove(f)


def writeDataFrame(dtable,
                   outfile,
                   nonNumericFile,
                   header,
                   chunki,
                   idcol,
                   colnames,
                   sep,
                   missingValues,
                   dateFormat,
                   timeFormat,
                   formatters):
    """Writes all of the data in ``dtable`` to ``outfile``.

    Called by :func:`exportTSV` to output one chunk of data.

    :arg dtable:         :class:`.DataTable` containing the data

    :arg outfile:        File to output to

    :arg nonNumericFile: If provided, non-numeric columns (after formatting)
                         are saved to this file instead of to ``outfile``

    :arg header:         If ``True``, write the header row (column names).

    :arg idcol:          Name to use for the subject ID column

    :arg colnames:       Dict containing ``{oldcol : newcol}`` mappings

    :arg chunki:         Chunk index (used for logging)

    :arg sep:            Separator character to use. Defaults to
                         :attr:`TSV_SEP`

    :arg missingValues:  String to use for missing/NA values. Defaults to the
                         empty string.

    :arg dateFormat:     Name of formatter to use for date columns.

    :arg timeFormat:     Name of formatter to use for time columns.

    :arg formatters:     Dict of ``{ [vid|column] : formatter }`` mappings,
                         specifying custom formatters to use for specific
                         variables.
    """

    # If nonNumericFile is specified, we
    # store the names of all numeric and
    # non-numeric columns here so we can
    # figure out which columns to put
    # where. We run the columns through
    # formatting before deciding whether
    # they are numeric or non-numeric.
    numericCols    = []
    nonNumericCols = []

    columns = dtable.dataColumns
    towrite = pd.DataFrame(index=dtable.index)

    log.info('Writing %u columns and %u rows [chunk %u] to %s ...',
             len(columns), len(dtable), chunki, outfile)

    # Format every column, and
    # separate out into numeric
    # and non-numeric
    for col in columns:
        name   = colnames.get(col.name, col.name)
        series = formatColumn(
            col, dtable, dateFormat, timeFormat, formatters, chunki)

        towrite[name] = series

        # now we can tell whether this column
        # is numeric or non- numeric - store
        # its name accordingly
        if pdtypes.is_numeric_dtype(series): numericCols   .append(name)
        else:                                nonNumericCols.append(name)

    # Do we have any non-numeric columns?
    if (nonNumericFile is None) or (len(nonNumericCols) == 0):
        numericChunk   = towrite
        nonNumericFile = None

    else:
        numericChunk    = towrite[numericCols]
        nonNumericChunk = towrite[nonNumericCols]

        log.debug('Redirecting %i non-numeric columns to %s '
                  '(remaining %i columns will be written to %s)',
                  len(nonNumericCols), nonNumericFile,
                  len(numericCols),    outfile)

    if not header:
        idcol = None

    numericChunk.to_csv(outfile,
                        sep=sep,
                        na_rep=missingValues,
                        header=header,
                        index_label=idcol)

    if nonNumericFile is not None:
        nonNumericChunk.to_csv(nonNumericFile,
                               sep=sep,
                               na_rep=missingValues,
                               header=header,
                               index_label=idcol)


def formatColumn(col,
                 dtable,
                 dateFormat,
                 timeFormat,
                 formatters,
                 chunki):
    """Formats the data for the specified column.

    :arg col:        :class:`.Column` to format

    :arg dtable:     :class:`.DataTable` containing the data

    :arg dateFormat: Name of formatter to use for date columns.

    :arg timeFormat: Name of formatter to use for time columns.

    :arg formatters: Dict of ``{ [vid|column] : formatter }`` mappings,
                     specifying custom formatters to use for specific
                     variables.

    :arg chunki:     Output chunk index (used for logging).

    :returns:        ``pandas.Series`` instance containing the formatted data.
    """

    vid      = col.basevid
    vartable = dtable.vartable
    series   = dtable[:, col.name]

    # formatters can be specified
    # by VID or by column name
    formatter = formatters.get(vid, None)
    if formatter is None:
        formatter = formatters.get(col.name, None)

    if vid in vartable.index: vtype = vartable['Type'][vid]
    else:                     vtype = None

    # fall back to date/time formatting
    # if relevant for this column
    if formatter is None:
        if   vtype == util.CTYPES.date:
            formatter = dateFormat
        elif vtype == util.CTYPES.time or \
             pdtypes.is_datetime64_any_dtype(series):
            formatter = timeFormat

    if formatter is not None:
        log.debug('Formatting column %s [chunk %u] with %s formatter',
                  col.name, chunki, formatter)
        series = custom.runFormatter(formatter, dtable, col, series)

    # apply column-specific fill
    # value, if there is one
    if col.fillval is not None:
        series.fillna(value=col.fillval, inplace=True)

    return series
