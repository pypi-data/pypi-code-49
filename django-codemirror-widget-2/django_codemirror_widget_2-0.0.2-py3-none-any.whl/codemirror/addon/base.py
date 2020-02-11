import importlib


class BaseAddon:
    folder = None
    file = None
    css = None
    dependencies = set()
    config = {}

    def __hash__(self):
        return hash(f'{self.folder}/{self.file}')

    def __str__(self):
        return f'Addon<{self.path()}>'

    @classmethod
    def path(cls):
        return f"addon/{cls.folder}/{cls.file}.js"

    @classmethod
    def css_path(cls):
        return f"addon/{cls.folder}/{cls.css}.css"

    @classmethod
    def _dependencies(cls):
        temp = set()
        for depend in cls.dependencies:
            if isinstance(depend, str):
                depend = cls.get(depend)
            temp |= depend.solve()
        return temp

    @classmethod
    def solve(cls):
        return cls._dependencies() | {cls}

    @classmethod
    def get(cls, folder: str, file: str = '') -> 'BaseAddon':
        if '.' in folder:
            folder, file = folder.split('.', 1)
        if '-' in file:
            file = file.title().replace('-', '')
        elif file[0].islower():
            file = file[0].upper() + file[1:]
        if not file.endswith('Addon'):
            file += 'Addon'
        target = importlib.import_module(f'codemirror.addon.{folder}')
        addon = getattr(target, file)
        return addon


class BaseFoldAddon(BaseAddon):
    folder = 'fold'


class BaseEditAddon(BaseAddon):
    folder = 'edit'


class BaseModeAddon(BaseAddon):
    folder = 'mode'


class BaseHintAddon(BaseAddon):
    folder = 'hint'


class BaseCommentAddon(BaseAddon):
    folder = 'comment'
