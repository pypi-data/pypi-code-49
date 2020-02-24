""" Definition of the `sermos.yaml` file
"""
import re
import os
import logging
import pkg_resources
import yaml
from yaml.loader import SafeLoader
from marshmallow import Schema, fields, pre_load, EXCLUDE, INCLUDE
from marshmallow.exceptions import ValidationError
from sermos_utils.utils import normalized_pkg_name
from sermos_utils.constants import DEFAULT_YAML_NAME, DEFAULT_BASE_IMAGE_NAME

logger = logging.getLogger(__name__)


class InvalidPackagePath(Exception):
    pass


class InvalidSermosConfig(Exception):
    pass


class MissingSermosConfig(Exception):
    pass


class InvalidCustomImage(Exception):
    pass


class ExcludeUnknownSchema(Schema):
    class Meta:
        unknown = EXCLUDE


class SermosEnvironmentVarSchema(ExcludeUnknownSchema):
    name = fields.String(
        required=True,
        description="Environment variable name.",
        example="MY_ENV_VAR"
    )
    value = fields.String(
        required=True,
        description="Environment variable value.",
        example="my special value"
    )

    @pre_load
    def redact_null_values(self, item, **kwargs):
        """ Environment variables are often secrets and therefore should not
            be committed to the sermos.yaml file. Instead, they should be
            templated with ${ENV_VAR_NAME} and injected into the file only
            in memory during deployments, etc.

            The Sermos application will use the sermos.yaml file for other
            configuration pieces that do not require the environment variables,
            therefore we add 'redacted' as the value to any null values in order
            for the schema to pass the load step as being non-null.
        """
        item["value"] = item["value"]\
            if item["value"] is not None else "redacted"
        return item


class SermosImageConfigCustomImagesSchema(ExcludeUnknownSchema):
    name = fields.String(
        required=True,
        description="Name for your image. Do not include any spaces nor "
                    "special characters.",
        example="special-feature"
    )
    command = fields.String(
        required=True,
        description="The pip install command to use.",
        example="sermos-client-pkg[core,special_feature]"
    )


class SermosImageConfigBaseImageSchema(ExcludeUnknownSchema):
    command = fields.String(
        required=True,
        description="The pip install command to use.",
        example="sermos-client-pkg[core]"
    )


class SermosImageConfigSchema(ExcludeUnknownSchema):
    baseImage = fields.Nested(
        SermosImageConfigBaseImageSchema,
        required=False
    )
    customImages = fields.List(
        fields.Nested(
            SermosImageConfigCustomImagesSchema,
            required=True
        ),
        required=False,
        description="Optional list of custom images."
    )


class SermosRouteDocumentationSchema(ExcludeUnknownSchema):
    class Meta:
        # Allows us to add some python identifiers as keys to the schema
        include = {
            'in': fields.String(
                required=True,
                description="Where the parameter exists (e.g. path, header)",
                example="path"
            ),
            'type': fields.String(
                required=True,
                description="Data type of the parameter (e.g. integer, string)",
                example="string"
            )
        }

    name = fields.String(
        required=True,
        description="Name of the parameter, typically the variable name.",
        example="apikey"
    )
    description = fields.String(
        required=False,
        description="A description of the paramter.",
        example="Your API Key"
    )
    example = fields.String(
        required=False,
        description="A useful example of the parameter",
        example="8dff67fc-7cba-49da-bc75-f29437a7d723"
    )
    required = fields.Boolean(
        required=True,
        description="Boolean flag for whether the parameter is required.",
        example="True"
    )


class SermosRouteConfigSchema(ExcludeUnknownSchema):
    route = fields.String(
        required=True,
        description="The route for this endpoint. Will be appended to base."
                    "e.g. /my-route --> /api/v1/apiUrlPrefix/my-route",
        example="/my-route"
    )
    routeDocumentation = fields.List(
        fields.Nested(
            SermosRouteDocumentationSchema,
            required=True
        ),
        required=False,
        description="Optional documentation for your route (recommended)."
    )


class SermosHttpMethodsVerbConfigSchema(ExcludeUnknownSchema):
    requestSchema = fields.String(
        required=False,
        description="The Marshmallow schema defining the request payload."
    )
    responseSchema = fields.String(
        required=False,
        description="The Marshmallow schema defining the endpoint's response."
    )


class SermosHttpMethodsConfigSchema(ExcludeUnknownSchema):
    post = fields.Nested(
        SermosHttpMethodsVerbConfigSchema,
        required=False,
        description="Request/Response schemas for the `post` method."
    )
    put = fields.Nested(
        SermosHttpMethodsVerbConfigSchema,
        required=False,
        description="Request/Response schemas for the `put` method."
    )
    get = fields.Nested(
        SermosHttpMethodsVerbConfigSchema,
        required=False,
        description="Request/Response schemas for the `get` method."
    )
    delete = fields.Nested(
        SermosHttpMethodsVerbConfigSchema,
        required=False,
        description="Request/Response schemas for the `delete` method."
    )


class SermosApiConfigEndpointsSchema(ExcludeUnknownSchema):
    handler = fields.String(
        required=True,
        description="Full path to the Class that defines this API endpoint.",
        example="sermos_customer_client.api.my_api.UsefulApiClass"
    )
    apiUrlPrefix = fields.String(
        required=True,
        description="The API prefix for this route. This is appended to the "
                    "base API route (e.g. /api/v1) and is used to group "
                    "endpoints in the API documentation. For example, "
                    "apiUrlPrefix==documents will result in a base url "
                    "of /api/v1/documents/(routeConfig.route) and will "
                    "be grouped with any other routes sharing the `documents` "
                    "prefix.",
        example="documents"
    )
    routeConfig = fields.Nested(
        SermosRouteConfigSchema,
        required=True
    )
    httpMethodsConfig = fields.Nested(
        SermosHttpMethodsConfigSchema,
        required=True
    )
    event = fields.Raw(
        required=False,
        unknown=INCLUDE,
        description="Arbitrary user data, exposed to your API endpoints "
                    "through `self.event`, which is injected by Sermos.",
    )


class SermosApiConfigPrefixDescriptionsSchema(ExcludeUnknownSchema):
    prefix = fields.String(
        required=True,
        description="The url prefix itself.",
        example="custom-prefix"
    )
    description = fields.String(
        required=True,
        description="Useful description of the url prefix.",
        example="A custom prefix to logically group operations."
    )
    name = fields.String(
        required=False,
        description="The 'nice name' of the prefix. Recommended to leave this "
                    "empty; Sermos will autogenerate from the prefix.",
        example="Custom Prefx"
    )

    @pre_load
    def create_name(self, in_data, **kwargs):
        if in_data.get('name', None) is None:
            in_data['name'] = ' '.join(in_data['prefix'].split('-')).title()
        return in_data


class SermosApiDescriptionSchema(ExcludeUnknownSchema):
    version = fields.String(
        description="The API version of your application. Recommended to leave "
                    "this field empty, Sermos will use your current package "
                    "version automatically so this is dynamically versioned.",
        example="0.1.0",
        required=False
    )
    title = fields.String(
        description="Title of your API documentation.",
        example="Company's Sermos API",
        required=False
    )
    description = fields.String(
        description="A description of your Sermos API",
        example="API endpoints managing custom document processing needs.",
        required=False
    )


class SermosApiConfigSchema(ExcludeUnknownSchema):
    customImageName = fields.String(
        required=False,
        description="Specify a custom image if not using the default. For "
                    "this to function as an API, it still needs to be an "
                    "image built by Sermos. To build more than one usable "
                    "Sermos image, you can specify multiple installations "
                    "under `imageConfig.customImages`",
        example="custom-api-name"
    )
    environmentVariables = fields.List(
        fields.Nested(
            SermosEnvironmentVarSchema,
            required=True
        ),
        description="List of name/value environment variable pairs available "
                    "to all API endpoints.",
        required=False
    )
    endpoints = fields.List(
        fields.Nested(
            SermosApiConfigEndpointsSchema,
            required=True
        ),
        description="List of endpoints to expose through your API.",
        required=True
    )
    prefixDescriptions = fields.List(
        fields.Nested(
            SermosApiConfigPrefixDescriptionsSchema,
            required=True
        ),
        description="List of custom prefixes to use in your API. This is "
                    "optional, if you exclude then you can still add new "
                    "prefixes as you like, the documentation just won't have "
                    "a description.",
        required=False
    )
    apiDocumentation = fields.Nested(
        SermosApiDescriptionSchema,
        description="Information for your API documentation service.",
        required=False
    )


class SermosRegisteredTaskDetailConfigSchema(ExcludeUnknownSchema):
    handler = fields.String(
        required=True,
        description="Full path to the Method handles work / pipeline tasks.",
        example="sermos_customer_client.workers.worker_group.useful_worker"
    )
    queue = fields.String(
        required=False,
        description="The default queue on which this worker listens. If none "
                    "is provided, it will listen to the default worker queue, "
                    "which is the default behavior (and fine in most cases). "
                    "Consider a custom queue for long running tasks and/or "
                    "specialized tasks that need extra resources/GPUs/etc. "
                    "NOTE: your Sermos deployment must specifically launch "
                    "workers that listen to any custom queues, otherwise no "
                    "tasks will be picked up.",
        example="my-long-running-task-queue"
    )
    event = fields.Raw(
        required=False,
        unknown=INCLUDE,
        description="Arbitrary user data, passed through `event` arg in task."
    )


class SermosRegisteredWorkerDetailConfigSchema(ExcludeUnknownSchema):
    name = fields.String(
        required=True,
        description="Name of the worker.",
        example="useful_worker"  # TODO add validation on this so it's valid
    )
    customImageName = fields.String(
        required=False,
        description="Specify a custom image if not using the default. For "
                    "this to function as a worker, it still needs to be an "
                    "image built by Sermos. To build more than one usable "
                    "Sermos image, you can specify multiple installations "
                    "under `imageConfig.customImages`",
        example="custom-worker-name"
    )
    queue = fields.String(
        required=False,
        description="The default queue on which this worker listens. If none "
                    "is provided, it will listen to the default worker queue, "
                    "which is the default behavior (and fine in most cases). "
                    "Consider a custom queue for long running tasks and/or "
                    "specialized tasks that need extra resources/GPUs/etc. "
                    "NOTE: your Sermos deployment must specifically launch "
                    "workers that listen to any custom queues, otherwise no "
                    "tasks will be picked up.",
        example="my-long-running-task-queue"
    )
    maxTtl = fields.Integer(
        required=False,
        description="Max TTL for a task in seconds.",
        default=300,
        example=300
    )
    replicaCount = fields.Integer(
        required=False,
        description="Number of workers to have available.",
        default=1,
        example=1
    )
    # scalingMethod = fields.String(
    #     required=False,
    #     validate=OneOf(['manual', 'queue', 'cpu'])
    #     description="Method for this worker to scale up/down.",
    #     default="manual",
    #     example="manual"
    # )
    cpuRequest = fields.String(
        required=False,
        description="CPUs expected to be available for each replica.",
        default="500m",
        example="2000m"
    )
    memoryRequest = fields.String(
        required=False,
        description="Memory expected to be available for each replica.",
        default="512Mi",
        example="2Gi"
    )
    environmentVariables = fields.List(
        fields.Nested(
            SermosEnvironmentVarSchema,
            required=True
        ),
        description="List of name/value environment variable pairs available "
                    "to this specific worker.",
        required=False
    )


class SermosWorkerConfigSchema(ExcludeUnknownSchema):
    registeredTasks = fields.List(
        fields.Nested(
            SermosRegisteredTaskDetailConfigSchema,
            required=True
        ),
        required=True,
        description="List of task handlers to register for to your Sermos app."
    )
    registeredWorkers = fields.List(
        fields.Nested(
            SermosRegisteredWorkerDetailConfigSchema,
            required=True
        ),
        required=True,
        description="List of unique workers (which can handle any number of "
                    "tasks). A worker listens to a queue. By default, there is "
                    "a generic 'work' queue that everything is placed on, "
                    "therefore, the convention is to set at least one "
                    "'base worker' that listens to the default queue. All "
                    "registeredTasks will, by default, look for their work on "
                    "the default queue. You can override this behavior by "
                    "registering the task and defining a specific queue, then, "
                    "register a worker here and specify the same queue. This "
                    "allows a quick way to separate out special types of work "
                    "that may take a long time, require more resources, have "
                    "different scaling behavior, etc."
    )
    environmentVariables = fields.List(
        fields.Nested(
            SermosEnvironmentVarSchema,
            required=True
        ),
        description="List of name/value environment variable pairs available "
                    "to all workers.",
        required=False
    )


class SermosYamlSchema(ExcludeUnknownSchema):
    name = fields.String(
        required=True,
        description="A name for your Sermos deployment.",
        example="My Deployment."
    )

    imageConfig = fields.Nested(
        SermosImageConfigSchema,
        description="An optional configuration that allows for a custom "
                    "installation command for the 'baseImage' (the "
                    "application that will run by default in all API and "
                    "Worker nodes) and, again optionally, a list of "
                    "'customImages' that can be used with any registered "
                    "worker or in your API. "
                    "Sermos will default to making a base image using a "
                    "standard `pip install my-pkg` installation. "
                    "If your python package is installed by a means other than "
                    "the standard `pip install my-pkg`, you can provide the "
                    "install command under imageConfig.baseImage.command. "
                    "Currently, this will work only with `extras`, "
                    "e.g. `my-pkg[extra1,extra2]`. "
                    "The 'customImages' key is a list of name/command pairs "
                    "used to build an image. In some cases, you need more "
                    "than one image (e.g. a special build with a particularly "
                    "large image size), this allows you to list more than one "
                    "image to build. You can use these custom images in your "
                    "workers by specifying the `customImageName` in your "
                    "`registeredWorkers` list, matching the `name` provided "
                    "in `imageConfig`.",
        required=False
    )

    environmentVariables = fields.List(
        fields.Nested(
            SermosEnvironmentVarSchema,
            required=True
        ),
        description="List of name/value environment variable pairs available "
                    "to all API classes and workers.",
        required=False
    )

    apiConfig = fields.Nested(
        SermosApiConfigSchema,
        required=False,
        description="Core API configuration."
    )

    workerConfig = fields.Nested(
        SermosWorkerConfigSchema,
        required=False,
        description="Core Worker configuration."
    )


class YamlPatternConstructor():
    """ Adds a pattern resolver + constructor to PyYaml.

        Typical/deault usage is for parsing environment variables
        in a yaml file but this can be used for any pattern you provide.
    """
    def __init__(self, env_var_pattern: str = None,
                 add_constructor: bool = True):
        self.env_var_pattern = env_var_pattern
        if self.env_var_pattern is None:
            # e.g. ${VAR:default}
            self.env_var_pattern = r'\$\{([\w\-\:\/\@]+)\}'
        self.path_matcher = re.compile(self.env_var_pattern)

        if add_constructor:
            self.add_constructur()

    def _path_constructor(self, loader, node):
        """ Extract the matched value, expand env variable, and replace the match
        """
        env_var_name = re.match(self.env_var_pattern, node.value)
        try:
            env_var_name = env_var_name.group(1)
        except AttributeError:
            return None

        env_var_name_split = env_var_name.split(':')
        env_var = os.environ.get(env_var_name_split[0], None)
        if env_var is None:
            # If a default was provided (e.g. VAR:default), return that.
            # We join anything after first element because the default
            # value might be a URL or something with a colon in it
            # which would have 'split' above
            if len(env_var_name_split) > 1:
                return ":".join(env_var_name_split[1:])
            return None  # Return None if not in environ nor default
        return env_var

    def add_constructur(self):
        """ Initialize PyYaml with ability to resolve/load environment
            variables defined in a yaml template when they exist in
            the environment.

            Add to SafeLoader in addition to standard Loader
        """
        yaml.add_implicit_resolver('!env_var', self.path_matcher)
        yaml.add_implicit_resolver(
            '!env_var', self.path_matcher, Loader=SafeLoader)
        yaml.add_constructor('!env_var', self._path_constructor)
        yaml.add_constructor(
            '!env_var', self._path_constructor, Loader=SafeLoader)


def _validate_custom_image_definitions_in_yaml(sermos_config: dict):
    """ Ensures any customImageName keys line up with customImage definitions.

        Specifically, protect against typos or missing definitions in one or
        the other. We want to prevent customImage definitions that are not
        used as well, because that would simply add to build and deploy time.
    """
    workers = sermos_config.get(
        'workerConfig', {}).get('registeredWorkers', [])
    if len(workers) == 0:
        return

    api_config = sermos_config.get('apiConfig', {})
    custom_images_list =\
        sermos_config.get('imageConfig', {}).get('customImages', [])
    custom_images = [ci['name'] for ci in custom_images_list]
    custom_images.append(DEFAULT_BASE_IMAGE_NAME)  # Add the 'base' image

    # 1) Ensure there is a corresponding customImage for every registered worker
    # custom worker
    for worker in workers:
        worker_img_name = worker.get(
            'customImageName', DEFAULT_BASE_IMAGE_NAME)
        if worker_img_name not in custom_images:
            raise InvalidCustomImage("`{}` not defined in customImages."
                                     .format(worker_img_name))

    # 2) Ensure there is a corresponding registered worker OR Api Config
    # for every customImage
    for ci in custom_images:
        registered_found = False
        for worker in workers:
            if ci == worker.get('customImageName', DEFAULT_BASE_IMAGE_NAME):
                registered_found = True
                break
        if sermos_config.get('apiConfig', {}).get('customImageName') == ci:
            registered_found = True

        if not registered_found:
            raise InvalidCustomImage("`{}` not used in any registeredTask"
                                     .format(ci))


def parse_config_file(sermos_yaml: str):
    """ Parse the `sermos.yaml` file when it's been loaded.

        Arguments:
            sermos_yaml (required): String of loaded sermos.yaml file.
    """
    YamlPatternConstructor()  # Add our env variable parser
    try:
        sermos_yaml_schema = SermosYamlSchema()
        # First suss out yaml issues
        sermos_config = yaml.safe_load(sermos_yaml)
        # Then schema issues
        sermos_config = sermos_yaml_schema.load(sermos_config)
        # Ensure, when customImages are used, that the image name exists
        _validate_custom_image_definitions_in_yaml(sermos_config)
        # TODO validate entries in imageConfig to ensure it has std chars, etc
    except ValidationError as e:
        msg = "Invalid Sermos configuration due to {}"\
            .format(e.messages)
        logger.error(msg)
        raise InvalidSermosConfig(msg)
    except InvalidCustomImage as e:
        msg = "Invalid customImage configuration due to {}"\
            .format(e)
        logger.error(msg)
        raise InvalidCustomImage(msg)
    except Exception as e:
        msg = "Invalid Sermos configuration, likely due to invalid "\
            "YAML formatting ..."
        logger.exception("{} {}".format(msg, e))
        raise InvalidSermosConfig(msg)
    return sermos_config


def load_sermos_config(pkg_name: str = None,
                       sermos_yaml_filename: str = None,
                       as_dict: bool = True):
    """ Load and parse the `sermos.yaml` file. Issue usable exceptions for
        known error modes so bootstrapping can handle appropriately.

        Arguments:
            pkg_name (required): Directory name for your Python
                package. e.g. my_package_name . If none provided, will check
                environment for `SERMOS_CLIENT_PKG_NAME`. If not found,
                will exit.
            sermos_yaml_filename (optional): Relative path to find your
                `sermos.yaml` configuration file. Defaults to `sermos.yaml`
                which should be found inside your `pkg_name`
            as_dict (optional): If true (default), return the loaded sermos
                configuration as a dictionary. If false, return the loaded
                string value of the yaml file.
    """
    sermos_config = None
    sermos_yaml = None
    if sermos_yaml_filename is None:
        sermos_yaml_filename = DEFAULT_YAML_NAME

    try:
        sermos_config_path = pkg_resources.resource_filename(
            normalized_pkg_name(pkg_name), sermos_yaml_filename
        )
    except Exception as e:
        msg = "Either pkg_name ({}) or sermos_yaml_filename ({}) is "\
            "invalid ...".format(pkg_name, sermos_yaml_filename)
        logger.error("{} ... {}".format(msg, e))
        raise InvalidPackagePath(e)

    try:
        with open(sermos_config_path, 'r') as f:
            sermos_yaml = f.read()
            sermos_config = parse_config_file(sermos_yaml)
    except InvalidSermosConfig as e:
        raise
    except InvalidCustomImage as e:
        raise
    except FileNotFoundError as e:
        msg = "Sermos config file could not be found at path {} ...".format(
            sermos_config_path
        )
        raise MissingSermosConfig(msg)
    except Exception as e:
        raise e
    if as_dict:
        return sermos_config
    return yaml.safe_dump(sermos_config)
