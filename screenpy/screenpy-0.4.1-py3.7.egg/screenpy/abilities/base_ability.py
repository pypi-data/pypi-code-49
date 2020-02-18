class Ability:
    """
    This base class is only used to enforce proper Ability implementation.
    """

    def forget(self):
        raise NotImplementedError(
            "Abilities must implement forget(self). Please implement this method on "
            f"the custom '{self.__class__.__name__}' Ability."
        )
