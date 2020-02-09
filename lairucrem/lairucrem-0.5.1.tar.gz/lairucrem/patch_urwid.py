"""fix urwid bug."""
import sys

from urwid import ExitMainLoop
from urwid.canvas import (
    LayoutSegment, TextCanvas, apply_target_encoding, rle_append_modify,
    rle_join_modify, rle_len, trim_line)
from urwid.main_loop import AsyncioEventLoop
from urwid.raw_display import Screen

from .utils import monkeypatch


# https://github.com/urwid/urwid/issues/221
@monkeypatch(Screen, 'hook_event_loop')
def fix_issue_221(self, event_loop, callback):
    """
    Register the given callback with the event loop, to be called with new
    input whenever it's available.  The callback should be passed a list of
    processed keys and a list of unprocessed keycodes.

    Subclasses may wish to use parse_input to wrap the callback.
    """
    if hasattr(self, 'get_input_nonblocking'):
        wrapper = self._make_legacy_input_wrapper(event_loop, callback)
    else:
        wrapper = lambda: self.parse_input(
            event_loop, callback, self.get_available_raw_input())
    fds = self.get_input_descriptors()
    handles = [
        event_loop.watch_file(fd, wrapper)
        for fd in fds]
    self._current_event_loop_handles = handles

# Fix exception handling
# https://github.com/urwid/urwid/pull/92 exists but not merged


@monkeypatch(AsyncioEventLoop)
def _exception_handler(self, loop, context):
    exc = context.get('exception')
    if exc:
        if not isinstance(exc, ExitMainLoop):
            self._exc = exc
        else:
            loop.default_exception_handler(context)
        loop.stop()


@monkeypatch(AsyncioEventLoop)
def run(self):
    """
    Start the event loop.  Exit the loop when any callback raises
    an exception.  If ExitMainLoop is raised, exit cleanly.
    """
    self._loop.set_exception_handler(self._exception_handler)
    self._loop.run_forever()
    if getattr(self, '_exc', None):
        raise self._exc


def apply_text_layout(text, attr, ls, maxcol):
    t = []
    a = []
    c = []

    class AttrWalk:
        pass
    aw = AttrWalk
    aw.k = 0 # counter for moving through elements of a
    aw.off = 0 # current offset into text of attr[ak]

    def arange( start_offs, end_offs ):
        """Return an attribute list for the range of text specified."""
        if start_offs < aw.off:
            aw.k = 0
            aw.off = 0
        o = []
        while aw.off < end_offs:
            if len(attr)<=aw.k:
                # run out of attributes
                o.append((None,end_offs-max(start_offs,aw.off)))
                break
            at,run = attr[aw.k]
            if aw.off+run <= start_offs:
                # move forward through attr to find start_offs
                aw.k += 1
                aw.off += run
                continue
            if end_offs <= aw.off+run:
                o.append((at, end_offs-max(start_offs,aw.off)))
                break
            o.append((at, aw.off+run-max(start_offs, aw.off)))
            aw.k += 1
            aw.off += run
        return o


    for line_layout in ls:
        # trim the line to fit within maxcol
        line_layout = trim_line( line_layout, text, 0, maxcol )

        line = []
        linea = []
        linec = []

        def attrrange( start_offs, end_offs, destw ):
            """
            Add attributes based on attributes between
            start_offs and end_offs.
            """
            if destw == end_offs-start_offs:
                for at, run in arange(start_offs,end_offs):
                    rle_append_modify( linea, ( at, run ))
                return
            # encoded version has different width
            o = start_offs
            for at, run in arange(start_offs, end_offs):
                if o+run == end_offs:
                    rle_append_modify( linea, ( at, destw ))
                    return
                tseg = text[o:o+run]
                tseg, cs = apply_target_encoding( tseg )
                segw = rle_len(cs)

                rle_append_modify( linea, ( at, segw ))
                o += run
                destw -= segw


        for seg in line_layout:
            #if seg is None: assert 0, ls
            s = LayoutSegment(seg)
            if s.end:
                tseg, cs = apply_target_encoding(
                    text[s.offs:s.end])
                line.append(tseg)
                attrrange(s.offs, s.end, rle_len(cs))
                rle_join_modify( linec, cs )
            elif s.text:
                tseg, cs = apply_target_encoding( s.text )
                line.append(tseg)
                attrrange( s.offs, s.offs, len(tseg) )
                rle_join_modify( linec, cs )
            elif s.offs:
                if s.sc:
                    line.append(bytes().rjust(s.sc))
                    attrrange( s.offs, s.offs, s.sc )
            else:
                line.append(bytes().rjust(s.sc))
                linea.append((None, s.sc))
                linec.append((None, s.sc))

        t.append(bytes().join(line))
        a.append(linea)
        c.append(linec)

    return TextCanvas(t, a, c, maxcol=maxcol)
