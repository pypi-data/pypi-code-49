class UserFormKwargsMixin:
    """
    Mixin for adding user instance to forms. Use with form's UserFormKwargsMixin.
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(dict(user=self.request.user))
        return kwargs
