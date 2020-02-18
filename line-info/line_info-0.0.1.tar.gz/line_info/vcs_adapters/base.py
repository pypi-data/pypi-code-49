class BaseVCSAdapter:

    def __init__(self, domain, group, project):
        self.domain = domain
        self.group = group
        self.project = project

    def get_info(self, issue_number):
        raise NotImplementedError()
