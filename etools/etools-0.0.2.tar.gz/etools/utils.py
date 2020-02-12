def clear_none_in_dict(d, recursive=True):
    clear_keys = []
    for k, v in d.items():
        if v is None:
            clear_keys.append(k)
        if isinstance(v, dict) and recursive:
            clear_none_in_dict(v, True)
    for k in clear_keys:
        del d[k]
    return d
