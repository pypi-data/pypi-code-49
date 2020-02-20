from sneks import snekjson as json

def generate_client_from_file(fname):
    return generate_client(json.loadf(fname))

PRIMITIVES = [
    "string", # String
    "float", # floating-point number
    "int", # int
    "boolean", # true/false
    "bytes" # Binary blob, passed as base64
    "undefined", # type is undefined.  In languages like Java that require types, it'll be whatever the generic type is.
    "list", # List of objects.  Elements has a single entry, "Items", indicating the type of the objects contained in the list.
    "map", # Map of keys to values.  Elements has two entries, "Keys" indicating the key type (usually string) and "Values" indicating the value type.
    "object", # Object with any number of key-value pairs.  Difference between this and map is that this has predefined keys corresponding to values of predefined types.  So, this is like a normal object, whereas map is like a dict or java map.  Elements has any number of entries, with the keys giving the names of the attributes and the values giving the types.
]

def generate_client(model):
    datatypes = model.get("DataTypes",{})
    pass
