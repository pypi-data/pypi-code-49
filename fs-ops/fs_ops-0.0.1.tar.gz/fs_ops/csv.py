import csv


def rows2csv(path,
             rows,
             writer_kwds={'delimiter':',',
                          'quotechar':'"',
                          'quoting':csv.QUOTE_MINIMAL}):
    """Dump rows to csv.
    
    Arguments:
        path (str): where to dump the outputs.
        rows (iter): iterable of values to put into the csv.
        writer_kwds (dict): parameters for csv.writer
    """
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f,**writer_kwds)
        for r in rows:
            writer.writerow(r)

