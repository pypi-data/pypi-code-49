"""
Main interface for imagebuilder service type definitions.

Usage::

    from mypy_boto3.imagebuilder.type_defs import ClientCancelImageCreationResponseTypeDef

    data: ClientCancelImageCreationResponseTypeDef = {...}
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCancelImageCreationResponseTypeDef",
    "ClientCreateComponentResponseTypeDef",
    "ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    "ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef",
    "ClientCreateDistributionConfigurationDistributionsTypeDef",
    "ClientCreateDistributionConfigurationResponseTypeDef",
    "ClientCreateImageImageTestsConfigurationTypeDef",
    "ClientCreateImagePipelineImageTestsConfigurationTypeDef",
    "ClientCreateImagePipelineResponseTypeDef",
    "ClientCreateImagePipelineScheduleTypeDef",
    "ClientCreateImageRecipeBlockDeviceMappingsebsTypeDef",
    "ClientCreateImageRecipeBlockDeviceMappingsTypeDef",
    "ClientCreateImageRecipeComponentsTypeDef",
    "ClientCreateImageRecipeResponseTypeDef",
    "ClientCreateImageResponseTypeDef",
    "ClientCreateInfrastructureConfigurationLoggings3LogsTypeDef",
    "ClientCreateInfrastructureConfigurationLoggingTypeDef",
    "ClientCreateInfrastructureConfigurationResponseTypeDef",
    "ClientDeleteComponentResponseTypeDef",
    "ClientDeleteDistributionConfigurationResponseTypeDef",
    "ClientDeleteImagePipelineResponseTypeDef",
    "ClientDeleteImageRecipeResponseTypeDef",
    "ClientDeleteImageResponseTypeDef",
    "ClientDeleteInfrastructureConfigurationResponseTypeDef",
    "ClientGetComponentPolicyResponseTypeDef",
    "ClientGetComponentResponsecomponentTypeDef",
    "ClientGetComponentResponseTypeDef",
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef",
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsTypeDef",
    "ClientGetDistributionConfigurationResponsedistributionConfigurationTypeDef",
    "ClientGetDistributionConfigurationResponseTypeDef",
    "ClientGetImagePipelineResponseimagePipelineimageTestsConfigurationTypeDef",
    "ClientGetImagePipelineResponseimagePipelinescheduleTypeDef",
    "ClientGetImagePipelineResponseimagePipelineTypeDef",
    "ClientGetImagePipelineResponseTypeDef",
    "ClientGetImagePolicyResponseTypeDef",
    "ClientGetImageRecipePolicyResponseTypeDef",
    "ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsebsTypeDef",
    "ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsTypeDef",
    "ClientGetImageRecipeResponseimageRecipecomponentsTypeDef",
    "ClientGetImageRecipeResponseimageRecipeTypeDef",
    "ClientGetImageRecipeResponseTypeDef",
    "ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    "ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef",
    "ClientGetImageResponseimagedistributionConfigurationdistributionsTypeDef",
    "ClientGetImageResponseimagedistributionConfigurationTypeDef",
    "ClientGetImageResponseimageimageRecipeblockDeviceMappingsebsTypeDef",
    "ClientGetImageResponseimageimageRecipeblockDeviceMappingsTypeDef",
    "ClientGetImageResponseimageimageRecipecomponentsTypeDef",
    "ClientGetImageResponseimageimageRecipeTypeDef",
    "ClientGetImageResponseimageimageTestsConfigurationTypeDef",
    "ClientGetImageResponseimageinfrastructureConfigurationloggings3LogsTypeDef",
    "ClientGetImageResponseimageinfrastructureConfigurationloggingTypeDef",
    "ClientGetImageResponseimageinfrastructureConfigurationTypeDef",
    "ClientGetImageResponseimageoutputResourcesamisstateTypeDef",
    "ClientGetImageResponseimageoutputResourcesamisTypeDef",
    "ClientGetImageResponseimageoutputResourcesTypeDef",
    "ClientGetImageResponseimagestateTypeDef",
    "ClientGetImageResponseimageTypeDef",
    "ClientGetImageResponseTypeDef",
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggings3LogsTypeDef",
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggingTypeDef",
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationTypeDef",
    "ClientGetInfrastructureConfigurationResponseTypeDef",
    "ClientImportComponentResponseTypeDef",
    "ClientListComponentBuildVersionsResponsecomponentSummaryListTypeDef",
    "ClientListComponentBuildVersionsResponseTypeDef",
    "ClientListComponentsFiltersTypeDef",
    "ClientListComponentsResponsecomponentVersionListTypeDef",
    "ClientListComponentsResponseTypeDef",
    "ClientListDistributionConfigurationsFiltersTypeDef",
    "ClientListDistributionConfigurationsResponsedistributionConfigurationSummaryListTypeDef",
    "ClientListDistributionConfigurationsResponseTypeDef",
    "ClientListImageBuildVersionsFiltersTypeDef",
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisstateTypeDef",
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisTypeDef",
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesTypeDef",
    "ClientListImageBuildVersionsResponseimageSummaryListstateTypeDef",
    "ClientListImageBuildVersionsResponseimageSummaryListTypeDef",
    "ClientListImageBuildVersionsResponseTypeDef",
    "ClientListImagePipelineImagesFiltersTypeDef",
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisstateTypeDef",
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisTypeDef",
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesTypeDef",
    "ClientListImagePipelineImagesResponseimageSummaryListstateTypeDef",
    "ClientListImagePipelineImagesResponseimageSummaryListTypeDef",
    "ClientListImagePipelineImagesResponseTypeDef",
    "ClientListImagePipelinesFiltersTypeDef",
    "ClientListImagePipelinesResponseimagePipelineListimageTestsConfigurationTypeDef",
    "ClientListImagePipelinesResponseimagePipelineListscheduleTypeDef",
    "ClientListImagePipelinesResponseimagePipelineListTypeDef",
    "ClientListImagePipelinesResponseTypeDef",
    "ClientListImageRecipesFiltersTypeDef",
    "ClientListImageRecipesResponseimageRecipeSummaryListTypeDef",
    "ClientListImageRecipesResponseTypeDef",
    "ClientListImagesFiltersTypeDef",
    "ClientListImagesResponseimageVersionListTypeDef",
    "ClientListImagesResponseTypeDef",
    "ClientListInfrastructureConfigurationsFiltersTypeDef",
    "ClientListInfrastructureConfigurationsResponseinfrastructureConfigurationSummaryListTypeDef",
    "ClientListInfrastructureConfigurationsResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientPutComponentPolicyResponseTypeDef",
    "ClientPutImagePolicyResponseTypeDef",
    "ClientPutImageRecipePolicyResponseTypeDef",
    "ClientStartImagePipelineExecutionResponseTypeDef",
    "ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    "ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef",
    "ClientUpdateDistributionConfigurationDistributionsTypeDef",
    "ClientUpdateDistributionConfigurationResponseTypeDef",
    "ClientUpdateImagePipelineImageTestsConfigurationTypeDef",
    "ClientUpdateImagePipelineResponseTypeDef",
    "ClientUpdateImagePipelineScheduleTypeDef",
    "ClientUpdateInfrastructureConfigurationLoggings3LogsTypeDef",
    "ClientUpdateInfrastructureConfigurationLoggingTypeDef",
    "ClientUpdateInfrastructureConfigurationResponseTypeDef",
)

ClientCancelImageCreationResponseTypeDef = TypedDict(
    "ClientCancelImageCreationResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

ClientCreateComponentResponseTypeDef = TypedDict(
    "ClientCreateComponentResponseTypeDef",
    {"requestId": str, "clientToken": str, "componentBuildVersionArn": str},
    total=False,
)

ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef = TypedDict(
    "ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    {"userIds": List[str], "userGroups": List[str]},
    total=False,
)

ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef = TypedDict(
    "ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "amiTags": Dict[str, str],
        "launchPermission": ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef,
    },
    total=False,
)

_RequiredClientCreateDistributionConfigurationDistributionsTypeDef = TypedDict(
    "_RequiredClientCreateDistributionConfigurationDistributionsTypeDef", {"region": str}
)
_OptionalClientCreateDistributionConfigurationDistributionsTypeDef = TypedDict(
    "_OptionalClientCreateDistributionConfigurationDistributionsTypeDef",
    {
        "amiDistributionConfiguration": ClientCreateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef,
        "licenseConfigurationArns": List[str],
    },
    total=False,
)


class ClientCreateDistributionConfigurationDistributionsTypeDef(
    _RequiredClientCreateDistributionConfigurationDistributionsTypeDef,
    _OptionalClientCreateDistributionConfigurationDistributionsTypeDef,
):
    pass


ClientCreateDistributionConfigurationResponseTypeDef = TypedDict(
    "ClientCreateDistributionConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "distributionConfigurationArn": str},
    total=False,
)

ClientCreateImageImageTestsConfigurationTypeDef = TypedDict(
    "ClientCreateImageImageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientCreateImagePipelineImageTestsConfigurationTypeDef = TypedDict(
    "ClientCreateImagePipelineImageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientCreateImagePipelineResponseTypeDef = TypedDict(
    "ClientCreateImagePipelineResponseTypeDef",
    {"requestId": str, "clientToken": str, "imagePipelineArn": str},
    total=False,
)

ClientCreateImagePipelineScheduleTypeDef = TypedDict(
    "ClientCreateImagePipelineScheduleTypeDef",
    {
        "scheduleExpression": str,
        "pipelineExecutionStartCondition": Literal[
            "EXPRESSION_MATCH_ONLY", "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        ],
    },
    total=False,
)

ClientCreateImageRecipeBlockDeviceMappingsebsTypeDef = TypedDict(
    "ClientCreateImageRecipeBlockDeviceMappingsebsTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
    },
    total=False,
)

ClientCreateImageRecipeBlockDeviceMappingsTypeDef = TypedDict(
    "ClientCreateImageRecipeBlockDeviceMappingsTypeDef",
    {
        "deviceName": str,
        "ebs": ClientCreateImageRecipeBlockDeviceMappingsebsTypeDef,
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

ClientCreateImageRecipeComponentsTypeDef = TypedDict(
    "ClientCreateImageRecipeComponentsTypeDef", {"componentArn": str}
)

ClientCreateImageRecipeResponseTypeDef = TypedDict(
    "ClientCreateImageRecipeResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageRecipeArn": str},
    total=False,
)

ClientCreateImageResponseTypeDef = TypedDict(
    "ClientCreateImageResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

ClientCreateInfrastructureConfigurationLoggings3LogsTypeDef = TypedDict(
    "ClientCreateInfrastructureConfigurationLoggings3LogsTypeDef",
    {"s3BucketName": str, "s3KeyPrefix": str},
    total=False,
)

ClientCreateInfrastructureConfigurationLoggingTypeDef = TypedDict(
    "ClientCreateInfrastructureConfigurationLoggingTypeDef",
    {"s3Logs": ClientCreateInfrastructureConfigurationLoggings3LogsTypeDef},
    total=False,
)

ClientCreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "ClientCreateInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "infrastructureConfigurationArn": str},
    total=False,
)

ClientDeleteComponentResponseTypeDef = TypedDict(
    "ClientDeleteComponentResponseTypeDef",
    {"requestId": str, "componentBuildVersionArn": str},
    total=False,
)

ClientDeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "ClientDeleteDistributionConfigurationResponseTypeDef",
    {"requestId": str, "distributionConfigurationArn": str},
    total=False,
)

ClientDeleteImagePipelineResponseTypeDef = TypedDict(
    "ClientDeleteImagePipelineResponseTypeDef",
    {"requestId": str, "imagePipelineArn": str},
    total=False,
)

ClientDeleteImageRecipeResponseTypeDef = TypedDict(
    "ClientDeleteImageRecipeResponseTypeDef", {"requestId": str, "imageRecipeArn": str}, total=False
)

ClientDeleteImageResponseTypeDef = TypedDict(
    "ClientDeleteImageResponseTypeDef", {"requestId": str, "imageBuildVersionArn": str}, total=False
)

ClientDeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "ClientDeleteInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "infrastructureConfigurationArn": str},
    total=False,
)

ClientGetComponentPolicyResponseTypeDef = TypedDict(
    "ClientGetComponentPolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

ClientGetComponentResponsecomponentTypeDef = TypedDict(
    "ClientGetComponentResponsecomponentTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": Literal["BUILD", "TEST"],
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetComponentResponseTypeDef = TypedDict(
    "ClientGetComponentResponseTypeDef",
    {"requestId": str, "component": ClientGetComponentResponsecomponentTypeDef},
    total=False,
)

ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef = TypedDict(
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    {"userIds": List[str], "userGroups": List[str]},
    total=False,
)

ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef = TypedDict(
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "amiTags": Dict[str, str],
        "launchPermission": ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef,
    },
    total=False,
)

ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsTypeDef = TypedDict(
    "ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsTypeDef",
    {
        "region": str,
        "amiDistributionConfiguration": ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef,
        "licenseConfigurationArns": List[str],
    },
    total=False,
)

ClientGetDistributionConfigurationResponsedistributionConfigurationTypeDef = TypedDict(
    "ClientGetDistributionConfigurationResponsedistributionConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "distributions": List[
            ClientGetDistributionConfigurationResponsedistributionConfigurationdistributionsTypeDef
        ],
        "timeoutMinutes": int,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetDistributionConfigurationResponseTypeDef = TypedDict(
    "ClientGetDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": ClientGetDistributionConfigurationResponsedistributionConfigurationTypeDef,
    },
    total=False,
)

ClientGetImagePipelineResponseimagePipelineimageTestsConfigurationTypeDef = TypedDict(
    "ClientGetImagePipelineResponseimagePipelineimageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientGetImagePipelineResponseimagePipelinescheduleTypeDef = TypedDict(
    "ClientGetImagePipelineResponseimagePipelinescheduleTypeDef",
    {
        "scheduleExpression": str,
        "pipelineExecutionStartCondition": Literal[
            "EXPRESSION_MATCH_ONLY", "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        ],
    },
    total=False,
)

ClientGetImagePipelineResponseimagePipelineTypeDef = TypedDict(
    "ClientGetImagePipelineResponseimagePipelineTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "imageRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ClientGetImagePipelineResponseimagePipelineimageTestsConfigurationTypeDef,
        "schedule": ClientGetImagePipelineResponseimagePipelinescheduleTypeDef,
        "status": Literal["DISABLED", "ENABLED"],
        "dateCreated": str,
        "dateUpdated": str,
        "dateLastRun": str,
        "dateNextRun": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImagePipelineResponseTypeDef = TypedDict(
    "ClientGetImagePipelineResponseTypeDef",
    {"requestId": str, "imagePipeline": ClientGetImagePipelineResponseimagePipelineTypeDef},
    total=False,
)

ClientGetImagePolicyResponseTypeDef = TypedDict(
    "ClientGetImagePolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

ClientGetImageRecipePolicyResponseTypeDef = TypedDict(
    "ClientGetImageRecipePolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsebsTypeDef = TypedDict(
    "ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsebsTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
    },
    total=False,
)

ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsTypeDef = TypedDict(
    "ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsTypeDef",
    {
        "deviceName": str,
        "ebs": ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsebsTypeDef,
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

ClientGetImageRecipeResponseimageRecipecomponentsTypeDef = TypedDict(
    "ClientGetImageRecipeResponseimageRecipecomponentsTypeDef", {"componentArn": str}, total=False
)

ClientGetImageRecipeResponseimageRecipeTypeDef = TypedDict(
    "ClientGetImageRecipeResponseimageRecipeTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "version": str,
        "components": List[ClientGetImageRecipeResponseimageRecipecomponentsTypeDef],
        "parentImage": str,
        "blockDeviceMappings": List[
            ClientGetImageRecipeResponseimageRecipeblockDeviceMappingsTypeDef
        ],
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImageRecipeResponseTypeDef = TypedDict(
    "ClientGetImageRecipeResponseTypeDef",
    {"requestId": str, "imageRecipe": ClientGetImageRecipeResponseimageRecipeTypeDef},
    total=False,
)

ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef = TypedDict(
    "ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    {"userIds": List[str], "userGroups": List[str]},
    total=False,
)

ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef = TypedDict(
    "ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "amiTags": Dict[str, str],
        "launchPermission": ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationlaunchPermissionTypeDef,
    },
    total=False,
)

ClientGetImageResponseimagedistributionConfigurationdistributionsTypeDef = TypedDict(
    "ClientGetImageResponseimagedistributionConfigurationdistributionsTypeDef",
    {
        "region": str,
        "amiDistributionConfiguration": ClientGetImageResponseimagedistributionConfigurationdistributionsamiDistributionConfigurationTypeDef,
        "licenseConfigurationArns": List[str],
    },
    total=False,
)

ClientGetImageResponseimagedistributionConfigurationTypeDef = TypedDict(
    "ClientGetImageResponseimagedistributionConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "distributions": List[
            ClientGetImageResponseimagedistributionConfigurationdistributionsTypeDef
        ],
        "timeoutMinutes": int,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImageResponseimageimageRecipeblockDeviceMappingsebsTypeDef = TypedDict(
    "ClientGetImageResponseimageimageRecipeblockDeviceMappingsebsTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": Literal["standard", "io1", "gp2", "sc1", "st1"],
    },
    total=False,
)

ClientGetImageResponseimageimageRecipeblockDeviceMappingsTypeDef = TypedDict(
    "ClientGetImageResponseimageimageRecipeblockDeviceMappingsTypeDef",
    {
        "deviceName": str,
        "ebs": ClientGetImageResponseimageimageRecipeblockDeviceMappingsebsTypeDef,
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

ClientGetImageResponseimageimageRecipecomponentsTypeDef = TypedDict(
    "ClientGetImageResponseimageimageRecipecomponentsTypeDef", {"componentArn": str}, total=False
)

ClientGetImageResponseimageimageRecipeTypeDef = TypedDict(
    "ClientGetImageResponseimageimageRecipeTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "version": str,
        "components": List[ClientGetImageResponseimageimageRecipecomponentsTypeDef],
        "parentImage": str,
        "blockDeviceMappings": List[
            ClientGetImageResponseimageimageRecipeblockDeviceMappingsTypeDef
        ],
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImageResponseimageimageTestsConfigurationTypeDef = TypedDict(
    "ClientGetImageResponseimageimageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientGetImageResponseimageinfrastructureConfigurationloggings3LogsTypeDef = TypedDict(
    "ClientGetImageResponseimageinfrastructureConfigurationloggings3LogsTypeDef",
    {"s3BucketName": str, "s3KeyPrefix": str},
    total=False,
)

ClientGetImageResponseimageinfrastructureConfigurationloggingTypeDef = TypedDict(
    "ClientGetImageResponseimageinfrastructureConfigurationloggingTypeDef",
    {"s3Logs": ClientGetImageResponseimageinfrastructureConfigurationloggings3LogsTypeDef},
    total=False,
)

ClientGetImageResponseimageinfrastructureConfigurationTypeDef = TypedDict(
    "ClientGetImageResponseimageinfrastructureConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "instanceTypes": List[str],
        "instanceProfileName": str,
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": ClientGetImageResponseimageinfrastructureConfigurationloggingTypeDef,
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImageResponseimageoutputResourcesamisstateTypeDef = TypedDict(
    "ClientGetImageResponseimageoutputResourcesamisstateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientGetImageResponseimageoutputResourcesamisTypeDef = TypedDict(
    "ClientGetImageResponseimageoutputResourcesamisTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": ClientGetImageResponseimageoutputResourcesamisstateTypeDef,
    },
    total=False,
)

ClientGetImageResponseimageoutputResourcesTypeDef = TypedDict(
    "ClientGetImageResponseimageoutputResourcesTypeDef",
    {"amis": List[ClientGetImageResponseimageoutputResourcesamisTypeDef]},
    total=False,
)

ClientGetImageResponseimagestateTypeDef = TypedDict(
    "ClientGetImageResponseimagestateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientGetImageResponseimageTypeDef = TypedDict(
    "ClientGetImageResponseimageTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "state": ClientGetImageResponseimagestateTypeDef,
        "imageRecipe": ClientGetImageResponseimageimageRecipeTypeDef,
        "sourcePipelineName": str,
        "sourcePipelineArn": str,
        "infrastructureConfiguration": ClientGetImageResponseimageinfrastructureConfigurationTypeDef,
        "distributionConfiguration": ClientGetImageResponseimagedistributionConfigurationTypeDef,
        "imageTestsConfiguration": ClientGetImageResponseimageimageTestsConfigurationTypeDef,
        "dateCreated": str,
        "outputResources": ClientGetImageResponseimageoutputResourcesTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetImageResponseTypeDef = TypedDict(
    "ClientGetImageResponseTypeDef",
    {"requestId": str, "image": ClientGetImageResponseimageTypeDef},
    total=False,
)

ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggings3LogsTypeDef = TypedDict(
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggings3LogsTypeDef",
    {"s3BucketName": str, "s3KeyPrefix": str},
    total=False,
)

ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggingTypeDef = TypedDict(
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggingTypeDef",
    {
        "s3Logs": ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggings3LogsTypeDef
    },
    total=False,
)

ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationTypeDef = TypedDict(
    "ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "instanceTypes": List[str],
        "instanceProfileName": str,
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationloggingTypeDef,
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientGetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "ClientGetInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": ClientGetInfrastructureConfigurationResponseinfrastructureConfigurationTypeDef,
    },
    total=False,
)

ClientImportComponentResponseTypeDef = TypedDict(
    "ClientImportComponentResponseTypeDef",
    {"requestId": str, "clientToken": str, "componentBuildVersionArn": str},
    total=False,
)

ClientListComponentBuildVersionsResponsecomponentSummaryListTypeDef = TypedDict(
    "ClientListComponentBuildVersionsResponsecomponentSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "type": Literal["BUILD", "TEST"],
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ClientListComponentBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List[
            ClientListComponentBuildVersionsResponsecomponentSummaryListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListComponentsFiltersTypeDef = TypedDict(
    "ClientListComponentsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListComponentsResponsecomponentVersionListTypeDef = TypedDict(
    "ClientListComponentsResponsecomponentVersionListTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "type": Literal["BUILD", "TEST"],
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

ClientListComponentsResponseTypeDef = TypedDict(
    "ClientListComponentsResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List[ClientListComponentsResponsecomponentVersionListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListDistributionConfigurationsFiltersTypeDef = TypedDict(
    "ClientListDistributionConfigurationsFiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientListDistributionConfigurationsResponsedistributionConfigurationSummaryListTypeDef = TypedDict(
    "ClientListDistributionConfigurationsResponsedistributionConfigurationSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListDistributionConfigurationsResponseTypeDef = TypedDict(
    "ClientListDistributionConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List[
            ClientListDistributionConfigurationsResponsedistributionConfigurationSummaryListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListImageBuildVersionsFiltersTypeDef = TypedDict(
    "ClientListImageBuildVersionsFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisstateTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisstateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisstateTypeDef,
    },
    total=False,
)

ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesTypeDef",
    {"amis": List[ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesamisTypeDef]},
    total=False,
)

ClientListImageBuildVersionsResponseimageSummaryListstateTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseimageSummaryListstateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientListImageBuildVersionsResponseimageSummaryListTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseimageSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "state": ClientListImageBuildVersionsResponseimageSummaryListstateTypeDef,
        "owner": str,
        "dateCreated": str,
        "outputResources": ClientListImageBuildVersionsResponseimageSummaryListoutputResourcesTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListImageBuildVersionsResponseTypeDef = TypedDict(
    "ClientListImageBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ClientListImageBuildVersionsResponseimageSummaryListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListImagePipelineImagesFiltersTypeDef = TypedDict(
    "ClientListImagePipelineImagesFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisstateTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisstateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisstateTypeDef,
    },
    total=False,
)

ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesTypeDef",
    {"amis": List[ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesamisTypeDef]},
    total=False,
)

ClientListImagePipelineImagesResponseimageSummaryListstateTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseimageSummaryListstateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ClientListImagePipelineImagesResponseimageSummaryListTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseimageSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "state": ClientListImagePipelineImagesResponseimageSummaryListstateTypeDef,
        "owner": str,
        "dateCreated": str,
        "outputResources": ClientListImagePipelineImagesResponseimageSummaryListoutputResourcesTypeDef,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListImagePipelineImagesResponseTypeDef = TypedDict(
    "ClientListImagePipelineImagesResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ClientListImagePipelineImagesResponseimageSummaryListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListImagePipelinesFiltersTypeDef = TypedDict(
    "ClientListImagePipelinesFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListImagePipelinesResponseimagePipelineListimageTestsConfigurationTypeDef = TypedDict(
    "ClientListImagePipelinesResponseimagePipelineListimageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientListImagePipelinesResponseimagePipelineListscheduleTypeDef = TypedDict(
    "ClientListImagePipelinesResponseimagePipelineListscheduleTypeDef",
    {
        "scheduleExpression": str,
        "pipelineExecutionStartCondition": Literal[
            "EXPRESSION_MATCH_ONLY", "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        ],
    },
    total=False,
)

ClientListImagePipelinesResponseimagePipelineListTypeDef = TypedDict(
    "ClientListImagePipelinesResponseimagePipelineListTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "imageRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": ClientListImagePipelinesResponseimagePipelineListimageTestsConfigurationTypeDef,
        "schedule": ClientListImagePipelinesResponseimagePipelineListscheduleTypeDef,
        "status": Literal["DISABLED", "ENABLED"],
        "dateCreated": str,
        "dateUpdated": str,
        "dateLastRun": str,
        "dateNextRun": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListImagePipelinesResponseTypeDef = TypedDict(
    "ClientListImagePipelinesResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List[ClientListImagePipelinesResponseimagePipelineListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListImageRecipesFiltersTypeDef = TypedDict(
    "ClientListImageRecipesFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListImageRecipesResponseimageRecipeSummaryListTypeDef = TypedDict(
    "ClientListImageRecipesResponseimageRecipeSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListImageRecipesResponseTypeDef = TypedDict(
    "ClientListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List[ClientListImageRecipesResponseimageRecipeSummaryListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListImagesFiltersTypeDef = TypedDict(
    "ClientListImagesFiltersTypeDef", {"name": str, "values": List[str]}, total=False
)

ClientListImagesResponseimageVersionListTypeDef = TypedDict(
    "ClientListImagesResponseimageVersionListTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

ClientListImagesResponseTypeDef = TypedDict(
    "ClientListImagesResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List[ClientListImagesResponseimageVersionListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientListInfrastructureConfigurationsFiltersTypeDef = TypedDict(
    "ClientListInfrastructureConfigurationsFiltersTypeDef",
    {"name": str, "values": List[str]},
    total=False,
)

ClientListInfrastructureConfigurationsResponseinfrastructureConfigurationSummaryListTypeDef = TypedDict(
    "ClientListInfrastructureConfigurationsResponseinfrastructureConfigurationSummaryListTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ClientListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ClientListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List[
            ClientListInfrastructureConfigurationsResponseinfrastructureConfigurationSummaryListTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ClientPutComponentPolicyResponseTypeDef = TypedDict(
    "ClientPutComponentPolicyResponseTypeDef", {"requestId": str, "componentArn": str}, total=False
)

ClientPutImagePolicyResponseTypeDef = TypedDict(
    "ClientPutImagePolicyResponseTypeDef", {"requestId": str, "imageArn": str}, total=False
)

ClientPutImageRecipePolicyResponseTypeDef = TypedDict(
    "ClientPutImageRecipePolicyResponseTypeDef",
    {"requestId": str, "imageRecipeArn": str},
    total=False,
)

ClientStartImagePipelineExecutionResponseTypeDef = TypedDict(
    "ClientStartImagePipelineExecutionResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef = TypedDict(
    "ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef",
    {"userIds": List[str], "userGroups": List[str]},
    total=False,
)

ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef = TypedDict(
    "ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "amiTags": Dict[str, str],
        "launchPermission": ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationlaunchPermissionTypeDef,
    },
    total=False,
)

_RequiredClientUpdateDistributionConfigurationDistributionsTypeDef = TypedDict(
    "_RequiredClientUpdateDistributionConfigurationDistributionsTypeDef", {"region": str}
)
_OptionalClientUpdateDistributionConfigurationDistributionsTypeDef = TypedDict(
    "_OptionalClientUpdateDistributionConfigurationDistributionsTypeDef",
    {
        "amiDistributionConfiguration": ClientUpdateDistributionConfigurationDistributionsamiDistributionConfigurationTypeDef,
        "licenseConfigurationArns": List[str],
    },
    total=False,
)


class ClientUpdateDistributionConfigurationDistributionsTypeDef(
    _RequiredClientUpdateDistributionConfigurationDistributionsTypeDef,
    _OptionalClientUpdateDistributionConfigurationDistributionsTypeDef,
):
    pass


ClientUpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateDistributionConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "distributionConfigurationArn": str},
    total=False,
)

ClientUpdateImagePipelineImageTestsConfigurationTypeDef = TypedDict(
    "ClientUpdateImagePipelineImageTestsConfigurationTypeDef",
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ClientUpdateImagePipelineResponseTypeDef = TypedDict(
    "ClientUpdateImagePipelineResponseTypeDef",
    {"requestId": str, "clientToken": str, "imagePipelineArn": str},
    total=False,
)

ClientUpdateImagePipelineScheduleTypeDef = TypedDict(
    "ClientUpdateImagePipelineScheduleTypeDef",
    {
        "scheduleExpression": str,
        "pipelineExecutionStartCondition": Literal[
            "EXPRESSION_MATCH_ONLY", "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        ],
    },
    total=False,
)

ClientUpdateInfrastructureConfigurationLoggings3LogsTypeDef = TypedDict(
    "ClientUpdateInfrastructureConfigurationLoggings3LogsTypeDef",
    {"s3BucketName": str, "s3KeyPrefix": str},
    total=False,
)

ClientUpdateInfrastructureConfigurationLoggingTypeDef = TypedDict(
    "ClientUpdateInfrastructureConfigurationLoggingTypeDef",
    {"s3Logs": ClientUpdateInfrastructureConfigurationLoggings3LogsTypeDef},
    total=False,
)

ClientUpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "ClientUpdateInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "infrastructureConfigurationArn": str},
    total=False,
)
