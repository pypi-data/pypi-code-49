"""Quick setup for my local/tower develop environemnt
"""
import sys


class DevMode:
    """Control package path in local and tower dev env
    """

    def __init__(self, pkg, pkg_path=None, auto_on=True):
        """Start a DevMode with a project
        Projects:
          - k-seq
          - skin-mb
          - microNet
        """
        from pathlib import Path

        pkgs = {
            'k-seq': ['/home/yuning/research/k-seq/src/',
                      '/Users/yuning/research/k-seq/src'],
            'skin-mb': '/home/yuning/research/skin_microbiome/src/',
            'microNet': ['/Users/yuning/research/microNet/src']
        }

        if pkg in pkgs.keys():
            self.pkg_path = pkgs[pkg]
        elif Path(pkg).is_dir():
            self.pkg_path = pkg
        else:
            raise ValueError(f'Package {pkg_path} is not built-in or valid path')
        if not isinstance(self.pkg_path, (list, tuple)):
            self.pkg_path = [self.pkg_path]
        if auto_on:
            self.on()

    def on(self):
        """Turn on the dev mode"""

        # prioritize the dev package location
        for p in self.pkg_path:
            if p not in sys.path:
                sys.path.insert(0, p)
            elif sys.path.index(p) != 0:
                sys.path.remove(p)
                sys.path.insert(0, p)

        # redirect logging info to standard output
        import logging
        root = logging.getLogger()
        if root.handlers != [] and any(
            [handler.name is not None and 'stdout' in handler.name
             for handler in root.handlers]
        ):
            pass
        else:
            handler = logging.StreamHandler(sys.stdout)
            handler.name = 'stdout'
            root.addHandler(handler)
        root.setLevel(logging.INFO)

    def off(self):
        for p in self.pkg_path:
            if p in sys.path:
                sys.path.remove(p)
