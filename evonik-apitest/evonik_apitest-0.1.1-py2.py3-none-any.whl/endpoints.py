from .util import attr_from_obj, obj_has_attr

class Endpoints:
    """Specification of endpoints of an API.

    The following endpoints with specific meaning can be specified:

    1. create, signature: create(values, references)
    2. update, signature: update(values, instance)
    3. delete, signature: delete(values, instance)
    4. get, signature: get(values, instance)
    5. list, signature: list(values, references, limit, offset)

    These endpoints are identified with the following keys:

    1. create: Endpoints.CREATE
    2. update: Endpoints.UPDATE
    2. delete: Endpoints.DELETE
    2. get: Endpoints.GET
    2. list: Endpoints.LIST

    Other endpoints can be specified with arbitrary names.
    They must have the following signature:

    6. other, signature: other(values)

    Each of these endpoints is identified with its name as key,
    e.g., "other".

    Parameters
    ----------
    create: callable, default None
        Function for creating a new resource
    update: callable, default None
        Function for updating an existing resource
    delete: callable, default None
        Function for deleting an existing resource
    get: callable, default None
        Function for getting an existing resource
    list: callable, default None
        Function to list all existing resources (possibly with paging)
    prop_from_res: callable, default None
        Function to get a property from an API call result
    res_has_prop: callable, default None
        Function to determine if an API call result has a property
    **others: callable
        Other functions

    Examples
    --------
    component_api = Endpoints(
        create=lambda values,references: {**values, "ref1_id": references["ref1"].data.id},
        update=lambda values,instance: {**instance.data, **values},
        delete=lambda values,instance: {**instance.data},
        get=lambda values,instance: {**instance.data},
        list=lambda values: [],
        prop_from_res=value_from_dict,
        res_has_prop=dict_has_value
    )
    compute_api = Endppoints(
        square=lambda values: values["number"]**2
    )
    """

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    GET = "GET"
    LIST = "LIST"

    def __init__(self,
                 create=None,
                 update=None,
                 delete=None,
                 get=None,
                 list=None,
                 prop_from_res=attr_from_obj,
                 res_has_prop=obj_has_attr,
                 **others):
        self.create = create
        self.get = get
        self.update = update
        self.delete = delete
        self.list = list
        self.others = others
        self.prop_from_res = prop_from_res
        self.res_has_prop = res_has_prop


import pytest

def test_constr():
    Endpoints()
    Endpoints(create=lambda values,references: 1)
    Endpoints(update=lambda values,instance: 2, delete=lambda values,instance: 3)
    Endpoints(xyz=lambda values,references: 4)
