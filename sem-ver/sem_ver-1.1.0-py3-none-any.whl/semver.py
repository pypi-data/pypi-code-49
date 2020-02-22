"""Semantic version processor."""


import itertools
import re
from functools import total_ordering
from typing import Any, List, Optional, Sequence, Union, cast


SEMVER_REGEX = re.compile(r'''
    ^(?P<major>0|[1-9]\d*)
    \.
    (?P<minor>0|[1-9]\d*)
    \.
    (?P<patch>0|[1-9]\d*)
    (?:-
        (?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        )
    )?
    (?:\+
        (?P<build>
            (?:[0-9a-zA-Z-]+)
            (?:\.[0-9a-zA-Z-]+)*
        )
    )?
    $''', re.VERBOSE)
PRERELEASE_REGEX = re.compile(r'^(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*$')
BUILD_REGEX = re.compile(r'^(?:[0-9a-zA-Z-]+)(?:\.[0-9a-zA-Z-]+)*$')
RELAXED_REGEX = re.compile(r'''
    ^[a-zA-Z]*
    (?P<major>\d+)
    (?:\.
        (?P<minor>\d+)
        (?:\.
            (?P<patch>\d+)
        )?
    )?
    (?:-?
        (?P<prerelease>
            (?:[0-9a-zA-Z-\.]*)
        )?
    )?
    (?:\+
        (?P<build>
            (?:[0-9a-zA-Z-]+)
            (?:\.[0-9a-zA-Z-]+)*
        )?
    )?
    $''', re.VERBOSE)


@total_ordering
class SemVer:
    """
    Class to handle Semantic Versions.

    per https://semver.org.
    """

    _major: int
    _minor: int
    _patch: int
    prereleases: List[Union[int, str]]
    builds: List[str]

    @classmethod
    def validate(cls, version: str) -> bool:
        """Test if string is valid SemVer."""
        try:
            cls(version=version)
            return True
        except ValueError:
            return False

    @classmethod
    def compare(cls, version_a: str, version_b: str) -> int:
        """Compare two version strings."""
        a = SemVer(version_a)
        b = SemVer(version_b)
        if (a == b):
            return 0
        return (-1 if (a < b) else 1)

    @classmethod
    def force(cls, version: str) -> Optional['SemVer']:
        """Attempt for create a SemVer with relaxed parsing rules."""
        match = RELAXED_REGEX.match(version)
        if (match is None):
            return None
        parts = match.groupdict()
        semver = cls(major=int(parts['major'] or 0), minor=int(parts['minor'] or 0), patch=int(parts['patch'] or 0))
        try:
            semver.prerelease = parts['prerelease'].strip('.') if (parts['prerelease']) else None
        except ValueError:
            pass
        try:
            semver.build = parts['build'].strip('.') if (parts['build']) else None
        except ValueError:
            pass
        return semver

    def __init__(self, version: str = None,
                 major: int = 0, minor: int = 0, patch: int = 0,
                 prerelease: Union[str, Sequence[Union[int, str]]] = '',
                 build: Union[str, Sequence[str]] = '') -> None:
        self._major = major
        self._minor = minor
        self._patch = patch
        if (isinstance(prerelease, str)):
            self.prerelease = prerelease
        else:
            self.prereleases = list(prerelease)
        if (isinstance(build, str)):
            self.build = build
        else:
            self.builds = list(build)

        if (version is not None):
            match = SEMVER_REGEX.match(version)
            if (match is None):
                raise ValueError('Invalid SemVer: "{version}"'.format(version=version))
            parts = match.groupdict()
            self._major = int(parts['major'])
            self._minor = int(parts['minor'])
            self._patch = int(parts['patch'])
            self.prereleases = self._split_prerelease(parts.get('prerelease'))
            self.builds = self._split_build(parts.get('build'))

    def _split_prerelease(self, value: str = None) -> List[Union[int, str]]:
        def _convert(part: str) -> Union[int, str]:
            try:
                return int(part)
            except ValueError:
                return part
        return [_convert(part) for part in value.split('.')] if (value) else []

    def _split_build(self, value: str = None) -> List[str]:
        return value.split('.') if (value) else []

    @property
    def major(self) -> int:
        """Get major version."""
        return self._major

    @major.setter
    def major(self, value: int) -> None:
        """Set major version, reset rest."""
        self._major = value
        self.minor = 0

    @property
    def minor(self) -> int:
        """Get minor version."""
        return self._minor

    @minor.setter
    def minor(self, value: int) -> None:
        """Set minor version, reset rest."""
        self._minor = value
        self.patch = 0

    @property
    def patch(self) -> int:
        """Get patch version."""
        return self._patch

    @patch.setter
    def patch(self, value: int) -> None:
        """Set patch version, reset prerelease."""
        self._patch = value
        self.prerelease = None

    @property
    def prerelease(self) -> Optional[str]:
        """Get prereleases as a single string."""
        return '.'.join([str(prerelease) for prerelease in self.prereleases]) if (self.prereleases) else None

    @prerelease.setter
    def prerelease(self, value: Optional[str]) -> None:
        if (value and (PRERELEASE_REGEX.match(value) is None)):
            raise ValueError('Invalid prerelease tags: "{value}"'.format(value=value))
        self.prereleases = self._split_prerelease(value)
        self.build = None

    @property
    def build(self) -> Optional[str]:
        """Get builds as a single string."""
        return '.'.join([str(build) for build in self.builds]) if (self.builds) else None

    @build.setter
    def build(self, value: Optional[str]) -> None:
        if (value and (BUILD_REGEX.match(value) is None)):
            raise ValueError('Invalid build tags: "{value}"'.format(value=value))
        self.builds = self._split_build(value)

    def next_major(self) -> 'SemVer':
        """Create new version at next major."""
        return SemVer(major=(self.major + 1))

    def next_minor(self) -> 'SemVer':
        """Create new version at next minor."""
        return SemVer(major=self.major, minor=(self.minor + 1))

    def next_patch(self) -> 'SemVer':
        """Create new version at next patch."""
        return SemVer(major=self.major, minor=self.minor, patch=(self.patch + 1))

    def __str__(self) -> str:
        """Convert to string."""
        return (str(self.major) + '.' + str(self.minor) + '.' + str(self.patch)
                + (('-' + cast(str, self.prerelease)) if (self.prereleases) else '')
                + (('+' + cast(str, self.build)) if (self.builds) else ''))

    def __eq__(self, other: Any) -> bool:
        """Compare equality, does not compare builds."""
        if (not isinstance(other, SemVer)):
            other = SemVer(str(other))
        return ((other.major == self.major) and (other.minor == self.minor)
                and (other.patch == self.patch) and (other.prereleases == self.prereleases))

    def _prerelease_lt(self, other: 'SemVer') -> bool:
        def compare_part(a: Union[int, str], b: Union[int, str]) -> int:
            if isinstance(a, int) and isinstance(b, int):
                return ((b < a) - (a < b))
            elif isinstance(a, int):
                return -1
            elif isinstance(b, int):
                return 1
            return ((b < a) - (a < b))

        for self_part, other_part in itertools.zip_longest(self.prereleases, other.prereleases, fillvalue=''):
            result = compare_part(self_part, other_part)
            if result != 0:
                return (result < 0)
        return False

    def __lt__(self, other: Any) -> bool:
        """Compare to other version."""
        if (not isinstance(other, SemVer)):
            other = SemVer(str(other))
        if (self.major < other.major):
            return True
        if (self.major == other.major):
            if (self.minor < other.minor):
                return True
            if (self.minor == other.minor):
                if (self.patch < other.patch):
                    return True
                if (self.patch == other.patch):
                    if (self.prerelease and not other.prerelease):
                        return True
                    if (self.prerelease and other.prerelease):
                        return self._prerelease_lt(other)
        return False
