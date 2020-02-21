import curses
import importlib.util
import os

from pmn.list_process_view import ListProcessView
from pmn.tree_process_view import TreeProcessView


def _load_config(config_path):
    """
    Load configuration file by path
    :param config_path: path of a configuration file
    :return: loaded config
    """
    path = os.path.expanduser(os.path.expandvars(config_path))
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config


# TODO: refactor
def _init_config(config_path):
    import pmn.default_config as default
    if config_path:
        loaded = _load_config(config_path)
        default.colors = getattr(loaded, 'colors', default.colors)
        default.application_keymap = getattr(loaded, 'application_keymap', default.application_keymap)
        default.list_layout = getattr(loaded, 'list_layout', default.list_layout)
        default.list_keymap = getattr(loaded, 'list_keymap', default.list_keymap)
        default.tree_layout = getattr(loaded, 'tree_layout', default.tree_layout)
        default.tree_keymap = getattr(loaded, 'tree_keymap', default.tree_keymap)
    return default


class Application:
    def __init__(self, config=None):
        self.screen = None
        self.views = []
        os.environ.setdefault('ESCDELAY', '25')
        # faking terminal in order to make colors work
        # https://github.com/xoreaxeaxeax/sandsifter/issues/14
        os.environ['TERM'] = 'xterm-256color'
        self.config = _init_config(config)

        curses.wrapper(self._start)

    def _start(self, screen):
        self.screen = screen

        curses.curs_set(0)
        curses.use_default_colors()

        self.screen.refresh()
        self.config.colors()
        self.views = [
            ListProcessView(self.screen, self.config),
            TreeProcessView(self.screen, self.config)
        ]
        self.current_view_index = 0
        self.config.application_keymap(self)
