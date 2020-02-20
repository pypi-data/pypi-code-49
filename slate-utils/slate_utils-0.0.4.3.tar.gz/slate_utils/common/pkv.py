from lxml import html

def pkvtodict(xml):
    """Parses PKV xml to a dictionary. If there are multiple entries for the
    same key, those values will be returned as a list. Otherwise a single
    string will be returned as a value.

    Parameters
    ----------
    xml : str (xml)
        The xml containing PKV values.
    """
    pkv_dict = {}
    for p in html.fromstring(xml):
        k = p.find('k').text
        v = p.find('v').text
        if k in pkv_dict:
            if isinstance(pkv_dict[k], str):
                pkv_dict[k] = [pkv_dict[k], v]
            else:
                pkv_dict[k].append(v)
        else:
            pkv_dict[k] = v
    return pkv_dict
