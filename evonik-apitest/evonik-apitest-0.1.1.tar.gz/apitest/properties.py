import json
import random

def expand_dicts(dicts, key, values):
    """Expand and return the dicts with all values for the key.

    For each dict in dicts and each value in values, a new dict is generated.
    This new dict contains all entries from the original one as well
    as a mapping from key to value.
    If a value is None, a copy of the original dict is added.
    Overall, len(dicts)*len(values) dicts are generated and returned.

    Parameters
    ----------
    dicts: list
        List of dictionaries to expand
    key: str
        Key of the entry to be added to each dict
    values: list
        List of values to be added to each dict
    """
    expanded = []
    for old in dicts:
        for value in values:
            if value is not None:
                expanded.append({**old, key:value})
            else:
                expanded.append({**old})
    return expanded

def update_dicts(dicts, key, values):
    """Update and return the dicts with all values for the key.

    For each dict in dicts and each value in values, a new dict is generated.
    It contains all entries from the original one except for key.
    If a value is not None, key is mapped to value.
    Otherwise, key is not added to the dict as key.
    Overall, len(dicts)*len(values) dicts are generated and returned.

    Parameters
    ----------
    dicts: list
        List of dictionaries to update
    key: str
        Key of the entry to be updated in each dict
    values: list
        List of values to be added to each dict
    """
    updated = []
    for old in dicts:
        for value in values:
            old_ = {k:v for k,v in old.items() if k != key}
            if value is not None:
                old_.update({key: value})
            updated.append(old_)
    return updated

def dicts_without_key(dicts, key):
    """Return a list of new dicts without the key."""
    updated = []
    for old in dicts:
        updated.append({k:v for k,v in old.items() if k != key})
    return updated

def _dict_as_str(dict_):
    """Return as string representation of the dict."""
    return json.dumps(dict_, sort_keys=True)

def unique_dicts(dicts):
    """Return a list of all unique dicts."""
    return list({
        _dict_as_str(d):d
        for d in dicts
    }.values())

def exclude_dicts(dicts, exclude):
    """Return a list of all dicts that are not in exclude."""
    buts = [_dict_as_str(d) for d in exclude]
    return [
        d for d in dicts
        if _dict_as_str(d) not in buts
    ]

def non_empty_dicts(dicts):
    """Return a list all dicts with at least one entry."""
    return [x for x in dicts if len(x) > 0]

class Properties:
    """Wrapper for generating valid / invalid combinations of properties.

    Parameters
    ----------
    *props: list of Property
        List of the properties to wrap

    Examples
    --------
    prop1 = Property("prop1", rand_str, rand_int)
    prop2 = Property("prop2", rand_int, rand_str)
    props = Properties(prop1, prop2)
    """

    RANDOM_SAMPLING = "RANDOM_SAMPLING"
    SIZE_DESC_SAMPLING = "SIZE_DESC"
    SIZE_ASC_SAMPLING = "SIZE_ASC"

    ALL_VALIDS = "ALL_VALIDS"
    BASIC_VALIDS = "BASIC_VALIDS"


    ALL_INVALIDS = "ALL_INVALIDS"
    REQUIRED_INVALIDS = "REQUIRED_INVALIDS"
    INVALID_INVALIDS = "INVALID_INVALIDS"

    def __init__(self, *props):
        names = []
        spec_names = []
        res_names = []
        for prop in props:
            if prop.name in names:
                raise ValueError("Two properties with name '{}' specified.".format(prop.name))
            if prop.spec_name in spec_names:
                raise ValueError("Two properties with spec_name '{}' specified.".format(prop.spec_name))
            if prop.res_name in res_names:
                raise ValueError("Two properties with res_name '{}' specified.".format(prop.res_name))
            names.append(prop.name)
            spec_names.append(prop.spec_name)
            res_names.append(prop.res_name)
        self.props = props

    def get_prop(self, name=None, spec_name=None, res_name=None):
        if name is None and spec_name is None and res_name is None:
            raise ValueError("Must specify a name to get prop for.")
        print(name, spec_name, res_name)
        for prop in self.props:
            print(prop.name, prop.spec_name, prop.res_name)
            if name is not None and prop.name == name:
                return prop
            elif spec_name is not None and prop.spec_name == spec_name:
                return prop
            elif res_name is not None and prop.res_name == res_name:
                return prop
        if name is not None:
            raise KeyError("No prop exists with name {}.".format(name))
        if spec_name is not None:
            raise KeyError("No prop exists with spec_name {}.".format(spec_name))
        if res_name is not None:
            raise KeyError("No prop exists with res_name {}.".format(res_name))

    def _select_entries(entries, max_entries, sampling):
        if max_entries is None or max_entries >= len(entries):
            return entries
        if sampling == Properties.RANDOM_SAMPLING:
            return random.sample(entries, k=max_entries)
        elif sampling == Properties.SIZE_DESC_SAMPLING:
            return sorted(entries, key=lambda x: -len(x))[:max_entries]
        elif sampling == Properties.SIZE_ASC_SAMPLING:
            return sorted(entries, key=lambda x: len(x))[:max_entries]
        else:
            raise ValueError("Invalid sampling type: {}".format(sampling))

    def get_valids(self, endpoint, count=1, max_entries=None,
                   sampling=None,
                   generator=None):
        """Return a list of valid value dicts from all properties.

        For each property, a list of valid values is generated.
        Then, all valid combinations of these values are generated
        and stored in dicts.
        As a key, the name of a property is used.

        Valid values for generator are:
            - Properties.ALL_VALIDS (many combinations, can become large!)
            - Properties.REQUIRED_INVALIDS (one entry per required prop, all other required props valid)
            - Properties.INVALID_INVALIDS (count entries per property with invalid, all others valid)

        Parameters
        ----------
        endpoint: str
            Key of the endpoint to get values for
        count: int
            Number of values to generate per property
        max_entries: int, default None
            Maximum number of generated valids to return
        sampling: str, default Properties.RANDOM_SAMPLING
            Sampling method to apply if max_entries is set
        generator: str, default Properties.ALL_VALIDS
            How to generate valids
        """
        if sampling is None:
            sampling = Properties.RANDOM_SAMPLING
        if generator is None:
            generator = Properties.ALL_VALIDS

        if generator == Properties.ALL_VALIDS:
            all_valids = [{}]
            for prop in self.props:
                valids = prop.get_valids(endpoint, count)
                if len(valids) > 0:
                    all_valids = expand_dicts(all_valids, prop.spec_name, valids)
        elif generator == Properties.BASIC_VALIDS:
            valids1 = {}
            for prop in self.props:
                if prop.is_required(endpoint):
                    valids1[prop.spec_name] = prop.get_valids(endpoint, count=1)[0]
            valids2 = {}
            for prop in self.props:
                if not prop.is_excluded(endpoint):
                    prop_valids = prop.get_valids(endpoint, count=1)
                    if len(prop_valids) > 0:
                        valids2[prop.spec_name] = prop_valids[0]
            all_valids = [valids1, valids2]
        else:
            raise ValueError("Invalid generator for valids: {}".format(generator))

        return Properties._select_entries(all_valids, max_entries, sampling)

    def get_invalids(self, endpoint, count=1, max_entries=None,
                     sampling=None,
                     generator=None):
        """Return a list of invalid value dicts from all properties.

        Valid values for generator are:
            - Properties.ALL_INVALIDS (many combinations, can become large!)
            - Properties.BASIC_VALIDS (two entries: valid for only required or all props)

        Parameters
        ----------
        endpoint: str
            Key of the endpoint to get values for
        count: int
            Number of values to generate per property
        max_entries: int, default None
            Maximum number of generated invalids to return
        sampling: str, default Properties.RANDOM_SAMPLING
            Sampling method to apply if max_entries is set
        generator: str, default Properties.ALL_INVALIDS
            How to generate invalids
        """
        if sampling is None:
            sampling = Properties.RANDOM_SAMPLING
        if generator is None:
            generator = Properties.ALL_INVALIDS

        all_invalids = []

        if generator == Properties.ALL_INVALIDS:
            all_valids = self.get_valids(endpoint, count)
            # create invalids from valids
            for prop in self.props:
                invalids = prop.get_invalids(endpoint, count)
                if len(invalids) > 0:
                    updated = [{k:v for k,v in x.items()} for x in all_valids]
                    updated = update_dicts(updated, prop.spec_name, invalids)
                    all_invalids += updated
            # remove duplicated
            all_invalids = unique_dicts(all_invalids)
            # remove empty dict
            all_invalids = non_empty_dicts(all_invalids)
            # add empty dict if this would be invalid
            for prop in self.props:
                if prop.is_required(endpoint):
                    all_invalids.append({})
                    break
            # remove still valid dicts
            all_invalids = exclude_dicts(all_invalids, all_valids)
        elif generator == Properties.REQUIRED_INVALIDS:
            requirements = {}
            for prop in self.props:
                if prop.is_required(endpoint) and not prop.is_excluded(endpoint):
                    valid = prop.get_valids(endpoint, count=1)[0]
                    requirements[prop.spec_name] = valid
            for spec_name in requirements:
                all_invalids.append({k:v for k,v in requirements.items() if k != spec_name})
        elif generator == Properties.INVALID_INVALIDS:
            valids = {}
            invalids = {}
            for prop in self.props:
                if not prop.is_excluded(endpoint):
                    prop_valids = [x for x in prop.get_valids(endpoint, 1) if x is not None]
                    if len(prop_valids) > 0:
                        valids[prop.spec_name] = prop_valids[0]
                    prop_invalids = [x for x in prop.get_invalids(endpoint, count) if x is not None]
                    if len(prop_invalids) > 0:
                        invalids[prop.spec_name] = prop_invalids
            for spec_name in valids:
                if spec_name in invalids:
                    for invalid_value in invalids[spec_name]:
                        all_invalids.append({k:v for k,v in valids.items() if k != spec_name})
                        all_invalids[-1][spec_name] = invalid_value
        else:
            raise ValueError("Invalid generator for invalids: {}".format(generator))

        return Properties._select_entries(all_invalids, max_entries, sampling)


import pytest
from .property import Property
from .endpoints import Endpoints
from .util import rand_str, rand_int

def test_names():
    p1 = Property(rand_str(), [], [], spec_name=rand_str(), res_name=rand_str())
    p2 = Property(rand_str(), [], [], spec_name=rand_str(), res_name=rand_str())
    p1_1 = Property(p1.name, [], [], spec_name=rand_str(), res_name=rand_str())
    p1_2 = Property(rand_str(), [], [], spec_name=p1.spec_name, res_name=rand_str())
    p1_3 = Property(rand_str(), [], [], spec_name=rand_str(), res_name=p1.res_name)
    Properties(p1, p2)
    Properties(p2, p1_1)
    Properties(p2, p1_2)
    Properties(p2, p1_3)
    with pytest.raises(Exception):
        Properties(p1, p1_1)
    with pytest.raises(Exception):
        Properties(p1, p1_2)
    with pytest.raises(Exception):
        Properties(p1, p1_3)

def test_prop_by_name():
    p1 = Property(rand_str(), [], [], spec_name=rand_str(), res_name=rand_str())
    p2 = Property(rand_str(), [], [], spec_name=rand_str(), res_name=rand_str())
    props = Properties(p1, p2)
    assert props.get_prop(p1.name).name == p1.name
    assert props.get_prop(name=p1.name).name == p1.name
    assert props.get_prop(spec_name=p1.spec_name).name == p1.name
    assert props.get_prop(res_name=p1.res_name).name == p1.name
    with pytest.raises(Exception):
        props.get_prop(rand_str())
    with pytest.raises(Exception):
        props.get_prop(name=rand_str())
    with pytest.raises(Exception):
        props.get_prop(spec_name=rand_str())
    with pytest.raises(Exception):
        props.get_prop(res_name=rand_str())

def test_valids():
    c, u = Endpoints.CREATE, Endpoints.UPDATE
    p1 = Property("p1", [1, 2, 3, 4, 5], [], [c])
    p2 = Property("p2", [11, 12, 13], [])
    props = Properties(p1, p2)
    assert len(props.get_valids(c, count=1)) == len(p1.get_valids(c)) * len(p2.get_valids(c))
    assert len(props.get_valids(u, count=1)) == len(p1.get_valids(u)) * len(p2.get_valids(u))

def test_generators_valid():
    c, u = Endpoints.CREATE, Endpoints.UPDATE
    p1 = Property("p1", [1, 2, 3, 4, 5], rand_str, [c])
    p2 = Property("p2", [11, 12, 13], rand_str)
    props = Properties(p1, p2)
    for e in [c, u]:
        print(e)
        props.get_valids(e, generator=Properties.ALL_VALIDS)
        props.get_valids(e, generator=Properties.BASIC_VALIDS)
        for g in [rand_str(), Properties.ALL_INVALIDS, Properties.REQUIRED_INVALIDS, Properties.INVALID_INVALIDS]:
            with pytest.raises(Exception):
                print("   ", g)
                props.get_valids(e, generator=g)

def test_generators_invalid():
    c, u = Endpoints.CREATE, Endpoints.UPDATE
    p1 = Property("p1", [1, 2, 3, 4, 5], rand_str, [c])
    p2 = Property("p2", [11, 12, 13], rand_str)
    props = Properties(p1, p2)
    for e in [c, u]:
        print(e)
        props.get_invalids(e, generator=Properties.ALL_INVALIDS)
        props.get_invalids(e, generator=Properties.REQUIRED_INVALIDS)
        props.get_invalids(e, generator=Properties.INVALID_INVALIDS)
        for g in [rand_str(), Properties.ALL_VALIDS, Properties.BASIC_VALIDS]:
            with pytest.raises(Exception):
                print("   ", g)
                props.get_invalids(e, generator=g)

def test_sampling():
    props = [Property(str(i), rand_str, rand_int) for i in range(5)]
    props = Properties(*props)
    assert len(props.get_valids("", count=2)) > 10
    assert len(props.get_valids("", count=2, max_entries=5)) == 5
