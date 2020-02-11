"""
Main interface for cloudsearch service client

Usage::

    import boto3
    from mypy_boto3.cloudsearch import CloudSearchClient

    session = boto3.Session()

    client: CloudSearchClient = boto3.client("cloudsearch")
    session_client: CloudSearchClient = session.client("cloudsearch")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from typing import Any, Dict, List, TYPE_CHECKING
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
if TYPE_CHECKING:
    import mypy_boto3_cloudsearch.client as client_scope
else:
    client_scope = object
from mypy_boto3_cloudsearch.type_defs import (
    ClientBuildSuggestersResponseTypeDef,
    ClientCreateDomainResponseTypeDef,
    ClientDefineAnalysisSchemeAnalysisSchemeTypeDef,
    ClientDefineAnalysisSchemeResponseTypeDef,
    ClientDefineExpressionExpressionTypeDef,
    ClientDefineExpressionResponseTypeDef,
    ClientDefineIndexFieldIndexFieldTypeDef,
    ClientDefineIndexFieldResponseTypeDef,
    ClientDefineSuggesterResponseTypeDef,
    ClientDefineSuggesterSuggesterTypeDef,
    ClientDeleteAnalysisSchemeResponseTypeDef,
    ClientDeleteDomainResponseTypeDef,
    ClientDeleteExpressionResponseTypeDef,
    ClientDeleteIndexFieldResponseTypeDef,
    ClientDeleteSuggesterResponseTypeDef,
    ClientDescribeAnalysisSchemesResponseTypeDef,
    ClientDescribeAvailabilityOptionsResponseTypeDef,
    ClientDescribeDomainEndpointOptionsResponseTypeDef,
    ClientDescribeDomainsResponseTypeDef,
    ClientDescribeExpressionsResponseTypeDef,
    ClientDescribeIndexFieldsResponseTypeDef,
    ClientDescribeScalingParametersResponseTypeDef,
    ClientDescribeServiceAccessPoliciesResponseTypeDef,
    ClientDescribeSuggestersResponseTypeDef,
    ClientIndexDocumentsResponseTypeDef,
    ClientListDomainNamesResponseTypeDef,
    ClientUpdateAvailabilityOptionsResponseTypeDef,
    ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef,
    ClientUpdateDomainEndpointOptionsResponseTypeDef,
    ClientUpdateScalingParametersResponseTypeDef,
    ClientUpdateScalingParametersScalingParametersTypeDef,
    ClientUpdateServiceAccessPoliciesResponseTypeDef,
)


__all__ = ("CloudSearchClient",)


class CloudSearchClient:
    """
    [CloudSearch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client)
    """

    exceptions: "client_scope.Exceptions"

    def build_suggesters(self, DomainName: str) -> ClientBuildSuggestersResponseTypeDef:
        """
        [Client.build_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.build_suggesters)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.can_paginate)
        """

    def create_domain(self, DomainName: str) -> ClientCreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.create_domain)
        """

    def define_analysis_scheme(
        self, DomainName: str, AnalysisScheme: ClientDefineAnalysisSchemeAnalysisSchemeTypeDef
    ) -> ClientDefineAnalysisSchemeResponseTypeDef:
        """
        [Client.define_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.define_analysis_scheme)
        """

    def define_expression(
        self, DomainName: str, Expression: ClientDefineExpressionExpressionTypeDef
    ) -> ClientDefineExpressionResponseTypeDef:
        """
        [Client.define_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.define_expression)
        """

    def define_index_field(
        self, DomainName: str, IndexField: ClientDefineIndexFieldIndexFieldTypeDef
    ) -> ClientDefineIndexFieldResponseTypeDef:
        """
        [Client.define_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.define_index_field)
        """

    def define_suggester(
        self, DomainName: str, Suggester: ClientDefineSuggesterSuggesterTypeDef
    ) -> ClientDefineSuggesterResponseTypeDef:
        """
        [Client.define_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.define_suggester)
        """

    def delete_analysis_scheme(
        self, DomainName: str, AnalysisSchemeName: str
    ) -> ClientDeleteAnalysisSchemeResponseTypeDef:
        """
        [Client.delete_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.delete_analysis_scheme)
        """

    def delete_domain(self, DomainName: str) -> ClientDeleteDomainResponseTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.delete_domain)
        """

    def delete_expression(
        self, DomainName: str, ExpressionName: str
    ) -> ClientDeleteExpressionResponseTypeDef:
        """
        [Client.delete_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.delete_expression)
        """

    def delete_index_field(
        self, DomainName: str, IndexFieldName: str
    ) -> ClientDeleteIndexFieldResponseTypeDef:
        """
        [Client.delete_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.delete_index_field)
        """

    def delete_suggester(
        self, DomainName: str, SuggesterName: str
    ) -> ClientDeleteSuggesterResponseTypeDef:
        """
        [Client.delete_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.delete_suggester)
        """

    def describe_analysis_schemes(
        self, DomainName: str, AnalysisSchemeNames: List[str] = None, Deployed: bool = None
    ) -> ClientDescribeAnalysisSchemesResponseTypeDef:
        """
        [Client.describe_analysis_schemes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_analysis_schemes)
        """

    def describe_availability_options(
        self, DomainName: str, Deployed: bool = None
    ) -> ClientDescribeAvailabilityOptionsResponseTypeDef:
        """
        [Client.describe_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_availability_options)
        """

    def describe_domain_endpoint_options(
        self, DomainName: str, Deployed: bool = None
    ) -> ClientDescribeDomainEndpointOptionsResponseTypeDef:
        """
        [Client.describe_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_domain_endpoint_options)
        """

    def describe_domains(
        self, DomainNames: List[str] = None
    ) -> ClientDescribeDomainsResponseTypeDef:
        """
        [Client.describe_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_domains)
        """

    def describe_expressions(
        self, DomainName: str, ExpressionNames: List[str] = None, Deployed: bool = None
    ) -> ClientDescribeExpressionsResponseTypeDef:
        """
        [Client.describe_expressions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_expressions)
        """

    def describe_index_fields(
        self, DomainName: str, FieldNames: List[str] = None, Deployed: bool = None
    ) -> ClientDescribeIndexFieldsResponseTypeDef:
        """
        [Client.describe_index_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_index_fields)
        """

    def describe_scaling_parameters(
        self, DomainName: str
    ) -> ClientDescribeScalingParametersResponseTypeDef:
        """
        [Client.describe_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_scaling_parameters)
        """

    def describe_service_access_policies(
        self, DomainName: str, Deployed: bool = None
    ) -> ClientDescribeServiceAccessPoliciesResponseTypeDef:
        """
        [Client.describe_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_service_access_policies)
        """

    def describe_suggesters(
        self, DomainName: str, SuggesterNames: List[str] = None, Deployed: bool = None
    ) -> ClientDescribeSuggestersResponseTypeDef:
        """
        [Client.describe_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.describe_suggesters)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.generate_presigned_url)
        """

    def index_documents(self, DomainName: str) -> ClientIndexDocumentsResponseTypeDef:
        """
        [Client.index_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.index_documents)
        """

    def list_domain_names(self, *args: Any, **kwargs: Any) -> ClientListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.list_domain_names)
        """

    def update_availability_options(
        self, DomainName: str, MultiAZ: bool
    ) -> ClientUpdateAvailabilityOptionsResponseTypeDef:
        """
        [Client.update_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.update_availability_options)
        """

    def update_domain_endpoint_options(
        self,
        DomainName: str,
        DomainEndpointOptions: ClientUpdateDomainEndpointOptionsDomainEndpointOptionsTypeDef,
    ) -> ClientUpdateDomainEndpointOptionsResponseTypeDef:
        """
        [Client.update_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.update_domain_endpoint_options)
        """

    def update_scaling_parameters(
        self,
        DomainName: str,
        ScalingParameters: ClientUpdateScalingParametersScalingParametersTypeDef,
    ) -> ClientUpdateScalingParametersResponseTypeDef:
        """
        [Client.update_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.update_scaling_parameters)
        """

    def update_service_access_policies(
        self, DomainName: str, AccessPolicies: str
    ) -> ClientUpdateServiceAccessPoliciesResponseTypeDef:
        """
        [Client.update_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.11.15/reference/services/cloudsearch.html#CloudSearch.Client.update_service_access_policies)
        """


class Exceptions:
    BaseException: Boto3ClientError
    ClientError: Boto3ClientError
    DisabledOperationException: Boto3ClientError
    InternalException: Boto3ClientError
    InvalidTypeException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
