import pandas


class InputCSV(object):
    """
    Load a single CSV into a `pandas.DataFrame`.
    """

    def __init__(self, csv_path, primary_key):
        self.primary_key = primary_key
        self.data_frame = pandas.read_csv(
            csv_path,
            delimiter=';',
            encoding='utf-8',
            dtype='object',
        )


class InputBundle(object):
    """
    Combine multiple CSV's into a single `pandas.DataFrame`.
    """

    def __init__(self, *csvs):
        self.data_frame = csvs[0].data_frame
        for previous, current in zip(csvs, csvs[1:]):
            self.data_frame = pandas.merge(
                self.data_frame,
                current.data_frame,
                how='outer',
                left_on=previous.primary_key,
                right_on=current.primary_key,
            )
