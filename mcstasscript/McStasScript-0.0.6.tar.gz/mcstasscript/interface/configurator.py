import yaml
import os

class Configurator:
    """
    Class for setting the configuration file for McStasScript.
    
    Attributes
    ----------
    configuration_file_name : str
        absolute path of configuration file
        
    Methods
    -------
    set_mcstas_path(string)
        sets mcstas path
        
    set_mcrun_path(string)
        sets mcrun path
        
    set_line_length(int)
        sets maximum line length to given int
    
    _write_yaml(dict)
        internal method, writes a configuration yaml file with dict content
        
    _read_yaml()
        internal method, reads a configuration yaml file and returns a dict
    
    _create_new_config_file()
        internal method, creates default configuration file

    """

    def __init__(self, *args):
        """
        Initialization of configurator, checks that the configuration file
        actually exists, and if it does not, creates a default configuration
        file.
        
        Parameters
        ----------
        (optional) custom name : str
            Custom name for configuration file for testing purposes
        """

        if len(args) == 1:
            name = args[0]
        else:
            name = "configuration"

        # check configuration file exists
        THIS_DIR = os.path.dirname(os.path.abspath(__file__))
        self.configuration_file_name = THIS_DIR + "/../" + name + ".yaml"
        if not os.path.isfile(self.configuration_file_name):
            # no config file found, write default config file
            self._create_new_config_file()

    def _write_yaml(self, dictionary):
        """
        Writes a dictionary as the new configuration file
        """
        with open(self.configuration_file_name, 'w') as yaml_file:
            yaml.dump(dictionary, yaml_file, default_flow_style=False)   

    def _read_yaml(self):
        """
        Reads yaml configuration file
        """
        with open(self.configuration_file_name, 'r') as ymlfile:
            return yaml.safe_load(ymlfile)

    def _create_new_config_file(self):
        """
        Writes a default configuration file to the package root directory
        """

        run = "/Applications/McStas-2.5.app/Contents/Resources/mcstas/2.5/bin/"
        mcstas = "/Applications/McStas-2.5.app/Contents/Resources/mcstas/2.5/"

        default_paths = {"mcrun_path" : run,
                         "mcstas_path" : mcstas}
        default_other = {"characters_per_line" : 93}

        default_config = {"paths" : default_paths,
                          "other" : default_other}

        self._write_yaml(default_config)

    def set_mcstas_path(self, path):
        """
        Sets the path to McStas

        Parameters
        ----------
        path : str
            Path to the mcstas directory containing "sources", "optics", ...
        """

        # read entire configuration file 
        config = self._read_yaml()

        # update mcstas_path
        config["paths"]["mcstas_path"] = path

        # write new configuration file
        self._write_yaml(config)

    def set_mcrun_path(self, path):
        """
        Sets the path to mcrun

        Parameters
        ----------
        path : str
            Path to the mcrun executable
        """

        # read entire configuration file 
        config = self._read_yaml()

        # update mcstas_path
        config["paths"]["mcrun_path"] = path

        # write new configuration file
        self._write_yaml(config)

    def set_line_length(self, line_length):
        """
        Sets maximum line length for output

        Parameters
        ----------
        line_length : int
            maximum line length for output
        """

        # read entire configuration file 
        config = self._read_yaml()

        # update mcstas_path
        config["other"]["characters_per_line"] = int(line_length)

        # write new configuration file
        self._write_yaml(config)

