from kabas.kabas_file_details import KabasFileDetails

class KabasProjectDetails:

    def __init__(self,
                    project_id,
                    project_name,
                    public,
                    max_size_gb,
                    active,
                    files):

        self.project_id = project_id
        self.project_name = project_name
        self.public = public
        self.max_size_gb = max_size_gb
        self.active = active
        self.files = files

    @staticmethod
    def from_json(project_json):

        try:
            return KabasProjectDetails(project_json['id'],
                                        project_json['name'],
                                        project_json['public'],
                                        project_json['maxSizeGb'],
                                        project_json['isActive'],
                                        list(map(lambda x: KabasFileDetails.from_json(project_json['id'], x), project_json["files"])))
        except:
            raise Exception("Could not parse API result for project")