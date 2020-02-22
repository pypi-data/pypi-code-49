import fnmatch
import logging
import os
import re
import shutil
from pathlib import Path
from typing import Iterable, List, Optional, Pattern

from binaryornot.check import is_binary

from .templates import TemplateRenderer

logger = logging.getLogger(__name__)


MATCH_NOTHING = re.compile("(?!.*)")


class FileTreeGenerator:
    def __init__(
        self,
        source_dir: Path,
        target_dir: Path,
        renderer: TemplateRenderer,
        ignore_patterns: Optional[List[str]] = None,
    ):
        if not target_dir.exists():
            target_dir.mkdir()

        self.target_dir = target_dir
        self.source_dir = source_dir.resolve()
        self.renderer = renderer
        self.ignore_pattern = fnmatches_to_regex(ignore_patterns)

        # Keep a mapping between source directories and target directories.
        # This simplifies resolution of rendered directory names.
        self._directory_mapping = {str(source_dir): target_dir}

    def copy(self) -> None:
        for root, dirs, files in os.walk(self.source_dir):
            source_root = Path(root)
            target_root = self._directory_mapping[str(source_root)]

            for filename in files:
                self._copy_file(filename, source_root, target_root)

            for subdir in dirs:
                self._ensure_dir_exists(subdir, source_root, target_root)

    def _copy_file(
        self, source_filename: str, source_root: Path, target_root: Path
    ) -> None:
        # Render source_filename since it may be a template:
        tgt_path = target_root / self.renderer.render_string(source_filename)

        if self.ignore_pattern.match(source_filename):
            return

        src_path = Path(source_root, source_filename)
        if is_binary(str(src_path)):
            shutil.copy(src_path, tgt_path)
            logger.debug(f"Copied binary file from {src_path} to {tgt_path}")
        else:
            with tgt_path.open("w") as f:
                f.write(self.renderer.render(str(src_path)))
            logger.debug(f"Rendered template from {src_path} to {tgt_path}")

        # Copy file mode (i.e. permissions) of `src_path` to `tgt_path`
        shutil.copymode(src_path, tgt_path)

    def _ensure_dir_exists(
        self, source_subdir: str, source_root: Path, target_root: Path
    ) -> None:
        """Create subdirectory in target directory ."""
        # Render source_subdir since it may be a template:
        tgt_path = target_root / self.renderer.render_string(source_subdir)

        # Whenever a new directory is traversed, add to directory mapping.
        src_path = source_root / source_subdir
        self._directory_mapping[str(src_path)] = tgt_path

        tgt_path.mkdir(exist_ok=True)
        logger.debug(f"Created directory {tgt_path}")


def fnmatches_to_regex(
    patterns: Optional[Iterable[str]], case_insensitive: bool = False, flags: int = 0
) -> Pattern[str]:
    """Return a compiled regex Convert fnmatch patterns to that matches any of them.

    Slashes are always converted to match either slash or backslash, for
    Windows support, even when running elsewhere.

    Args:
        partial: If True, then the pattern will match if the target string starts with
            the pattern. Otherwise, it must match the entire string.

    Adapted from coveragepy's `fnmatches_to_regex`.
    See https://github.com/nedbat/coveragepy/blob/master/coverage/files.py
    """
    if not patterns:
        return MATCH_NOTHING
    regexes = (fnmatch.translate(pattern) for pattern in patterns)
    # Python3.7 fnmatch translates "/" as "/". Before that, it translates as "\/",
    # so we have to deal with maybe a backslash.
    regexes = (re.sub(r"\\?/", r"[\\\\/]", regex) for regex in regexes)

    return re.compile(join_regex(regexes), flags=flags)


def join_regex(regexes: Iterable[str]) -> str:
    """Combine a list of regexes into one that matches any of them."""
    return "|".join("(?:%s)" % r for r in regexes)
