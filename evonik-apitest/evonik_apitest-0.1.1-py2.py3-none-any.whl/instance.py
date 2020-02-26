import random
from .endpoints import Endpoints

class Instance:
    """Wrapper for the creation and deletion of a component.

    An instance object provides __enter__ and __exit__ methods.
    They use the component's andpoints specification to
    create a resource and delete it.

    During enter, a component is created using the endpoint
    comp.endpoints.create.
    As payload data, it uses a random element from the
    generated list of valids for comp.endpoints.CREATE.

    During exit, the component is deleted using the endpoint
    comp.endpooints.delete.
    As payload data, it uses a random element from the
    generated list of valids for comp.endpoints.DELETE.

    The payload submitted when calling the create entpoint
    is stored in self.spec.
    The result of the create endpoint is stored in
    self.data for accessing it later.

    Parameters
    ----------
    comp: Component object
        Component to create an instance from
    references: dictionary of Instance objects, default None
        Instances of references components (as specified by the component's references)
    **values: arbitrary
        Arbitrary values to overwrite values (from valids) for resource creation

    Examples
    --------
    comp = ...
    with Instance(comp) as instance:
        print(instance.data)
        print(instance.spec)
    """
    def __init__(self, comp, references=None, **values):
        self.comp = comp
        self.references = references if references is not None else {}
        self.values = values

    def __enter__(self):
        self._references = {}
        for k,reference in self.comp.references.items():
            if k not in self.references:
                self._references[k] = Instance(reference)
                self._references[k].__enter__()

        valids = random.choice(self.comp.get_valids(Endpoints.CREATE))
        values = {**valids, **self.values}
        references = {**self.references, **self._references}
        self.data = self.comp.endpoints.create(values, references)
        self.spec = values
        return self

    def __exit__(self, type, value, traceback):
        valids = random.choice(self.comp.get_valids(Endpoints.DELETE))
        self.comp.endpoints.delete(valids, self)
        for reference in self._references.values():
            reference.__exit__(None, None, None)
    
    def get_references(self):
        return {**self.references, **self._references}


import pytest
from .util import rand_int, rand_str, rand_uuid
from .property import Property
from .properties import Properties
from .endpoints import Endpoints
from .component import Component

def test_constr():
    p1 = Property("p1", rand_str, rand_int)
    p2 = Property("p2", rand_int, rand_str)
    def create(values, references):
        return values
    def delete(values, instance):
        return instance.data
    endpoints = Endpoints(create=create, delete=delete)
    comp = Component("c1", Properties(p1, p2), endpoints)
    with Instance(comp) as instance:
        pass
