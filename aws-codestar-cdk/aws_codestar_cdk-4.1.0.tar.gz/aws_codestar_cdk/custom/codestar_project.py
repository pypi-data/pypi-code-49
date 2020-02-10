from typing import Any, Dict
from aws_cdk import core
from aws_cdk.aws_iam import Role
from aws_cdk.custom_resources import AwsCustomResource


class CodeStarProject:
    """
    Custom CloudFormation resource which manages a CodeStar project.
    """
    def __init__(
            self,
            project_id: str,
            project_name: str,
            project_description: str,
            custom_resource_role: Role,
            codestar_toolchain_role: Role,
            bucket_name: str,
            stack_parameters: Dict[Any, Any]
    ) -> None:
        """
        Constructor.

        :param project_id: Your made up project id. Can be anything in lowercase.
        :param project_name: Your made up project name.
        :param project_description: Your made up project description.
        :param custom_resource_role: A role for a CloudFormation custom resource.
        :param codestar_toolchain_role: A role for a codestar project which will create necessary resources in a toolchain.
        :param bucket_name: A bucket name, where deployment files are.
        :param stack_parameters: Parameters for a toolchain cloudformation stack.
        """
        # Naming.
        self.project_id = project_id
        self.project_name = project_name
        self.project_description = project_description

        # Permissions.
        self.custom_resource_role = custom_resource_role
        self.codestar_toolchain_role = codestar_toolchain_role

        # Other parameters.
        self.bucket_name = bucket_name
        self.stack_parameters = stack_parameters

    def get_resource(self, scope: core.Construct):
        """
        Creates a custom resource to manage a codestar project.

        :param scope: A scope in which this resource should be created.

        :return: Custom resource to manage a codestar project.
        """
        return AwsCustomResource(
            scope,
            self.project_name + "CustomCodeStarResource",
            on_create=self.__on_create(),
            on_update=self.__on_update(),
            on_delete=self.__on_delete(),
            role=self.custom_resource_role
        )

    @staticmethod
    def service_name() -> str:
        """
        Returns a service name that this custom resource manages.

        :return: Service name.
        """
        return 'CodeStar'

    def __on_create(self):
        """
        Creates an "on_create" command.

        :return: A dictionary command.
        """
        # S3 file keys, which coincide with file names in files/folder.
        code_bucket_key = 'source.zip'
        toolchain_bucket_key = 'toolchain.yml'

        return {
            "service": self.service_name(),
            "action": "createProject",
            "parameters": {
                'id': self.project_id,
                'name': self.project_name,
                'sourceCode': [
                    {
                        'destination': {
                            'codeCommit': {
                                'name': self.project_name
                            },
                        },
                        'source': {
                            's3': {
                                'bucketKey': code_bucket_key,
                                'bucketName': self.bucket_name
                            }
                        }
                    },
                ],
                'toolchain': {
                    'source': {
                        's3': {
                            'bucketKey': toolchain_bucket_key,
                            'bucketName': self.bucket_name
                        }
                    },
                    'roleArn': self.codestar_toolchain_role.role_arn,
                    'stackParameters': self.stack_parameters
                }
            },
            "physical_resource_id": self.project_name
        }

    def __on_update(self):
        """
        Creates an "on_update" command".

        :return: A dictionary command.
        """
        return {
            "service": self.service_name(),
            "action": "updateProject",
            "parameters": {
                'id': self.project_id,
                "description": self.project_description,
            },
            "physical_resource_id": self.project_name
        }

    def __on_delete(self):
        """
        Creates an "on_delete" command".

        :return: A dictionary command.
        """
        return {
            "service": self.service_name(),
            "action": "deleteProject",
            "parameters": {
                'id': self.project_id,
                "deleteStack": True,
            },
            "physical_resource_id": self.project_name
        }
