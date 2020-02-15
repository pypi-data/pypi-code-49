import collections
import json
from .ZeitzonoCity import ZeitzonoCity
import copy


class ZeitzonoCities:
    """
    a city list object

    NB: We actually kinda do a bad thing by returning this class
        for search results. We should have a separate class (maybe called
        ZeitzonoSearchResults) that inherits it and then adds the
        self.nresults variable.

        We will need to refactor this later.
    """

    def __init__(self, cities=None, nresults=None):
        if cities is None:
            self.cities = []
        else:
            self.cities = cities
        self.nresults = nresults

        self.undo_stack = []
        self.redo_stack = []

    def save_state(self):
        city_copy = copy.copy(self.cities)
        self.undo_stack.append(city_copy)
        self.redo_stack = []

        if len(self.undo_stack) > 10:
            self.undo_stack.pop(0)

    def undo(self):
        if len(self.undo_stack) > 0:
            old_state = self.undo_stack.pop()
            self.redo_stack.append(self.cities)
            self.cities = old_state

    def redo(self):
        if len(self.redo_stack) > 0:
            new_state = self.redo_stack.pop()
            self.undo_stack.append(self.cities)
            self.cities = new_state

    def numcities(self):
        return len(self.cities)

    def numresults(self):
        return self.nresults

    def isempty(self):
        return self.numcities() == 0

    def addcity(self, city):
        self.save_state()
        self.cities.append(city)

    def addcities(self, hcities):
        self.save_state()
        self.cities.extend(hcities.cities)

    def clear(self):
        self.save_state()
        self.cities = []
        self.nresults = None

    def del_first(self):
        self.save_state()
        if self.cities:
            self.cities.pop(0)

    def del_last(self):
        self.save_state()
        if self.cities:
            self.cities.pop()

    def _rotate(self, n):
        if self.cities:
            self.save_state()
            deck = collections.deque(self.cities)
            deck.rotate(n)
            self.cities = list(deck)

    def rotate_right(self):
        self._rotate(1)

    def rotate_left(self):
        self._rotate(-1)

    def roll_4(self):
        if self.numcities() >= 4:
            self.save_state()
            city1 = self.cities.pop()
            city2 = self.cities.pop()
            city3 = self.cities.pop()
            city4 = self.cities.pop()

            self.cities.append(city1)
            self.cities.append(city4)
            self.cities.append(city3)
            self.cities.append(city2)

    def roll_3(self):
        if self.numcities() >= 3:
            self.save_state()
            city1 = self.cities.pop()
            city2 = self.cities.pop()
            city3 = self.cities.pop()
            self.cities.append(city1)
            self.cities.append(city3)
            self.cities.append(city2)

    def roll_2(self):
        if self.numcities() >= 2:
            self.save_state()
            city1 = self.cities.pop()
            city2 = self.cities.pop()
            self.cities.append(city1)
            self.cities.append(city2)

    def sort_utc_offset(self, reverse=False):
        self.save_state()
        self.cities.sort(key=lambda city: city.utc_offset(), reverse=reverse)

    def __iter__(self):
        return iter(self.cities)

    def _hcity_to_dict(self, c):
        # used by self.toJSON() to serialize
        return c.__dict__

    def toJSON(self, filehandle):
        return json.dump(self.cities, filehandle, default=self._hcity_to_dict, indent=4)

    def fromJSON(self, filehandle):
        string_cities = json.load(filehandle)
        self.cities = []
        for sc in string_cities:
            hc = ZeitzonoCity(**sc)
            self.cities.append(hc)
