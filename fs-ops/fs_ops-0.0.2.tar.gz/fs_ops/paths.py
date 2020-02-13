from pathlib import Path


def find_suffixed_files(paths, file_patterns, extensions=[]):
    """Recursively find files with given suffixes within a set of paths.

    If 'paths' point to files, then we filter those with given extensions.
    If 'paths' point to folders, we recursively search inside each path for a given pattern.
    Paths to files with extension in 'extensions' will not be filtered out.
    Provided file paths are checked for existance.

    Arguments:
        paths (list): List of paths (str, pathlib.Path). List.
        file_patterns (list): List of file patterns to match.
    Yields:
        pathlib.Path: paths to the required files.
    """
    for p in paths:
        p = Path(p).expanduser()
        # is_file checks for existance too
        if p.is_file() and p.suffix in extensions:
            yield p
        if p.is_dir():
            for file_pattern in file_patterns:
                yield from p.glob(file_pattern)

