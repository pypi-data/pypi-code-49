from alfa_sdk.common.exceptions import AlfaConfigError
from alfa_sdk.common.session import Session, parse_response
from alfa_sdk.resources.meta import MetaUnit
from alfa_cli.common.exceptions import AlfaCliError
from alfa_cli.common.utils import load_or_parse
from alfa_cli.lib.runner import LocalRunner


def initialize_runners(obj, algorithm_id, environment_name):
    """
    Initializes the runners (based upon the specification in the alfa.yml file) that
    are used to execute the training locally. Returns one runner per function that needs
    to be executed.
    """
    search_runner = None
    try:
        search_runner = LocalRunner(obj, algorithm_id, environment_name, "search")
    except AlfaConfigError:
        pass

    score_runner = None
    try:
        score_runner = LocalRunner(obj, algorithm_id, environment_name, "score")
    except AlfaConfigError:
        pass

    build_runner = None
    build_runner = LocalRunner(obj, algorithm_id, environment_name, "build")

    return {
        "search": search_runner,
        "score": score_runner,
        "build": build_runner,
    }


def fetch_build_configuration(build_configuration=None, algorithm_environment_id=None, tag=None):
    """
    Loads the build configuration if it has been provided; otherwise, it will fetch the build
    configuration from ALFA. Returns the build configuration with tag and algorithmEnvironmentId
    included in it.
    """
    if build_configuration:
        build_configuration = load_or_parse(build_configuration)
    else:
        if not algorithm_environment_id or not tag:
            raise AlfaCliError(message="Failed to fetch build configuration.")

        meta_unit = MetaUnit(algorithm_environment_id, tag)
        if not meta_unit:
            raise AlfaCliError(message="Failed to fetch build configuration.")

        build_configurations = meta_unit.build_configurations
        if not build_configurations or len(build_configurations) < 1:
            raise AlfaCliError(message="Failed to fetch build configuration.")

        build_configuration = build_configurations[0]

    if not "algorithmEnvironmentId" in build_configuration:
        build_configuration["algorithmEnvironmentId"] = algorithm_environment_id
    if not "tag" in build_configuration:
        if tag is not None:
            build_configuration["tag"] = tag
        if "unitId" in build_configuration:
            build_configuration["tag"] = build_configuration["unitId"].split(":")[-1]

    return build_configuration


def fetch_data(data, build_configuration):
    """
    Loads the data if it is provided by the client. Otherwise, tries to fetch it from
    the data request that is specified in the build configuration.
    """
    if data:
        return load_or_parse(data)

    data_request = build_configuration.get("dataRequest")
    if not data_request:
        raise AlfaCliError(message="Failed to fetch data.")

    session = Session()
    return parse_response(
        session.http_session.request(
            data_request.get("method"),
            data_request.get("url"),
            params=data_request.get("qs"),
            json=data_request.get("body"),
        )
    )


def validate_build_configuration(build_configuration):
    """
    Validates whether the required fields are specified in the build configuration.
    """
    required_fields = ["tag", "algorithmEnvironmentId"]
    if not all(field in build_configuration.keys() and build_configuration[field] is not None for field in required_fields):
        raise AlfaCliError(message="Invalid build configuration.")
