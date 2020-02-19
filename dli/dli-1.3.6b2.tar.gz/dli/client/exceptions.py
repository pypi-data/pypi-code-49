import json

class DatalakeException(Exception):
    def __init__(self, entity=None, params=None, message=None, response=None):
        if not params and not message:
            message = "%s not found" % entity

        self.params = params
        self.message = (
            message or 'entity with params `{}` not found'.format(params)
        )
        self.entity = entity
        self.response = response

        super(DatalakeException, self).__init__(
            self.message, entity,
            params, message
        )

    def __str__(self):
        error = f'\n{self.response.request.method} {self.response.request.url}\n\n'

        if self.response.status_code == 413:
            error += (
                'A file you are attempting to pass is probably too large for our server.'
                ' If passing a sample_data file please make sure it is under 10 Megabytes.\n\n'
            )

        try:
            error += (
                f'{json.dumps(self.response.json(), indent=4)}'
            )
        except json.JSONDecodeError:
            error += (
                f'{self.response.text}'
            )

        return error


class DataframeStreamingException(DatalakeException):

    def __init__(self, error, url):
        self.url = url
        self.error = error

    def __str__(self):
        msg = json.dumps(self.error, indent=4)
        return f'\nGET {self.url}\n\n{msg}'


class CatalogueEntityNotFoundException(DatalakeException):
    pass


class InvalidPayloadException(DatalakeException):
    pass


class UnAuthorisedAccessException(DatalakeException):
    pass


class InsufficientPrivilegesException(DatalakeException):
    message = 'Insufficient privileges to perform this action'


class S3FileDoesNotExist(DatalakeException):
    def __init__(self, file_path):
        self.message = (
            "Either file at path `%s` does not exist / Potential issue with the bucket policy."
            "Please reach out to Datalake Tech Data Ops user for resolution." % file_path
        )

        super(S3FileDoesNotExist, self).__init__(self.message)


class DownloadFailed(DatalakeException):
    pass


class NoAccountSpecified(DatalakeException):

    def __init__(self, accounts):
        self.accounts = accounts
        self.message = (
            "Unable to default the account for access_manager_id, tech_data_ops_id and/or manager_id "
            "due to multiple accounts being attached to this API key. "
            "Your accounts are: %s" % [(a.id, a.name) for a in accounts]
        )
        super(NoAccountSpecified, self).__init__(self.message)


class AuthenticationFailure(Exception):
    """
    An exception wrapping an authentication failure response. If the response
    had a payload, that payload is reported as the exception message, otherwise
    a generic error message is returned.
    """
    GENERIC_ERROR_MESSAGE = (
        'API key is not valid or has expired.'
        ' Please generate a new key in the Catalogue UI and try again.'
    )

    def __init__(self, response=None, message=None):
        self.response = response
        self.message = message

    def __str__(self):
        if self.response and self.response.text:
            return self.response.text
        elif self.message:
            return self.message
        return self.GENERIC_ERROR_MESSAGE
