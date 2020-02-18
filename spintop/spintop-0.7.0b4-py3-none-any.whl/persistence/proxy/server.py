from ..base import PersistenceFacade

class ProxyPersistenceFacadeServer(PersistenceFacade):
    def __init__(self, real_facade):
        self._real_facade = real_facade