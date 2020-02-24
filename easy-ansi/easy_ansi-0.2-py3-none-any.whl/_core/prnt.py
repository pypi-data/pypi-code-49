# Because prnt is used by almost every module, I was getting circular import errors.
# So I moved this method to it's own module for all the other modules to pull from.


def prnt(text: str) -> None:
    """Convenience method to print without a newline."""
    print(text, end='', flush=True)
