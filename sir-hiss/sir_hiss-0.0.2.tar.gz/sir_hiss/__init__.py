import importlib.util
import subprocess
import sys
import time
from functools import lru_cache
from logging import debug
from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Optional, Type
from warnings import warn

import toml

Cmd = List[Optional[str]]

TOOLS: Dict[str, Type["Tool"]] = {}


@lru_cache()
def find_project_root(*srcs: str) -> Path:
    """Return a directory containing .git, .hg, or pyproject.toml.
    That directory can be one of the directories passed in `srcs` or their
    common parent.
    If no directory in the tree contains a marker that would specify it's the
    project root, the root of the file system is returned.
    """
    # Copied from Black project https://github.com/psf/black
    if not srcs:
        return Path("/").resolve()

    common_base = min(Path(src).resolve() for src in srcs)
    if common_base.is_dir():
        # Append a fake file so `parents` below returns `common_base_dir`, too.
        common_base /= "fake-file"
    for directory in common_base.parents:
        if (directory / ".git").is_dir():
            return directory

        if (directory / ".hg").is_dir():
            return directory

        if (directory / "pyproject.toml").is_file():
            return directory

    return directory


@lru_cache()
def load_conf(root: Path, file: str) -> MutableMapping[str, Any]:
    file = root / file
    if not file.exists():
        return {}

    return toml.load(file)


@lru_cache()
def pyproject(root: Path) -> MutableMapping[str, Any]:
    return load_conf(root, "pyproject.toml")


def setup_cfg(root: Path) -> MutableMapping[str, Any]:
    return load_conf(root, "setup.cfg")


def section(config: MutableMapping[str, Any], key: str) -> MutableMapping[str, Any]:
    for part in key.split("."):
        config = config.get(part, None)
        if config is None:
            return {}
    return config


class Tool:
    slow: bool = False

    def __init_subclass__(cls):
        TOOLS[cls.package()] = cls

    def __init__(self, root: Path):
        self.root = root

    def __eq__(self, other):
        return type(self) == type(other) and self.root == other.root

    def cmd(self, file: str, check: bool = False) -> Cmd:
        return [self.package(), file]

    def enabled(self) -> bool:
        """Checks if the tool is enabled in the given project.

        This contains generic check that should work for most plugin.
        You can override _custom_enabled() to do more checks.
        """
        package = self.package()
        tools = section(pyproject(self.root), "tool")

        if (
            package in tools
            or package in section(tools, "poetry.dev-dependencies")
            or package in section(tools, "poetry.dependencies")
        ):
            return True

        cfg = setup_cfg(self.root)
        if package in cfg or f"tool:{package}" in cfg:
            return True
        # TODO: check into options.extras_require

        return self._custom_enabled()

    def has_conf_file(self, *files: str) -> bool:
        return any(((self.root / f).exists() for f in files))

    def _custom_enabled(self) -> bool:
        """Extension method for tool specific checks.

        Make sure that this method is reproducible.
        Do NOT check for cache files or directories.
        """
        return False

    @classmethod
    def package(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def available(cls) -> bool:
        return importlib.util.find_spec(cls.package()) is not None

    def run(self, file: str, check: bool = False) -> None:
        cmd = [p for p in self.cmd(file, check) if p is not None]
        debug(" ".join(cmd))
        subprocess.run(cmd, stdout=sys.stdout, stderr=sys.stderr)

    def __repr__(self):
        return self.package()


def o(key: str, value: bool) -> Optional[str]:
    return key if value else None


class Black(Tool):
    def cmd(self, file: str, check: bool = False) -> Cmd:
        return ["black", o("--check", check), file]


class ISort(Tool):
    def cmd(self, file: str, check: bool = False) -> Cmd:
        return ["isort", o("--check", check), "-rc", file]


class MyPy(Tool):
    def cmd(self, file: str, check: bool = False) -> Cmd:
        use_pyproject = section(pyproject(self.root), "mypy") is not None
        if use_pyproject:
            return ["mypy", "--config-file", str(self.root / "pyproject.toml"), file]
        else:
            return ["mypy", file]

    def _custom_enabled(self) -> bool:
        if (self.root / "mypy.ini").exists():
            return True

        # mypy doesn't officially support pyproject.toml, but you can still
        # add your configuration there under a "mypy" section.
        return pyproject(self.root).get("mypy", None) is not None


class Flake(Tool):
    def _custom_enabled(self) -> bool:
        return (self.root / ".flake8").exists()


class Pylint(Tool):
    # TODO: pylint works best with module, check that it works as expected

    def _custom_enabled(self) -> bool:
        return self.has_conf_file(".pylintrc", "pylintrc")


class NoseTest(Tool):
    slow = True

    def _custom_enabled(self) -> bool:
        return self.has_conf_file(".noserc", "nose.cfg")


class PyTest(Tool):
    slow = True

    def _custom_enabled(self) -> bool:

        if (self.root / "pytest.ini").exists():
            return True
        elif (self.root / "tox.ini").exists():
            if "pytest" in toml.load(self.root / "tox.ini"):
                return True

        return self.has_conf_file("test/conftest.py", "tests/conftest.py")


def find_tools(root: Path) -> List[Tool]:
    hiss_config = section(pyproject(root), "tool.hiss")
    listed_tools = hiss_config.get("include", [])
    for t in listed_tools:
        assert t in TOOLS, f"Tool '{t}' not found. Chose from {list(TOOLS.keys())}."

    tools = []
    for tool_cls in TOOLS.values():
        t = tool_cls(root)
        if t.package() not in listed_tools and not t.enabled():
            continue
        if not t.available():
            warn(f"Package {t.package()} not found")
            continue
        tools.append(t)

    return tools


def main(
    file: str = ".",
    check: bool = False,
    fast: bool = False,
    preview: bool = False,
    root: Path = None,
):
    print(sys.executable)
    t_start = time.time()
    tools_time = 0.0
    if root is None:
        root = find_project_root(file)
        print(root)

    tools = find_tools(root)
    n = 0
    for tool in tools:
        if fast and tool.slow:
            print("***", tool, " (skipped in --fast mode) ***")
            continue

        print("***", tool, "***")
        if preview:
            continue
        n += 1

        t0 = time.time()
        tool.run(file, check)
        elapsed = time.time() - t0
        tools_time += elapsed
        print(" -", tool, f"took {elapsed:.1f}s")

    wall_time = time.time() - t_start
    hiss_time = wall_time - tools_time
    print(
        f" - hiss ran {n} tools in {wall_time:.1f}s. (spend {hiss_time:.1f}s internally)"
    )


def _main():
    import func_argparse

    return func_argparse.single_main(main)


if __name__ == "__main__":
    _main()
