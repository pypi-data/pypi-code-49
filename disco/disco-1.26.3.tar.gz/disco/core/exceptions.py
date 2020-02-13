"""
Exceptions raised by the SDK
"""


class _ExceptionWithDocSupport(Exception):
    """Base exception that uses its first docstring line in lieu of a
    message.
    """

    def __init__(self, message=None):
        # We use `None` as the default for `message`, so the user can input ''
        # to force an empty message.

        """
        Args:
            message:
        """
        if message is None:
            if isinstance(self, _ExceptionWithDocSupport):
                message = (self.__doc__ or '').strip().split('\n')[0]

        super().__init__(message)


class DiscoException(_ExceptionWithDocSupport):
    """The base of all other exceptions"""


class NoCredentials(DiscoException):
    """Please provide email and password for DISCO,
    use `disco.set_credentials`.
    """


class InvalidCredentials(DiscoException):
    """
    Wrong email or password
    """


class NoValidProfileException(DiscoException):
    """This user is not allowed to run jobs on Dis.co"""


class TimeOutError(DiscoException, TimeoutError):  # pylint: disable=too-many-ancestors
    """Timeout error"""


class RequestException(DiscoException):
    """Error in a request sent to the backend of DISCO"""

    DEFAULT_MESSAGE = 'Request error'

    def __init__(self, message=None, additional_info=None):
        super().__init__(message or self.DEFAULT_MESSAGE)
        self.additional_info = additional_info or {}


class GraphQLRequestException(DiscoException):
    """
    Error in GraphQL call
    """

    errors = []

    def __init__(self, message=None, graphql_errors=None):
        self.errors = graphql_errors if graphql_errors is not None else []
        super().__init__(message)

    def messages(self):
        """Returns all messages from the gql errors"""
        return list(map(lambda err: err['message'], self.errors))


class BucketPathsException(DiscoException):
    """
    User got an error when trying to register files from a bucket path/s
    """

    def __init__(self, message=None, bucket_paths_errors=None):
        super().__init__(message)
        self.bucket_paths_errors = bucket_paths_errors or {}


class DiscoErrorCodes:
    """
    Disco Error Codes
    """
    BucketPaths = 'bucket_paths'


class BucketPathsErrorTypes:
    """
    Bucket Paths Error Types
    """
    # User tried to register files from an invalid or missing bucket path
    InvalidPath = 'invalid_path'

    # User tried to register files from an empty bucket path
    NoFilesInPath = 'no_files_in_path'
