from klotan.criteria.core import fn_to_criteria


@fn_to_criteria
def more(x, eq=False):
    return lambda y: (y >= x) if eq else (y > x)


@fn_to_criteria
def less(x, eq=False):
    return lambda y: (y <= x) if eq else (y < x)


@fn_to_criteria
def between(x, y):
    return lambda w: w > x and w < y


@fn_to_criteria
def is_positive(accept_zero=False):
    return lambda y: (y > 0) if not (accept_zero) else (y >= 0)

