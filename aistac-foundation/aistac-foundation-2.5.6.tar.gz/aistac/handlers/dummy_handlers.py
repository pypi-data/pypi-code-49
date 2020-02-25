from aistac.handlers.abstract_handlers import AbstractSourceHandler, ConnectorContract, AbstractPersistHandler

__author__ = 'Darryl Oatridge'


class DummySourceHandler(AbstractSourceHandler):
    """ A dummy handler that doesn't read from disk but returns an empty dictionary. This can be used with the
        Properties Manager if persistence is not wanted or don't have permission to write to store but wish to run in
        memory
    """

    def __init__(self, connector_contract: ConnectorContract):
        """ initialise the Handler passing the source_contract dictionary """
        super().__init__(connector_contract)

    def supported_types(self) -> list:
        """ The source types supported with this module"""
        return []

    def load_canonical(self, **kwargs) -> dict:
        """ returns an empty canonical dictionary """
        return dict()

    def exists(self) -> bool:
        """ Returns True is the file exists """
        return True

    def get_modified(self) -> [int, float, str]:
        """ returns if the file has been modified"""
        return 0


class DummyPersistHandler(DummySourceHandler, AbstractPersistHandler):
    """ A dummy handler that doesn't write to disk. This can be used with the Properties Manager if persistence
        is not wanted or don't have permission to write to store but wish to run in memory
    """

    def persist_canonical(self, canonical: dict, **kwargs):
        """ persists the canonical dataset """
        return

    def remove_canonical(self) -> bool:
        """removes the canonical"""
        return True

    def backup_canonical(self, canonical: dict, uri: str, **kwargs):
        """ creates a backup of the canonical to am alternative URI """
        return
