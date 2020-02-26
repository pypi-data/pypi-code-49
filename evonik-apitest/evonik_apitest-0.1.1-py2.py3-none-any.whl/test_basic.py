import random

from apitest import Property, Properties, Endpoints, Component, Instance, ComponentTest
from apitest.util import rand_str, rand_int, value_from_dict, dict_has_value


class MyApi:
    def __init__(self):
        self.categories = {}
        self.entries = {}

    def create_cat(self, values, references):
        if "name" not in values:
            raise ValueError("must specify name")
        if values["name"] in [None, ""]:
            raise ValueError("name cannot be empty")
        id = random.randint(0, 1000)
        data = {**values, "id": id}
        self.categories[id] = data
        return data

    def update_cat(self, values, instance):
        id = instance.data["id"]
        data = {**self.categories[id], **values}
        self.categories[instance.data["id"]] = data
        return data

    def delete_cat(self, values, instance):
        id = instance.data["id"]
        children = [e for e in self.entries.values() if e["category_id"] == id]
        if len(children) > 0:
            raise ValueError("Cannot delete category, {} entries reference it".format(len(children)))
        data = self.categories[id]
        del self.categories[id]
        return data

    def list_cat(self, values, references, limit, offset):
        limit = limit if limit is not None else 3
        offset = offset if offset is not None else 0
        data = [v for v in self.categories.values()]
        data = data[offset:offset+limit]
        pagination = {
            "total": len(self.categories),
            "limit": limit,
            "offset": offset
        }
        return {
            "pagination": pagination,
            "data": data
        }

    def create_ent(self, values, references):
        if "name" not in values:
            raise ValueError("must specify name")
        if values["name"] in [None, ""]:
            raise ValueError("name cannot be empty")
        if "color" not in values:
            raise ValueError("must specify color")
        if values["color"] not in ["red", "green", "blue"]:
            raise ValueError("color is invalid: {}".format(values["color"]))
        id = random.randint(1, 1000)
        data = {**values, "category_id": references["cat"].data["id"], "id": id}
        self.entries[id] = data
        return data

    def update_ent(self, values, instance):
        id = instance.data["id"]
        data = {**self.entries[id], **values}
        self.entries[instance.data["id"]] = data
        return data

    def delete_ent(self, values, instance):
        id = instance.data["id"]
        data = self.entries[id]
        del self.entries[id]
        return data

    def list_ent(self, values, references, limit, offset):
        if references is not None:
            return [v for v in self.entries.values() if v["category_id"] == references["cat"].data["id"]]
        else:
            return [v for v in self.entries.values()]

    def compute(self, data):
        return data["counter"] + 1

api = MyApi()

category_api = Endpoints(
    create=api.create_cat,
    update=api.update_cat,
    delete=api.delete_cat,
    list=api.list_cat,
    prop_from_res=value_from_dict,
    res_has_prop=dict_has_value
)
entry_api = Endpoints(
    create=api.create_ent,
    update=api.update_ent,
    delete=api.delete_ent,
    list=api.list_ent,
    prop_from_res=value_from_dict,
    res_has_prop=dict_has_value
)
compute_api = Endpoints(
    compute=api.compute
)

name = Property("name", rand_str, [""], [Endpoints.CREATE])
description = Property("description", rand_str, [])
color = Property("color", ["red", "green", "blue"], rand_str, [Endpoints.CREATE])
counter = Property("counter", rand_int, rand_str, ["compute"])

category = Component("Category", Properties(name, description), category_api)
entry = Component("Entry", Properties(name, description, color), entry_api, {"cat": category})
computation = Component("Computation", Properties(counter), compute_api)

def test_create_category():
    ComponentTest(category).test_create()
def test_update_category():
    ComponentTest(category).test_update()
def test_list_category():
    ComponentTest(category).test_list(
        entries=5,
        total_from_res=lambda res: res["pagination"]["total"]
    )
def test_pagination_category():
    ComponentTest(category).test_pagination(
        total_from_res=lambda res: res["pagination"]["total"],
        size_from_res=lambda res: len(res["data"])
    )

def test_create_entry():
    ComponentTest(entry).test_create()
def test_update_entry():
    ComponentTest(entry).test_update()
def test_list_entry():
    ComponentTest(entry).test_list(entries=5)
    ComponentTest(entry).test_list(entries=5, same_references=True)
def test_child_delete():
    ComponentTest(entry).test_child_delete()

def test_compute():
    ComponentTest(computation).test("compute", 2, val_res=lambda values,x: type(x) == int)
