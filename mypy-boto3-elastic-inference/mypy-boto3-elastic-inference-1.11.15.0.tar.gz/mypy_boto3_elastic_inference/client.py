"""
Main interface for elastic-inference service client

Usage::

    import boto3
    from mypy_boto3.elastic_inference import ElasticInferenceClient

    session = boto3.Session()

    client: ElasticInferenceClient = boto3.client("elastic-inference")
    session_client: ElasticInferenceClient = session.client("elastic-inference")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_elastic_inference.client as client_scope
else:
    client_scope = object
from mypy_boto3_elastic_inference.type_defs import ClientListTagsForResourceResponseTypeDef


__all__ = ("ElasticInferenceClient",)


class ElasticInferenceClient:
    """
    [ElasticInference.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/elastic-inference.html#ElasticInference.Client.untag_resource)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InternalServerException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
