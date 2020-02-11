"""GraceDB API endpoints."""
from .events import Events, Superevents


class API:

    def __init__(self, url, session):
        self.url = url
        self.session = session
        self.events = Events(self)
        self.superevents = Superevents(self)
