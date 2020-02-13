from pathlib import PosixPath, Path


def flatten_seq(seq):
    """convert a sequence of embedded sequences into a plain list"""
    result = []
    vals = seq.values() if type(seq) == dict else seq
    for i in vals:
        if isinstance(i, (dict, list)):
            result.extend(flatten_seq(i))
        elif isinstance(i, str):
            result.append(i)
    return result


class Chapters:
    """
    Helper class converting chapter list of complicated structure
    into a plain list of chapter names or path to actual md files
    in the src dir.
    """

    def __init__(self,
                 chapters: list):
        self._chapters = chapters

    @property
    def flat(self):
        """Flat list of chapter file names"""
        return flatten_seq(self._chapters)

    @property
    def paths(self, parent_dir: str or PosixPath):
        """Flat list of PosixPath objects relative to project root."""
        return (Path(parent_dir) / chap for chap in self.flat)
