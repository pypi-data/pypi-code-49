def to_kwarg(key: str, value, prepend: str = "", append: str = "") -> dict:
    return {"{}{}{}".format(prepend, key, append): value}