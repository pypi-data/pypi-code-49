from aws_codestar_cdk.parameters.deployment_parameters import DeploymentParameters
from aws_codestar_cdk.parameters.lambda_type_parameters import LambdaTypeParameters
from aws_codestar_cdk.parameters.vpc_parameters import VpcParameters


class CodeStarLambdaParameters:
    """
    Parameters group class.
    """
    def __init__(
            self,
            vpc_params: VpcParameters,
            deployment_params: DeploymentParameters,
            lambda_type_params: LambdaTypeParameters
    ) -> None:
        """
        Constructor.

        :param vpc_params: VPC defining parameters.
        :param deployment_params: Parameters for how to deploy a lambda application.
        :param lambda_type_params: Lambda type and behaviour parameters.
        """
        self.lambda_type_params = lambda_type_params
        self.deployment_params = deployment_params
        self.vpc_params = vpc_params
