"""
Custom exceptions for mpaas.
"""

class MpaasError(Exception):
    """
    Highest level mpaas Eception.
    """

    def __init__(self):
        super().__init__()
        self.message = "Undefined mpaas error"

class NoContextError(MpaasError):
    """
    Raised when the current context is 'None'
    """

    def __init__(self):
        super().__init__()
        self.message = """No project context is set. To set context,\
 try 'mpaas project use [PROJECT_NAME]'"""

class NoConfigError(MpaasError):
    """
    Raised when an action that needs a kubeconfig file cannot find it
    """

    def __init__(self):
        super().__init__()
        self.message = 'No kubeconfig file found.\n' \
                       'See https://docs.kompaas.io/#configs\n' \
                       '    https://docs.kompaas.io/#a-note-on-kubernetes-configurations'

class MissingResourceError(MpaasError):
    """
    Raised when a resource cannot be found.
    """

    def __init__(self, resource_type, resource_name, context=None):
        super().__init__()
        if context is None:
            self.message = "%s %s does not exist or cannot be found."\
                           % (resource_type, resource_name)
        else:
            self.message = "%s %s does not exist or cannot be found in %s."\
                           % (resource_type, resource_name, context)

    def __str__(self):
        return self.message

class MissingRancherConfigError(MissingResourceError):
    """
    Raised when rancher cannot find its config
    """

    def __init__(self):
        super().__init__('Rancher', 'config')


class MissingChartError(MissingResourceError):
    """
    Raised when a chart cannot be found.
    """

    def __init__(self, project_name, chart_name):
        super().__init__('Chart', chart_name, context='project ' + project_name)

class MissingConfigError(MissingResourceError):
    """
    Raised when a target config file does not exist
    """

    def __init__(self, config_name):
        super().__init__('Config', config_name)

class MissingProjectError(MissingResourceError):
    """
    Raised when a project cannot be found.
    """

    def __init__(self, project_name):
        super().__init__('Project', project_name)

class MissingValueError(MissingResourceError):
    """
    Raised when a value cannot be found in a yaml file.
    """

    def __init__(self, value_name, chart_name):
        super().__init__('Value', value_name, context='chart ' + chart_name)

class MissingDirectoryError(MissingResourceError):
    """
    Raised when target directory does not exist
    """

    def __init__(self, directory):
        super().__init__('Directory', directory)

class MissingLinksError(MissingResourceError):
    """
    Raised when the links.yaml file is empty or does not exist
    """

    def __init__(self, project):
        super().__init__('Links', 'file', context=project)

class MissingTemplateError(MissingResourceError):
    """
    Raised when target template does not exist at target location
    """

    def __init__(self, template_name):
        super().__init__('Template', template_name)


class EmptyDirectoryError(MpaasError):
    """
    Raised when a directory that is supposed to contain data is empty
    """

    def __init__(self, directory):
        super().__init__()
        self.message = "%s directory is empty." % directory

class EmptyConfigDirectoryError(MpaasError):
    """
    Raised when the config directory is empty
    """

    def __init__(self):
        super().__init__()
        self.message = "The config directory is empty"

class EmptyLinksError(MpaasError):
    """
    Raised when the links.yaml file in a project is empty.
    """

    def __init__(self, project):
        super().__init__()
        self.message = "No links found in %s project" % project

class RequirementsFileError(MpaasError):
    """
    Raised when the requirements.yaml file in a chart is not fill a required.
    """

    def __init__(self, chart_name):
        super().__init__()
        self.message = "Bad content found in requirements.yaml for %s chart" % chart_name

class ResourceExistsError(MpaasError):
    """
    Raised when a resource already exists.
    """

    def __init__(self, resource_type, resource_name, context=None):
        super().__init__()
        if context is None:
            self.message = "%s %s already exists." % (resource_type, resource_name)
        else:
            self.message = "%s %s already exists in %s." % (resource_type, resource_name, context)

class ChartExistsError(ResourceExistsError):
    """
    Raised when a chart already exists.
    """

    def __init__(self, project_name, chart_name):
        super().__init__('Chart', chart_name, context='project ' + project_name)

class ConfigExistsError(ResourceExistsError):
    """
    Raised when a config with the same name already exists.
    """

    def __init__(self, config_name):
        super().__init__('Config', config_name)

class ProjectExistsError(ResourceExistsError):
    """
    Raised when a project already exists.
    """

    def __init__(self, project_name):
        super().__init__('Project', project_name)

class LinkExistsError(ResourceExistsError):
    """
    Raised when a link already exists
    """

    def __init__(self, project_name):
        super().__init__('This link', '', context='project ' + project_name)

class TemplateFetchError(MpaasError):
    """
    Raised when a template could not be fetched from a remote chart museum
    """

    def __init__(self, template_name):
        super().__init__()
        self.message = "Template %s could not be fetched" % template_name

class RenderError(MpaasError):
    """
    Raised when here is an error in the helm templating process
    """

    def __init__(self, resource):
        super().__init__()
        self.message = "%s could not be rendered by helm." % resource

class DeployError(MpaasError):
    """
    Raised when here is an error in the kubectl deploying process
    """

    def __init__(self, resource):
        super().__init__()
        self.message = "%s could not be deployed by kubectl." % resource

class NoValidTemplateError(MpaasError):
    """
    Raised when no valid templates could be found in target directory
    """

    def __init__(self, directory):
        super().__init__()
        self.message = "Directory '%s' contains no valid helm template." % directory
