import os
import re

from aws_cdk import core, aws_iam, aws_s3, aws_s3_deployment
from aws_empty_bucket.empty_s3_bucket import EmptyS3Bucket
from aws_codestar_cdk.custom.codestar_project import CodeStarProject
from aws_codestar_cdk.parameters.codestar_lambda_parameters import CodeStarLambdaParameters


class LambdaCodeStar:
    """
    Stack management class to create a codestar project and necessary resources for the project.
    """
    PROJECT_ID_MAX_LENGTH = 15

    def __init__(self, scope: core.Stack, params: CodeStarLambdaParameters) -> None:
        """
        Constructor.

        :param scope: A scope in which resources shall be created.
        :param params: Parameters configuring the deployment.
        """
        bucket_name = self.__convert(params.deployment_params.bucket_name)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(dir_path, 'files')
        deployment_files = aws_s3_deployment.Source.asset(path)

        # Deployment parameters.
        project_name = params.deployment_params.project_name

        self.bucket = EmptyS3Bucket(
            scope,
            project_name + 'DeploymentBucket',
            access_control=aws_s3.BucketAccessControl.PRIVATE,
            bucket_name=bucket_name
        )

        self.deployment = aws_s3_deployment.BucketDeployment(
            scope,
            project_name + 'Deployment',
            destination_bucket=self.bucket,
            sources=[deployment_files]
        )

        # Make sure deployment is configured after the bucket is created.
        self.deployment.node.add_dependency(self.bucket)

        # VPC parameters for lambda function.
        subnet_ids = params.vpc_params.subnet_ids_string
        security_group_ids = params.vpc_params.security_group_ids_string

        # Parameters for function invocation
        event_type = params.lambda_type_params.event_type
        lambda_role = params.lambda_type_params.lambda_exec_role

        project_id = self.__convert(project_name)[:self.PROJECT_ID_MAX_LENGTH]

        stack_parameters = {
            "ProjectId": project_name,
            "MySubnetIds": subnet_ids,
            "MySecurityGroupIds": security_group_ids,
            "EventType": event_type,
            "ExecutionRoleArn": lambda_role.role_arn,
            "PascalId": project_id
        }

        if event_type == 'Schedule':
            schedule_expression = params.lambda_type_params.schedule_expression
            stack_parameters["ScheduleExpression"] = schedule_expression

        custom_resource_role = self.__codestar_custom_resource_role(project_name, scope)
        toolchain_role = self.__codestar_toolchain_role(project_name, scope)

        # Create a CodeStar project.
        self.codestar_project = CodeStarProject(
            project_id=project_id,
            project_name=project_name,
            project_description='No description.',
            custom_resource_role=custom_resource_role,
            codestar_toolchain_role=toolchain_role,
            bucket_name=bucket_name,
            stack_parameters=stack_parameters
        ).get_resource(scope)

        """
        Dependencies
        """

        # Since this custom resource would create separate CloudFormation templates for lambda deployment,
        # add main template dependencies in order to have a smooth deletion transition. Not having these
        # dependencies would result in failed stack deletions.
        self.codestar_project.node.add_dependency(params.lambda_type_params.lambda_exec_role)

        for subnet in params.vpc_params.subnets:
            self.codestar_project.node.add_dependency(subnet)

        for sg in params.vpc_params.security_groups:
            self.codestar_project.node.add_dependency(sg)

        # Ensure these resources are deployed before executing codestar-generated CloudFormation templates
        # which do not depend on a current stack.
        self.codestar_project.node.add_dependency(self.bucket)
        self.codestar_project.node.add_dependency(self.deployment)
        self.codestar_project.node.add_dependency(toolchain_role)
        self.codestar_project.node.add_dependency(custom_resource_role)

    @staticmethod
    def __codestar_custom_resource_role(project_name: str, scope: core.Construct) -> aws_iam.Role:
        """
        Creates a role for a codestar custom resource.

        :param project_name: Name of the project.
        :param scope: A scope in which the rould should be created.

        :return: Role.
        """
        policy = aws_iam.PolicyStatement(
            actions=[
                "iam:PassRole",
                "codestar:CreateProject",
                "codestar:UpdateProject",
                "codestar:DeleteProject",
                "s3:GetObject"
            ]
        )
        policy.add_all_resources()

        custom_resource_role = aws_iam.Role(
            scope,
            project_name + 'AwsCodeStarCustomResourceRole',
            assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        )
        custom_resource_role.add_to_policy(policy)

        return custom_resource_role

    @staticmethod
    def __codestar_toolchain_role(project_name: str, scope: core.Construct) -> aws_iam.Role:
        """
        Creates a role for codestar project to create resources defined in toolchain.

        :param project_name: Name of the project.
        :param scope: A scope in which the rould should be created.

        :return: Role.
        """
        return aws_iam.Role(
            scope,
            project_name + 'AwsCodestarServiceRole',
            assumed_by=aws_iam.ServicePrincipal('codestar.amazonaws.com'),
            managed_policies=[
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('AWSLambdaFullAccess'),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSCodeStarServiceRole'),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('AWSCodeStarFullAccess'),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('AWSCloudFormationFullAccess'),
                aws_iam.ManagedPolicy.from_aws_managed_policy_name('IAMFullAccess')
            ]
        )

    @staticmethod
    def __convert(name: str) -> str:
        """
        Converts CamelCase string to pascal-case where underscores are dashes.
        This is required due to S3 not supporting capital letters or underscores.
        """
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()
