"""
Main interface for rds-data service client

Usage::

    import boto3
    from mypy_boto3.rds_data import RDSDataServiceClient

    session = boto3.Session()

    client: RDSDataServiceClient = boto3.client("rds-data")
    session_client: RDSDataServiceClient = session.client("rds-data")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_rds_data.client as client_scope
else:
    client_scope = object
from mypy_boto3_rds_data.type_defs import (
    ClientBatchExecuteStatementParameterSetsTypeDef,
    ClientBatchExecuteStatementResponseTypeDef,
    ClientBeginTransactionResponseTypeDef,
    ClientCommitTransactionResponseTypeDef,
    ClientExecuteSqlResponseTypeDef,
    ClientExecuteStatementParametersTypeDef,
    ClientExecuteStatementResponseTypeDef,
    ClientExecuteStatementResultSetOptionsTypeDef,
    ClientRollbackTransactionResponseTypeDef,
)


__all__ = ("RDSDataServiceClient",)


class RDSDataServiceClient:
    """
    [RDSDataService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client)
    """

    exceptions: "client_scope.Exceptions"

    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[List[ClientBatchExecuteStatementParameterSetsTypeDef]] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientBatchExecuteStatementResponseTypeDef:
        """
        [Client.batch_execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement)
        """

    def begin_transaction(
        self, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> ClientBeginTransactionResponseTypeDef:
        """
        [Client.begin_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.begin_transaction)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.can_paginate)
        """

    def commit_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientCommitTransactionResponseTypeDef:
        """
        [Client.commit_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.commit_transaction)
        """

    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None,
    ) -> ClientExecuteSqlResponseTypeDef:
        """
        [Client.execute_sql documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.execute_sql)
        """

    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List[ClientExecuteStatementParametersTypeDef] = None,
        resultSetOptions: ClientExecuteStatementResultSetOptionsTypeDef = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ClientExecuteStatementResponseTypeDef:
        """
        [Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.execute_statement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.generate_presigned_url)
        """

    def rollback_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> ClientRollbackTransactionResponseTypeDef:
        """
        [Client.rollback_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.16/reference/services/rds-data.html#RDSDataService.Client.rollback_transaction)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    ForbiddenException: Boto3ClientError
    InternalServerErrorException: Boto3ClientError
    NotFoundException: Boto3ClientError
    ServiceUnavailableError: Boto3ClientError
    StatementTimeoutException: Boto3ClientError
