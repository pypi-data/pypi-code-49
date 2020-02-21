import curses

from pmn.info_format import InfoFormat
from pmn.process_tree import ProcessTree
from pmn.size import Size, Method, Unit, Align


def colors():
    curses.init_pair(1, 0, 231)
    curses.init_pair(2, 231, 0)
    curses.init_pair(3, 2, -1)
    curses.init_pair(4, 2, 0)


def application_keymap(application):
    while True:
        key = application.views[application.current_view_index].loop()

        if key == ord('t'):
            application.current_view_index = (application.current_view_index + 1) % len(application.views)
        if key == ord('q') or key == 27:
            return


def list_layout(process):
    return [
        InfoFormat(str(process.pid), Size(4, Method.FIT, Unit.PX, Align.RIGHT)),
        InfoFormat(' '),
        InfoFormat(process.name(), Size(14, Method.FIT, Unit.PX)),
        InfoFormat(' '),
        InfoFormat(' '.join(process.cmdline()), Size(0, Method.AVAILABLE, Unit.PX, Align.LEFT))
    ]


def list_keymap(list_view):
    while True:
        h, w = list_view.screen.getmaxyx()
        list_view.show()

        key = list_view.screen.getch()

        if key == ord('i') or key == curses.KEY_UP:
            list_view.prev()
        if key == ord('k') or key == curses.KEY_DOWN:
            list_view.next()
        if key == ord('g'):
            list_view.first()
        if key == ord('G'):
            list_view.last()
        if key == ord('c'):
            if list_view.search_string != '':
                list_view.clear_search()
        if key == ord('/'):
            list_view.search_loop()
        if key == curses.KEY_RESIZE:
            list_view.resize(h)
        if key in [ord('q'), 27, ord('t')]:
            return key


def tree_layout(node):
    return [
        InfoFormat(str(node.process.pid), Size(4, Method.FIT, Unit.PX, Align.RIGHT)),
        InfoFormat(' '),
        InfoFormat(node.process.name(), Size(14, Method.FIT, Unit.PX), Align.LEFT),
        InfoFormat(' '),
        InfoFormat(
            ProcessTree.prefix(node)[0][:-1],
            Size.self(),
            3,
            4
        ),
        InfoFormat(
            (('─' if not node.collapsed else '┼') if node.parent else ''),
            Size.self(),
            3,
            4
        ),
        InfoFormat(
            ' '.join(node.process.cmdline()),
            Size(0, Method.AVAILABLE, Unit.PX, Align.LEFT)
        )
    ]


def tree_keymap(tree_view):
    while True:
        h, w = tree_view.screen.getmaxyx()
        tree_view.show()

        key = tree_view.screen.getch()

        if key == ord('i') or key == curses.KEY_UP:
            tree_view.prev()
        if key == ord('k') or key == curses.KEY_DOWN:
            tree_view.next()
        if key == ord('g'):
            tree_view.first()
        if key == ord('G'):
            tree_view.last()
        if key == curses.KEY_RESIZE:
            tree_view.resize(h)
        if key == ord('c'):
            tree_view.trigger_collapse_current()
        if key in [ord('q'), 27, ord('t')]:
            return key
