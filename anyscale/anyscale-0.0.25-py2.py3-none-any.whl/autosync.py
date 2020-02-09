import copy
import os
import subprocess
import sys
import xml.etree.ElementTree


class AutosyncRunner:
    def __init__(self):
        self.syncthing_home = os.path.expanduser("~/.anyscale/syncthing")
        self.syncthing_config_path = os.path.join(
            self.syncthing_home, "config.xml")

        # Get the right syncthing executable path depending on the OS.
        current_dir = os.path.dirname(os.path.realpath(__file__))
        if sys.platform.startswith("linux"):
            self.syncthing_executable = os.path.join(
                current_dir, "syncthing-linux")
        elif sys.platform.startswith("darwin"):
            self.syncthing_executable = os.path.join(
                current_dir, "syncthing-macos")
        else:
            raise NotImplementedError(
                "Autosync not supported on platform {}".format(sys.platform))

        # This line creates the configuration file for the autosync.
        assert subprocess.check_call([
            self.syncthing_executable, "-generate", self.syncthing_home]) == 0

    def add_device(self, project_name: str, device_id: str):
        """Add a device to syncthing config to device and folder section.

        The syncthing configuration path used is in the SYNCTHING_CONFIG_PATH
        variable. If this device_id has already been added it will not be
        added again.

        Args:
            project_name: Name of the project we add the device to.
            device_id: ID of the device being added.
        """
        config = xml.etree.ElementTree.parse(self.syncthing_config_path)
        root = config.getroot()
        project_folder_element = None
        device_element = None
        for child in root.getchildren():
            if child.get("id") == project_name:
                project_folder_element = child
            if child.get("id") == device_id:
                device_element = child
        assert project_folder_element is not None
        # Add the device element to the top level configuration if it
        # is not already there.
        if not device_element:
            device_element = xml.etree.ElementTree.SubElement(
                root, "device", {
                    "compression": "metadata",
                    "id": device_id,
                    "introducedBy": "",
                    "introducer": "false",
                    "name": project_name,
                    "skipIntroductionRemovals": "false"
                })
            properties = {
                "address": "dynamic",
                "paused": "false",
                "autoAcceptFolders": "false",
                "maxSendKbps": "0",
                "maxRecvKbps": "0",
                "maxRequestKiB": "0"
            }
            for key, value in properties.items():
                element = xml.etree.ElementTree.SubElement(
                    device_element, key)
                element.text = value
            root.append(device_element)

        # We want to add the device element to the folder if it is
        # not already there. First check if it is, then add it if needed.
        folder_device_element_present = False
        for child in project_folder_element.getchildren():
            if project_folder_element.get("id") == device_id:
                folder_device_element_present = True
        if not folder_device_element_present:
            folder_device_element = xml.etree.ElementTree.SubElement(
                project_folder_element, "device", {"id": device_id})
            project_folder_element.append(folder_device_element)

        config.write(self.syncthing_config_path)

    def add_or_update_project_folder(
            self, project_name: str, project_folder_path: str):
        """Add a project folder to the syncthing config.xml.

        The syncthing configuration path used is in the SYNCTHING_CONFIG_PATH
        variable. This function will not add any devices to the folder.

        Args:
            project_name: Name of the project we add the folder
                for. This is used as an identifier for the folder.
            project_folder_path: Full path to the folder we want
                to add to syncthing.
        """
        config = xml.etree.ElementTree.parse(self.syncthing_config_path)
        root = config.getroot()
        default_folder_element = None
        project_folder_element = None
        for child in root.getchildren():
            if child.get("id") == "default":
                default_folder_element = child
            if child.get("id") == project_name:
                project_folder_element = child
        assert default_folder_element is not None
        if not project_folder_element:
            project_folder_element = copy.deepcopy(default_folder_element)
            project_folder_element.set("id", project_name)
            project_folder_element.set(
                "label", "Project Folder for {}".format(project_name))
            project_folder_element.set("path", project_folder_path)
            project_folder_element.set("fsWatcherDelayS", "1")
            root.append(project_folder_element)
        else:
            project_folder_element.set("path", project_folder_path)
        config.write(self.syncthing_config_path)

    def get_device_id(self):
        return subprocess.check_output([
            self.syncthing_executable, "-home", self.syncthing_home,
            "-device-id"]).decode().strip()

    def start_autosync(self):
        syncthing = subprocess.Popen([
            self.syncthing_executable, "-home", self.syncthing_home])
        syncthing.communicate()

    def kill_autosync(self):
        subprocess.check_output(["pkill syncthing"], shell=True)
