def set_obj_attr(obj, meta):
    for key in meta.keys():
        if type(meta[key]) is dict:
            obj.__setattr__(key, JsJson(meta[key]))
        elif type(meta[key]) is list:
            obj.__setattr__(key, [JsJson(item) for item in meta[key]])
        else:
            obj.__setattr__(key, meta[key])


class JsJson:
    def __init__(self, obj):
        set_obj_attr(self, obj)

    def __new__(cls, obj):
        if type(obj) is dict:
            ret = super(JsJson, cls).__new__(cls)
        elif type(obj) is list:
            ret = [JsJson(item) for item in obj]
        else:
            ret = obj

        return ret

    def as_dict_copy(self):
        out = self.__dict__.copy()
        for key in out.keys():
            if type(out[key]) is JsJson:
                out[key] = out[key].as_dict_copy()
            elif type(out[key]) is list:
                l = []
                for item in out[key]:
                    if type(item) is JsJson:
                        l.append(item.as_dict_copy())
                    else:
                        l.append(item)
                out[key] = l

        return out

    def __str__(self):
        return str(self.as_dict_copy())
