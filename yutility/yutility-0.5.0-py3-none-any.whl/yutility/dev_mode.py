"""Quick setup for my local/tower develop environemnt
"""
import sys
import json
from pathlib import Path
import logging
import os


class DevMode:
    """Control package path in the development environment. Load info from
        ``~/.yutil.config`` if file exists
    """

    def __repr__(self):

        def proj_formatter(proj):
            return f"{proj}:\n     " + '\n    '.join(self.pkg_path[proj])
        return '\n'.join([proj_formatter(proj) for proj in self.pkg_path.keys()])

    def __init__(self, project=None, auto_on=True):
        """Start a DevMode with a project
        Projects:
          - k-seq
          - skin-mb
          - microNet
       """

        _HOME = os.getenv('HOME', '~')
        if Path(_HOME + '/.yutil.config').exists():
            with open(_HOME + '/.yutil.config', 'r') as handle:
                _config_info = json.load(handle)
        else:
            _config_info = dict(pkg_path=dict())

        self.pkg_path = _config_info['pkg_path']
        self.current_on = None

        if auto_on and project is not None:
            self.on(project)

    def add_project(self, project):
        """Add a project"""
        if project not in self.pkg_path.keys():
            self.pkg_path[project] = []
        else:
            logging.error(f"Project '{project}' exists")
            raise ValueError(f"Project '{project}' exists")

    def add_pkg_path(self, path, project=None):
        """Add pkg path under a project name"""
        if Path(path).exists():
            if project is None:
                if self.pkg_path == {}:
                    logging.error('yutil.config seems empty, indicate the project name')
                    raise ValueError('yutil.config seems empty, indicate the project name')
                else:
                    for pkg_list in self.pkg_path.values():
                        pkg_list.append(path)
            else:
                if project in self.pkg_path.keys():
                    self.pkg_path[project].append(path)
                else:
                    self.pkg_path[project] = [path]
        else:
            logging.error(f'{path} does not seem to be an existing directory')
            raise NotADirectoryError(f'{path} does not seem to be an existing directory')

    def delete_pkg_path(self, path, project=None):
        """Delete path from given project"""
        if project is None:
            for pkg_list in self.pkg_path.values():
                _ = pkg_list.pop(path)
        else:
            if project not in self.pkg_path.keys():
                logging.error(f"'{project}' not found")
                raise ValueError(f"'{project}' not found")
            else:
                self.pkg_path[project].pop(path)

    def on(self, project):
        """Turn on the dev mode by prioritize python PATHs"""

        if project not in self.pkg_path.keys():
            logging.error(f'{project} not found')
            raise ValueError(f'{project} not found')

        # prioritize the dev package location
        for p in self.pkg_path[project][::-1]:
            if p not in sys.path:
                sys.path.insert(0, p)
            elif sys.path.index(p) != 0:
                sys.path.remove(p)
                sys.path.insert(0, p)

        # redirect logging info to standard output
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
        self.current_on = project

    def off(self):
        for p in self.pkg_path:
            if p in sys.path:
                sys.path.remove(p)

    def save(self):
        _HOME = os.getenv('HOME', '~')
        with open(_HOME + '/.yutil.config', 'w') as handle:
            json.dump(obj={'pkg_path': self.pkg_path}, fp=handle)
