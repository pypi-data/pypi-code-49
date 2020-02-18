"""
Main interface for lakeformation service type definitions.

Usage::

    from mypy_boto3.lakeformation.type_defs import ClientBatchGrantPermissionsEntriesPrincipalTypeDef

    data: ClientBatchGrantPermissionsEntriesPrincipalTypeDef = {...}
"""
from datetime import datetime
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
    "ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsEntriesResourceTypeDef",
    "ClientBatchGrantPermissionsEntriesTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchGrantPermissionsResponseFailuresTypeDef",
    "ClientBatchGrantPermissionsResponseTypeDef",
    "ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsEntriesResourceTypeDef",
    "ClientBatchRevokePermissionsEntriesTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    "ClientBatchRevokePermissionsResponseFailuresTypeDef",
    "ClientBatchRevokePermissionsResponseTypeDef",
    "ClientDescribeResourceResponseResourceInfoTypeDef",
    "ClientDescribeResourceResponseTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    "ClientGetDataLakeSettingsResponseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    "ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    "ClientGetEffectivePermissionsForPathResponseTypeDef",
    "ClientGrantPermissionsPrincipalTypeDef",
    "ClientGrantPermissionsResourceDataLocationTypeDef",
    "ClientGrantPermissionsResourceDatabaseTypeDef",
    "ClientGrantPermissionsResourceTableTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    "ClientGrantPermissionsResourceTypeDef",
    "ClientListPermissionsPrincipalTypeDef",
    "ClientListPermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResourceTableTypeDef",
    "ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    "ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    "ClientListPermissionsResponseTypeDef",
    "ClientListResourcesFilterConditionListTypeDef",
    "ClientListResourcesResponseResourceInfoListTypeDef",
    "ClientListResourcesResponseTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    "ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    "ClientRevokePermissionsPrincipalTypeDef",
    "ClientRevokePermissionsResourceDataLocationTypeDef",
    "ClientRevokePermissionsResourceDatabaseTypeDef",
    "ClientRevokePermissionsResourceTableTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    "ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    "ClientRevokePermissionsResourceTypeDef",
)

ClientBatchGrantPermissionsEntriesPrincipalTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef", {"Name": str}, total=False
)

ClientBatchGrantPermissionsEntriesResourceTableTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientBatchGrantPermissionsEntriesResourceTypeDef = TypedDict(
    "ClientBatchGrantPermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchGrantPermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)

_RequiredClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchGrantPermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchGrantPermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchGrantPermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchGrantPermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsEntriesResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchGrantPermissionsEntriesTypeDef(
    _RequiredClientBatchGrantPermissionsEntriesTypeDef,
    _OptionalClientBatchGrantPermissionsEntriesTypeDef,
):
    pass


ClientBatchGrantPermissionsResponseFailuresErrorTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchGrantPermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchGrantPermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientBatchGrantPermissionsResponseFailuresTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchGrantPermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchGrantPermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)

ClientBatchGrantPermissionsResponseTypeDef = TypedDict(
    "ClientBatchGrantPermissionsResponseTypeDef",
    {"Failures": List[ClientBatchGrantPermissionsResponseFailuresTypeDef]},
    total=False,
)

ClientBatchRevokePermissionsEntriesPrincipalTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef", {"Name": str}, total=False
)

ClientBatchRevokePermissionsEntriesResourceTableTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientBatchRevokePermissionsEntriesResourceTypeDef = TypedDict(
    "ClientBatchRevokePermissionsEntriesResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchRevokePermissionsEntriesResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsEntriesResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsEntriesResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsEntriesResourceDataLocationTypeDef,
    },
    total=False,
)

_RequiredClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_RequiredClientBatchRevokePermissionsEntriesTypeDef", {"Id": str}
)
_OptionalClientBatchRevokePermissionsEntriesTypeDef = TypedDict(
    "_OptionalClientBatchRevokePermissionsEntriesTypeDef",
    {
        "Principal": ClientBatchRevokePermissionsEntriesPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsEntriesResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)


class ClientBatchRevokePermissionsEntriesTypeDef(
    _RequiredClientBatchRevokePermissionsEntriesTypeDef,
    _OptionalClientBatchRevokePermissionsEntriesTypeDef,
):
    pass


ClientBatchRevokePermissionsResponseFailuresErrorTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresErrorTypeDef",
    {"ErrorCode": str, "ErrorMessage": str},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDatabaseTypeDef,
        "Table": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableTypeDef,
        "TableWithColumns": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTableWithColumnsTypeDef,
        "DataLocation": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceDataLocationTypeDef,
    },
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": ClientBatchRevokePermissionsResponseFailuresRequestEntryPrincipalTypeDef,
        "Resource": ClientBatchRevokePermissionsResponseFailuresRequestEntryResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientBatchRevokePermissionsResponseFailuresTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseFailuresTypeDef",
    {
        "RequestEntry": ClientBatchRevokePermissionsResponseFailuresRequestEntryTypeDef,
        "Error": ClientBatchRevokePermissionsResponseFailuresErrorTypeDef,
    },
    total=False,
)

ClientBatchRevokePermissionsResponseTypeDef = TypedDict(
    "ClientBatchRevokePermissionsResponseTypeDef",
    {"Failures": List[ClientBatchRevokePermissionsResponseFailuresTypeDef]},
    total=False,
)

ClientDescribeResourceResponseResourceInfoTypeDef = TypedDict(
    "ClientDescribeResourceResponseResourceInfoTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)

ClientDescribeResourceResponseTypeDef = TypedDict(
    "ClientDescribeResourceResponseTypeDef",
    {"ResourceInfo": ClientDescribeResourceResponseResourceInfoTypeDef},
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsDataLakeAdminsTypeDef
        ],
        "CreateDatabaseDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientGetDataLakeSettingsResponseDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)

ClientGetDataLakeSettingsResponseTypeDef = TypedDict(
    "ClientGetDataLakeSettingsResponseTypeDef",
    {"DataLakeSettings": ClientGetDataLakeSettingsResponseDataLakeSettingsTypeDef},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDatabaseTypeDef,
        "Table": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGetEffectivePermissionsForPathResponsePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)

ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef",
    {
        "Principal": ClientGetEffectivePermissionsForPathResponsePermissionsPrincipalTypeDef,
        "Resource": ClientGetEffectivePermissionsForPathResponsePermissionsResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientGetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "ClientGetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List[ClientGetEffectivePermissionsForPathResponsePermissionsTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientGrantPermissionsPrincipalTypeDef = TypedDict(
    "ClientGrantPermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)

ClientGrantPermissionsResourceDataLocationTypeDef = TypedDict(
    "ClientGrantPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)

ClientGrantPermissionsResourceDatabaseTypeDef = TypedDict(
    "ClientGrantPermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)

ClientGrantPermissionsResourceTableTypeDef = TypedDict(
    "ClientGrantPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)

ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientGrantPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "ClientGrantPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientGrantPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientGrantPermissionsResourceTypeDef = TypedDict(
    "ClientGrantPermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientGrantPermissionsResourceDatabaseTypeDef,
        "Table": ClientGrantPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientGrantPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientGrantPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)

ClientListPermissionsPrincipalTypeDef = TypedDict(
    "ClientListPermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)

ClientListPermissionsResourceDataLocationTypeDef = TypedDict(
    "ClientListPermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)

ClientListPermissionsResourceDatabaseTypeDef = TypedDict(
    "ClientListPermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)

ClientListPermissionsResourceTableTypeDef = TypedDict(
    "ClientListPermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)

ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientListPermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "ClientListPermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientListPermissionsResourceTypeDef = TypedDict(
    "ClientListPermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientListPermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResourceDataLocationTypeDef,
    },
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef",
    {"ResourceArn": str},
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef",
    {"Name": str},
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef",
    {"DatabaseName": str, "Name": str},
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDatabaseTypeDef,
        "Table": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientListPermissionsResponsePrincipalResourcePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)

ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef = TypedDict(
    "ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef",
    {
        "Principal": ClientListPermissionsResponsePrincipalResourcePermissionsPrincipalTypeDef,
        "Resource": ClientListPermissionsResponsePrincipalResourcePermissionsResourceTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
        "PermissionsWithGrantOption": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientListPermissionsResponseTypeDef = TypedDict(
    "ClientListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List[
            ClientListPermissionsResponsePrincipalResourcePermissionsTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)

ClientListResourcesFilterConditionListTypeDef = TypedDict(
    "ClientListResourcesFilterConditionListTypeDef",
    {
        "Field": Literal["RESOURCE_ARN", "ROLE_ARN", "LAST_MODIFIED"],
        "ComparisonOperator": Literal[
            "EQ",
            "NE",
            "LE",
            "LT",
            "GE",
            "GT",
            "CONTAINS",
            "NOT_CONTAINS",
            "BEGINS_WITH",
            "IN",
            "BETWEEN",
        ],
        "StringValueList": List[str],
    },
    total=False,
)

ClientListResourcesResponseResourceInfoListTypeDef = TypedDict(
    "ClientListResourcesResponseResourceInfoListTypeDef",
    {"ResourceArn": str, "RoleArn": str, "LastModified": datetime},
    total=False,
)

ClientListResourcesResponseTypeDef = TypedDict(
    "ClientListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List[ClientListResourcesResponseResourceInfoListTypeDef],
        "NextToken": str,
    },
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef",
    {
        "Principal": ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsPrincipalTypeDef,
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef",
    {"DataLakePrincipalIdentifier": str},
    total=False,
)

ClientPutDataLakeSettingsDataLakeSettingsTypeDef = TypedDict(
    "ClientPutDataLakeSettingsDataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": List[ClientPutDataLakeSettingsDataLakeSettingsDataLakeAdminsTypeDef],
        "CreateDatabaseDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateDatabaseDefaultPermissionsTypeDef
        ],
        "CreateTableDefaultPermissions": List[
            ClientPutDataLakeSettingsDataLakeSettingsCreateTableDefaultPermissionsTypeDef
        ],
    },
    total=False,
)

ClientRevokePermissionsPrincipalTypeDef = TypedDict(
    "ClientRevokePermissionsPrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)

ClientRevokePermissionsResourceDataLocationTypeDef = TypedDict(
    "ClientRevokePermissionsResourceDataLocationTypeDef", {"ResourceArn": str}, total=False
)

ClientRevokePermissionsResourceDatabaseTypeDef = TypedDict(
    "ClientRevokePermissionsResourceDatabaseTypeDef", {"Name": str}, total=False
)

ClientRevokePermissionsResourceTableTypeDef = TypedDict(
    "ClientRevokePermissionsResourceTableTypeDef", {"DatabaseName": str, "Name": str}, total=False
)

ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef = TypedDict(
    "ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef",
    {"ExcludedColumnNames": List[str]},
    total=False,
)

ClientRevokePermissionsResourceTableWithColumnsTypeDef = TypedDict(
    "ClientRevokePermissionsResourceTableWithColumnsTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "ColumnNames": List[str],
        "ColumnWildcard": ClientRevokePermissionsResourceTableWithColumnsColumnWildcardTypeDef,
    },
    total=False,
)

ClientRevokePermissionsResourceTypeDef = TypedDict(
    "ClientRevokePermissionsResourceTypeDef",
    {
        "Catalog": Dict[str, Any],
        "Database": ClientRevokePermissionsResourceDatabaseTypeDef,
        "Table": ClientRevokePermissionsResourceTableTypeDef,
        "TableWithColumns": ClientRevokePermissionsResourceTableWithColumnsTypeDef,
        "DataLocation": ClientRevokePermissionsResourceDataLocationTypeDef,
    },
    total=False,
)
