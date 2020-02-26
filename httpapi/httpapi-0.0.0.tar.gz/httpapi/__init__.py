from functools import partial
from typing import Text, Union, Callable
from urllib import parse as urlparse

from requests import Session

session = Session()


class HttpApi(object):
    """
    Stateful client intended to be instantiated around the base URL of a given
    HTTP API. Implemented as a class so the state can retain TCP connections
    (via requests.Session) but any interaction that changes the URL should
    return a new instance of this class (with the same stateful HTTP session
    retained) rather than mutate the class instance.
    """

    def __init__(self, base_url: Text, requests_client: Session = session):
        """
        Create a new client pointing initially at a given base URL. The intent
        is that subsequent calls via client('foo') or client.foo will then
        build up the URL while retaining the same TCP connection.

        :param base_url:        The URL to fetch initially, but with the idea
                                that you will call or use attributes of this
                                class to build up URLs with longer paths, e.g.
                                base_url http://example.com with a call to
                                httpapi.foo('bar') will then hit
                                http://example.com/foo/bar.
        :param requests_client: Optional argument to pass in any object that
                                behaves like requests or an instance of
                                requests.Session() (i.e. it has a get, post,
                                etc. function). If you omit this, a new
                                requests.Session object will be used.
        """
        self.http = requests_client
        self.base_url = base_url

    def __call__(self, *args: [Text]) -> "HttpApi":
        """
        Allows for e.g. HttpApi('http://example.com/')('foo', 'bar') to fetch
        http://example.com/foo/bar
        :param args: All args e.g. 'a', 'b', 'c' into /a/b/c
        :return: An instance of HttpApi with base URL pointing at the new URL.
        """
        if len(args) == 0:
            return self
        else:
            print(self.base_url)
            new_url = urlparse.urljoin(
                self.base_url + "/", "/".join(str(arg) for arg in args)
            )
            print(new_url)
            return self.__class__(new_url, requests_client=self.http)

    def __getattr__(self, key: Text) -> Union[Callable, "HttpApi"]:
        """
        Allows for e.g. HttpApi('http://example.com/').foo to then fetch
        http://example.com/foo
        Or HttpApi('http://example.com/').get will return a function that does
        requests.get on the given url such that
        HttpApi('http://example.com/').get() will do a simple fetch, but the
        function takes all arguments requests tasks e.g.
        HttpApi('http://example.com/').post(json={}) will do a POST with the
        given JSON/dict sent as the body.
        :param key: The string to append to the current URL or a HTTP request
                    to do on the current URL if key is an HTTP verb e.g. 'get'.
        :return:    A function that will do the given HTTP verb if 'key' an HTTP
                    verb other an HttpApi instance is returned with the current
                    URL having /key appended.
        """
        if key in ["put", "get", "post", "delete"]:
            requests_verb = getattr(self.http, key)
            return partial(requests_verb, self.base_url)
        else:
            new_url = urlparse.urljoin(self.base_url, "/" + str(key))
            print(new_url)
            return self.__class__(new_url, requests_client=self.http)
