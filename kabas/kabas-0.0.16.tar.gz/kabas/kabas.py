from datetime import datetime, timedelta
import json
import os
import shutil

from kabas._kabas_client import KabasClient
from kabas.kabas_project import KabasProject
from kabas.project_access_type import ProjectAccessType

class Kabas:

    # def create_new(self, project_name, public):

    #     with KabasClient() as client:

    #         create_project_response = client.create_new(project_name, public)
            
    #         project_key = create_project_response["fullAccessKey"]
    #         project_id = create_project_response["id"]
    #         print("Free project {0} created with id {1}. Full access granted".format(project_name, project_id))
    #         print(">> Read access key: {0}".format(create_project_response["readAccessKey"]))
    #         print(">> Full access key: {0}".format(create_project_response["fullAccessKey"]))
    #         print("Please store your keys in a safe location. When creating a project as an unauthenticated user, you can never retrieve or reset your keys.")
    #         print("This is a free project. It expires in 30 days and has a maximum storage size of 2GB. Please visit the website for more options.")

    #         client.close()
    #         return KabasProject(project_id = project_id, project_name = project_name, access_type = ProjectAccessType.FULL, project_key = project_key)
            

    def connect_project(self, project_name, project_key = None):

        with KabasClient(project_key = project_key) as client:

            find_project_response = client.find_project(project_name)

            project_id = find_project_response["id"]
            access_type = self._parse_access_type(find_project_response["accessType"])

            print("Project {0} connected with {1} access".format(project_name, access_type.name))

            return KabasProject(project_id = project_id, project_name = project_name, access_type = access_type, project_key = project_key)

    def get_public_projects(self):

        with KabasClient() as client:

            return client.get_public_projects()

    def _parse_access_type(self, access_type_string):

        return ProjectAccessType[access_type_string.upper()]