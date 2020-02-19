from klotan.criteria.core import fn_to_criteria

@fn_to_criteria
def equals(x):
    return lambda y: x == y


@fn_to_criteria
def is_type(x):
    return lambda y: type(y) == x


@fn_to_criteria
def accept():
    return lambda y: True


@fn_to_criteria
def reject():
    return lambda y: False


@fn_to_criteria
def is_in(*kargs):
    return lambda y: y in kargs


@fn_to_criteria
def empty():
    return lambda y: len(y) == 0


@fn_to_criteria
def contains(st, min=1, max=float("inf")):
    return lambda y: min <= y.count(st) <= max


@fn_to_criteria
def is_size(size):
    return lambda y: len(y) == size
