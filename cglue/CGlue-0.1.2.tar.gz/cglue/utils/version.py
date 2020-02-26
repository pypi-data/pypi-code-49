import re


version_re = re.compile('(?P<major>\\d+?)\\.(?P<minor>\\d+?)(\\.(?P<rev>\\d+))?(-(?P<branch>.*?))?$')
constraint_re = re.compile('(?P<start>[\\[(])(?P<min>.*?),\\s?(?P<max>.*?)?(?P<end>[\\])])?$')


def cmp(a, b):
    return -1 if a < b else 1


class FormatError(Exception):
    pass


class Version:
    def __init__(self, ver_str):
        """
        >>> Version('1.0.123')
        Version(1.0.123)
        >>> Version('1.0-foobar')
        Version(1.0.0-foobar)
        """
        match = version_re.match(ver_str)
        if not match:
            raise FormatError
        self._major = int(match.group('major'))
        self._minor = int(match.group('minor'))
        self._rev = int(match.group('rev')) if match.group('rev') else 0
        self._branch = match.group('branch') or 'stable'
        if self._branch == 'stable':
            self._normalized = f'{self._major}.{self._minor}.{self._rev}'
        else:
            self._normalized = f'{self._major}.{self._minor}.{self._rev}-{self._branch}'

    @property
    def major(self):
        """
        >>> Version('2.3').major
        2
        """
        return self._major

    @property
    def minor(self):
        """
        >>> Version('2.3').minor
        3
        """
        return self._minor

    @property
    def revision(self):
        """
        >>> Version('2.3.45').revision
        45
        """
        return self._rev

    @property
    def branch(self):
        """
        >>> Version('2.3-foobranch').branch
        'foobranch'
        """
        return self._branch

    def __le__(self, other):
        """
        >>> Version('1.0.0') <= Version('1.0.0')
        True
        >>> Version('1.0.0') <= Version('1.0.1')
        True
        >>> Version('1.0.0') <= Version('1.1.0')
        True
        >>> Version('1.0.0') <= Version('2.0.0')
        True
        >>> Version('1.0.1') <= Version('1.0.0')
        False
        >>> Version('1.1.0') <= Version('1.0.0')
        False
        >>> Version('2.0.0') <= Version('1.0.0')
        False
        """
        return self.compare(other) != 1

    def __eq__(self, other):
        """
        >>> Version('1.0.0') == Version('1.0.0')
        True
        >>> Version('1.0.0') == Version('1.0.1')
        False
        >>> Version('1.0.0') == Version('1.1.0')
        False
        >>> Version('1.0.0') == Version('2.0.0')
        False
        >>> Version('1.0.0') == Version('1.0.0-dev')
        False
        """
        return self.compare(other) == 0 and self.branch == other.branch

    def __ne__(self, other):
        """
        >>> Version('1.0.0') != Version('1.0.0')
        False
        >>> Version('1.0.0') != Version('1.0.1')
        True
        >>> Version('1.0.0') != Version('1.1.0')
        True
        >>> Version('1.0.0') != Version('2.0.0')
        True
        >>> Version('1.0.0') != Version('1.0.0-dev')
        True
        """
        return not (self == other)

    def __lt__(self, other):
        """
        >>> Version('1.0.0') < Version('1.0.0')
        False
        >>> Version('1.0.0') < Version('1.0.1')
        True
        >>> Version('1.0.0') < Version('1.1.0')
        True
        >>> Version('1.0.0') < Version('2.0.0')
        True
        >>> Version('1.0.1') < Version('1.0.0')
        False
        >>> Version('1.1.0') < Version('1.0.0')
        False
        >>> Version('2.0.0') < Version('1.0.0')
        False
        """
        return self.compare(other) == -1

    def __gt__(self, other):
        """
        >>> Version('1.0.0') > Version('1.0.0')
        False
        >>> Version('1.0.0') > Version('1.0.1')
        False
        >>> Version('1.0.0') > Version('1.1.0')
        False
        >>> Version('1.0.0') > Version('2.0.0')
        False
        >>> Version('1.0.1') > Version('1.0.0')
        True
        >>> Version('1.1.0') > Version('1.0.0')
        True
        >>> Version('2.0.0') > Version('1.0.0')
        True
        """
        return self.compare(other) == 1

    def __ge__(self, other):
        """
        >>> Version('1.0.0') >= Version('1.0.0')
        True
        >>> Version('1.0.0') >= Version('1.0.1')
        False
        >>> Version('1.0.0') >= Version('1.1.0')
        False
        >>> Version('1.0.0') >= Version('2.0.0')
        False
        >>> Version('1.0.1') >= Version('1.0.0')
        True
        >>> Version('1.1.0') >= Version('1.0.0')
        True
        >>> Version('2.0.0') >= Version('1.0.0')
        True
        """
        return self.compare(other) != -1

    # noinspection PyProtectedMember
    def compare(self, other):
        """
        >>> Version('1.0.0').compare(Version('1.0.0'))
        0
        >>> Version('1.0.1').compare(Version('1.0.0'))
        1
        >>> Version('1.0.0').compare(Version('1.0.1'))
        -1
        """

        if self._major != other._major:
            return cmp(self._major, other._major)
        elif self._minor != other._minor:
            return cmp(self._minor, other._minor)
        elif self._rev != other._rev:
            return cmp(self._rev, other._rev)
        return 0

    def __str__(self) -> str:
        """
        >>> str(Version('1.0'))
        '1.0.0'
        >>> str(Version('1.0-dev'))
        '1.0.0-dev'
        """
        return self._normalized

    def __repr__(self):
        return f'Version({self._normalized})'

    def __hash__(self) -> int:
        return self._normalized.__hash__()


class VersionConstraint:
    """
    >>> constraint = VersionConstraint('[3.2.1, 3.3.2]')
    >>> constraint.check(Version('3.3.1'))
    True
    >>> constraint.check(Version('3.4.1'))
    False

    >>> constraint = VersionConstraint('[3.2.1, ')
    >>> constraint.check(Version('3.2.1'))
    True
    >>> constraint.check(Version('3.3.1'))
    True
    >>> constraint.check(Version('3.4.1'))
    True

    >>> constraint = VersionConstraint('(3.2.1, ')
    >>> constraint.check(Version('3.2.1'))
    False
    """
    def __init__(self, constraint):
        match = constraint_re.match(constraint)
        if not match:
            raise FormatError

        min_version = match.group('min')
        max_version = match.group('max')
        start = match.group('start')
        end = match.group('end') or ''

        self._bounds = start + end
        self._min_version = Version(min_version)

        if max_version:
            self._max_version = Version(max_version)
        else:
            self._max_version = None

    def check(self, version: Version):
        compares = {
            '[]': lambda minimum, maximum: minimum <= version <= maximum,
            '(]': lambda minimum, maximum: minimum < version <= maximum,
            '[)': lambda minimum, maximum: minimum <= version < maximum,
            '()': lambda minimum, maximum: minimum < version < maximum,
            '[': lambda minimum, _: minimum <= version,
            '(': lambda minimum, _: minimum < version
        }
        return compares[self._bounds](self._min_version, self._max_version)

    def __str__(self):
        patterns = {
            '[]': lambda minimum, maximum: f'{minimum} <= version <= {maximum}',
            '(]': lambda minimum, maximum: f'{minimum} < version <= {maximum}',
            '[)': lambda minimum, maximum: f'{minimum} <= version < {maximum}',
            '()': lambda minimum, maximum: f'{minimum} < version < {maximum}',
            '[': lambda minimum, _: f'{minimum} <= version',
            '(': lambda minimum, _: f'{minimum} < version'
        }
        return patterns[self._bounds](self._min_version, self._max_version)
