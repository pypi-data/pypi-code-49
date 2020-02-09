import os
import json
import shutil

# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
# Implementation of the singleton pattern
class KabasCache(object):

    __instance = None

    @staticmethod
    def getInstance():

        if KabasCache.__instance == None:
            KabasCache()

        return KabasCache.__instance

    def __init__(self):

        if KabasCache.__instance != None:
            raise Exception("Cannot instantiate singleton object. Use KabasCache.getInstance() instead")

        
        config_file_name = 'config.json'

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), config_file_name), 'r', encoding = 'utf-8-sig') as f:

            self.location = json.load(f)['cache']['location']
        
        if (not os.path.exists(self.location)):

            os.makedirs(self.location)

        self._lookup_path = os.path.join(self.location, "lookup.json")
        self._lookup = self._load()

        KabasCache.__instance = self

    def get_lookup_version(self, project_id, file_name):

        if not project_id in self._lookup.keys():

            return None

        if not file_name in self._lookup[project_id].keys():

            return None

        return self._lookup[project_id][file_name]

    def add_to_cache(self, file_details, source_path):

        self._ensure_path(file_details.project_id)
        self._copy(source_path, os.path.join(self.location, file_details.project_id, file_details.file_name))
        self._update_lookup(file_details.project_id, file_details.file_name, file_details.latest_version_id)

    def retrieve_from_cache(self, project_id, file_name, target_directory):

        source = self.get_cache_location(project_id, file_name)
        target = os.path.join(target_directory, file_name)

        self._copy(source, target)

    def delete_from_cache(self, project_id, file_name):

        self._lookup[project_id].pop(file_name, None)
        os.remove(self.get_cache_location(project_id, file_name))

    def _copy(self, source, target):

        if source != target:

            shutil.copyfile(source, target)

    def _update_lookup(self, project_id, file_name, latest_version_id):

        if not project_id in self._lookup.keys():

            self._lookup[project_id] = {}

        self._lookup[project_id][file_name] = latest_version_id

        self._save()

    def _ensure_path(self, project_id):

        project_path = os.path.join(self.location, project_id)

        if not os.path.exists(project_path):

            os.makedirs(project_path)

    def get_cache_location(self, project_id, file_name):

        return os.path.join(self.location, project_id, file_name)

    def _load(self):

        lookup = {}

        if (os.path.exists(self._lookup_path)):

            with open(self._lookup_path, 'r') as f:

                lookup = json.load(f)

        return lookup

    def _save(self):

        with open(self._lookup_path, "w") as f:
                
            json.dump(self._lookup, f)