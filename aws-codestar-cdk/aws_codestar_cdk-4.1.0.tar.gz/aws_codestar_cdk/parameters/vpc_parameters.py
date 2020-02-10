from typing import List
from aws_cdk import aws_ec2


class VpcParameters:
    """
    Parameters class.
    """
    def __init__(self, subnets: List[aws_ec2.ISubnet], security_groups: List[aws_ec2.ISecurityGroup]):
        """
        Parameters for your lambda functions Virtual Private Network configuration.

        :param subnets: List of subnets your function should be deployed to.
        These subnets need a NAT gateway in order for the function to to access the internet.
        :param security_groups: List of security groups for your function.

        :return No return.
        """
        self.__subnets = subnets
        self.__security_groups = security_groups

        self.__subnet_ids = [subnet.subnet_id for subnet in self.__subnets]
        self.__security_group_ids = [sg.security_group_id for sg in self.__security_groups]

        self.__subnet_ids_string = self.__list_to_comma_separated_list(self.__subnet_ids)
        self.__security_group_ids_string = self.__list_to_comma_separated_list(self.__security_group_ids)

    @property
    def subnets(self) -> List[aws_ec2.ISubnet]:
        return self.__subnets

    @property
    def security_groups(self) -> List[aws_ec2.ISecurityGroup]:
        return self.__security_groups

    @property
    def subnet_ids(self) -> List[str]:
        return self.__subnet_ids

    @property
    def security_group_ids(self) -> List[str]:
        return self.__security_group_ids

    @property
    def subnet_ids_string(self) -> str:
        return self.__subnet_ids_string

    @property
    def security_group_ids_string(self) -> str:
        return self.__security_group_ids_string

    @staticmethod
    def __list_to_comma_separated_list(strings: List[str]) -> str:
        """
        Converts a list to a comma separated strings.

        :param strings: A list to modify.

        :return: A string containing list's elements.
        """
        return ', '.join(strings)
