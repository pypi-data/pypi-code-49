from cvplotlib.data_source import base


class CollectionDataSource(base.BaseDataSource):
    """docstring for CollectionDataSource"""

    def load_data(self) -> None:
        raise NotImplementedError

    def preprocess(self) -> None:
        raise NotImplementedError

    def postprocess(self) -> None:
        raise NotImplementedError
