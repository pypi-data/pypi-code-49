import os
import boto3
import argparse
import requests


def session_id(sts=boto3.client("sts")):
    arn = sts.get_caller_identity()["Arn"]
    return arn.split("/")[-1]


def get_public_ip():
    return requests.get("https://ifconfig.me/ip").text


def get_args():
    parser = argparse.ArgumentParser()
    gressify = parser.add_argument_group("gressify")
    gressify.add_argument(
        "-i", "--ip", type=str, help="Ipv4 address", default=get_public_ip()
    )
    gressify.add_argument(
        "-g", "--group-id", type=str, help="GroupId of security group", required=True
    )
    gressify.add_argument(
        "-w",
        "--way",
        type=str,
        help="Direction of rule",
        choices=["ingress", "egress"],
        default="ingress",
    )
    gressify.add_argument(
        "-r",
        "--region",
        type=str,
        help="AWS region name",
        default=os.environ.get("AWS_DEFAULT_REGON", "eu-west-1"),
    )
    gressify.add_argument(
        "-d",
        "--description",
        type=str,
        help="Rule description",
        default=f"Added by {session_id()}",
    )
    return vars(parser.parse_args())


def main():
    args = get_args()
    ec2 = boto3.client("ec2", region_name=args["region"])
    response = getattr(ec2, f"authorize_security_group_{args['way']}")(
        GroupId=args["group_id"],
        IpPermissions=[
            {
                "FromPort": 443,
                "ToPort": 443,
                "IpProtocol": "TCP",
                "IpRanges": [
                    {"CidrIp": f"{args['ip']}/32", "Description": args["description"]},
                ],
            }
        ],
    )
    print(f"Response: {response}")
    print(
        f"Successfully created {args['way']} rule for "
        f"<ip={args['ip']}/32> on <group_id={args['group_id']}>"
    )


if __name__ == "__main__":
    main()
