import re

class MongoQuery():
    def __init__(self, model_query):
        self.orig_query = model_query

    def build(self):
        query = {}

        if self.orig_query is None:
            return query

        for key, value in self.orig_query.value_equals.items():
            query[key] = value
        
        for key, value in self.orig_query.list_contains.items():
            raise NotImplementedError()

        for key, list_of_values in self.orig_query.value_equals_one_of.items():
            query[key] = q_any_in_list(list_of_values)
        
        return query
    
def q_any_in_list(_list):
    return {'$in': _list}