# ----------------------------------------------------------------------------------------------------------------
# Recursive function that can make a json from complex nested objects
# ----------------------------------------------------------------------------------------------------------------
def rec_to_json(objects):
    # ----------------------------------------------------------------------------------------------------------------
    # Function check if object can be a dict
    # ----------------------------------------------------------------------------------------------------------------
    def contains_dict(object):
        try:
            _ = object.__dict__
            return True
        except:
            return False

    if objects is None:
        return objects

    if contains_dict(objects):
        dic = objects.__dict__
    else:
        dic = objects

    for key, value in dic.items():
        if isinstance(value, list):
            temp = []
            for v in value:
                if isinstance(v, dict) or isinstance(v, list) or contains_dict(v):
                    temp.append(rec_to_json(v))
                else:
                    temp.append(v)
            dic[key] = temp
        elif isinstance(value, dict) or contains_dict(value):
            dic[key] = rec_to_json(value)
    return dic
