import os
import yaml


class NodeMissingError(KeyError):
    """Raised if data node doesn't exist."""


class QueryTypeError(TypeError):
    """Raised if query is of an invalid type."""


class SourceInvalidError(FileNotFoundError):
    """Raised if the data source cannot be found."""


class ValueCountError(Exception):
    """Raised if query is incomplete."""


class Reader:
    def __init__(self, source: str) -> None:
        yaml_data = os.path.join(os.path.dirname(__file__), "sources.yml")
        try:
            if not os.path.exists(yaml_data):
                raise SourceInvalidError(
                    "Cannot find source at '{}'!".format(yaml_data)
                )
            data_source = yaml.load(open(yaml_data), Loader=yaml.FullLoader)
            if source not in data_source:
                raise NodeMissingError("Cannot find source table '{}'!".format(source))
            self.data_source = data_source[source]
            sorted(self.data_source)
        except SourceInvalidError as error:
            exit(error)
        except NodeMissingError as error:
            exit(error)

    def find(self, query=None) -> (dict, list):
        """Returns results for query, if any."""
        data_source = self.data_source
        if query is None or isinstance(query, (list, tuple)) and len(query) is 0:
            return data_source
        try:
            if not isinstance(query, (list, tuple)):
                raise QueryTypeError(
                    "find: query argument must be type 'list' or 'tuple'!"
                )
            if len(query) == 3:
                data_source = self.data_source[query[0]][query[1]][query[2]]
            elif len(query) == 2:
                data_source = self.data_source[query[0]][query[1]]
            elif len(query) == 1:
                data_source = self.data_source[query[0]]
            else:
                raise ValueCountError(
                    "find: query requires a max of '3' purged_values. {} given.".format(
                        len(query)
                    )
                )
        except ValueCountError as error:
            exit("find: {}".format(error))
        except QueryTypeError as error:
            exit(error)
        except KeyError:
            return dict()
        else:
            if isinstance(data_source, dict):
                sorted(data_source)
            if isinstance(data_source, list):
                data_source.sort()
        return data_source
