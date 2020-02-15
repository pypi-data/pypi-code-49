import urllib.parse as parse


def get_url_param_dict(url):
    """
    获取url上的参数，保存到dict中
    :example
        get_url_param_dict("http://p.com/query?a=1&b=2")["a"] == "1"
    :param url:
    :return:
    """
    p = parse.urlsplit(url)
    params = parse.parse_qsl(p.query, 1)
    params_dict = dict(params)
    return params_dict


