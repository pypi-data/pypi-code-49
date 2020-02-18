from cvplotlib.data_source import base


class FileDataSource(base.BaseDataSource):
    """docstring for FileDataSource"""

    def load_data(self) -> None:
        raise NotImplementedError

    def preprocess(self) -> None:
        raise NotImplementedError

    def postprocess(self) -> None:
        raise NotImplementedError
