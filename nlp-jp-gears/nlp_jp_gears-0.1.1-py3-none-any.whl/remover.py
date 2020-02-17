from typing import Optional, List, Tuple, Callable
from nlp_jp_gears.utils import delete_by_regex


class AbstractRemover:
    def __init__(
        self,
        targets: Optional[List[str]] = None,
        excludes: Optional[List[str]] = None,
        *args,
        **kwargs,
    ):
        self._remover: Optional[Callable[..., str]] = None
        self.removes: str = ""

    def __call__(self, text: str):
        raise NotImplementedError


class TextBtwBracketsRemover(AbstractRemover):
    """
    remove brackets and the contents.
    support:
        <>{}[]()「」『』（）［］〈〉《》〔〕｛｝«»‹›

    Args:
        targets: declaire target brackets. if None (default), all support brackets is removed.
        excludes: declaire brackets to keep.
    """

    def __init__(
        self,
        targets: Optional[List[str]] = None,
        excludes: Optional[List[str]] = None,
        *args,
        **kwargs,
    ):
        # removes-attribute shows intrinsic all targets a instance removes
        self.removes, delete_regex = _get_delete_pattern_and_regex(targets, excludes)
        self._remover: Callable[[str], str] = delete_by_regex(delete_regex)

    def __call__(self, text: str) -> str:
        """Remove brackets and the contents in input text
        Args:
            text: input text

        Returns:
            output text removed brackets and the contents
        """
        return self._remover(text)


def _get_delete_pattern_and_regex(
    targets: Optional[List[str]] = None, excludes: Optional[List[str]] = None,
) -> Tuple[str, str]:
    """
    create regular expression to remove brackets and the contents.
    """
    pat_f = "<{[(「『（［〈《〔｛«‹"
    pat_b = ">}])」』）］〉》〕｝»›"
    if targets:
        temp = ["", ""]
        for f, g in zip(pat_f, pat_b):
            if f in targets or g in targets:
                temp[0] += f
                temp[1] += g
        pat_f, pat_b = temp
    elif excludes:
        temp = ["", ""]
        for f, g in zip(pat_f, pat_b):
            if f not in excludes and g not in excludes:
                temp[0] += f
                temp[1] += g
        pat_f, pat_b = temp

    pat = [f"(\\{f}.*?\\{g})" for f, g in zip(pat_f, pat_b)]
    regex = r"|".join(pat)

    return pat_f, regex
