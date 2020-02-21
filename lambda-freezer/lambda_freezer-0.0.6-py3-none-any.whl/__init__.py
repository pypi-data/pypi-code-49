from collections import namedtuple
import os
import subprocess
import re
import boto3
import json

DEFAULT_ALIAS_NAME = "latest"
STAGE_VARIABLE_ALIAS = "lambdaAlias"
INTEGRATION_URI_APPENDER = ":${{stageVariables.{0}}}".format(STAGE_VARIABLE_ALIAS)
_INTEGRATION = namedtuple(
    "INTEGRATION", [
        "rest_api_id",
        "resource_id",
        "http_method",
        "path"
    ]
)
_APIFNS = namedtuple(
    "APIFNS", [
        "rest_api_id",
        "resource_id",
        "http_method",
        "uri",
        "path",
        "function_name",
        "source_arn",
        "aliases"
    ]
)
STATEMENT_ID = "f6803b46-df32-4504-8c40-567a0390f549"
CLIENT_GATEWAY = boto3.client('apigateway')
CLIENT_LAMBDA = boto3.client('lambda')
CLIENT_CLOUDFORMATION = boto3.client('cloudformation')
SERVICE_FROM_PATH_PATTERN = re.compile(r"^(?:\\.|[^/\\])*/((?:\\.|[^/\\])*)/")

class Mapper:
    """
    This is a class that groups a collection of helper functions that
    help in gathering information of lambda functions that are integrated
    with an AWS api gateway
    """

    @staticmethod
    def _map_fn(rest_api_id, region, http_method, path, uri):
        """
        Extracts the underlying (lambda) function name and
        source arn of a particular resource attached to an api gateway.
        """
        account_id = boto3.client('sts').get_caller_identity().get('Account')
        regex_template = ".*/arn:aws:lambda:{0}:{1}:function:(.*)/invocations$"
        source_arn_template = "arn:aws:execute-api:{0}:{1}:{2}/*/{3}{4}"
        source_arn = source_arn_template.format(
            region,
            account_id,
            rest_api_id,
            http_method,
            path
        )
        regex = regex_template.format(region, account_id)

        function_name = re.search(regex, uri).group(1)
        if function_name[-len(INTEGRATION_URI_APPENDER):] == INTEGRATION_URI_APPENDER:
            function_name = function_name[:-len(INTEGRATION_URI_APPENDER)]

        return function_name, source_arn

    @staticmethod
    def _map_aliases(func_name):
        """
        Returns all aliases associated with a given (lambda) function.
        """
        list_aliases_res = CLIENT_LAMBDA.list_aliases(
            FunctionName=func_name,
        )
        aliases = list_aliases_res["Aliases"]
        return aliases

    @staticmethod
    def _get_integrations(rest_api_id):
        """
        Gathers all resources for a given api gateway and returns
        its' integrations.
        In particular, the `resource id`, `resource method`
        and `resource path`
        """
        # fetch api resources
        resources = CLIENT_GATEWAY.get_resources(
            restApiId=rest_api_id,
        )
        integrations = []
        # traverse all the resources
        for resource in resources['items']:
            # we are only interested in "resource methods"
            if "resourceMethods" not in resource.keys():
                continue
            resource_methods = resource["resourceMethods"].keys()
            for resource_method in resource_methods:
                integrations.append(
                    _INTEGRATION(
                        rest_api_id,
                        resource["id"],
                        resource_method,
                        resource["path"]))
        return integrations

    @staticmethod
    def _assemble(region, integrations):
        """
        Helper function tha combines data.
        """
        apifns = []
        for integration in integrations:
            get_integration_res = CLIENT_GATEWAY.get_integration(
                restApiId=integration.rest_api_id,
                resourceId=integration.resource_id,
                httpMethod=integration.http_method
            )
            # we are only interested at AWS_PROXY integrations as those
            # are integrations that are created by serverless framework
            if get_integration_res["type"] != "AWS_PROXY":
                continue

            function_name, source_arn = Mapper._map_fn(
                integration.rest_api_id,
                region,
                integration.http_method,
                integration.path,
                get_integration_res["uri"]
            )

            aliases = Mapper._map_aliases(function_name)
            apifns.append(
                _APIFNS(
                    integration.rest_api_id,
                    integration.resource_id,
                    integration.http_method,
                    get_integration_res["uri"],
                    integration.path,
                    function_name,
                    source_arn,
                    aliases
                )
            )
        return apifns

    @staticmethod
    def run(rest_api_id, region):
        """
        Gets the integrations of a given api gateway and appends
        information to them (_assemble)
        """
        integrations = Mapper._get_integrations(rest_api_id)
        apifns = Mapper._assemble(region, integrations)
        return apifns

def _add_permission(api_fn, stage_name):
    """
    Add `lambda:InvokeFunction` permission to an (aliased) lambda function
    that is wired to an api gateway.
    """
    try:
        CLIENT_LAMBDA.add_permission(
            FunctionName="{0}:{1}".format(api_fn.function_name, stage_name),
            StatementId=STATEMENT_ID,
            Action='lambda:InvokeFunction',
            Principal='apigateway.amazonaws.com',
            SourceArn=api_fn.source_arn,
        )
    except CLIENT_LAMBDA.exceptions.ResourceConflictException as err:
        error_msg = {
            "exception": "CLIENT_LAMBDA.exceptions.ResourceConflictException",
            "fn": api_fn,
            "error": err
        }
        print(json.dumps(error_msg, indent=4))

def _default_alias_is_added(fn_aliases):
    """
    Checks if the `default alias` is part of a list of aliases
    """
    for alias in fn_aliases:
        if alias["Name"] == DEFAULT_ALIAS_NAME:
            return True
    return False

def _create_alias(function_name, alias_name, function_version):
    """
    Creates an alias and points to a specific version of a 
    (lambda) function.
    """
    CLIENT_LAMBDA.create_alias(
        FunctionName=function_name,
        Name=alias_name,
        FunctionVersion=function_version
    )

def _integration_uri_is_already_updated(uri):
    """
    A typical uri would look like this:
    arn:aws:apigateway:{0}:lambda:path/2015-03-31/functions/arn:aws:lambda:{0}:{1}:function:{2}/invocations
    {0}: region
    {1}: account id
    {2}: function name

    Example of a function name:
        helloWorld

    We consider a uri integration to be `updated` when the function name is such:
        helloWorld:${stageVariables.lambdaAlias}

    This ensures that only a specific alias (therefore a specific locked version) can be called for
    a (lambda) function.
    """
    invocation_str = "/invocations"
    uri_minus_invocation_str = uri[:-len(invocation_str)]
    is_already_updated = uri_minus_invocation_str[-len(INTEGRATION_URI_APPENDER):] == INTEGRATION_URI_APPENDER
    return is_already_updated, invocation_str, uri_minus_invocation_str

def _get_service_from_path(path):
    """
    Resource paths are general simple urls such as:
        /generalcalc/getHouseCostByCity
        /subscription/signUp
        /subscription/subscribeBasicPlan
        /country/countries
        /subscription/login
        /subscription/confirmSignUp
        /country/countries/{cca2}
    This simply extract the first piece of string that is between / /
    """
    return re.search(SERVICE_FROM_PATH_PATTERN, path).group(1)

def _tag_documentation_exists(rest_api_id, path, http_method):
    """
    Checks if a specific resource path/method has a `tag` documentation.
    """
    get_documentation_parts_res = CLIENT_GATEWAY.get_documentation_parts(
        restApiId=rest_api_id,
        type="METHOD",
        path=path,
    )
    if not get_documentation_parts_res["items"]:
        return False
    for item in get_documentation_parts_res["items"]:
        if item["location"]["method"] == http_method:
            return True
    return False

def _get_cloudformation_export(exportName):
    exports = CLIENT_CLOUDFORMATION.list_exports()
    if 'Exports' not in exports.keys():
        exit()
    for export in exports['Exports']:
        if export['Name'] == exportName:
            return export['Value']
    exit()

def get_deployed_stages(rest_api_id):
    """
    Returns all the stages that are deployed
    """
    stages = []
    get_stages_res = CLIENT_GATEWAY.get_stages(
        restApiId=rest_api_id,
    )
    for get_stage_res in get_stages_res["item"]:
        stages.append(get_stage_res["stageName"])
    return stages

def create_alias_default(api_fns):
    """
    Creates the so called `default alias` which is just
    an alias that points to the latest version of
    (lambda) function(s).
    """
    def create(function_name):
        return _create_alias(function_name, DEFAULT_ALIAS_NAME, "$LATEST")

    for api_fn in api_fns:
        aliases = api_fn.aliases
        function_name = api_fn.function_name
        if not aliases:
            create(function_name)
        else:
            default_is_added = _default_alias_is_added(aliases)
            if not default_is_added:
                create(function_name)

def update_integration_uri(api_fns):
    """
    For every (lambda) functions that are integrated with
    an api gateway - updated the uri integration such that
    the api gateway can only call a specific version of
    those (lambda) functions through an alias.
    """
    for api_fn in api_fns:
        is_already_updated, invocation_str, uri_minus_invocation_str = _integration_uri_is_already_updated(api_fn.uri)
        if not is_already_updated:
            new_uri = "{0}{1}{2}".format(
                uri_minus_invocation_str,
                INTEGRATION_URI_APPENDER,
                invocation_str
            )
            CLIENT_GATEWAY.update_integration(
                restApiId=api_fn.rest_api_id,
                resourceId=api_fn.resource_id,
                httpMethod=api_fn.http_method,
                patchOperations=[
                    {
                        'op': 'replace',
                        'path': '/uri',
                        'value': new_uri,
                    },
                ]
            )
            _add_permission(api_fn, DEFAULT_ALIAS_NAME)

def create_domain_mapping_default(rest_api_id, domain_name):
    """
    Creates the domain name mapping for the default stage.
    """
    def create():
        CLIENT_GATEWAY.create_base_path_mapping(
            domainName=domain_name,
            basePath=DEFAULT_ALIAS_NAME,
            restApiId=rest_api_id,
            stage=DEFAULT_ALIAS_NAME
        )

    get_base_path_mappings_res = CLIENT_GATEWAY.get_base_path_mappings(
        domainName=domain_name,
    )
    mappings = get_base_path_mappings_res['items']

    if not mappings:
        create()
    else:
        already_mapped = False
        for mapping in mappings:
            if mapping["basePath"] == DEFAULT_ALIAS_NAME and mapping["stage"] == DEFAULT_ALIAS_NAME:
                already_mapped = True

        if not already_mapped:
            create()

def default_stage_contains_staged_variable(rest_api_id):
    """
    Checks if the default stage contains the `stage variable alias`.
    """
    get_stage_res = CLIENT_GATEWAY.get_stage(
        restApiId=rest_api_id,
        stageName=DEFAULT_ALIAS_NAME
    )
    if "variables" not in get_stage_res.keys():
        return False

    stage_variables = get_stage_res["variables"]
    if STAGE_VARIABLE_ALIAS not in stage_variables.keys():
        return False

    if stage_variables[STAGE_VARIABLE_ALIAS] != DEFAULT_ALIAS_NAME:
        return False
    return True

def create_tag_documentation(rest_api_id, api_fns):
    """
    Creates tag documentation for a given list of functions.
    """
    for api_fn in api_fns:
        path = api_fn.path
        http_method = api_fn.http_method
        already_exists = _tag_documentation_exists(rest_api_id, path, http_method)
        if not already_exists:
            service_name = _get_service_from_path(path)
            tag = {
                "tags": [
                    service_name
                ]
            }
            CLIENT_GATEWAY.create_documentation_part(
                restApiId=rest_api_id,
                location={
                    "type": "METHOD",
                    "path": path,
                    "method": http_method
                },
                properties=json.dumps(tag),
            )

def run_after_default_deployment(rest_api_id, region, domain_name=None):
    """
    Typically what you would need to run after a
    `serverless deploy` deployment.
    This ensures that every function integrations' are such that
    the api gateway can only call a specific version of any
    lambda functions via an alias, using a stage variable.
    """
    api_fns = Mapper.run(rest_api_id, region)
    create_alias_default(api_fns)
    update_integration_uri(api_fns)

    if domain_name is not None:
        create_domain_mapping_default(rest_api_id, domain_name)
    create_tag_documentation(rest_api_id, api_fns)

    contains_stage_var = default_stage_contains_staged_variable(rest_api_id)
    if not contains_stage_var:
        print('''
PLEASE ADD THE FOLLOWING STAGE VARIABLE TO [STAGE: {0}]:
    {1} : {2}        
'''.format(DEFAULT_ALIAS_NAME, STAGE_VARIABLE_ALIAS, DEFAULT_ALIAS_NAME))

def freeze_functions(api_fns, stage_name):
    """
    Creates an alias (that's the string for `stage_name`)
    for a given list of functions.
    """
    for api_fn in api_fns:
        function_name = api_fn.function_name
        publish_version_res = CLIENT_LAMBDA.publish_version(FunctionName=function_name)
        CLIENT_LAMBDA.create_alias(
            FunctionName=function_name,
            Name=stage_name,
            FunctionVersion=publish_version_res["Version"]
        )
        _add_permission(api_fn, stage_name)

def deploy(rest_api_id, region, version, stage_description, domain_name=None):
    """
    Deploys a stage to an api gateway.
    The definition of `deploy` here is:
        - take all resources of an api gateway (those are lambda functions at the core)
        - the integration of those lambda functions are assumed to have been modified
          such that only specific version
        - `freeze` those functions and create an alias that points to those frozen versions
        - creates a new stage under the api gateway and ensure that staged version calls only
          those previously frozen functions
    """
    # ensure version follows semantic versioning standard
    if not re.match("\d+\.\d+\.\d+", version):
        exit("{0} DOES NOT FOLLOW SEMANTIC VERSIONING. FOLLOW SEMANTIC VERSIONING!".format(version))

    # ensure that version was not already deployed
    stage_name = version.replace(".", "-")
    stages = get_deployed_stages(rest_api_id)
    if stage_name in stages:
        exit("YOU ALREADY DEPLOYED {0}".format(version))

    # extracted functions' info and freeze them
    api_fns = Mapper.run(rest_api_id, region)
    freeze_functions(api_fns, stage_name)

    # deploy frozen functions
    CLIENT_GATEWAY.create_deployment(
        restApiId=rest_api_id,
        stageName=stage_name,
        stageDescription=stage_description,
        description=stage_description,
        variables={
            "{0}".format(STAGE_VARIABLE_ALIAS): stage_name
        },
    )

    # map to domain
    if domain_name is not None:
        CLIENT_GATEWAY.create_base_path_mapping(
            domainName=domain_name,
            basePath=stage_name.replace("-", "."),
            restApiId=rest_api_id,
            stage=stage_name
        )

def simple_push(cloudformation_rest_api_id_export_name, region, service_dir_relative_path, domain_name=None):
    APILIB_REST_API_ID = _get_cloudformation_export(cloudformation_rest_api_id_export_name)

    CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

    os.chdir(service_dir_relative_path)
    subprocess.run(["serverless", "deploy"])
    run_after_default_deployment(APILIB_REST_API_ID, region, domain_name)