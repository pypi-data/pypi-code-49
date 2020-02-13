# create one query for parse_filters
def create_filter_query(f: str):
    """
    :param f: string
    :return: dict
    """
    operators = {
        "=@": "in",
        "!@": "not_in",
        "=$": "end",
        "=^": "start",
        "==": "eq",
        "!=": "not_eq"
    }
    for operator in operators:
        if operator in f:
            set = operators[operator]
            field, value = f.split(operator)
            return {"field": field, "value": value, "set": set}
    else:
        raise ValueError("invalid operator")


def parse_filters(filter_: str):
    """
    :param filter_:
    :return: list of dicts/lists
    """
    parsed_filters = []
    if filter_:
        filter_values = filter_.split(",")
        for filters in filter_values:
            if filters:
                if ";" in filters:  # check 'AND' statement
                    and_filters = []
                    for f in filters.split(";"):
                        and_filters.append(create_filter_query(f.strip()))  # strip string for del spaces
                    parsed_filters.append(and_filters)  # return list of AND filters
                    continue
                parsed_filters.append(create_filter_query(filters.strip()))  # strip string for del spaces
    return parsed_filters


def create_filter_result(exist: bool, exclude: bool):
    """
    :param exist: bool
    :param exclude: bool
    :return: bool
    """
    if exist and exclude:  # field exist but need exclude value
        return False
    elif not exist and exclude:  # field not exist and need exclude value
        return True
    elif exist and not exclude:  # field exist and not need exclude value
        return True
    elif not exist:  # field does not exist
        return False
