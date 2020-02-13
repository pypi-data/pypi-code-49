##############################################################################
# CloudMage : GitHub Repository Class to Interact with the GitHub API
#=============================================================================
# CloudMage Github Repository Request Object Utility/Library
#   - Fetch a repository from Github and parse into a returnable object.
# Author: Richard Nason rnason@cloudmage.io
# Project Start: 2/11/2020
# License: GNU GPLv3
##############################################################################

###############
# Imports:    #
###############
# Import Pip Installed Modules:
import requests

# Import Base Python Modules
import json, os, sys, inspect


#####################
# Class Definition: #
#####################
class GitHubAPI(object):
    """CloudMage Git Parser Class
    This class is designed to interact with various Github API Endpoints and used to construct a repository
    return object that can then be interacted with through the instantiated object. The main purpose of this
    class is to allow an easy method of interacting with repository data without having to make repeated calls to Github every time repository data is required.
    """

    class RepoOwner():
        """GitHubAPI self class to create a repository owner object that can be referenced and used by the parent
        GitHubAPI class object.
        """

        def __init__(self, owner_id, owner_name, owner_avatar, owner_url):
            '''GitHubAPI Owner Class Constructor'''

            # Set class instantiation variables
            self.id = owner_id
            self.name = owner_name
            self.avatar = owner_avatar
            self.url = owner_url


    def __init__(self, repo_url, auth_token=None, verbose=False, log=None):
        '''GithubAPI Class Constructor'''

        ##### Class Public Attributes ######
        self.verbose = verbose
        self.state = 'Init'

        ##### Repository Base Properties ######
        self.name = None
        self.namespace = None
        self.id = None
        self.access = None
        self.http_url = None
        self.git_url = None
        self.mirror = None
        self.description = None
        self.created = None
        self.updated = None
        self.last_push = None
        self.size = None
        self.language = None
        self.license = None
        self.archived = None
        self.disabled = None
        self.default_branch = None

        ##### Repository Stat Properties ######
        self.fork = None
        self.forks = None
        self.watchers = None
        self.stars = None
        self.issues = None
        self.open_issues = None
        self.homepage = None
        self.wiki = None
        self.pages = None
        self.downloads = None
        self.projects = None

        ##### Repository Owner Object Property Data ######
        self.owner = None
        
        ##### Class Private Attributes ######
        self._target_repo_url = repo_url
        self._auth_token = auth_token
        self._log = log
        self._log_context = "CLS->GitHubAPI"

        ##### Repository API Request URLs ######
        self._repo_request_url = None
        self._repo_data = None

        ##### Init and populate the return the requested object instance ######
        self._parse_url()
        self._repository_url()
        self._repo_data = self._request_handler(self._repo_request_url)
        self.data = self._repo_data


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


    ############################################
    # Parse Git Config File:  [Verified]       #
    ############################################
    def _parse_url(self):
        """This class method will accept an HTTP/HTTPS or Git styled URL and parse the URL string to extract
        the repository name and repository namespace from the received URL string. The name and namespace class
        properties will then be set so that they will be available to both the rest of the class methods as well as
        the class caller as an available object attribute."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Call to parse url: {}".format(self._target_repo_url), 'info', self.__id)

        # Instantiate method variables
        parse_namespace = None
        parse_name = None
        
        # Parse the URL String to determine the object name and namespace.
        try:
            parse_url_list = self._target_repo_url.strip().split("/")
            self.log("Parsing repository namespace and name from: {}".format(parse_url_list), 'debug', self.__id)
            parse_namespace = parse_url_list[-2].split(":")[-1]
            parse_name = parse_url_list[-1].split(".")[0]
            if parse_namespace is not None:
                self.namespace = parse_namespace
                self.log("Repository namespace: {}".format(self.namespace), 'debug', self.__id)
            else:
                self.log("Repository namespace could not be determined. Aborting request.", 'error', self.__id)
                self.log(parse_namespace, 'debug', self.__id)
                return None
            if parse_name is not None:
                self.name = parse_name
                self.log("Repository name: {}".format(self.name), 'debug', self.__id)
            else:
                self.log("Repository name could not be determined. Aborting request.", 'error', self.__id)
                self.log(parse_name, 'debug', self.__id)
                return None
        except Exception as e:
            parse_exc_msg = "An Exception occurred during method {} exectution: {} in line: {}".format(
                self.__id,
                str(e),
                sys.exc_info()[2].tb_lineno
            )
            self.log(parse_exc_msg, 'error', self.__id)
            return None


    def _repository_url(self):
        """Class method that accepts the repository namespace and the repository name as arguments, and based on those values, sets the request URL for the main repository API."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Constructing API URL for Github Repository API", 'info', self.__id)

        # Construct the URL
        if self.namespace is not None and self.name is not None:
            self._repo_request_url = "https://api.github.com/repos/{}/{}".format(self.namespace, self.name)
            self.log("Constructed Github repository request url: {}".format(self._repo_request_url), 'debug', self.__id)
        else:
            self.log("Repository namespace or name is not valid, aborting request", 'error', self.__id)
            self.log("Namespace: {}".format(self.namespace), 'error', self.__id)
            self.log("Name: {}".format(self.name), 'error', self.__id)
            return None


    def _request_handler(self, request_url):
        """Class Method to send an http/https request for github repository data and validate that the response object is valid, once completed, the method will store the response in self.data."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Sending request to Github API", 'info', self.__id)
        # Instantiate method variables
        request_data = None
        
        # Set the request headers and provide auth token if valid instance argument
        request_headers = {}
        if self._auth_token is not None:
            request_headers.update({'Authorization': 'token {}'.format(self._auth_token)})
            self.log("Auth token found! Adding to request headers.", 'debug', self.__id)
        
        # Send the request or return None
        try:
            # Send the request
            r = requests.get(request_url, headers=request_headers)
            self.log("Request successfully sent to: {}.".format(request_url), 'debug', self.__id)
            request_handler_response = json.loads(r.text)
            
            # Validate that the request was successful and if so, then flag the response object for processing
            if r.status_code == 200:
                if isinstance(request_handler_response, dict):
                    if bool(request_handler_response):
                        self.log("Response contains return code: {}".format(r.status_code), 'debug', self.__id)
                        self.log("Verified response object contains valid formatting.", 'debug', self.__id)
                        self.log("The following response object assigned to .data property.", 'debug', self.__id)
                        self.log(json.dumps(request_handler_response, indent=4, sort_keys=True), 'debug', self.__id)
                        return request_handler_response
                    else:
                        self.log("Empty response object received", 'error', self.__id)
                        self.log(json.dumps(request_handler_response, indent=4, sort_keys=True), 'debug', self.__id)
                        return None
                else:
                    self.log("Expected valid JSON response but received response object type: {}".format(type(request_handler_response)), 'error', self.__id)
                    self.log("{}".format(str(request_handler_response)), 'debug', self.__id)
                    return None
            else:
                self.log("Request unsuccessful. Received response status code: {}".format(r.status_code), 'error', self.__id)
                return None
        except Exception as e:
            request_exc_msg = "An Exception occurred during method {} exectution: {} in line: {}".format(
                self.__id,
                str(e),
                sys.exc_info()[2].tb_lineno
            )
            self.log(request_exc_msg, 'error', self.__id)
            return None


    ############################################
    # Construct Repository Object Properties:  #
    ############################################
    @property
    def data(self):
        """Class getter method used to retrieve the originally stored Github response object that is the source used for setting the rest of the object properties."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Request for data property received.", 'info', self.__id)

        if self._repo_data is not None and isinstance(self._repo_data, dict) and bool(self._repo_data):
            return self._repo_data
        else:
            return {}


    @data.setter
    def data(self, data_source):
        """Class setter method that will set the object property values with the data received from the request handler self._data dictionary object.
        Normally a setter would be used to set the actual .data object property, but in this case we are using the setter to use the ._data property
        as the data passed data source, that is used to populate or set all of the object property values based on the ._data source values."""
        # Define this function for logging
        self.__id = inspect.stack()[0][3]
        self.log("Initializing object properties.", 'info', self.__id)

        # Populate the object property values.
        if data_source is not None and isinstance(data_source, dict) and bool(data_source):
            self.id = data_source.get('id')
            self.access = 'private' if data_source.get('private') else 'public'
            self.http_url = data_source.get('html_url')
            self.git_url = data_source.get('git_url')
            self.mirror = data_source.get('mirror_url')
            self.description = data_source.get('description')
            self.created = data_source.get('created_at')
            self.updated = data_source.get('updated_at')
            self.last_push = data_source.get('pushed_at')
            self.size = data_source.get('size')
            self.language = data_source.get('language')
            self.license = data_source.get('license')
            self.archived = data_source.get('archived')
            self.disabled = data_source.get('disabled')
            self.default_branch = data_source.get('default_branch')

            # Stats
            self.fork = data_source.get('fork')
            self.forks = data_source.get('fork_count')
            self.watchers = data_source.get('subscribers_count')
            self.stars = data_source.get('stargazers_count')
            self.issues = data_source.get('issue_count')
            self.open_issues = data_source.get('open_issues')
            self.homepage = data_source.get('homepage')
            self.wiki = data_source.get('has_wiki')
            self.pages = data_source.get('has_pages')
            self.downloads = data_source.get('has_downloads')
            self.projects = data_source.get('has_projects')

            # Owner
            self.owner = self.RepoOwner(
                data_source.get('owner').get('id'),
                data_source.get('owner').get('login'),
                data_source.get('owner').get('avatar_url'),
                data_source.get('owner').get('html_url')
            )

            self.state = 'Success'
            self.log("Object property update state: {}!".format(self.state), 'info', self.__id)
        else:
            self.state = 'Fail'
            self.log("Object property update state: {}!".format(self.state), 'error', self.__id)
            self.log("Updating object properties failed. Bad data source received", 'error', self.__id)
            return None
