import re


def parse_query(query: str):
    """Parse the query to a dictionary"""

    query = query.strip()
    if query.startswith("[") and query.endswith("]"):
        query = query[1:-1].strip()
        meth = "getall"
    else:
        meth = "get"

    lang = "css"
    if query.startswith("_"):
        query = query[1:].strip()
        lang = "xpath"
    filters = re.split(r"\s*\|(?!\=)\s*", query)
    query = filters.pop(0)
    q = {
        "query": query,
        "meth": meth,
        "lang": lang,
        "filters": _parse_filters("|".join(filters)),
    }
    return q


def _parse_args(string):
    args = []
    regex = re.compile(r"\"([^\"]*)\"|'([^']*)'|([^ \t,]+)")
    for match in re.finditer(regex, string):
        args.append(match.group(3) or match.group(2) or match.group(1))
    return args


def _parse_filters(string: str) -> list:
    results = []
    if string:
        for call in re.split(r" *\| *", string):
            parts = call.split(":")
            name = parts.pop(0)
            args = _parse_args(":".join(parts))
            results.append({"name": name, "args": args})
    return results


def enhanced_css(query):
    match = re.search(r"(@[^ ]+)$", query)
    if match:
        attr = match.group(1)[1:]
        query = re.sub(r"(@[^ ]+)$", "", query)
    else:
        attr = "text"
    if attr == "text":
        query += "::text"
    elif attr == "html":
        pass
    else:
        query += f"::attr({attr})"
    return query


def partial(func, *args, new_args_before=False, **keywords):
    def newfunc(*fargs, **fkeywords):
        if new_args_before:
            newkeywords = {**fkeywords, **keywords}
            newargs = [*fargs, *args]
        else:
            newkeywords = {**keywords, **fkeywords}
            newargs = [*args, *fargs]
        return func(*newargs, **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


def args_convert(*args, converter=str, validator=None):
    return [converter(arg) if (validator and validator(arg)) else arg for arg in args]

