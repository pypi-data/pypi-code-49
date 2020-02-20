class A(object):

    __slots__ = ('_tup','_ref')

    _meta_fields = ['x', 'y']
    _sub_fields = ['a', 'b', '*args']

    @classmethod
    def _preprocess_(self, *args):
        """
        Override this in subclasses to preprocess the arguments to the
        constructor.

        This is here so that code using this class doesn't care if
        it's initialized using __init__ or using __new__ (as is
        recstruct_tuple).

        """
        return args

    def __init__(self, x, y, a, b, *args, , **kwargs):
        self._tup = tuple(type(self)._preprocess_(x, y, a, b, *args, ))
        self._ref = kwargs.get('ref',None)

    def __repr__(self):
        """Return a nicely formatted representation string"""
        return type(self).__name__ + repr(self._tup)

    def __eq__(self, other):
        return type(self) is type(other) and (self._tup) == (other._tup)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return ((A,) + self._tup) < other

    def __le__(self, other):
        return ((A,) + self._tup) <= other

    def __gt__(self, other):
        return ((A,) + self._tup) > other

    def __ge__(self, other):
        return ((A,) + self._tup) >= other

    def __hash__(self):
        #return hash((type(self), ) + self._tup)
        return self._tup.__hash__()

    def _subs(self):
        return self._tup[2:]

    def __getslice__(self, i, j):
        return self._subs().__getslice__(i, j)

    def __getitem__(self, i):
        return self._subs().__getitem__(i)

    def __iter__(self):
        return self._subs().__iter__()

    def __contains__(self, x):
        return self._subs().__contains__(x)

    def __len__(self):
        return self._subs().__len__()

    def __nonzero__(self):
        raise TypeError("recstruct should not be converted to bool")

    def __getstate__(self):
        return {'_tup': self._tup}

    def __setstate__(self, state):
        self._tup = state['_tup']

    @property
    def ref(self):
        return self._ref

    x = _property(_itemgetter(0))

    y = _property(_itemgetter(1))

    a = _property(_itemgetter(2))

    b = _property(_itemgetter(3))

    args = _property(_itemgetter(slice(4, None)))

