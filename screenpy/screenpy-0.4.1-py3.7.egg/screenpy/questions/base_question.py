"""
Questions provide the mechanism for actors to ask about the state of the
application under test. For example:

    Text.of_the(WELCOME_BANNER)

When paired with Resolutions, they form Screenplay Pattern's test
assertions. The Question will then be passed in to an actor's test method,
along with a Resolution to assert the expected value. An assertion might
look like:

    Perry.should_see_the(
        (Text.of(THE_WELCOME_MESSAGE), ReadsExactly("Welcome!")),
    )
"""


from ..actors import Actor


class Question:
    """
    This base class is only used and enforce proper Question
    implementation.
    """

    def answered_by(self, the_actor: Actor):
        raise NotImplementedError(
            "Questions must implement answered_by(self, the_actor). Please implement "
            f"this method for the custom '{self.__class__.__name__}' Question."
        )
