import os
from addict import Dict


class _Error(Exception):
    pass


class _BadDirectoryName(_Error):
    pass


class _BadDepth(_Error):
    pass


class _BadPath(_Error):
    pass


def _path_recursion(given_path, ignore_hidden=True):

    result = Dict()

    path = [x for x in os.walk(given_path)][0][0]
    dirs = [x for x in os.walk(given_path)][0][1]
    all_files = [x for x in os.walk(given_path)][0][2]

    exceptions = ['files', 'dirs', 'path', 'filepaths']
    for exception in exceptions:
        if exception in dirs:
            raise _BadDirectoryName('\nUse of '
                                    f'"{exception}" '
                                    'as a directory name is ambiguous.')

    if ignore_hidden:
        files = [f for f in all_files if f[0] != '.' and f[0] != '_']
        dirs[:] = [d for d in dirs if d[0] != '.' and d[0] != '_']
    else:
        files = all_files

    filepaths = []
    if len(files):
        for file in files:
            filepaths.append(os.path.join(given_path, file))

    result['files'] = files
    result['path'] = path + '/'
    result['dirs'] = dirs
    result['filepaths'] = filepaths

    for folder in dirs:
        result[folder] = _path_recursion(os.path.join(path, folder),
                                         ignore_hidden)

    return result


class Root(object):

    def __init__(self,
                 file=None,
                 depth=0,
                 ignore_hidden=True,
                 alt_path=False):

        self.file = file
        self.depth = depth + 1
        self.ignore_hidden = ignore_hidden

        if alt_path and not file:
            self.basepath = alt_path
        elif file and not alt_path:
            self._set_basepath()
        else:
            raise _BadPath('Must specify root path or pass in'
                           ' file=__file__')

    def _set_basepath(self):

        self.basepath = os.path.abspath(self.file)

        if self.depth < 0 or type(self.depth) != int:
            raise _BadDepth('Depth must be int >= 0')
        else:
            for _ in range(self.depth):
                self.basepath = os.path.split(self.basepath)[0]

    def paths(self):
        return _path_recursion(self.basepath, self.ignore_hidden)


if __name__ == "__main__":
    root2 = Root(__file__, 2).paths()
    print(root2.path)

    root1 = Root(__file__, 1).paths()
    print(root1.tests.testdir.Jetsons.filepaths)

    root0 = Root(__file__, 0).paths()
    print(root0.path)
