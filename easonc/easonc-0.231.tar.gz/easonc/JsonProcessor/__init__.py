try: 
    import simplejson as json
except ModuleNotFoundError:
    print("work better with simplejson\nPlease use pip install simplejson to get better performance.")
    import json

class dict_to_obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [dict_to_obj(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, dict_to_obj(b) if isinstance(b, dict) else b)
    def __str__(self):
        return "dict_to_obj_format"


def obj_to_dict(obj):
    out = vars(obj)
    for key in out.keys():
        if str(out[key]) == "dict_to_obj_format":
            out[key] = obj_to_dict(out[key])
    return out

def obj_to_json(obj):
    return json.dumps(obj_to_dict(obj))

def json_to_obj(jsons):
    return dict_to_obj(json.loads(jsons))

def dict_to_json_file(dicts, filename):
    with open(filename, 'w') as filename:
        json.dump(dicts, filename, sort_keys = True, indent= 4)
        
def obj_to_json_file(obj, filename):
    dict_to_json_file(obj_to_dict(obj), filename)


def json_file_to_dict(filename):
    with open(filename) as json_file:
        return json.load(json_file)

def json_file_to_obj(filename):
    return dict_to_obj(json_file_to_dict(filename))