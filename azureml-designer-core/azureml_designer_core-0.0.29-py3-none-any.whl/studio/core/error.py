class UserError(Exception):
    """This is a base exception to indicate the errors that caused by unexpected user input.

    Once an exception inherited from UserError is raised,
    it could be displayed in Web UI to help the user adjust his input.
    """
    pass
