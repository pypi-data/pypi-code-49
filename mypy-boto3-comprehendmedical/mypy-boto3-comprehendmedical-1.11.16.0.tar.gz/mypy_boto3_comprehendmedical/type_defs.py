"""
Main interface for comprehendmedical service type definitions.

Usage::

    from mypy_boto3.comprehendmedical.type_defs import ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef

    data: ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Any, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribePhiDetectionJobResponseTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesResponseTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTypeDef",
    "ClientDetectPhiResponseEntitiesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesTypeDef",
    "ClientDetectPhiResponseTypeDef",
    "ClientInferIcd10CmResponseEntitiesAttributesTraitsTypeDef",
    "ClientInferIcd10CmResponseEntitiesAttributesTypeDef",
    "ClientInferIcd10CmResponseEntitiesICD10CMConceptsTypeDef",
    "ClientInferIcd10CmResponseEntitiesTraitsTypeDef",
    "ClientInferIcd10CmResponseEntitiesTypeDef",
    "ClientInferIcd10CmResponseTypeDef",
    "ClientInferRxNormResponseEntitiesAttributesTraitsTypeDef",
    "ClientInferRxNormResponseEntitiesAttributesTypeDef",
    "ClientInferRxNormResponseEntitiesRxNormConceptsTypeDef",
    "ClientInferRxNormResponseEntitiesTraitsTypeDef",
    "ClientInferRxNormResponseEntitiesTypeDef",
    "ClientInferRxNormResponseTypeDef",
    "ClientListEntitiesDetectionV2JobsFilterTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseTypeDef",
    "ClientListPhiDetectionJobsFilterTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListPhiDetectionJobsResponseTypeDef",
    "ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobResponseTypeDef",
    "ClientStartPhiDetectionJobInputDataConfigTypeDef",
    "ClientStartPhiDetectionJobOutputDataConfigTypeDef",
    "ClientStartPhiDetectionJobResponseTypeDef",
    "ClientStopEntitiesDetectionV2JobResponseTypeDef",
    "ClientStopPhiDetectionJobResponseTypeDef",
)

ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientDescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)

ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientDescribePhiDetectionJobResponseTypeDef = TypedDict(
    "ClientDescribePhiDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)

ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesResponseEntitiesAttributesTypeDef = TypedDict(
    "ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)

ClientDetectEntitiesResponseEntitiesTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectEntitiesResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesResponseEntitiesAttributesTypeDef],
    },
    total=False,
)

ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef],
    },
    total=False,
)

ClientDetectEntitiesResponseUnmappedAttributesTypeDef = TypedDict(
    "ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Attribute": ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)

ClientDetectEntitiesResponseTypeDef = TypedDict(
    "ClientDetectEntitiesResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef],
        "UnmappedAttributes": List[ClientDetectEntitiesResponseUnmappedAttributesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)

ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesV2ResponseEntitiesTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef],
    },
    total=False,
)

ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef],
    },
    total=False,
)

ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Attribute": ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)

ClientDetectEntitiesV2ResponseTypeDef = TypedDict(
    "ClientDetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesV2ResponseEntitiesTypeDef],
        "UnmappedAttributes": List[ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectPhiResponseEntitiesAttributesTypeDef = TypedDict(
    "ClientDetectPhiResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)

ClientDetectPhiResponseEntitiesTraitsTypeDef = TypedDict(
    "ClientDetectPhiResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)

ClientDetectPhiResponseEntitiesTypeDef = TypedDict(
    "ClientDetectPhiResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectPhiResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectPhiResponseEntitiesAttributesTypeDef],
    },
    total=False,
)

ClientDetectPhiResponseTypeDef = TypedDict(
    "ClientDetectPhiResponseTypeDef",
    {
        "Entities": List[ClientDetectPhiResponseEntitiesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientInferIcd10CmResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "ClientInferIcd10CmResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["NEGATION", "DIAGNOSIS", "SIGN", "SYMPTOM"], "Score": Any},
    total=False,
)

ClientInferIcd10CmResponseEntitiesAttributesTypeDef = TypedDict(
    "ClientInferIcd10CmResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal["ACUITY", "DIRECTION", "SYSTEM_ORGAN_SITE", "QUALITY", "QUANTITY"],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientInferIcd10CmResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)

ClientInferIcd10CmResponseEntitiesICD10CMConceptsTypeDef = TypedDict(
    "ClientInferIcd10CmResponseEntitiesICD10CMConceptsTypeDef",
    {"Description": str, "Code": str, "Score": Any},
    total=False,
)

ClientInferIcd10CmResponseEntitiesTraitsTypeDef = TypedDict(
    "ClientInferIcd10CmResponseEntitiesTraitsTypeDef",
    {"Name": Literal["NEGATION", "DIAGNOSIS", "SIGN", "SYMPTOM"], "Score": Any},
    total=False,
)

ClientInferIcd10CmResponseEntitiesTypeDef = TypedDict(
    "ClientInferIcd10CmResponseEntitiesTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": str,
        "Type": str,
        "Score": Any,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List[ClientInferIcd10CmResponseEntitiesAttributesTypeDef],
        "Traits": List[ClientInferIcd10CmResponseEntitiesTraitsTypeDef],
        "ICD10CMConcepts": List[ClientInferIcd10CmResponseEntitiesICD10CMConceptsTypeDef],
    },
    total=False,
)

ClientInferIcd10CmResponseTypeDef = TypedDict(
    "ClientInferIcd10CmResponseTypeDef",
    {
        "Entities": List[ClientInferIcd10CmResponseEntitiesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientInferRxNormResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "ClientInferRxNormResponseEntitiesAttributesTraitsTypeDef",
    {"Name": str, "Score": Any},
    total=False,
)

ClientInferRxNormResponseEntitiesAttributesTypeDef = TypedDict(
    "ClientInferRxNormResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientInferRxNormResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)

ClientInferRxNormResponseEntitiesRxNormConceptsTypeDef = TypedDict(
    "ClientInferRxNormResponseEntitiesRxNormConceptsTypeDef",
    {"Description": str, "Code": str, "Score": Any},
    total=False,
)

ClientInferRxNormResponseEntitiesTraitsTypeDef = TypedDict(
    "ClientInferRxNormResponseEntitiesTraitsTypeDef", {"Name": str, "Score": Any}, total=False
)

ClientInferRxNormResponseEntitiesTypeDef = TypedDict(
    "ClientInferRxNormResponseEntitiesTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": str,
        "Type": Literal["BRAND_NAME", "GENERIC_NAME"],
        "Score": Any,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List[ClientInferRxNormResponseEntitiesAttributesTypeDef],
        "Traits": List[ClientInferRxNormResponseEntitiesTraitsTypeDef],
        "RxNormConcepts": List[ClientInferRxNormResponseEntitiesRxNormConceptsTypeDef],
    },
    total=False,
)

ClientInferRxNormResponseTypeDef = TypedDict(
    "ClientInferRxNormResponseTypeDef",
    {
        "Entities": List[ClientInferRxNormResponseEntitiesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientListEntitiesDetectionV2JobsFilterTypeDef = TypedDict(
    "ClientListEntitiesDetectionV2JobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ClientListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListPhiDetectionJobsFilterTypeDef = TypedDict(
    "ClientListPhiDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)

ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

ClientListPhiDetectionJobsResponseTypeDef = TypedDict(
    "ClientListPhiDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
):
    pass


_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
):
    pass


ClientStartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "ClientStartEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartPhiDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobInputDataConfigTypeDef,
):
    pass


_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartPhiDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef,
):
    pass


ClientStartPhiDetectionJobResponseTypeDef = TypedDict(
    "ClientStartPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)

ClientStopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "ClientStopEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

ClientStopPhiDetectionJobResponseTypeDef = TypedDict(
    "ClientStopPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)
