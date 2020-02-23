import math
from quicktions import Fraction


class ArithmeticProgression(object):
    def __init__(self, a1=None, an=None, n=None, d=None, s=None):
        self._a1 = None
        self._an = None
        self._n = None
        self._d = None
        self._s = None
        self._current = None
        self._index = None

        self.a1 = a1
        self.an = an
        self.n = n
        self.d = d
        self.s = s

    def _check_args(self):

        if len([v for v in self._parameters_dict.values() if v is not None]) > 2:
            err = 'attribute cannot be set. Three parameters are already set. ArithmeticProgression is already created!'
            raise AttributeError(err)

    def _calculate_a1(self):
        if self._d is None:
            self._a1 = (2. * self.s / self.n) - self.an
        elif self._s is None:
            self._a1 = self.an - ((self.n - 1) * self.d)

    def _calculate_an(self):
        if self._s is None:
            self._an = self.a1 + (self.n - 1) * self.d
        elif self._d is None:
            self._an = (2. * self.s / self.n) - self.a1

    def _calculate_n(self):
        if self._s is None:
            self._n = ((self.an - self.a1) / self.d) + 1
        elif self._d is None:
            self._n = 2. * self.s / (self.a1 + self.an)
        self._n = math.floor(self._n)

    def _calculate_d(self):

        if self._a1 is None:
            self._calculate_a1()
            self._d = Fraction(Fraction(self.an - self.a1), Fraction(self.n - 1))
        elif self._an is None:
            self._d = Fraction(Fraction((self.s - (self.n * self.a1)) * 2), Fraction((self.n - 1) * self.n))
        elif self._n is None:
            self._calculate_n()
            self._d = Fraction(Fraction(self.an - self.a1), Fraction(self.n - 1))
        else:
            self._d = Fraction(Fraction(self.an - self.a1), Fraction(self.n - 1))

    def _calculate_s(self):
        if self._a1 is None:
            self._calculate_a1()
            self._s = self.n * (self.a1 + self.an) / 2.
        elif self._an is None:
            self._s = self.n * self.a1 + ((self.n - 1) * self.n / 2) * self.d
        elif self._n is None:
            self._calculate_n()
            self._s = self.n * (self.a1 + self.an) / 2.
        else:
            self._s = self.n * (self.a1 + self.an) / 2.

    @property
    def _parameters_dict(self):
        return {'a': self._a1, 'an': self._an, 'n': self._n, 'd': self._d, 's': self._s}

    @property
    def parameters_dict(self):
        return {'a': self.a1, 'an': self.an, 'n': self.n, 'd': self.d, 's': self.s}

    @property
    def a1(self):
        if self._a1 is None:
            self._calculate_a1()
        return self._a1

    @a1.setter
    def a1(self, value):
        if value is not None:
            self._check_args()
        self._a1 = value

    @property
    def an(self):
        if self._an is None:
            self._calculate_an()
        return self._an

    @an.setter
    def an(self, value):
        if value is not None:
            self._check_args()
        self._an = value

    @property
    def n(self):
        if self._n is None:
            self._calculate_n()
        return self._n

    @n.setter
    def n(self, value):
        if value is not None:
            self._check_args()
        self._n = value

    @property
    def s(self):
        if self._s is None:
            self._calculate_s()
        return self._s

    @s.setter
    def s(self, value):
        if value is not None:
            self._check_args()
            if self._d is not None:
                err = 'you cannot set both d an s!'
                raise AttributeError(err)
        self._s = value

    @property
    def d(self):
        if self._d is None:
            self._calculate_d()
        return self._d

    @d.setter
    def d(self, value):
        if value is not None:
            self._check_args()
            if self._s is not None:
                err = 'you cannot set both d an s!'
                raise AttributeError(err)
        self._d = value

    def __iter__(self):
        return self

    def __next__(self):
        parameters = [self.a1, self.an, self.n, self.s, self.d]

        if len([v for v in parameters if v is not None]) < 5:
            err = 'Not enough parameter set to create an arithmetic progression. 3 parameters should be set first (s ' \
                  'and d cannot be set together) '
            raise Exception(err)

        if self._current is None:
            self._current = self.a1
            self._index = 0
        else:
            self._index += 1
            self._current += self.d

        if self._index < self.n:
            return self._current
        else:
            raise StopIteration()

    @property
    def index(self):
        return self._index

    def rest(self):
        self._current = None
