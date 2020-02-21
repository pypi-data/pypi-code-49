"""
Main interface for frauddetector service type definitions.

Usage::

    from mypy_boto3.frauddetector.type_defs import ClientBatchCreateVariableResponseerrorsTypeDef

    data: ClientBatchCreateVariableResponseerrorsTypeDef = {...}
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchCreateVariableResponseerrorsTypeDef",
    "ClientBatchCreateVariableResponseTypeDef",
    "ClientBatchCreateVariableVariableEntriesTypeDef",
    "ClientBatchGetVariableResponseerrorsTypeDef",
    "ClientBatchGetVariableResponsevariablesTypeDef",
    "ClientBatchGetVariableResponseTypeDef",
    "ClientCreateDetectorVersionModelVersionsTypeDef",
    "ClientCreateDetectorVersionResponseTypeDef",
    "ClientCreateDetectorVersionRulesTypeDef",
    "ClientCreateModelVersionResponseTypeDef",
    "ClientCreateRuleResponseruleTypeDef",
    "ClientCreateRuleResponseTypeDef",
    "ClientDescribeDetectorResponsedetectorVersionSummariesTypeDef",
    "ClientDescribeDetectorResponseTypeDef",
    "ClientDescribeModelVersionsResponsemodelVersionDetailslabelSchemaTypeDef",
    "ClientDescribeModelVersionsResponsemodelVersionDetailsmodelVariablesTypeDef",
    "ClientDescribeModelVersionsResponsemodelVersionDetailstrainingDataSourceTypeDef",
    "ClientDescribeModelVersionsResponsemodelVersionDetailsTypeDef",
    "ClientDescribeModelVersionsResponseTypeDef",
    "ClientGetDetectorVersionResponsemodelVersionsTypeDef",
    "ClientGetDetectorVersionResponserulesTypeDef",
    "ClientGetDetectorVersionResponseTypeDef",
    "ClientGetDetectorsResponsedetectorsTypeDef",
    "ClientGetDetectorsResponseTypeDef",
    "ClientGetExternalModelsResponseexternalModelsinputConfigurationTypeDef",
    "ClientGetExternalModelsResponseexternalModelsoutputConfigurationTypeDef",
    "ClientGetExternalModelsResponseexternalModelsroleTypeDef",
    "ClientGetExternalModelsResponseexternalModelsTypeDef",
    "ClientGetExternalModelsResponseTypeDef",
    "ClientGetModelVersionResponseTypeDef",
    "ClientGetModelsResponsemodelslabelSchemaTypeDef",
    "ClientGetModelsResponsemodelsmodelVariablesTypeDef",
    "ClientGetModelsResponsemodelstrainingDataSourceTypeDef",
    "ClientGetModelsResponsemodelsTypeDef",
    "ClientGetModelsResponseTypeDef",
    "ClientGetOutcomesResponseoutcomesTypeDef",
    "ClientGetOutcomesResponseTypeDef",
    "ClientGetPredictionExternalModelEndpointDataBlobsTypeDef",
    "ClientGetPredictionResponsemodelScoresmodelVersionTypeDef",
    "ClientGetPredictionResponsemodelScoresTypeDef",
    "ClientGetPredictionResponseTypeDef",
    "ClientGetRulesResponseruleDetailsTypeDef",
    "ClientGetRulesResponseTypeDef",
    "ClientGetVariablesResponsevariablesTypeDef",
    "ClientGetVariablesResponseTypeDef",
    "ClientPutExternalModelInputConfigurationTypeDef",
    "ClientPutExternalModelOutputConfigurationTypeDef",
    "ClientPutExternalModelRoleTypeDef",
    "ClientPutModelLabelSchemaTypeDef",
    "ClientPutModelModelVariablesTypeDef",
    "ClientPutModelTrainingDataSourceTypeDef",
    "ClientUpdateDetectorVersionModelVersionsTypeDef",
    "ClientUpdateDetectorVersionRulesTypeDef",
    "ClientUpdateRuleMetadataRuleTypeDef",
    "ClientUpdateRuleVersionResponseruleTypeDef",
    "ClientUpdateRuleVersionResponseTypeDef",
    "ClientUpdateRuleVersionRuleTypeDef",
)

ClientBatchCreateVariableResponseerrorsTypeDef = TypedDict(
    "ClientBatchCreateVariableResponseerrorsTypeDef",
    {"name": str, "code": int, "message": str},
    total=False,
)

ClientBatchCreateVariableResponseTypeDef = TypedDict(
    "ClientBatchCreateVariableResponseTypeDef",
    {"errors": List[ClientBatchCreateVariableResponseerrorsTypeDef]},
    total=False,
)

ClientBatchCreateVariableVariableEntriesTypeDef = TypedDict(
    "ClientBatchCreateVariableVariableEntriesTypeDef",
    {
        "name": str,
        "dataType": str,
        "dataSource": str,
        "defaultValue": str,
        "description": str,
        "variableType": str,
    },
    total=False,
)

ClientBatchGetVariableResponseerrorsTypeDef = TypedDict(
    "ClientBatchGetVariableResponseerrorsTypeDef",
    {"name": str, "code": int, "message": str},
    total=False,
)

ClientBatchGetVariableResponsevariablesTypeDef = TypedDict(
    "ClientBatchGetVariableResponsevariablesTypeDef",
    {
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "FLOAT", "BOOLEAN"],
        "dataSource": Literal["EVENT", "MODEL_SCORE", "EXTERNAL_MODEL_SCORE"],
        "defaultValue": str,
        "description": str,
        "variableType": str,
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientBatchGetVariableResponseTypeDef = TypedDict(
    "ClientBatchGetVariableResponseTypeDef",
    {
        "variables": List[ClientBatchGetVariableResponsevariablesTypeDef],
        "errors": List[ClientBatchGetVariableResponseerrorsTypeDef],
    },
    total=False,
)

_RequiredClientCreateDetectorVersionModelVersionsTypeDef = TypedDict(
    "_RequiredClientCreateDetectorVersionModelVersionsTypeDef", {"modelId": str}
)
_OptionalClientCreateDetectorVersionModelVersionsTypeDef = TypedDict(
    "_OptionalClientCreateDetectorVersionModelVersionsTypeDef",
    {"modelType": str, "modelVersionNumber": str},
    total=False,
)


class ClientCreateDetectorVersionModelVersionsTypeDef(
    _RequiredClientCreateDetectorVersionModelVersionsTypeDef,
    _OptionalClientCreateDetectorVersionModelVersionsTypeDef,
):
    pass


ClientCreateDetectorVersionResponseTypeDef = TypedDict(
    "ClientCreateDetectorVersionResponseTypeDef",
    {"detectorId": str, "detectorVersionId": str, "status": Literal["DRAFT", "ACTIVE", "INACTIVE"]},
    total=False,
)

_RequiredClientCreateDetectorVersionRulesTypeDef = TypedDict(
    "_RequiredClientCreateDetectorVersionRulesTypeDef", {"detectorId": str}
)
_OptionalClientCreateDetectorVersionRulesTypeDef = TypedDict(
    "_OptionalClientCreateDetectorVersionRulesTypeDef",
    {"ruleId": str, "ruleVersion": str},
    total=False,
)


class ClientCreateDetectorVersionRulesTypeDef(
    _RequiredClientCreateDetectorVersionRulesTypeDef,
    _OptionalClientCreateDetectorVersionRulesTypeDef,
):
    pass


ClientCreateModelVersionResponseTypeDef = TypedDict(
    "ClientCreateModelVersionResponseTypeDef",
    {"modelId": str, "modelType": str, "modelVersionNumber": str, "status": str},
    total=False,
)

ClientCreateRuleResponseruleTypeDef = TypedDict(
    "ClientCreateRuleResponseruleTypeDef",
    {"detectorId": str, "ruleId": str, "ruleVersion": str},
    total=False,
)

ClientCreateRuleResponseTypeDef = TypedDict(
    "ClientCreateRuleResponseTypeDef", {"rule": ClientCreateRuleResponseruleTypeDef}, total=False
)

ClientDescribeDetectorResponsedetectorVersionSummariesTypeDef = TypedDict(
    "ClientDescribeDetectorResponsedetectorVersionSummariesTypeDef",
    {
        "detectorVersionId": str,
        "status": Literal["DRAFT", "ACTIVE", "INACTIVE"],
        "description": str,
        "lastUpdatedTime": str,
    },
    total=False,
)

ClientDescribeDetectorResponseTypeDef = TypedDict(
    "ClientDescribeDetectorResponseTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List[
            ClientDescribeDetectorResponsedetectorVersionSummariesTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientDescribeModelVersionsResponsemodelVersionDetailslabelSchemaTypeDef = TypedDict(
    "ClientDescribeModelVersionsResponsemodelVersionDetailslabelSchemaTypeDef",
    {"labelKey": str, "labelMapper": Dict[str, List[str]]},
    total=False,
)

ClientDescribeModelVersionsResponsemodelVersionDetailsmodelVariablesTypeDef = TypedDict(
    "ClientDescribeModelVersionsResponsemodelVersionDetailsmodelVariablesTypeDef",
    {"name": str, "index": int},
    total=False,
)

ClientDescribeModelVersionsResponsemodelVersionDetailstrainingDataSourceTypeDef = TypedDict(
    "ClientDescribeModelVersionsResponsemodelVersionDetailstrainingDataSourceTypeDef",
    {"dataLocation": str, "dataAccessRoleArn": str},
    total=False,
)

ClientDescribeModelVersionsResponsemodelVersionDetailsTypeDef = TypedDict(
    "ClientDescribeModelVersionsResponsemodelVersionDetailsTypeDef",
    {
        "modelId": str,
        "modelType": str,
        "modelVersionNumber": str,
        "description": str,
        "status": str,
        "trainingDataSource": ClientDescribeModelVersionsResponsemodelVersionDetailstrainingDataSourceTypeDef,
        "modelVariables": List[
            ClientDescribeModelVersionsResponsemodelVersionDetailsmodelVariablesTypeDef
        ],
        "labelSchema": ClientDescribeModelVersionsResponsemodelVersionDetailslabelSchemaTypeDef,
        "validationMetrics": Dict[str, str],
        "trainingMetrics": Dict[str, str],
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientDescribeModelVersionsResponseTypeDef = TypedDict(
    "ClientDescribeModelVersionsResponseTypeDef",
    {
        "modelVersionDetails": List[ClientDescribeModelVersionsResponsemodelVersionDetailsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetDetectorVersionResponsemodelVersionsTypeDef = TypedDict(
    "ClientGetDetectorVersionResponsemodelVersionsTypeDef",
    {"modelId": str, "modelType": str, "modelVersionNumber": str},
    total=False,
)

ClientGetDetectorVersionResponserulesTypeDef = TypedDict(
    "ClientGetDetectorVersionResponserulesTypeDef",
    {"detectorId": str, "ruleId": str, "ruleVersion": str},
    total=False,
)

ClientGetDetectorVersionResponseTypeDef = TypedDict(
    "ClientGetDetectorVersionResponseTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List[ClientGetDetectorVersionResponsemodelVersionsTypeDef],
        "rules": List[ClientGetDetectorVersionResponserulesTypeDef],
        "status": Literal["DRAFT", "ACTIVE", "INACTIVE"],
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientGetDetectorsResponsedetectorsTypeDef = TypedDict(
    "ClientGetDetectorsResponsedetectorsTypeDef",
    {"detectorId": str, "description": str, "lastUpdatedTime": str, "createdTime": str},
    total=False,
)

ClientGetDetectorsResponseTypeDef = TypedDict(
    "ClientGetDetectorsResponseTypeDef",
    {"detectors": List[ClientGetDetectorsResponsedetectorsTypeDef], "nextToken": str},
    total=False,
)

ClientGetExternalModelsResponseexternalModelsinputConfigurationTypeDef = TypedDict(
    "ClientGetExternalModelsResponseexternalModelsinputConfigurationTypeDef",
    {
        "format": Literal["TEXT_CSV", "APPLICATION_JSON"],
        "isOpaque": bool,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)

ClientGetExternalModelsResponseexternalModelsoutputConfigurationTypeDef = TypedDict(
    "ClientGetExternalModelsResponseexternalModelsoutputConfigurationTypeDef",
    {
        "format": Literal["TEXT_CSV", "APPLICATION_JSONLINES"],
        "jsonKeyToVariableMap": Dict[str, str],
        "csvIndexToVariableMap": Dict[str, str],
    },
    total=False,
)

ClientGetExternalModelsResponseexternalModelsroleTypeDef = TypedDict(
    "ClientGetExternalModelsResponseexternalModelsroleTypeDef",
    {"arn": str, "name": str},
    total=False,
)

ClientGetExternalModelsResponseexternalModelsTypeDef = TypedDict(
    "ClientGetExternalModelsResponseexternalModelsTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": str,
        "role": ClientGetExternalModelsResponseexternalModelsroleTypeDef,
        "inputConfiguration": ClientGetExternalModelsResponseexternalModelsinputConfigurationTypeDef,
        "outputConfiguration": ClientGetExternalModelsResponseexternalModelsoutputConfigurationTypeDef,
        "modelEndpointStatus": Literal["ASSOCIATED", "DISSOCIATED"],
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientGetExternalModelsResponseTypeDef = TypedDict(
    "ClientGetExternalModelsResponseTypeDef",
    {
        "externalModels": List[ClientGetExternalModelsResponseexternalModelsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetModelVersionResponseTypeDef = TypedDict(
    "ClientGetModelVersionResponseTypeDef",
    {
        "modelId": str,
        "modelType": str,
        "modelVersionNumber": str,
        "description": str,
        "status": str,
    },
    total=False,
)

ClientGetModelsResponsemodelslabelSchemaTypeDef = TypedDict(
    "ClientGetModelsResponsemodelslabelSchemaTypeDef",
    {"labelKey": str, "labelMapper": Dict[str, List[str]]},
    total=False,
)

ClientGetModelsResponsemodelsmodelVariablesTypeDef = TypedDict(
    "ClientGetModelsResponsemodelsmodelVariablesTypeDef", {"name": str, "index": int}, total=False
)

ClientGetModelsResponsemodelstrainingDataSourceTypeDef = TypedDict(
    "ClientGetModelsResponsemodelstrainingDataSourceTypeDef",
    {"dataLocation": str, "dataAccessRoleArn": str},
    total=False,
)

ClientGetModelsResponsemodelsTypeDef = TypedDict(
    "ClientGetModelsResponsemodelsTypeDef",
    {
        "modelId": str,
        "modelType": str,
        "description": str,
        "trainingDataSource": ClientGetModelsResponsemodelstrainingDataSourceTypeDef,
        "modelVariables": List[ClientGetModelsResponsemodelsmodelVariablesTypeDef],
        "labelSchema": ClientGetModelsResponsemodelslabelSchemaTypeDef,
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientGetModelsResponseTypeDef = TypedDict(
    "ClientGetModelsResponseTypeDef",
    {"nextToken": str, "models": List[ClientGetModelsResponsemodelsTypeDef]},
    total=False,
)

ClientGetOutcomesResponseoutcomesTypeDef = TypedDict(
    "ClientGetOutcomesResponseoutcomesTypeDef",
    {"name": str, "description": str, "lastUpdatedTime": str, "createdTime": str},
    total=False,
)

ClientGetOutcomesResponseTypeDef = TypedDict(
    "ClientGetOutcomesResponseTypeDef",
    {"outcomes": List[ClientGetOutcomesResponseoutcomesTypeDef], "nextToken": str},
    total=False,
)

ClientGetPredictionExternalModelEndpointDataBlobsTypeDef = TypedDict(
    "ClientGetPredictionExternalModelEndpointDataBlobsTypeDef",
    {"byteBuffer": bytes, "contentType": str},
    total=False,
)

ClientGetPredictionResponsemodelScoresmodelVersionTypeDef = TypedDict(
    "ClientGetPredictionResponsemodelScoresmodelVersionTypeDef",
    {"modelId": str, "modelType": str, "modelVersionNumber": str},
    total=False,
)

ClientGetPredictionResponsemodelScoresTypeDef = TypedDict(
    "ClientGetPredictionResponsemodelScoresTypeDef",
    {
        "modelVersion": ClientGetPredictionResponsemodelScoresmodelVersionTypeDef,
        "scores": Dict[str, Any],
    },
    total=False,
)

ClientGetPredictionResponseTypeDef = TypedDict(
    "ClientGetPredictionResponseTypeDef",
    {"outcomes": List[str], "modelScores": List[ClientGetPredictionResponsemodelScoresTypeDef]},
    total=False,
)

ClientGetRulesResponseruleDetailsTypeDef = TypedDict(
    "ClientGetRulesResponseruleDetailsTypeDef",
    {
        "ruleId": str,
        "description": str,
        "detectorId": str,
        "ruleVersion": str,
        "expression": str,
        "language": str,
        "outcomes": List[str],
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientGetRulesResponseTypeDef = TypedDict(
    "ClientGetRulesResponseTypeDef",
    {"ruleDetails": List[ClientGetRulesResponseruleDetailsTypeDef], "nextToken": str},
    total=False,
)

ClientGetVariablesResponsevariablesTypeDef = TypedDict(
    "ClientGetVariablesResponsevariablesTypeDef",
    {
        "name": str,
        "dataType": Literal["STRING", "INTEGER", "FLOAT", "BOOLEAN"],
        "dataSource": Literal["EVENT", "MODEL_SCORE", "EXTERNAL_MODEL_SCORE"],
        "defaultValue": str,
        "description": str,
        "variableType": str,
        "lastUpdatedTime": str,
        "createdTime": str,
    },
    total=False,
)

ClientGetVariablesResponseTypeDef = TypedDict(
    "ClientGetVariablesResponseTypeDef",
    {"variables": List[ClientGetVariablesResponsevariablesTypeDef], "nextToken": str},
    total=False,
)

ClientPutExternalModelInputConfigurationTypeDef = TypedDict(
    "ClientPutExternalModelInputConfigurationTypeDef",
    {
        "format": Literal["TEXT_CSV", "APPLICATION_JSON"],
        "isOpaque": bool,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)

_RequiredClientPutExternalModelOutputConfigurationTypeDef = TypedDict(
    "_RequiredClientPutExternalModelOutputConfigurationTypeDef",
    {"format": Literal["TEXT_CSV", "APPLICATION_JSONLINES"]},
)
_OptionalClientPutExternalModelOutputConfigurationTypeDef = TypedDict(
    "_OptionalClientPutExternalModelOutputConfigurationTypeDef",
    {"jsonKeyToVariableMap": Dict[str, str], "csvIndexToVariableMap": Dict[str, str]},
    total=False,
)


class ClientPutExternalModelOutputConfigurationTypeDef(
    _RequiredClientPutExternalModelOutputConfigurationTypeDef,
    _OptionalClientPutExternalModelOutputConfigurationTypeDef,
):
    pass


_RequiredClientPutExternalModelRoleTypeDef = TypedDict(
    "_RequiredClientPutExternalModelRoleTypeDef", {"arn": str}
)
_OptionalClientPutExternalModelRoleTypeDef = TypedDict(
    "_OptionalClientPutExternalModelRoleTypeDef", {"name": str}, total=False
)


class ClientPutExternalModelRoleTypeDef(
    _RequiredClientPutExternalModelRoleTypeDef, _OptionalClientPutExternalModelRoleTypeDef
):
    pass


_RequiredClientPutModelLabelSchemaTypeDef = TypedDict(
    "_RequiredClientPutModelLabelSchemaTypeDef", {"labelKey": str}
)
_OptionalClientPutModelLabelSchemaTypeDef = TypedDict(
    "_OptionalClientPutModelLabelSchemaTypeDef", {"labelMapper": Dict[str, List[str]]}, total=False
)


class ClientPutModelLabelSchemaTypeDef(
    _RequiredClientPutModelLabelSchemaTypeDef, _OptionalClientPutModelLabelSchemaTypeDef
):
    pass


_RequiredClientPutModelModelVariablesTypeDef = TypedDict(
    "_RequiredClientPutModelModelVariablesTypeDef", {"name": str}
)
_OptionalClientPutModelModelVariablesTypeDef = TypedDict(
    "_OptionalClientPutModelModelVariablesTypeDef", {"index": int}, total=False
)


class ClientPutModelModelVariablesTypeDef(
    _RequiredClientPutModelModelVariablesTypeDef, _OptionalClientPutModelModelVariablesTypeDef
):
    pass


_RequiredClientPutModelTrainingDataSourceTypeDef = TypedDict(
    "_RequiredClientPutModelTrainingDataSourceTypeDef", {"dataLocation": str}
)
_OptionalClientPutModelTrainingDataSourceTypeDef = TypedDict(
    "_OptionalClientPutModelTrainingDataSourceTypeDef", {"dataAccessRoleArn": str}, total=False
)


class ClientPutModelTrainingDataSourceTypeDef(
    _RequiredClientPutModelTrainingDataSourceTypeDef,
    _OptionalClientPutModelTrainingDataSourceTypeDef,
):
    pass


_RequiredClientUpdateDetectorVersionModelVersionsTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorVersionModelVersionsTypeDef", {"modelId": str}
)
_OptionalClientUpdateDetectorVersionModelVersionsTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorVersionModelVersionsTypeDef",
    {"modelType": str, "modelVersionNumber": str},
    total=False,
)


class ClientUpdateDetectorVersionModelVersionsTypeDef(
    _RequiredClientUpdateDetectorVersionModelVersionsTypeDef,
    _OptionalClientUpdateDetectorVersionModelVersionsTypeDef,
):
    pass


_RequiredClientUpdateDetectorVersionRulesTypeDef = TypedDict(
    "_RequiredClientUpdateDetectorVersionRulesTypeDef", {"detectorId": str}
)
_OptionalClientUpdateDetectorVersionRulesTypeDef = TypedDict(
    "_OptionalClientUpdateDetectorVersionRulesTypeDef",
    {"ruleId": str, "ruleVersion": str},
    total=False,
)


class ClientUpdateDetectorVersionRulesTypeDef(
    _RequiredClientUpdateDetectorVersionRulesTypeDef,
    _OptionalClientUpdateDetectorVersionRulesTypeDef,
):
    pass


_RequiredClientUpdateRuleMetadataRuleTypeDef = TypedDict(
    "_RequiredClientUpdateRuleMetadataRuleTypeDef", {"detectorId": str}
)
_OptionalClientUpdateRuleMetadataRuleTypeDef = TypedDict(
    "_OptionalClientUpdateRuleMetadataRuleTypeDef", {"ruleId": str, "ruleVersion": str}, total=False
)


class ClientUpdateRuleMetadataRuleTypeDef(
    _RequiredClientUpdateRuleMetadataRuleTypeDef, _OptionalClientUpdateRuleMetadataRuleTypeDef
):
    pass


ClientUpdateRuleVersionResponseruleTypeDef = TypedDict(
    "ClientUpdateRuleVersionResponseruleTypeDef",
    {"detectorId": str, "ruleId": str, "ruleVersion": str},
    total=False,
)

ClientUpdateRuleVersionResponseTypeDef = TypedDict(
    "ClientUpdateRuleVersionResponseTypeDef",
    {"rule": ClientUpdateRuleVersionResponseruleTypeDef},
    total=False,
)

_RequiredClientUpdateRuleVersionRuleTypeDef = TypedDict(
    "_RequiredClientUpdateRuleVersionRuleTypeDef", {"detectorId": str}
)
_OptionalClientUpdateRuleVersionRuleTypeDef = TypedDict(
    "_OptionalClientUpdateRuleVersionRuleTypeDef", {"ruleId": str, "ruleVersion": str}, total=False
)


class ClientUpdateRuleVersionRuleTypeDef(
    _RequiredClientUpdateRuleVersionRuleTypeDef, _OptionalClientUpdateRuleVersionRuleTypeDef
):
    pass
