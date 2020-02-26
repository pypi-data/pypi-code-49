from __future__ import annotations

import cmake  # type: ignore
import json
import logging
import os
import re
import shutil
import subprocess as sp
import sys
import yaml

from dataclasses import dataclass, field
from typing import *

# TODO: support file and streams in from_yaml and from_json

_default_build_dir = '_build'
_source_ext_header = ('.h', '.hpp')
_source_ext_code = ('.C', '.c', '.c++', '.cc', '.cp', '.cpp', '.cxx')
_source_ext = (*_source_ext_header, *_source_ext_code)

_main_re = re.compile(r'\w+\s+main\s*\([^)]*\)\s*[{;]', re.MULTILINE)
_include_re = re.compile(
    r'^[ \t]*#[ \t]*include[ \t]+[<"]([^">]+)[">][ \t]*$', re.MULTILINE)


@dataclass
class Build:
    source_dir: str = os.path.abspath('.')
    build_dir: str = os.path.join(source_dir, _default_build_dir)
    file_dependencies: Dict[str, List[str]] = field(default_factory=dict)
    modules: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        logging.info(f"cwd:         {os.getcwd()}")
        logging.info(f"source_dir:  {self.source_dir}")
        logging.info(f"build_dir:   {self.build_dir}")

    @staticmethod
    def load(source_dir: Optional[str] = None, build_dir: Optional[str] = None) -> Build:

        source_dir = os.path.abspath(source_dir or '.')
        build_dir = os.path.abspath(
            build_dir or os.path.join(source_dir, _default_build_dir))
        if not os.path.exists(source_dir):
            raise FileNotFoundError(
                f"source directory does not exist: {source_dir}")
        return Build._load_build(source_dir, build_dir)

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

    @staticmethod
    def from_dict(build_dict: Dict[str, Any]) -> Build:
        raise NotImplementedError()

    def to_yaml(self) -> str:
        return yaml.dump(self.to_dict())

    @staticmethod
    def from_yaml(build_yaml: str) -> Build:
        return Build.from_dict(yaml.load(build_yaml))

    def to_json(self, pretty: bool = False) -> str:
        if pretty:
            return json.dumps(self.to_dict(), indent=2)
        return json.dumps(self.to_dict(), separators=(',', ':'))

    @staticmethod
    def from_json(build_json: str) -> Build:
        return Build.from_dict(json.loads(build_json))

    def __str__(self) -> str:
        return self.to_json(pretty=True)

    #===--- Core methods ---===#

    def _clean(self) -> None:
        if os.path.exists(self.build_dir):
            logging.info(f"removing: {self.build_dir}")
            shutil.rmtree(self.build_dir)

    def _analyze(self) -> None:
        project_dir = os.path.dirname(self.source_dir)
        ignore_dirs = (self.build_dir,
                       os.path.join(self.source_dir, '__pycache__'))

        logging.info(
            f"analyzing *before* dependency graph analysis (includes)")

        all_source_files: List[str] = []
        inferred_modules: Dict[str, Any] = {}
        for root, dirs, files in os.walk(self.source_dir):
            if root.startswith(ignore_dirs):
                continue

            def project_path(filename: str = '') -> str:
                return os.path.relpath(os.path.join(root, filename), project_dir)

            def has_main(project_file_path: str) -> bool:
                with open(os.path.join(project_dir, project_file_path)) as f:
                    return bool(_main_re.search(f.read()))

            module = project_path()
            inferred_modules[module] = {}

            source_files = [project_path(f)
                            for f in files if f.endswith(_source_ext)]
            logging.info(f"module source files: {module} -> {source_files}")

            sublibraries = [project_path(d) for d in dirs if not os.path.join(
                self.source_dir, d).startswith(ignore_dirs)]
            logging.info(f"module sublibraries: {module} -> {sublibraries}")

            # Add executables information.
            files_with_main = [f for f in source_files if has_main(f)]
            lib_files = [f for f in source_files if f not in files_with_main]
            inferred_modules[module]['executables'] = {
                os.path.splitext(f)[0]: {
                    'name': os.path.splitext(f)[0],
                    'source-files': files_with_main,
                    # Link to static libraries for executables by default.
                    'static-libraries': [module] if lib_files else [],
                    'shared-libraries': sublibraries,
                }
                for f in files_with_main
                if f.endswith(_source_ext_code)}

            # Add library information.
            inferred_modules[module]['name'] = module
            inferred_modules[module]['source-files'] = lib_files
            # Link to shared libraries for libraries by default.
            inferred_modules[module]['static-libraries'] = []
            inferred_modules[module]['shared-libraries'] = sublibraries
            logging.debug(f"module: {module}: "
                          f"{yaml.dump(inferred_modules[module])}")

            all_source_files += source_files

        logging.info(f"analyzing dependency graph analysis (includes)")

        # Depth-first search to find all include dependencies recursively.
        dependencies_graph: Dict[str, Set[str]] = {}

        def get_dependencies(file_path: str) -> Set[str]:
            if file_path in dependencies_graph:
                return dependencies_graph[file_path]
            dependencies_graph[file_path] = {file_path}
            dir_name = os.path.dirname(file_path)
            with open(os.path.join(project_dir, file_path)) as f:
                includes = {
                    os.path.join(dir_name, include)
                    for include in _include_re.findall(f.read())
                    if os.path.isfile(
                        os.path.join(project_dir, dir_name, include))}
            for include_path in includes:
                dependencies_graph[file_path] |= get_dependencies(include_path)
            return dependencies_graph[file_path]

        inferred_file_dependencies = {
            source_path: list(get_dependencies(source_path))
            for source_path in all_source_files}

        logging.debug(f"user-supplied file dependencies:\n"
                      f"{yaml.dump(self.file_dependencies)}")
        logging.debug(f"inferred file dependencies:\n"
                      f"{yaml.dump(inferred_file_dependencies)}")
        self.file_dependencies = {
            **inferred_file_dependencies, **self.file_dependencies}
        logging.info(f"file dependencies:\n"
                      f"{yaml.dump(inferred_file_dependencies)}")

        logging.debug(f"user-supplied modules:\n{yaml.dump(self.modules)}")
        logging.debug(f"inferred modules:\n{yaml.dump(inferred_modules)}")
        self.modules = {**inferred_modules, **self.modules}
        logging.info(f"modules:\n{yaml.dump(self.modules)}")

    def _build(self) -> None:
        if not os.path.exists(self.build_dir):
            # Only create the directory if it's nested one level, do not create
            # directories recursively.
            os.mkdir(self.build_dir)

        with open(os.path.join(self.build_dir, 'CMakeLists.txt'), 'w') as f:
            f.writelines([
                f"cmake_minimum_required(VERSION {cmake.__version__})\n",
                f"project('{os.path.basename(self.source_dir)}')\n",
                f"if(NOT CMAKE_BUILD_TYPE)\n",
                f"  set(CMAKE_BUILD_TYPE Release)\n",
                f"endif()\n",
                f'set(CMAKE_CXX_FLAGS "-Wall -Wextra")\n',
                f'set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")\n',
                f'set(CMAKE_CXX_FLAGS_RELEASE "-O2")\n',
                f"add_subdirectory({os.path.basename(self.source_dir)})\n",
            ])

        for module_path, module in self.modules.items():
            module_build_path = os.path.join(self.build_dir, module_path)
            if not os.path.exists(module_build_path):
                os.makedirs(module_build_path)

            def target_path(path: str) -> str:
                return os.path.join(self.build_dir, path)

            def source_path(path: str) -> str:
                return os.path.relpath(
                    os.path.join(os.path.dirname(self.source_dir), path),
                    module_build_path)

            def target_lib(path: str) -> str:
                return f"lib--{path.replace(os.path.sep, '--')}"

            def target_exec(path: str) -> str:
                return f"exec--{path.replace(os.path.sep, '--')}"

            def target_dependencies(target: Dict[str, Any], h_only: bool = False) -> str:
                return '\n  '.join({
                    source_path(dependency)
                    for f in target['source-files']
                    for dependency in self.file_dependencies[f]})

            def link_libraries(target: Dict[str, Any]) -> str:
                return '\n  '.join([
                    *[f"{target_lib(lib)}-static"
                      for lib in target['static-libraries']],
                    *[f"{target_lib(lib)}-shared"
                      for lib in target['shared-libraries']],
                ])

            logging.info(f"module: {module_path}")
            cmake_file = target_path(
                os.path.join(module_path, 'CMakeLists.txt'))
            logging.info(f"cmake file: {cmake_file}")
            with open(cmake_file, 'w') as f:
                # Add sublibraries.
                sublibraries = set(module['static-libraries'])
                sublibraries |= set(module['shared-libraries'])
                for executable in module['executables'].values():
                    sublibraries |= set(executable['static-libraries'])
                    sublibraries |= set(executable['shared-libraries'])
                sublibraries -= {module_path}
                if sublibraries:
                    f.writelines([
                        f"# sublibraries\n",
                        *[f"add_subdirectory({os.path.relpath(lib, module_path)})\n"
                          for lib in sublibraries],
                        f"\n",
                    ])

                # Write library targets.
                lib_dependencies = target_dependencies(module)
                if lib_dependencies:
                    target_lib_name = target_lib(module_path)
                    static_lib = f"{target_lib_name}-static"
                    shared_lib = f"{target_lib_name}-shared"
                    f.writelines([
                        f"# library {module_path} - static\n",
                        f"add_library({static_lib} STATIC\n",
                        f"  {lib_dependencies})\n"
                        f"set_target_properties({static_lib} PROPERTIES\n",
                        f"  OUTPUT_NAME {os.path.basename(module['name'])})\n",
                        f"target_link_libraries({static_lib}\n",
                        f"  {link_libraries(module)})\n"
                        f"\n",
                        f"# library {module_path} - shared\n",
                        f"add_library({shared_lib} SHARED\n"
                        f"  {target_dependencies(module, h_only=True)})\n",
                        f"set_target_properties({shared_lib} PROPERTIES\n",
                        f"  OUTPUT_NAME {os.path.basename(module['name'])}\n",
                        f"  LINKER_LANGUAGE CXX)\n",
                        f"target_link_libraries({shared_lib} {static_lib})\n",
                        f"\n",
                    ])

                # Write executable targets.
                for exec_path, executable in module['executables'].items():
                    target_exec_name = target_exec(exec_path)
                    f.writelines([
                        f"# executable {exec_path}\n",
                        f"add_executable({target_exec_name}\n"
                        f"  {target_dependencies(executable)})\n",
                        f"set_target_properties({target_exec_name} PROPERTIES\n",
                        f"  OUTPUT_NAME {os.path.basename(executable['name'])})\n",
                        f"target_link_libraries({target_exec_name}\n",
                        f"  {link_libraries(executable)})\n",
                        f"\n",
                    ])

        sp.call(['cmake', '-S', self.build_dir, '-B', self.build_dir])
        sp.call(['cmake', '--build', self.build_dir])
                #  '--', f"-j{os.cpu_count()}"

    def _run(self, source_file: str, args: List[str]) -> None:
        exec_path = os.path.splitext(os.path.relpath(
            os.path.join(self.source_dir, source_file),
            os.path.dirname(self.source_dir)))[0]
        executable = os.path.join(self.build_dir, exec_path)
        logging.info(f"executable: {executable}")
        logging.info(f"args: {args}")
        sp.call([executable, *args])

    def _package(self) -> None:
        raise NotImplementedError()

    def _install(self) -> None:
        raise NotImplementedError()

    def _publish(self) -> None:
        raise NotImplementedError()

    #===--- Overridable methods ---===#

    def pre_clean(self) -> None:
        pass

    def post_clean(self) -> None:
        pass

    def clean(self) -> Build:
        logging.info('>> clean')
        self.pre_clean()
        self._clean()
        self.post_clean()
        return self

    def pre_analyze(self) -> None:
        pass

    def post_analyze(self) -> None:
        pass

    def analyze(self) -> Build:
        logging.info(f">> analyze")
        self.pre_analyze()
        self._analyze()
        self.post_analyze()
        return self

    def pre_build(self) -> None:
        pass

    def post_build(self) -> None:
        pass

    def build(self) -> Build:
        self.analyze()
        logging.info('>> build')
        self.pre_build()
        self._build()
        self.post_build()
        return self

    def pre_run(self, source_file: str, args: List[str]) -> None:
        pass

    def post_run(self, source_file: str, args: List[str]) -> None:
        pass

    def run(self, source_file: str, args: Optional[List[str]] = None) -> Build:
        self.build()
        logging.info('>> run')
        self.pre_run(source_file, args or [])
        self._run(source_file, args or [])
        self.post_run(source_file, args or [])
        return self

    def pre_package(self) -> None:
        pass

    def post_package(self) -> None:
        pass

    def package(self) -> Build:
        self.build()
        logging.info('>> package')
        self.pre_package()
        self._package()
        self.post_package()
        return self

    def pre_install(self) -> None:
        pass

    def post_install(self) -> None:
        pass

    def install(self) -> Build:
        self.package()
        logging.info('>> install')
        self.pre_install()
        self._install()
        self.post_install()
        return self

    def pre_publish(self) -> None:
        pass

    def post_publish(self) -> None:
        pass

    def publish(self) -> Build:
        self.package()
        logging.info('>> publish')
        self.pre_publish()
        self._publish()
        self.post_publish()
        return self

    #===--- Helper methods ---===#

    @staticmethod
    def _load_build(source_dir: str, build_dir: str) -> Build:
        # Try build.py
        build_file = os.path.join(source_dir, 'build.py')
        if os.path.isfile(build_file):
            import inspect
            logging.info(f"build_file: {build_file}")
            logging.info(f"adding import path: {source_dir}")

            sys.path.insert(0, os.path.abspath(source_dir))
            import build  # type: ignore
            custom_builds = [
                custom_build[1]
                for custom_build in inspect.getmembers(build, inspect.isclass)
                if issubclass(custom_build[1], Build)]

            if len(custom_builds) == 0:
                raise ValueError('Build class not found')
            elif len(custom_builds) > 1:
                raise ValueError('Multiple Build classes defined')
            logging.info(f"build class: {custom_builds[0].__name__}")
            return custom_builds[0](source_dir, build_dir)

        # If no build file is found, return a generic build.
        return Build(source_dir, build_dir)
