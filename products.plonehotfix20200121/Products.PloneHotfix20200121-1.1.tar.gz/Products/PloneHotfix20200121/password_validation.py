from Products.CMFPlone.RegistrationTool import RegistrationTool


# The pasValidation method was introduced in Plone 4.3.
# Only if this method exists, do we need a patch.
if hasattr(RegistrationTool, "pasValidation"):
    from Products.CMFPlone import PloneMessageFactory as _

    def wrapped_testPasswordValidity(self, password, confirm=None):
        # Verify that the password satisfies the portal's requirements.
        #
        # o If the password is valid, return None.
        # o If not, return a string explaining why.
        err = self.pasValidation("password", password)
        if err:
            return err

        if confirm is not None and confirm != password:
            return _(u"Your password and confirmation did not match. Please try again.")
        return None

    orig = RegistrationTool.testPasswordValidity
    wrapped_testPasswordValidity.__doc__ = orig.__doc__
    RegistrationTool.testPasswordValidity = wrapped_testPasswordValidity
