from typing import Callable, Tuple


class Composer:
    """Composer of NLP gears

    Args:
        ops: NLP gears instance such as remover.TextBtwBracketsRemover instance
    """

    def __init__(self, *ops: Callable[[str], str]):
        self.ops: Tuple[Callable[[str], str], ...] = ops

    def __call__(self, text: str) -> str:
        for op in self.ops:
            text = op(text)
        return text
