from string import Template

class KabasFileDetails:

    def __init__(self,
                project_id,
                file_id,
                file_name,
                file_size_bytes,
                latest_version_id,
                url):

        self.project_id = project_id
        self.file_id = file_id
        self.file_name = file_name
        self.file_size_bytes = file_size_bytes

        self.latest_version_id = latest_version_id
        self.url = url

    @staticmethod
    def from_json(project_id, file_json):
       
        try:
            return KabasFileDetails(project_id,
                                    file_json['id'],
                                    file_json['name'],
                                    file_json['sizeBytes'],
                                    file_json['latestVersionId'],
                                    file_json['url'])

        except:
            raise Exception("Could not parse API result for file")

    def __str__(self):

        return Template("Name: $file_name: \n\tbytes: $file_size_bytes").substitute(file_name = self.file_name,
                                                                                    file_size_bytes = self.file_size_bytes)