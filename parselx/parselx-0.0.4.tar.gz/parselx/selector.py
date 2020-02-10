import sys

import six
from lxml import etree
from parsel import Selector, SelectorList

from .process import process as _process


class SelectorListX(SelectorList):
    def g(self, query, **kwargs):
        """
        Any additional named arguments can be used to pass values for XPath
        variables in the XPath expression
        """
        return _process(self, query, **kwargs)


class SelectorX(Selector):
    """
    :class:`Selector` allows you to select parts of an XML or HTML text using CSS
    or XPath expressions and extract data from it.

    ``type`` defines the selector type, it can be ``"html"``, ``"xml"`` or ``None`` (default).
    If ``type`` is ``None``, the selector defaults to ``"html"``.

    ``vars`` are used to pass values for XPath variables in the XPath expression
    """

    selectorlist_cls = SelectorListX

    def __init__(
        self,
        text=None,
        vars: dict = None,
        type=None,
        namespaces=None,
        root=None,
        base_url=None,
        _expr=None,
    ):
        super().__init__(
            text=text,
            type=type,
            namespaces=namespaces,
            root=root,
            base_url=base_url,
            _expr=_expr,
        )
        self.vars = {}
        if isinstance(vars, dict):
            self.vars = {k: v for k, v in vars.items() if isinstance(v, str)}

    def g(self, query, **kwargs):
        """
        Any additional named arguments can be used to pass values for XPath
        variables in the XPath expression
        """
        return _process(self, query, **kwargs)

    def xpath(self, query, namespaces=None, **kwargs):
        """
        Find nodes matching the xpath ``query`` and return the result as a
        :class:`SelectorList` instance with all elements flattened. List
        elements implement :class:`Selector` interface too.

        ``query`` is a string containing the XPATH query to apply.

        ``namespaces`` is an optional ``prefix: namespace-uri`` mapping (dict)
        for additional prefixes to those registered with ``register_namespace(prefix, uri)``.
        Contrary to ``register_namespace()``, these prefixes are not
        saved for future calls.

        Any additional named arguments can be used to pass values for XPath
        variables in the XPath expression, e.g.::

            selector.xpath('//a[href=$url]', url="http://www.example.com")
        """
        try:
            xpathev = self.root.xpath
        except AttributeError:
            return self.selectorlist_cls([])

        nsp = dict(self.namespaces)
        if namespaces is not None:
            nsp.update(namespaces)
        try:
            result = xpathev(
                query,
                namespaces=nsp,
                smart_strings=self._lxml_smart_strings,
                **self.vars,
                **kwargs
            )
        except etree.XPathError as exc:
            msg = u"XPath error: %s in %s" % (exc, query)
            msg = msg if six.PY3 else msg.encode("unicode_escape")
            six.reraise(ValueError, ValueError(msg), sys.exc_info()[2])

        if type(result) is not list:
            result = [result]

        result = [
            self.__class__(
                vars=self.vars,
                root=x,
                _expr=query,
                namespaces=self.namespaces,
                type=self.type,
            )
            for x in result
        ]
        return self.selectorlist_cls(result)
