from easycli import SubCommand


class Version(SubCommand):
    __command__ = 'version'
    __aliases__ = ['v', 'ver']

    def __call__(self, args):
        from markdownserver import __version__
        print(__version__)
