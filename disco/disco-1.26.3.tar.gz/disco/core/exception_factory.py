from .exceptions import DiscoErrorCodes, RequestException, BucketPathsException


class ExceptionFactory:
    """
    Exception Factory
    """

    @classmethod
    def from_response(cls, json_response):
        """
        Args:
            json_response (dict):

        Returns:
            RequestException
        """
        http_status_code = json_response.get('code')
        message = json_response.get('error', {}).get('message') \
            or f'{RequestException.DEFAULT_MESSAGE} ({http_status_code})'

        additional_info = json_response.get('additional_info', {})

        error_code = additional_info.get('errorCode')

        if error_code == DiscoErrorCodes.BucketPaths:
            return BucketPathsException(message, additional_info.get('bucketPaths'))

        return RequestException(message, additional_info)
