"""
Utility functions used by the object clerk
"""
import logging

from botocore.exceptions import ClientError

from object_clerk.exceptions import ObjectClerkException, ObjectNotFoundException


logger = logging.getLogger(__name__)


def mutate_client_exceptions(client_func):
    """
    Decorator to wrap boto3 call functions to capture Client Exceptions
    and translate to object clerk exceptions
    :param client_func: boto3 client function to wrap
    :return: Output of boto3 client function
    """

    def call_client_func(*args, **kwargs):
        """
        Wrapper function for  boto3 client translating ClientError codes to exceptions
        """
        try:
            return client_func(*args, **kwargs)
        except ClientError as e:
            error_detail = f"function={client_func.__name__}, args={args}, kwargs={kwargs}, detail={e.response}"
            logger.error(f"Error executing client function: {error_detail}")
            error_code = None
            if isinstance(e.response.get("Error"), dict):
                error_code = e.response["Error"].get("Code")
            if error_code in ["404", "NoSuchBucket", "NoSuchKey"]:
                raise ObjectNotFoundException(f"Object not found: detail={e.response}")
            raise ObjectClerkException(f"Error executing client function: {error_detail}")
    return call_client_func
