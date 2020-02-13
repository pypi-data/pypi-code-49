##############################################################################
# CloudMage : Git Config Parser Class
#=============================================================================
# CloudMage Git Config Object Utility/Library
#   - Search a provided directory path location for a .git/config directory.
#   - If config found, extract the repository URL, and git provider and return 
# Author: Richard Nason rnason@cloudmage.io
# Project Start: 2/12/2020
# License: GNU GPLv3
##############################################################################

###############
# Imports:    #
###############

# Import Base Python Modules
import os, sys, inspect


#####################
# Class Definition: #
#####################
class GitConfigParser(object):
    """CloudMage Git Config Parser Class
    This class is designed to search a provided file path location for a .git/config directory/file. If found, 
    the config file will be parsed, and attempt to extract the repository URL, and the git provider.
    If those properties are properly extracted, then the respective class properties are set, and the object is returned.
    """

    def __init__(self, path, verbose=False, log=None):
        '''GitConfigParser Class Constructor'''

        ##### Class Public Attributes ######
        self.path = path
        self.verbose = verbose
        self._log = log
        self._log_context = "CLS->GitConfigParser"

        ##### Class Base Variables to set and hold values for respective method properties. ######
        self._url = None
        self._provider = None
        self.user = None

        ##### Init and populate the return the requested object instance ######
        self.url = self.path
        self.provider = self._url


    ############################################
    # Class Logger:                            #
    ############################################
    def log(self, log_msg, log_type, log_id):
        """This class method provides the logging for this class. If the class caller
        instantiates the object with the verbose setting set to true, then the class 
        will log to stdout/stderr."""

        # Function variable assignments
        log_msg_caller = "{}.{}".format(self._log_context, log_id)
        # Set the message type offset, debug=3, info=4, warning=1, error=3
        log_msg_offset = 3
        log_msg_offset = 4 if log_type.lower() == 'info' else log_msg_offset
        log_msg_offset = 1 if log_type.lower() == 'warning' else log_msg_offset

        # Push the log to either the provided log or to stdout/stderr
        if self._log is not None:
            # Set the log message prefix
            log_message = "{}:   {}".format(log_msg_caller, log_msg)
            if log_type.lower() == 'error':
                self._log.error(log_message)
            elif log_type.lower() == 'warning':
                self._log.warning(log_message)
            elif log_type.lower() == 'info':
                self._log.info(log_message)
            else:
                self._log.debug(log_message)
        else:
            log_message = "{}{}{}:   {}".format(log_type.upper(), " " * log_msg_offset, log_msg_caller, log_msg)
            if log_type.lower() == 'error':
                if self.verbose:
                    print(log_message, file=sys.stderr)
            else:
                if self.verbose:
                    print(log_message, file=sys.stdout)


    ################################################
    # Search Directory Path and Search for Git URL #
    ################################################
    @property
    def url(self):
        """Class Getter method for the url property. This property will return the repository URL if a value was found and set by the property setter method."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Request for url property received.", 'info', self.__id)
        return self._url

    @url.setter
    def url(self, config_path):
        """Class Setter method for the object url property. This property will search the provided path and attempt to extact the a git repository URL if a .git/config file can be found in the provided path."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Call to set value for url property.", 'info', self.__id)
        try:
            # Search for a .git directory in the provided search path, and if found parse to get the repository URL.
            git_config_path = os.path.join(config_path, '.git/config')
            self.log("Config search path set to: {}".format(git_config_path), 'debug', self.__id)

            if os.path.exists(git_config_path):
                self.log(".git/config file found in provided search path... Searching for repository url...", 'debug', self.__id)
                try:
                    with open(git_config_path) as f:
                        for count, line in enumerate(f):
                            # For each line in the config, if url is found in the line, then attempt to parse it.
                            if 'url' in line:
                                k, v = line.partition("=")[::2]
                                self.log("URL string match found in the target git config directory, parsing URL string...", 'debug', self.__id)
                                git_config_url = v.strip()
                                if git_config_url.startswith(('http', 'https', 'git')) and git_config_url.endswith('.git'):
                                    self._url = git_config_url
                                    self.log("URL match verified... setting url to value: {}".format(self._url), 'debug', self.__id)
                                    break
                                else:
                                    self.log("Matched URL is not in the proper format, skipping match...", 'error', self.__id)
                                    self.log("{}".format(git_config_url), 'error', self.__id)
                                    continue
                except Exception as e:
                    request_exc_msg = "An Exception occurred during method {} exectution: {} in line: {}".format(
                        self.__id,
                        str(e),
                        sys.exc_info()[2].tb_lineno
                    )
                    self.log(request_exc_msg, 'error', self.__id)
                    return None
            else:
                self.log("Provided directory path does not exist. Exiting...", 'error', self.__id)
                return None
        except Exception as e:
            request_exc_msg = "An Exception occurred during method {} exectution: {} in line: {}".format(
                self.__id,
                str(e),
                sys.exc_info()[2].tb_lineno
            )
            self.log(request_exc_msg, 'error', self.__id)
            return None


    ################################################
    # Search Directory Path and Search for Git URL #
    ################################################
    @property
    def provider(self):
        """Class Getter method for the provider property. This property will return the repository platform provider if a value can be determined and set by the property setter method."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Request for provider property received.", 'info', self.__id)
        return self._provider

    @provider.setter
    def provider(self, repository_url):
        """Class Setter method for the object provider property. This property will search the provided url and attempt to extact the a git repository provider, such as github, gitlab, or bitbucket."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Call to set value for provider property.", 'info', self.__id)
        if repository_url is not None:
            try:
                # Parse the provided provider url and attempt to extract the provider.
                if repository_url.startswith(('http', 'https', 'git')) and repository_url.endswith('.git'):
                    provider_git_url = repository_url.strip().split("/")
                    self.log("Provided URL split into search list: {}".format(provider_git_url), 'debug', self.__id)
                    if len(provider_git_url) == 2:
                        provider_string = provider_git_url[-2].split(":")[0].split("@")[1]
                    elif len(provider_git_url) > 3:
                        provider_string = provider_git_url[-3]
                    else:
                        provider_string = None

                    if provider_string is not None and ('github' in provider_string or 'gitlab' in provider_string or 'bitbucket' in provider_string):
                        # If a user@provider.tld is set, then remove the user designation.
                        if '@' in provider_string:
                            self.user = provider_string.split('@')[0]
                            self.log("User detected in provider string, setting user property: {}".format(self.user), 'debug', self.__id)
                            provider_string = provider_string.split('@')[1]
                        self._provider = provider_string
                        self.log("Provider match {} found!".format(self._provider), 'debug', self.__id)
                    else:
                        self.log("No provider could be determined: {}".format(provider_string), 'error', self.__id)
                        return None
                else:
                    self.log("Provided URL is not in the proper format, aborting provider search...", 'error', self.__id)
                    self.log("{}".format(provider_git_url), 'error', self.__id)
                    return None
            except Exception as e:
                request_exc_msg = "An Exception occurred during method {} exectution: {} in line: {}".format(
                    self.__id,
                    str(e),
                    sys.exc_info()[2].tb_lineno
                )
                self.log(request_exc_msg, 'error', self.__id)
                return None
        else:
            self.log("Required url property argument was not provided... Aborting search...", 'error', self.__id)
            return None
