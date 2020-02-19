from klotan.criteria import args_to_string, expected, is_type, equals
from klotan.exceptions import ValidationError

# TODO: Handle criteria exception
class CriteriaResult:
    def __init__(self, criteria, *kargs, **kwargs):
        self.criteria = criteria
        self.kargs = kargs
        self.kwargs = kwargs

    def __bool__(self):
        return self.is_valid()

    def is_valid(self):
        return self.criteria(*self.kargs, **self.kwargs)

    def to_string(self, tab: int = 0, tab_size: int = 4):
        return str(self)

    def __repr__(self):
        return (
            f"{self.criteria} << {args_to_string(*self.kargs, **self.kwargs)}"
            f" => {self.criteria(*self.kargs, **self.kwargs)}"
        )


class MatchObjectList:
    def __init__(self):
        self.tree = []

    def add_criteria(self, criteria, *kargs, **kwargs):
        self.tree.append(CriteriaResult(criteria, *kargs, **kwargs))

    def add_dict(self):
        self.tree.append(MatchObjectDict())
        return self.tree[-1]

    def add_list(self):
        self.tree.append(MatchObjectList())
        return self.tree[-1]

    def is_valid(self):
        for value in self.tree:
            if type(value) in [MatchObjectDict, MatchObjectList, CriteriaResult]:
                if not value.is_valid():
                    return False
        return True

    def to_string(self, tab: int = 0, tab_size: int = 4):
        i = 0
        s = []
        for v in self.tree:
            v = v.to_string(tab + 1, tab_size)
            s.append(f'{" " * (tab + 1) * tab_size}{v}')
            i += 1
        e = "[\n"
        e += ",\n".join(s)
        e += "\n" + " " * tab * tab_size + "]"
        return e

    def __repr__(self):
        return self.to_string(self.tree, 0)


class MatchObjectDict:
    def __init__(self):
        self.tree = {}

    def add_criteria(self, key, criteria, *kargs, **kwargs):
        self.tree[key] = CriteriaResult(criteria, *kargs, **kwargs)

    def add_dict(self, key):
        self.tree[key] = MatchObjectDict()
        return self.tree[key]

    def add_list(self, key):
        self.tree[key] = MatchObjectList()
        return self.tree[key]

    def is_valid(self):
        for _, value in self.tree.items():
            if type(value) in [MatchObjectDict, MatchObjectList, CriteriaResult]:
                if not value.is_valid():
                    return False
        return True

    def to_string(self, tab: int = 0, tab_size: int = 4):
        i = 0
        s = []
        for k, v in self.tree.items():
            v = v.to_string(tab + 1, tab_size)
            maybe_quote = '"' if isinstance(k, str) else ""
            key = f"{maybe_quote}{k}{maybe_quote}: " if k is not None else ""
            s.append(f'{" " * (tab + 1) * tab_size}{key}{v}')
            i += 1
        e = "{\n"
        e += ",\n".join(s)
        e += "\n" + " " * tab * tab_size + "}"
        return e

    def raise_on_invalid_data(self):
        if not self.is_valid():
            raise ValidationError(self.to_string())


class OptionalKey:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return f"Optional[{self.key}]"

    def __eq__(self, a):
        return a.__hash__() == self.key.__hash__()

    def __hash__(self):
        return self.key.__hash__()


def optional(key):
    return OptionalKey(key)


def _select_match(key, template, value, match_object):
    if key is not None:
        add_dict = lambda: match_object.add_dict(key)
        add_list = lambda: match_object.add_list(key)
        get_template = lambda: template[key]
    elif isinstance(match_object, MatchObjectDict):
        add_dict = lambda: match_object
        add_list = lambda: match_object
    else:
        add_dict = lambda: match_object.add_dict()
        add_list = lambda: match_object.add_list()

    if isinstance(template, dict):
        match_dict(template, value, add_dict())
    elif isinstance(template, (list, tuple)):
        match_list(template, value, add_list())
    elif isinstance(template, type):
        match_object.add_criteria(key, is_type(template), value)
    elif callable(template):
        match_object.add_criteria(key, template, value)
    else:
        match_object.add_criteria(key, equals(template), value)


def match(template, value):
    match_object = MatchObjectDict()
    _select_match(None, template, value, match_object)
    return match_object


def match_dict(template: dict, tree: dict, match_object: MatchObjectDict):
    for key, value in template.items():
        optional = False
        if isinstance(key, OptionalKey):
            key = key.key
            optional = True
        if key in tree:
            _select_match(key, value, tree[key], match_object)
        else:
            match_object.add_criteria(key, expected(value, optional), None)


def match_list(template: list, array: list, match_object: MatchObjectList):
    for value_array in array:
        for i, template_value in enumerate(template):
            if callable(template_value):
                match_object.add_criteria(template_value, value_array)
                if template_value(value_array):
                    break
            elif isinstance(template_value, dict) and isinstance(value_array, dict):
                if match_dict(template_value, value_array, match_object.add_dict()):
                    break
            elif isinstance(template_value, (list, tuple)) and isinstance(
                value_array, (list, tuple)
            ):
                if match_list(template_value, value_array, match_object.add_list()):
                    break
