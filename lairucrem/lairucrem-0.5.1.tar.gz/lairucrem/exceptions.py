class HgNotFoundError(FileNotFoundError):
    """Raised when the Mercurial executable was not found."""

    def __init__(self):
        super().__init__(
            'Could not found a proper `hg` executable.'
            '\nUse --with-hg to specify the executable path.')

class RepositoryNotFound(FileNotFoundError):
    """Raised when not repository was found."""
