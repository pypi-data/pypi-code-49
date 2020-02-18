"""
A resolution that negates another resolution. Resolutions must be paired
with questions and passed together to an actor like so:

    the_actor.should_see_the(
        (Text.of_the(WELCOME_BANNER), IsNot(EqualTo("Goodbye!"))),
    )
"""


from typing import Type

from hamcrest import is_not

from .base_resolution import Resolution


class IsNot(Resolution):
    """
    Matches a negated Resolution (e.g. `not ReadsExactly("yes")`).
    """

    expected: Type[Resolution]
    matcher: object

    line = "not {expectation}"

    def __init__(self, resolution: Type[Resolution]) -> None:
        self.expected = resolution
        self.matcher = is_not(resolution)
