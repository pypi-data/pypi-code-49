from ..actors import Actor


class Action:
    """
    This base class is only used to enforce proper Action implementation.
    """

    def perform_as(self, the_actor: Actor):
        raise NotImplementedError(
            "Actions must implement perform_as(self, the actor). Please implement this "
            f"method for the custom '{self.__class__.__name__}' Action."
        )
