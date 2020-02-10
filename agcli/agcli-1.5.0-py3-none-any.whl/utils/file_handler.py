import os.path
from pathlib import Path

class FileHandler():

    file_handler = None

    def __init__(self, cmd_name, config_dir):
        global file_handler
        file_handler = self
        # if the command is in the "./dir1/dir2/cmd", keep only 'cmd' as the command name
        self.command_name = os.path.basename(cmd_name)
        self.config_dir = config_dir
        self._create_directories()

    def _create_directories(self):
        """
        Crete the interface and the template directories if they don't exist
        """
        Path(self.get_template_directory()).mkdir(parents=True, exist_ok=True)
        Path(self.get_interface_directory()).mkdir(parents=True, exist_ok=True)

    def get_default_template_file(self):
        """
        Return the path to the default template file according to the command name
        """
        template_file = os.path.join(self.get_template_directory(),
         'template_default_{}.yaml'.format(self.command_name))
        return template_file

    def get_template_directory(self):
        """
        Return the path to the template directory
        """
        template_dir = os.path.join(self.config_dir, '.agcli', 'templates')
        return template_dir

    def get_interface_directory(self):
        """
        Return the path to the interface directory
        """
        interface_dir = os.path.join(self.config_dir, '.agcli', 'interfaces')
        return interface_dir

    def get_interface_file(self):
        """
        Return the path to the interface file for this command name
        """
        interface_file = os.path.join(self.get_interface_directory(),
         'interface_{}.yaml'.format(self.command_name))
        return interface_file
