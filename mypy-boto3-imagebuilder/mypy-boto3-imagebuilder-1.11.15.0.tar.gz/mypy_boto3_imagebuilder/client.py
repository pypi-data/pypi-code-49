"""
Main interface for imagebuilder service client

Usage::

    import boto3
    from mypy_boto3.imagebuilder import ImagebuilderClient

    session = boto3.Session()

    client: ImagebuilderClient = boto3.client("imagebuilder")
    session_client: ImagebuilderClient = session.client("imagebuilder")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
import sys
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_imagebuilder.client as client_scope
else:
    client_scope = object
from mypy_boto3_imagebuilder.type_defs import (
    ClientCancelImageCreationResponseTypeDef,
    ClientCreateComponentResponseTypeDef,
    ClientCreateDistributionConfigurationDistributionsTypeDef,
    ClientCreateDistributionConfigurationResponseTypeDef,
    ClientCreateImageImageTestsConfigurationTypeDef,
    ClientCreateImagePipelineImageTestsConfigurationTypeDef,
    ClientCreateImagePipelineResponseTypeDef,
    ClientCreateImagePipelineScheduleTypeDef,
    ClientCreateImageRecipeBlockDeviceMappingsTypeDef,
    ClientCreateImageRecipeComponentsTypeDef,
    ClientCreateImageRecipeResponseTypeDef,
    ClientCreateImageResponseTypeDef,
    ClientCreateInfrastructureConfigurationLoggingTypeDef,
    ClientCreateInfrastructureConfigurationResponseTypeDef,
    ClientDeleteComponentResponseTypeDef,
    ClientDeleteDistributionConfigurationResponseTypeDef,
    ClientDeleteImagePipelineResponseTypeDef,
    ClientDeleteImageRecipeResponseTypeDef,
    ClientDeleteImageResponseTypeDef,
    ClientDeleteInfrastructureConfigurationResponseTypeDef,
    ClientGetComponentPolicyResponseTypeDef,
    ClientGetComponentResponseTypeDef,
    ClientGetDistributionConfigurationResponseTypeDef,
    ClientGetImagePipelineResponseTypeDef,
    ClientGetImagePolicyResponseTypeDef,
    ClientGetImageRecipePolicyResponseTypeDef,
    ClientGetImageRecipeResponseTypeDef,
    ClientGetImageResponseTypeDef,
    ClientGetInfrastructureConfigurationResponseTypeDef,
    ClientImportComponentResponseTypeDef,
    ClientListComponentBuildVersionsResponseTypeDef,
    ClientListComponentsFiltersTypeDef,
    ClientListComponentsResponseTypeDef,
    ClientListDistributionConfigurationsFiltersTypeDef,
    ClientListDistributionConfigurationsResponseTypeDef,
    ClientListImageBuildVersionsFiltersTypeDef,
    ClientListImageBuildVersionsResponseTypeDef,
    ClientListImagePipelineImagesFiltersTypeDef,
    ClientListImagePipelineImagesResponseTypeDef,
    ClientListImagePipelinesFiltersTypeDef,
    ClientListImagePipelinesResponseTypeDef,
    ClientListImageRecipesFiltersTypeDef,
    ClientListImageRecipesResponseTypeDef,
    ClientListImagesFiltersTypeDef,
    ClientListImagesResponseTypeDef,
    ClientListInfrastructureConfigurationsFiltersTypeDef,
    ClientListInfrastructureConfigurationsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientPutComponentPolicyResponseTypeDef,
    ClientPutImagePolicyResponseTypeDef,
    ClientPutImageRecipePolicyResponseTypeDef,
    ClientStartImagePipelineExecutionResponseTypeDef,
    ClientUpdateDistributionConfigurationDistributionsTypeDef,
    ClientUpdateDistributionConfigurationResponseTypeDef,
    ClientUpdateImagePipelineImageTestsConfigurationTypeDef,
    ClientUpdateImagePipelineResponseTypeDef,
    ClientUpdateImagePipelineScheduleTypeDef,
    ClientUpdateInfrastructureConfigurationLoggingTypeDef,
    ClientUpdateInfrastructureConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ImagebuilderClient",)


class ImagebuilderClient:
    """
    [Imagebuilder.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client)
    """

    exceptions: "client_scope.Exceptions"

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.can_paginate)
        """

    def cancel_image_creation(
        self, imageBuildVersionArn: str, clientToken: str
    ) -> ClientCancelImageCreationResponseTypeDef:
        """
        [Client.cancel_image_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.cancel_image_creation)
        """

    def create_component(
        self,
        name: str,
        semanticVersion: str,
        platform: Literal["Windows", "Linux"],
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateComponentResponseTypeDef:
        """
        [Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_component)
        """

    def create_distribution_configuration(
        self,
        name: str,
        distributions: List[ClientCreateDistributionConfigurationDistributionsTypeDef],
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateDistributionConfigurationResponseTypeDef:
        """
        [Client.create_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_distribution_configuration)
        """

    def create_image(
        self,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: ClientCreateImageImageTestsConfigurationTypeDef = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateImageResponseTypeDef:
        """
        [Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_image)
        """

    def create_image_pipeline(
        self,
        name: str,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: ClientCreateImagePipelineImageTestsConfigurationTypeDef = None,
        schedule: ClientCreateImagePipelineScheduleTypeDef = None,
        status: Literal["DISABLED", "ENABLED"] = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateImagePipelineResponseTypeDef:
        """
        [Client.create_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_pipeline)
        """

    def create_image_recipe(
        self,
        name: str,
        semanticVersion: str,
        components: List[ClientCreateImageRecipeComponentsTypeDef],
        parentImage: str,
        clientToken: str,
        description: str = None,
        blockDeviceMappings: List[ClientCreateImageRecipeBlockDeviceMappingsTypeDef] = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateImageRecipeResponseTypeDef:
        """
        [Client.create_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_recipe)
        """

    def create_infrastructure_configuration(
        self,
        name: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: ClientCreateInfrastructureConfigurationLoggingTypeDef = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientCreateInfrastructureConfigurationResponseTypeDef:
        """
        [Client.create_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.create_infrastructure_configuration)
        """

    def delete_component(
        self, componentBuildVersionArn: str
    ) -> ClientDeleteComponentResponseTypeDef:
        """
        [Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_component)
        """

    def delete_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> ClientDeleteDistributionConfigurationResponseTypeDef:
        """
        [Client.delete_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_distribution_configuration)
        """

    def delete_image(self, imageBuildVersionArn: str) -> ClientDeleteImageResponseTypeDef:
        """
        [Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image)
        """

    def delete_image_pipeline(
        self, imagePipelineArn: str
    ) -> ClientDeleteImagePipelineResponseTypeDef:
        """
        [Client.delete_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_pipeline)
        """

    def delete_image_recipe(self, imageRecipeArn: str) -> ClientDeleteImageRecipeResponseTypeDef:
        """
        [Client.delete_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_recipe)
        """

    def delete_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> ClientDeleteInfrastructureConfigurationResponseTypeDef:
        """
        [Client.delete_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.delete_infrastructure_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.generate_presigned_url)
        """

    def get_component(self, componentBuildVersionArn: str) -> ClientGetComponentResponseTypeDef:
        """
        [Client.get_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_component)
        """

    def get_component_policy(self, componentArn: str) -> ClientGetComponentPolicyResponseTypeDef:
        """
        [Client.get_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_component_policy)
        """

    def get_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> ClientGetDistributionConfigurationResponseTypeDef:
        """
        [Client.get_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_distribution_configuration)
        """

    def get_image(self, imageBuildVersionArn: str) -> ClientGetImageResponseTypeDef:
        """
        [Client.get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_image)
        """

    def get_image_pipeline(self, imagePipelineArn: str) -> ClientGetImagePipelineResponseTypeDef:
        """
        [Client.get_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_pipeline)
        """

    def get_image_policy(self, imageArn: str) -> ClientGetImagePolicyResponseTypeDef:
        """
        [Client.get_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_policy)
        """

    def get_image_recipe(self, imageRecipeArn: str) -> ClientGetImageRecipeResponseTypeDef:
        """
        [Client.get_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe)
        """

    def get_image_recipe_policy(
        self, imageRecipeArn: str
    ) -> ClientGetImageRecipePolicyResponseTypeDef:
        """
        [Client.get_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe_policy)
        """

    def get_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> ClientGetInfrastructureConfigurationResponseTypeDef:
        """
        [Client.get_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.get_infrastructure_configuration)
        """

    def import_component(
        self,
        name: str,
        semanticVersion: str,
        type: Literal["BUILD", "TEST"],
        format: str,
        platform: Literal["Windows", "Linux"],
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> ClientImportComponentResponseTypeDef:
        """
        [Client.import_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.import_component)
        """

    def list_component_build_versions(
        self, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ClientListComponentBuildVersionsResponseTypeDef:
        """
        [Client.list_component_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_component_build_versions)
        """

    def list_components(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[ClientListComponentsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListComponentsResponseTypeDef:
        """
        [Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_components)
        """

    def list_distribution_configurations(
        self,
        filters: List[ClientListDistributionConfigurationsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListDistributionConfigurationsResponseTypeDef:
        """
        [Client.list_distribution_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_distribution_configurations)
        """

    def list_image_build_versions(
        self,
        imageVersionArn: str,
        filters: List[ClientListImageBuildVersionsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListImageBuildVersionsResponseTypeDef:
        """
        [Client.list_image_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_build_versions)
        """

    def list_image_pipeline_images(
        self,
        imagePipelineArn: str,
        filters: List[ClientListImagePipelineImagesFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListImagePipelineImagesResponseTypeDef:
        """
        [Client.list_image_pipeline_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipeline_images)
        """

    def list_image_pipelines(
        self,
        filters: List[ClientListImagePipelinesFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListImagePipelinesResponseTypeDef:
        """
        [Client.list_image_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipelines)
        """

    def list_image_recipes(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[ClientListImageRecipesFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListImageRecipesResponseTypeDef:
        """
        [Client.list_image_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_recipes)
        """

    def list_images(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[ClientListImagesFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_images)
        """

    def list_infrastructure_configurations(
        self,
        filters: List[ClientListInfrastructureConfigurationsFiltersTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ClientListInfrastructureConfigurationsResponseTypeDef:
        """
        [Client.list_infrastructure_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_infrastructure_configurations)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.list_tags_for_resource)
        """

    def put_component_policy(
        self, componentArn: str, policy: str
    ) -> ClientPutComponentPolicyResponseTypeDef:
        """
        [Client.put_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.put_component_policy)
        """

    def put_image_policy(self, imageArn: str, policy: str) -> ClientPutImagePolicyResponseTypeDef:
        """
        [Client.put_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_policy)
        """

    def put_image_recipe_policy(
        self, imageRecipeArn: str, policy: str
    ) -> ClientPutImageRecipePolicyResponseTypeDef:
        """
        [Client.put_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_recipe_policy)
        """

    def start_image_pipeline_execution(
        self, imagePipelineArn: str, clientToken: str
    ) -> ClientStartImagePipelineExecutionResponseTypeDef:
        """
        [Client.start_image_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.start_image_pipeline_execution)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.untag_resource)
        """

    def update_distribution_configuration(
        self,
        distributionConfigurationArn: str,
        distributions: List[ClientUpdateDistributionConfigurationDistributionsTypeDef],
        clientToken: str,
        description: str = None,
    ) -> ClientUpdateDistributionConfigurationResponseTypeDef:
        """
        [Client.update_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.update_distribution_configuration)
        """

    def update_image_pipeline(
        self,
        imagePipelineArn: str,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: ClientUpdateImagePipelineImageTestsConfigurationTypeDef = None,
        schedule: ClientUpdateImagePipelineScheduleTypeDef = None,
        status: Literal["DISABLED", "ENABLED"] = None,
    ) -> ClientUpdateImagePipelineResponseTypeDef:
        """
        [Client.update_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.update_image_pipeline)
        """

    def update_infrastructure_configuration(
        self,
        infrastructureConfigurationArn: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: ClientUpdateInfrastructureConfigurationLoggingTypeDef = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
    ) -> ClientUpdateInfrastructureConfigurationResponseTypeDef:
        """
        [Client.update_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/imagebuilder.html#Imagebuilder.Client.update_infrastructure_configuration)
        """


class Exceptions:
    CallRateLimitExceededException: Boto3ClientError
    ClientError: Boto3ClientError
    ClientException: Boto3ClientError
    ForbiddenException: Boto3ClientError
    IdempotentParameterMismatchException: Boto3ClientError
    InvalidPaginationTokenException: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    InvalidVersionNumberException: Boto3ClientError
    ResourceAlreadyExistsException: Boto3ClientError
    ResourceDependencyException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ServiceException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
