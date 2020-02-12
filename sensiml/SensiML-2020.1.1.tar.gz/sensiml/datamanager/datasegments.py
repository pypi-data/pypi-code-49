import matplotlib.pyplot as plt


class DataSegment(object):
    def __init__(self, data, metadata, label=None):
        self._metadata = metadata
        self._label = label
        self._original_index = data.index
        self._data = data.reset_index(drop=True)

    def plot(self, **kwargs):
        self._data.plot(title=self.__str__(), **kwargs)

    def __str__(self):
        return " ".join(["{}:{}".format(k, v) for k, v in self._metadata.items()])


class DataSegments(list):
    def plot(self, **kwargs):
        for segment in self.__iter__():
            segment.plot(**kwargs)


def to_datasegments(data, metdata_columns, label_column):
    """ Converts a dataframe into a data setments """

    group_columns = metdata_columns + [label_column]
    g = data.groupby(group_columns)
    ds = DataSegments()

    data_columns = [x for x in data.columns if x not in group_columns]

    for key in g.groups.keys():

        metadata = {}
        for index, value in enumerate(group_columns):
            metadata[value] = key[index]

        tmp_df = g.get_group(key)[data_columns]

        ds.append(DataSegment(tmp_df, metadata, metadata[label_column]))

    return ds

