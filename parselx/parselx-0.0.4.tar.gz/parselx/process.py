from .utils import parse_query, enhanced_css
from .x_processors import x


def _parsel_one(sel, query: str, **kwargs):
    """Use parsel to extract original values"""
    if not isinstance(query, str):
        raise TypeError(f"Query should be string: {query}")
    q = parse_query(query)
    lang = q["lang"]

    # extract values
    if lang == "xpath":
        val = getattr(getattr(sel, lang)(q["query"], **kwargs), q["meth"])()
    else:
        query = enhanced_css(q["query"])
        val = getattr(getattr(sel, lang)(query), q["meth"])()

    # apply filters function
    filters = q["filters"]
    for filt in filters:
        func = x.filters[filt["name"]]
        val = func(val, *filt["args"])
    return val


def process(sel, queries, **kwargs):

    if isinstance(queries, list):
        if should_divide(queries):
            scope = queries[0]
            sp_query = parse_query(scope)
            sels = getattr(sel, sp_query["lang"])(sp_query["query"])
            if sp_query["meth"] == "getall":
                return [
                    process(sel, queries[1:])
                    for sel in getattr(sel, sp_query["lang"])(sp_query["query"])
                ]
            return process(sels, queries[1:])

        query = queries[0]
        funcs = queries[1:]
        val = process(sel, query, **kwargs)
        return _process_by_funcs(val, funcs)
    if isinstance(queries, dict):
        return {k: process(sel, v, **kwargs) for k, v in queries.items()}

    if callable(queries):
        return queries()

    return _parsel_one(sel, queries, **kwargs)


def _process_by_funcs(val, funcs=None):
    for func in funcs or []:
        val = func(val)
    return val


def should_divide(queries: list):
    return len(queries) > 1 and not callable(queries[1])
