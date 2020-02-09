from urwid.canvas import CompositeCanvas
from urwid.decoration import AttrMapError

from ..mixin import _mixin
from ..utils import apply_mixin


class attrwrap(_mixin):
    """same as urwid.decorations.AttrWrap but as a mixin."""

    _attr_map = {}
    _focus_map = {}

    def _repr_attrs(self):
        # only include the focus_attr when it takes effect (not None)
        d = dict(super()._repr_attrs(), attr_map=self._attr_map)
        if self._focus_map is not None:
            d['focus_map'] = self._focus_map
        return d

    def get_attr_map(self):
        return dict(self._attr_map)

    def set_attr_map(self, attr_map):
        for from_attr, to_attr in list(attr_map.items()):
            if not from_attr.__hash__ or not to_attr.__hash__:
                raise AttrMapError(
                    "%r:%r attribute mapping is invalid.  "
                    "Attributes must be hashable" % (from_attr, to_attr))
        self._attr_map = attr_map
        self._invalidate()
    attr_map = property(get_attr_map, set_attr_map)

    def get_focus_map(self):
        if self._focus_map:
            return dict(self._focus_map)

    def set_focus_map(self, focus_map):
        if focus_map is not None:
            for from_attr, to_attr in list(focus_map.items()):
                if not from_attr.__hash__ or not to_attr.__hash__:
                    raise AttrMapError(
                        "%r:%r attribute mapping is invalid.  "
                        "Attributes must be hashable" % (from_attr, to_attr))
        self._focus_map = focus_map
        self._invalidate()
    focus_map = property(get_focus_map, set_focus_map)

    def get_focus_attr(self):
        focus_map = self.focus_map
        if focus_map:
            return focus_map[None]

    def set_focus_attr(self, focus_attr):
        self.set_focus_map({None: focus_attr})
    focus_attr = property(get_focus_attr, set_focus_attr)

    def _render(self, size, focus=False):
        return super().render(size, focus)

    def render(self, size, focus=False):
        attr_map = self._attr_map
        if focus and self._focus_map is not None:
            attr_map = self._focus_map
        canv = self._render(size, focus=focus)
        canv = CompositeCanvas(canv)
        canv.fill_attr_apply(attr_map)
        return canv


def apply_attrwrap(widget, attr=None, focus_attr=None):
    """Same as AttrMap but modifies the widget istself.

    apply_attrwrap(MyWidget(), 'style', 'style.focus') ~ AttrWrap(MyWidget(), 'style', 'style.focus')

    The main advantage over AttrWrap is that it does not create a
    container widget. So, there is no surprise when using
    `_invalidate`.
    """
    apply_mixin(widget, attrwrap)
    widget._attr_map = {None: attr}
    widget._focus_map = {None, focus_attr}
    return widget


def get_original_widget(widget):
    """Return inner widget that is not a decoration."""
    inner = getattr(widget, 'original_widget', None)
    while inner:
        widget = inner
        inner = getattr(widget, 'original_widget', None)
    return widget
