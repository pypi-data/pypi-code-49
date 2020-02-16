##############################################################################
# CloudMage : Jinja Templating Helper Class to simplify using Jinja Templates
#=============================================================================
# CloudMage Jinja Helper Object Utility/Library
#   - Find, Load, and Render Jinja Templates with Simplicity.
# Author: Richard Nason rnason@cloudmage.io
# Project Start: 2/13/2020
# License: GNU GPLv3
##############################################################################

###############
# Imports:    #
###############
# Import Pip Installed Modules:
from jinja2 import Template, Environment, FileSystemLoader

# Import Base Python Modules
import json, os, sys, inspect, ntpath, shutil, datetime

#####################
# Class Definition: #
#####################
class JinjaUtils(object):
    """CloudMage Jinja Helper Class
    This class is designed to make defining, loading, and rendering Jinja templates easily. It provides helper methods that will allow you to construct a Jinja object that will make loading, rendering and writing templates available through the instantiated object constructed by this class.
    """

    def __init__(self, verbose=False, log=None):
        '''JinjaHelper Class Constructor'''

        ##### Class Public Properties and Attributes ######
        # Check the passed value to ensure its a bool before assignment.
        if verbose is not None and isinstance(verbose, bool):
            self._verbose = verbose
        else:
            self._verbose = False
        
        # Check to ensure that the passed log object is in fact an object, and has the proper attributes, if not don't assign.
        if log is not None and isinstance(log, object) and hasattr(log, 'debug') and hasattr(log, 'info') and hasattr(log, 'warning') and hasattr(log, 'error'):
            self._log = log
        else:
            self._log = None
        self._log_context = "CLS->JinjaUtils"

        ##### Class Private Properties and Attributes ######
        # Getter and Setter propert vars
        self._trim_blocks = True
        self._lstrip_blocks = True
        self._template_directory = None  
        self._available_templates = []
        self._loaded_template = None
        self._loaded_template_filename = None
        self._rendered_template = None
        
        # Jinja Objects using Jinja FileSystemLoader, and Jinja Environment objects.
        self._jinja_loader = None
        self._jinja_template_library = None
        self._output_directory = None
        self._output_file = None

        ##### Method Properties ######
        # self.trim_blocks
        # self.lstrip_blocks
        # self.template_directory

        ##### Init and populate the return the requested object instance ######
        # self._parse_url()
        # self._repository_url()
        # self._repo_data = self._request_handler(self._repo_request_url)
        # self.data = self._repo_data


    ############################################
    # Class Exception Handler:                 #
    ############################################
    def _exception_handler(self, caller_function, exception_object):
        """Class Exception Handler
        
        Handle any exceptions that arise in a universal format for easy debuging purposes
        
        Parameters:
            caller_function  (str):  required
            exception_object (obj):  required

        Returns:
            Publish properly formatted exception to log object or stdout, stderr
        """
        parse_exc_msg = "An EXCEPTION has occurred in '{}.{}', on line {}: -> {}".format(
                self._log_context,
                caller_function,
                sys.exc_info()[2].tb_lineno,
                str(exception_object)
            )
        self.log(parse_exc_msg, 'error', caller_function)


    ############################################
    # Class Logger:                            #
    ############################################
    def log(self, log_msg, log_type, log_id):
        """Class Log Handler

        Provides the logging for this class. If the class caller instantiates the object with the verbose setting set to true, then the class 
        will log to stdout/stderr or to a provided log object if one was passed during object instantiation.
        
        Parameters:
            log_msg  (str):  required
            log_type (str):  required
            log_id   (str):  required

        Returns:
            Log Stream
        """
        # Define this methods identity for functional logging:
        self.__log_id = inspect.stack()[0][3]
        try:
            # Internal method variable assignments:
            log_msg_caller = "{}.{}".format(self._log_context, log_id)
            # Set the log message offset based on the message type: [debug=3, info=4, warning=1, error=3]
            log_msg_offset = 3
            log_msg_offset = 4 if log_type.lower() == 'info' else log_msg_offset
            log_msg_offset = 1 if log_type.lower() == 'warning' else log_msg_offset

            # If a valid log object was passed into the class constructor, publish the log to the log object:
            if self._log is not None:
                # Set the log message prefix
                log_message = "{}: -> {}".format(log_msg_caller, log_msg)
                if log_type.lower() == 'error':
                    self._log.error(log_message)
                elif log_type.lower() == 'warning':
                    self._log.warning(log_message)
                elif log_type.lower() == 'info':
                    self._log.info(log_message)
                else:
                    self._log.debug(log_message)
            # If no valid log object was passed into the class constructor, write the message to stdout, stderr:
            else:
                log_message = "{}     {}{}{}: -> {}".format(datetime.datetime.now(), log_type.upper(), " " * log_msg_offset, log_msg_caller, log_msg)
                if log_type.lower() == 'error':
                    if self._verbose:
                        print(log_message, file=sys.stderr)
                else:
                    if self._verbose:
                        print(log_message, file=sys.stdout)
        except Exception as e:
            self._exception_handler(self.__log_id, e)


    ############################################
    # Jinja Option Getters and Setters:        #
    ############################################
    @property
    def trim_blocks(self):
        """Getter method for Jinja trim_blocks property. This method returns the current trim_blocks setting value."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        return self._trim_blocks


    @trim_blocks.setter
    def trim_blocks(self, trim_blocks_setting=True):
        """Setter method for Jinja trim_blocks property. This method will only take a value of true or false as a valid value for the property."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property update requested.".format(self.__id), 'info', self.__id)
        # if the passed value is a valid bool value then set the value.
        if trim_blocks_setting is not None and isinstance(trim_blocks_setting, bool):
            self._trim_blocks = trim_blocks_setting
            self.log("Updated {} property with value: {}".format(self.__id, self._trim_blocks), 'info', self.__id)
        else:
            self.log("Property {} argument expected bool but received type: {}. Aborting update!".format(self.__id, type(trim_blocks_setting)), 'error', self.__id)


    @property
    def lstrip_blocks(self):
        """Getter method for Jinja lstrip_blocks property. This method returns the current lstrip_blocks setting value."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        return self._lstrip_blocks


    @lstrip_blocks.setter
    def lstrip_blocks(self, lstrip_blocks_setting=True):
        """Setter method for Jinja lstrip_blocks property. This method will only take a value of true or false as a valid value for the property."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property update requested.".format(self.__id), 'info', self.__id)
        # if the passed value is a valid bool value then set the value.
        if lstrip_blocks_setting is not None and isinstance(lstrip_blocks_setting, bool):
            self._lstrip_blocks = lstrip_blocks_setting
            self.log("Updated {} property with value: {}".format(self.__id, self._lstrip_blocks), 'info', self.__id)
        else:
            self.log("Property {} argument expected bool but received type: {}. Aborting update!".format(self.__id, type(lstrip_blocks_setting)), 'error', self.__id)


    ################################################
    # Verbose Setter / Getter Methods:             #
    ################################################
    @property
    def verbose(self):
        """Getter method for the verbose property. This method will return the verbose setting."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        return self._verbose


    @verbose.setter
    def verbose(self, verbose):
        """Setter method for the verbose property. This method will set the verbose setting if a valid bool value is provided."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property update requested.".format(self.__id), 'info', self.__id)
        if verbose is not None and isinstance(verbose, bool):
            self._verbose = verbose
            self.log("Updated {} property with value: {}".format(self.__id, self._verbose), 'info', self.__id)
        else:
            self.log("Property {} argument expected bool but received type: {}. Aborting update!".format(self.__id, type(verbose)), 'error', self.__id)


    ############################################
    # Jinja Template Directory Getter/Setter:  #
    ############################################
    @property
    def template_directory(self):
        """This class Getter method will retreive the currently set value of the template directory and return
        it back to the method caller."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        if self._template_directory is None:
            return "No setting found!. Set this property with object.template_directory = 'valid/path/to/template/directory'."
        else:
            return self._template_directory


    @property
    def available_templates(self):
        """Class property method that will return the self._available_templates property. The available_templates property is a list of all templates available in the configured template_directory. The template_directory setter method constructs the list of template files when a template_directory is updated."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("Call to retrieve available_templates", 'info', self.__id)
        if self._available_templates is not None and isinstance(self._available_templates, list):
            return self._available_templates
        else:
            return []


    @template_directory.setter
    def template_directory(self, template_directory_path):
        """Setter method that will take a valid directory path location and use that location to set the object
        template_directory property. Once validated this method will call the load method to load the template directory
        and populate the available_templates list property."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property update requested.".format(self.__id), 'info', self.__id)
        try:
            # Set template directory
            if template_directory_path is not None and isinstance(template_directory_path, str):
                if os.path.exists(template_directory_path) and os.access(template_directory_path, os.R_OK):
                    # Set the template_directory property.
                    self._template_directory = template_directory_path
                    self.log("Template directory path set to: {}".format(self._template_directory), 'debug', self.__id)
                    # Load the templates into Jinja
                    self._jinja_loader = FileSystemLoader(self._template_directory)
                    self._jinja_template_library = Environment(
                        loader=self._jinja_loader,
                        trim_blocks=self._trim_blocks,
                        lstrip_blocks=self._lstrip_blocks
                    )
                    self._jinja_template_library.filters['to_json'] = json.dumps
                    self.log("Jinja loaded the provided template_directory successfully!", 'debug', self.__id)
                    self.log("Added to_json filter to Jinja Environment object.", 'debug', self.__id)
                    template_list = self._jinja_template_library.list_templates()
                    if isinstance(template_list, list) and len(template_list) > 0:
                        self._available_templates = template_list
                        self.log("Updated {} property with: {}".format(self.__id, self._available_templates), 'debug', self.__id)
                else:
                    self.log("Provided directory path doesn't exit.", 'error', self.__id)
                    self.log("Aborting property update...", 'error', self.__id)
            else:
                self.log("Provided directory path expected type str but received: {}".format(type(template_directory_path)), 'error', self.__id)
                self.log("Aborting property update...", 'error', self.__id)
        except Exception as e: # pragma: no cover
            self._exception_handler(self.__id, e) # pragma: no cover


    ############################################
    # Jinja Template Getter/Setter:            #
    ############################################
    @property
    def load(self):
        """Getter Method that returns the value of self._loaded_template back to the caller"""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        # Return the loaded template name.
        if self._loaded_template_filename is not None and isinstance(self._loaded_template_filename, str):
            return str(self._loaded_template_filename)
        else:
            return "No template has been loaded!"

    @load.setter
    def load(self, template):
        """Class method to load the specified template. The template can be:
        
        * The name of a template already loaded in the jinja_loader from a template_directory
        * A file path to a valid jinja file on the filesystem
        """
        # Reinitialize the loaded template
        self._available_templates = []
        self._loaded_template = None
        self._loaded_template_filename = None
        try:
            # Define this methods identity for functional logging:
            self.__id = inspect.stack()[0][3]
            self.log("{} property update requested.".format(self.__id), 'info', self.__id)
            
            # Check the value passed to determine what type of template was passed.
            if os.path.isfile(template) and os.access(template, os.R_OK):
                self._loaded_template = Template(open(template).read())
                self._loaded_template_filename = os.path.basename(template)
                self.log("Loaded template file from path: {}".format(self._loaded_template), 'info', self.__id)
                self.log("Loaded template name set to: {}".format(self._loaded_template_filename), 'debug', self.__id)
            else:
                if isinstance(template, str):
                    for tpl in self._jinja_template_library.list_templates():
                        if template == tpl:
                            self._loaded_template = self._jinja_template_library.get_template(template)
                            self._loaded_template_filename = template
                            self.log("Loaded template file from template_directory: {}".format(self._loaded_template), 'info', self.__id)
                    if self._loaded_template is None and self._loaded_template_filename is None:
                        self.log("Requested template not found in template directory: {}".format(self._template_directory), 'warning', self.__id)
                else:
                    self.log("{} expected template of type str but received type: {}".format(self.__id, type(template)), 'error', self.__id)
        except Exception as e:
            self._exception_handler(self.__id, e)

    @property
    def rendered(self):
        """Class method that will return the current rendered template from the current loaded template."""
        # Define this methods identity for functional logging:
        self.__id = inspect.stack()[0][3]
        self.log("{} property requested.".format(self.__id), 'info', self.__id)
        # Return the rendered template value.
        if self._rendered_template is not None:
            return self._rendered_template
        else:
            return "No template has been rendered!"


    def render(self, **kwargs):
        """Class method that will render the template loaded in the objects self._loaded_template property.
        This method will accept multiple dictionary objects as an input provided that they were provided
        in the format of keyword = dictionary where keyword is the variable in the Jinja template that will
        map to the dictionary object being passed.
        """
        # Reinitialize the rendered property
        self._rendered_template = None
        try:
            # Define this methods identity for functional logging:
            self.__id = inspect.stack()[0][3]
            self.log("{} of loaded template requested.".format(self.__id), 'info', self.__id)
            if isinstance(self._loaded_template, Template) and hasattr(self._loaded_template, 'render'):
                # Render the template passing in the kwargs input.
                self._rendered_template = self._loaded_template.render(**kwargs)
                self.log("{} rendered successfully!".format(self._loaded_template), 'info', self.__id)
            else:
                self.log("No template loaded, Aborting render!", 'error', self.__id)
        except Exception as e: # pragma: no cover
            self._exception_handler(self.__id, e) # pragma: no cover


    def write(self, output_directory, output_file, backup=True):
        """Class method that will write the rendered jinja template to a directory/path location."""
        try:
            # Define this methods identity for functional logging:
            self.__id = inspect.stack()[0][3]
            self.log("{} called on rendered template requested.".format(self.__id), 'info', self.__id)
            
            # Set the Output Directory and perform directory validation checks
            if isinstance(output_directory, str) and os.path.exists(output_directory) and not os.path.isfile(output_directory):
                self._output_directory = output_directory
                self.log("Output directory has been set to: {}!".format(self._output_directory), 'debug', self.__id)
                # Set the Output file and perform validation checks
                if isinstance(output_file, str):
                    head, tail = ntpath.split(output_file)
                    if tail or ntpath.basename(head) is not None:
                        self._output_file = tail or ntpath.basename(head)
                        self.log("Output file has been set to: {}!".format(self._output_file), 'debug', self.__id)
                else:
                    self.log("Output file name expected str value but received type: {}... Aborting request!".format(type(output_file)), 'error', self.__id)
                    return False
            else:
                self.log("Invalid output directory specified in {} request... Aborting request!".format(self.__id), 'error', self.__id)
                return False

            # Check if file back up is enabled and if so backup the file.
            if os.path.exists(os.path.join(self._output_directory, self._output_file)):
                # If backup enabled, make a backup of the file.
                if backup:
                    # Separate the filename from the file extention
                    raw_filename, raw_file_extention = os.path.splitext(self._output_file)
                    backup_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    source_filename = os.path.join(self._output_directory, self._output_file)
                    backup_filename = os.path.join(self._output_directory, "{}_{}.bak".format(raw_filename, backup_timestamp))
                    shutil.copy(source_filename, backup_filename)
                    self.log("{} backed up to: {}".format(self._output_file, backup_filename), "info", self.__id)
                else:
                    self.log("Existing file backup disabled, {} will be overwritten!".format(self._output_file), "warning", self.__id)
            # Write the output file.
            write_output_file = os.path.join(self._output_directory, self._output_file)
            self.log("Writing rendered template to output file: {}".format(write_output_file), "debug", self.__id)
            output = open(write_output_file, "w")
            output.write(self._rendered_template)
            output.close()
            self.log("{} written successfully!".format(write_output_file), "info", self.__id)
            return True
        except Exception as e: # pragma: no cover
            self._exception_handler(self.__id, e) # pragma: no cover
