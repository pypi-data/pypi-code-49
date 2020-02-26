class Component:
    """Specification of a resource managed by an API.

    Parameters
    ----------
    name: str
        Name of the component
    props: Properties object
        Properties of the component
    endpoints: Endpoints object
        Endpoints of this component
    references: dictionary of Component objects, default None
        Referenced components, e.g., parent(s)

    Examples
    --------
    prop1 = Property("prop1", rand_str, rand_int)
    prop2 = Property("prop2", rand_int, rand_str)
    props = Properties(prop1, prop2)
    component_api = Endpoints(
        create=lambda values,references: {**values},
        delete=lambda values,instance: {**instance.data}
    )
    comp = Component("Test", props, component_api)
    """
    def __init__(self, name, props, endpoints, references=None):
        self.name = name
        self.props = props
        self.endpoints = endpoints
        if references is not None and not isinstance(references, dict):
            raise TypeError("references must be of type dict")
        self.references = references if references is not None else {}

    def get_valids(self, endpoint, count=1, max_entries=None, sampling=None, generator=None):
        """Generate and return list of valids from properties for endpoint."""
        return self.props.get_valids(endpoint, count=count,
                                     max_entries=max_entries,
                                     sampling=sampling, generator=generator)

    def get_invalids(self, endpoint, count=1, max_entries=None, sampling=None, generator=None):
        """Generate and return list of invalids from properties for endpoint."""
        return self.props.get_invalids(endpoint, count=count,
                                       max_entries=max_entries,
                                       sampling=sampling, generator=generator)


import pytest
from .util import rand_int, rand_str, rand_uuid
from .property import Property
from .properties import Properties
from .endpoints import Endpoints

def test_constr():
    p1 = Property("p1", rand_str, rand_int)
    p2 = Property("p2", rand_int, rand_str)
    p3 = Property("p3", rand_uuid, rand_str)
    c1 = Component("c1", Properties(p1, p2), Endpoints())
    c2 = Component("c2", Properties(p1), Endpoints(), {"c1": c1})
    c3 = Component("c3", Properties(p2, p1), Endpoints(), {"c1": c1, "c2": c2})
