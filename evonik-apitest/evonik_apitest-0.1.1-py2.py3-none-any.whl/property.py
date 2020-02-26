from .endpoints import Endpoints

class Property:
    """Model of a single property with different valid and invalid values.

    Parameters
    ----------
    name: str
        Name of the property
    valids: list or callable
        Specification of valid values
    invalids: list or callable
        Specification of invalid values
    required: list of str, default None
        List of endpoints this property is required for
    excluded: list of str, default ['GET', DELETE', 'LIST']
        List of endpoints this property should be excluded from
    spec_name: str, default None
        Name used in the payload spec (name if None)
    res_name: str, default None
        Name expected in the endpoint's result (nane if None)

    Examples
    --------
    Property("name", rand_str, [""], [Endpoints.CREATE])
    Property("description", rand_str, [])
    Property("count", rand_int, [])
    """
    def __init__(self, name, valids, invalids,
                 required=None, excluded=None,
                 spec_name=None, res_name=None):
        if name is None:
            raise ValueError("Must specify a name")
        if valids is None:
            raise ValueError("Must specify valids")
        if invalids is None:
            raise ValueError("Must specify invalids")
        self.name = name
        self.valids = valids
        self.invalids = invalids
        self.required = required if required is not None else []
        self.excluded = excluded if excluded is not None else [Endpoints.GET, Endpoints.DELETE, Endpoints.LIST]
        for r in self.required:
            if r in self.excluded:
                raise ValueError("'{}' cannot be required AND excluded endpoint".format(r))
        if not callable(self.valids) and len(self.valids) == 0 and len(self.required) > 0:
            raise ValueError("Property {} is required for {} but has no valids".format(self.name, self.required))
        self.spec_name = spec_name if spec_name is not None else name
        self.res_name = res_name if res_name is not None else name

    def __str__(self):
        return self.name

    def is_required(self, endpoint):
        """Return True if this property is required for the endpoint."""
        return endpoint in self.required

    def is_excluded(self, endpoint):
        """Return True if this property should be excluded for the endpoint."""
        return endpoint in self.excluded

    def _get_values(self, endpoint, values, count):
        """Return a list of vlud for the endpoint.

        Returns an empty list if this property is excluded for
        the endpoint.
        If values is specified as a list, a copy of this list
        is returned (i.e. count is ignored).
        If values is specified as a callable, count values
        are generated and returned in a new list.

        Parameters
        ----------
        endpoint: str
            Key of the endpoint to get values for
        values: list or callable
            Specification of the values
        count: int
            Number of values to generate if values is callable
        """
        if self.is_excluded(endpoint):
            return []
        if callable(values):
            values = [values() for _ in range(count)]
        else:
            values = [v for v in values]
        return values

    def get_valids(self, endpoint, count=1):
        """Return a list of count valid values of this property for the endpoint.

        If valids is specified as a list, a copy of this list
        is returned (i.e. count is ignored).
        If valids is specified as a callable, count values
        are generated and returned in a new list.
        If this property is not required for the endpoint,
        None is added to the list.

        endpoint: str
            Key of the endpoint to get values for
        count: int
            Number of values to generate if valid values are specified as callable
        """
        values = self._get_values(endpoint, self.valids, count)
        if not self.is_required(endpoint):
            values.append(None)
        return values

    def get_invalids(self, endpoint, count=1):
        """Return a list of count invalid values of this property for the endpoint.

        If invalids is specified as a list, a copy of this list
        is returned (i.e. count is ignored).
        If invalids is specified as a callable, count values
        are generated and returned in a new list.
        If this property is required for the endpoint,
        None is added to the list.

        endpoint: str
            Key of the endpoint to get values for
        count: int
            Number of values to generate if valid values are specified as callable
        """
        values = self._get_values(endpoint, self.invalids, count)
        if self.is_required(endpoint):
            values.append(None)
        return values

import pytest
from .util import rand_str, rand_int

def test_constr():
    with pytest.raises(Exception):
        Property()
    with pytest.raises(Exception):
        Property("")
    with pytest.raises(Exception):
        Property("", [])
    with pytest.raises(Exception):
        Property("", [], [], [""])

def test_names():
    name, spec_name, res_name = rand_str(), rand_str(), rand_str()
    prop = Property(name, [], [])
    assert prop.name == name
    assert prop.spec_name == name
    assert prop.res_name == name
    prop = Property(name, [], [], spec_name=spec_name)
    assert prop.name == name
    assert prop.spec_name == spec_name
    assert prop.res_name == name
    prop = Property(name, [], [], res_name=res_name)
    assert prop.name == name
    assert prop.spec_name == name
    assert prop.res_name == res_name
    prop = Property(name, [], [], spec_name=spec_name, res_name=res_name)
    assert prop.name == name
    assert prop.spec_name == spec_name
    assert prop.res_name == res_name

def test_required():
    prop = Property("prop", [1], [], required=["a", "b", "c"])
    assert prop.is_required("b")
    assert not prop.is_required("d")

def test_excluded():
    prop = Property("prop", [], [], excluded=["a", "b", "c"])
    assert prop.is_excluded("b")
    assert not prop.is_excluded("d")

def test_required_and_excluded():
    Property("prop", [], [], required=[], excluded=[])
    Property("prop", [1], [], required=["a", "d"], excluded=["b", "c"])
    with pytest.raises(Exception):
        Property("prop", [], [], required=["a"], excluded=["a"])
    with pytest.raises(Exception):
        Property("prop", [], [], required=["a", "b"], excluded=["c", "d", "b"])

def test_valid():
    valids = [1, 3, 5]
    prop = Property("prop", valids, [], [Endpoints.CREATE])
    assert None not in prop.get_valids(Endpoints.CREATE)
    assert None in prop.get_valids(Endpoints.UPDATE)
    assert set(valids) == set(prop.get_valids(Endpoints.CREATE))

def test_invalid():
    invalids = ["a", "b"]
    prop = Property("prop", [1], invalids, [Endpoints.CREATE])
    assert None in prop.get_invalids(Endpoints.CREATE)
    assert None not in prop.get_invalids(Endpoints.UPDATE)
    assert set(invalids) == set(prop.get_invalids(""))

def test_valid_counts():
    valids = [1, 3, 5]
    prop = Property("prop", valids, [], [Endpoints.CREATE])
    assert len(prop.get_valids(Endpoints.CREATE)) == 3
    assert len(prop.get_valids(Endpoints.CREATE, count=100)) == 3
    assert len(prop.get_valids(Endpoints.UPDATE)) == 4
    assert len(prop.get_valids(Endpoints.UPDATE, count=100)) == 4
    prop = Property("prop", rand_int, [], [Endpoints.CREATE])
    assert len(prop.get_valids(Endpoints.CREATE, count=100)) == 100
    assert len(prop.get_valids(Endpoints.UPDATE, count=100)) == 101

def test_invalid_counts():
    invalids = ["a", "b"]
    prop = Property("prop", [1], invalids, [Endpoints.CREATE])
    assert len(prop.get_invalids(Endpoints.CREATE)) == 3
    assert len(prop.get_invalids(Endpoints.CREATE, count=100)) == 3
    assert len(prop.get_invalids(Endpoints.UPDATE)) == 2
    assert len(prop.get_invalids(Endpoints.UPDATE, count=100)) == 2
    prop = Property("prop", [1], rand_str, [Endpoints.CREATE])
    assert len(prop.get_invalids(Endpoints.CREATE, count=100)) == 101
    assert len(prop.get_invalids(Endpoints.UPDATE, count=100)) == 100
