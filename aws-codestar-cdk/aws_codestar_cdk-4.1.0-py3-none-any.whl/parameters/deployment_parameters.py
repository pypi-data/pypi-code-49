class DeploymentParameters:
    """
    Parameters class. 
    """
    def __init__(self, project_name: str, bucket_name):
        """
        Parameters for project deployment.

        :param project_name: Name of your project, which is also used in naming most of the resources and CloudFormation stacks.
        :param bucket_name: Name of the bucket, where deployment files are located.

        :return No return.
        """
        self.project_name = project_name
        self.bucket_name = bucket_name
