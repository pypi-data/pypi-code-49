# -*- coding: utf-8 -*-
import ipaddress
import json
import os
import random
import shutil
import subprocess
import tempfile

import click
import git

from spell.cli.exceptions import (
    api_client_exception_handler,
    ExitException,
)
from spell.cli.utils import is_installed, cluster_utils
from spell.cli.utils.kube_cluster_templates import (
    eks_cluster_aws_auth_string,
    generate_eks_cluster_autoscaler_yaml,
    generate_eks_cluster_secret_yaml,
    generate_cluster_ambassador_yaml,
)

INGRESS_PORTS = [22, 2376, 9999]  # SSH, Docker Daemon, and Jupyter respectively

cluster_version = 1


@click.command(name="aws",
               short_help="Sets up an AWS VPC as a Spell cluster")
@click.pass_context
@click.option("-n", "--name", "name",
              help="This will be used by Spell for you to identify the cluster")
@click.option("-p", "--profile", "profile",
              help="This AWS profile will be used to get your Access Key ID and Secret as well as your Region. "
                   "You will be prompted to confirm the Key and Region are correct before continuing. "
                   "This key will be used to create all the resources necessary for Spell to manage machines "
                   "in your external VPC. It must have permissions to create these resources.")
# Hidden option for creating cluster inside an existing VPC
# Note this will use all subnets for spell workers
# A new security group will still be created
@click.option("-v", "--vpc", "vpc_id", hidden=True)
def create_aws(ctx, name, profile, vpc_id):
    """
    This command sets an AWS VPC of your choosing as an external Spell cluster.
    This will let your organization run runs in that VPC, so your data never leaves
    your VPC. You set an S3 bucket of your choosing for all run outputs to be written to.
    After this cluster is set up you will be able to select the types and number of machines
    you would like Spell to create in this cluster.

    NOTE: This command uses your AWS credentials, found in ~/.aws/credentials to create the necessary
    AWS resources for Spell to access and manage those machines. Your AWS credentials will
    need permission to setup these resources.
    """

    # Verify the owner is the admin of an org and cluster name is valid
    spell_client = ctx.obj["client"]
    cluster_utils.validate_org_perms(spell_client, ctx.obj["owner"])

    if not name:
        name = click.prompt("Enter a display name for this AWS cluster within Spell")
    if not profile:
        profile = click.prompt("Enter the name of the AWS profile you would like to use", default=u"default")

    with api_client_exception_handler():
        spell_client.validate_cluster_name(name)

    try:
        import boto3
        from botocore.exceptions import BotoCoreError
    except ImportError:
        click.echo("Please pip install boto3 and rerun this command")
        return

    # Setup clients with the provided profile
    try:
        session = boto3.session.Session(profile_name=profile)
        s3 = session.resource("s3")
        ec2 = session.resource("ec2")
        iam = session.resource("iam")
    except BotoCoreError as e:
        click.echo("Failed to set profile {} with error: {}".format(profile, e))
        return

    supports_gpu = session.region_name in (
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-west-1",
        "eu-west-2",
        "us-east-1",
        "us-east-2",
        "us-west-2",
    )
    if not supports_gpu:
        if not click.confirm("AWS does not support GPU types in {}. You can still create a cluster, but it will "
                             "only have access to CPU types - continue?".format(session.region_name)):
            return

    click.echo("""This command will help you
    - Setup an S3 bucket to store your run outputs in
    - Setup a VPC which Spell will spin up workers in to run your jobs
    - Ensure subnets in the VPC in multiple availability zones
    - Setup a Security Group providing Spell SSH and Docker access to workers
    - Setup an IAM role allowing Spell to spin up and down machines and access the S3 bucket""")
    if not click.confirm(
        "All of this will be done with your AWS profile '{}' which has "
        "Access Key ID '{}' and region '{}' - continue?".format(
            profile,
            session.get_credentials().access_key,
            session.region_name)):
        return

    bucket_name = get_bucket_name(s3, session.region_name, name)
    if not vpc_id:
        vpc = get_vpc(ec2, name)
    else:
        vpc = verify_existing_vpc(ec2, vpc_id)
    security_group = get_security_group(ec2, vpc)
    role_arn, external_id, read_policy = get_role_arn(iam, bucket_name)

    with api_client_exception_handler():
        cluster = spell_client.create_aws_cluster(name, role_arn, external_id, read_policy, security_group.id,
                                                  bucket_name, vpc.id, [s.id for s in vpc.subnets.all()],
                                                  session.region_name)
        cluster_utils.echo_delimiter()
        url = "https://web.spell.run/{}/clusters/{}".format(ctx.obj["owner"], cluster["name"])
        click.echo("Your cluster {} is initialized! Head over to the web console to create machine types "
                   "to execute your runs on - {}".format(name, url))

    spell_client.update_cluster_version(cluster["name"], cluster_version)


def eks_init(ctx, cluster, auth_api_url, eks_cluster_name, nodes_min, nodes_max, node_volume_size):
    """
    Create a new EKS cluster for model serving using your current
    AWS credentials. Your profile must have privileges to EC2, EKS, IAM, and
    CloudFormation. You need to have both `kubectl` and `eksctl` installed.
    This command will walk you through the process and allows users to specify
    networking and security options.

    NOTE: This can take a very long time (15-20 minutes), so make sure you are on a
    computer with a stable Internet connection and power before beginning.
    """

    # default auth_api_url to --api-url if it's not overriden by --auth-api-url
    auth_api_url = auth_api_url or ctx.obj["client_args"]["base_url"]

    try:
        import boto3
        from botocore.exceptions import BotoCoreError
        import kubernetes.client
        import kubernetes.config
    except ImportError:
        raise ExitException("boto3 and kubernetes are both required. "
                            "Please `pip install boto3 kubernetes` and rerun this command")

    if not is_installed("aws-iam-authenticator"):
        raise ExitException("`aws-iam-authenticator` is required, please install it before proceeding")
    if not is_installed("eksctl"):
        raise ExitException("`eksctl` is required, please install it before proceeding https://eksctl.io/")
    if not is_installed("kubectl"):
        raise ExitException("`kubectl` is required, please install it before proceeding")

    # Verify valid cluster_name
    spell_client = ctx.obj["client"]
    if cluster["cloud_provider"] != "AWS":
        raise ExitException("Input cluster is using cloud provider {} and therefore cannot use EKS. "
                            "Only AWS is suppported".format(cluster["cloud_provider"]))

    # Setup clients with the provided profile
    aws_profile = click.prompt("We need your AWS profile to get your Access Key ID and Secret "
                               "as well as your Region. \nYou will be prompted to confirm the Key "
                               "and Region are correct before continuing. \nThis key will be used to "
                               "create all the resources necessary to host a cluster for model serving.\n"
                               "It must have permissions to create these resources.\n"
                               "Enter the name of the AWS profile you would like to use",
                               default="default")
    try:
        session = boto3.session.Session(profile_name=aws_profile)
        autoscaling = session.client("autoscaling")
        iam = session.resource("iam")
    except BotoCoreError as e:
        raise ExitException("Failed to set profile {} with error: {}".format(aws_profile, e))
    click.confirm("Profile '{}' has Access Key ID '{}' and region '{}' - continue?".format(
        aws_profile, session.get_credentials().access_key, session.region_name),
        default=True, abort=True)

    response = click.prompt("Create an EKS cluster for model serving? "
                            "You may skip this step if you have previously run it.",
                            type=click.Choice(["create", "skip"])).strip()
    if response == "create":
        vpc_public_subnets = []
        create_new_vpc = click.confirm("Do you want to create a new VPC for your model server EKS cluster?")
        if not create_new_vpc:
            vpc_public_subnets = cluster["networking"]["aws"]["subnets"]
        node_private_networking = click.confirm("Do you want to isolate the nodes of your cluster "
                                                "from the public internet?")
        create_eks_cluster(aws_profile, eks_cluster_name, session, vpc_public_subnets,
                           node_private_networking, nodes_min, nodes_max, node_volume_size)
    elif response == "skip":
        click.echo("Skipping EKS cluster creation, existing contexts are:")
        subprocess.check_call(("kubectl", "config", "get-contexts"))
        kube_ctx = subprocess.check_output(("kubectl", "config", "current-context")).decode('utf-8').strip()
        correct_kube_ctx = click.confirm("Is context '{}' the EKS cluster to use for model serving?".format(kube_ctx))
        if not correct_kube_ctx:
            raise ExitException("Set context to correct EKS cluster with `kubectl config use-context`")

    # Set AWS access credentials in environment for kubectl
    # TODO(peter): Also support temporary role assumption credentials
    kubectl_env = os.environ
    kubectl_env["AWS_ACCESS_KEY_ID"] = session.get_credentials().access_key
    kubectl_env["AWS_SECRET_ACCESS_KEY"] = session.get_credentials().secret_key

    # Set up ClusterAutoscaling
    cluster_utils.echo_delimiter()
    click.echo("Setting up Cluster Autoscaling...")
    try:
        asgs = [asg for asg in autoscaling.describe_auto_scaling_groups()["AutoScalingGroups"]
                if asg["AutoScalingGroupName"].startswith("eksctl-{}-nodegroup".format(eks_cluster_name))]
        if len(asgs) == 0 or len(asgs) > 1:
            raise ExitException("Failed to find AutoScalingGroup for cluster. Contact support@spell.run for assistance")
        ca_yaml = generate_eks_cluster_autoscaler_yaml(nodes_min, nodes_max, asgs[0]["AutoScalingGroupName"])
        with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w+") as f:
            f.write(ca_yaml)
            f.flush()
            subprocess.check_call(("kubectl", "apply", "--filename", f.name), env=kubectl_env)
        click.echo("Cluster Autoscaling set up!")
    except Exception as e:
        click.echo("ERROR: Cluster Autoscaling failed to set up. Error was: {}".format(e), err=True)

    # Set up metrics-server
    cluster_utils.echo_delimiter()
    click.echo("Setting up metrics-server for HPA...")
    tmp_dir = tempfile.mkdtemp()
    try:
        git.Git(tmp_dir).clone("https://github.com/kubernetes-incubator/metrics-server")
        subprocess.check_call(
            ("kubectl", "apply", "--filename", os.path.join(tmp_dir, "metrics-server", "deploy", "1.8+")),
            env=kubectl_env,
        )
        click.echo("metrics-server set up!")
    except Exception as e:
        click.echo("ERROR: metrics-server failed to set up. Error was: {}".format(e), err=True)
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        tmp_dir = None

    # Create "serving" namespace
    cluster_utils.create_serving_namespace(kubernetes.config, kubernetes.client)

    # Give Spell permissions to the cluster
    cluster_utils.echo_delimiter()
    click.echo("Giving Spell permissions to the cluster...")
    try:
        kube_api = kubernetes.client.CoreV1Api()
        conf_map = kube_api.read_namespaced_config_map("aws-auth", "kube-system", exact=True, export=True)
        if "arn:aws:iam::002219003547:role/nodes.prod.spell" in conf_map.data["mapRoles"]:
            click.echo("Spell permissions already in the cluster! Skipping.")
        else:
            conf_map.data["mapRoles"] += eks_cluster_aws_auth_string
            kube_api.replace_namespaced_config_map("aws-auth", "kube-system", conf_map)
            click.echo("Spell permissions granted!")
    except Exception as e:
        click.echo("ERROR: Giving Spell permissions to the cluster failed. Error was: {}".format(e), err=True)

    # Add Ambassador
    cluster_utils.echo_delimiter()
    click.echo("Setting up Ambassador...")
    try:
        response = click.prompt("Would you like your model server to be public or private? "
                                "Spell does not yet support customer provided SSL/TLS certs (coming soon) "
                                "so public will be unauthenticated over HTTP. "
                                "Private will only be accessible from within the VPC of the EKS cluster.",
                                type=click.Choice(["public", "private"])).strip()
        cloud = "eks_public" if response == "public" else "eks"
        ambassador_yaml = generate_cluster_ambassador_yaml(auth_api_url, cloud=cloud)
        with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w+") as f:
            f.write(ambassador_yaml)
            f.flush()
            subprocess.check_call(("kubectl", "apply", "--namespace", "serving", "--filename", f.name), env=kubectl_env)
        click.echo("Ambassador set up!")
    except Exception as e:
        click.echo("ERROR: Setting up Ambassador failed. Error was: {}".format(e), err=True)

    # Create SpellReadS3 IAM User
    cluster_utils.echo_delimiter()
    policy_name = cluster["role_credentials"]["aws"]["read_policy"]
    suffix = policy_name.split("-")[-1]  # Get the ID suffix off the policy name
    user_name = "SpellReadS3User-{}".format(suffix)
    click.echo("Creating and configuring {} IAM user...".format(user_name))
    try:
        existing_users = [u for u in iam.users.all() if user_name == u.name]
        if len(existing_users) > 0:
            user = existing_users[0]
            click.echo("Existing {} user found".format(user_name))
        else:
            user = iam.create_user(UserName=user_name)
            click.echo("New {} user created".format(user_name))
        if len([p for p in user.attached_policies.all() if p.policy_name == policy_name]) == 0:
            matching_policies = [p for p in iam.policies.all() if p.policy_name == policy_name]
            if len(matching_policies) != 1:
                raise ExitException("Found unexpected number of policies named "
                                    "'{}': {}".format(policy_name, len(matching_policies)))
            s3_read_policy = matching_policies[0]
            user.attach_policy(PolicyArn=s3_read_policy.arn)
            click.echo("Policy {} attached to user".format(policy_name))
        for existing_access_key in user.access_keys.all():
            existing_access_key.delete()
        access_key = user.create_access_key_pair()
        iam_access_key, iam_secret_key = access_key.access_key_id, access_key.secret_access_key
        click.echo("{} user new access key pair created".format(user_name))
    except Exception as e:
        raise ExitException("Unable to create and attach IAM policies. Error: {}".format(e))

    # Create secrets on cluster with SpellReadS3 IAM user
    cluster_utils.echo_delimiter()
    click.echo("Setting secrets on the cluster...")
    try:
        secret_yaml = generate_eks_cluster_secret_yaml(iam_access_key, iam_secret_key)
        with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w+") as f:
            f.write(secret_yaml)
            f.flush()
            subprocess.check_call(("kubectl", "apply", "--filename", f.name), env=kubectl_env)
        click.echo("Cluster Secrets set up!")
    except Exception as e:
        raise ExitException("Unable to apply secrets to cluster. Error: {}".format(e))

    # Add StatsD
    cluster_utils.add_statsd()

    # Upload config to Spell API
    cluster_utils.echo_delimiter()
    click.echo("Uploading config to Spell...")
    try:
        with tempfile.NamedTemporaryFile(mode="r", suffix=".yaml") as f:
            cmd = ("eksctl", "utils", "write-kubeconfig",
                   "--profile", aws_profile,
                   "--name", eks_cluster_name,
                   "--kubeconfig", f.name)
            subprocess.check_call(cmd)
            config_yaml = f.read()
        with api_client_exception_handler():
            status_code = spell_client.set_kube_config(cluster["name"], config_yaml)
            if status_code == 202:
                click.echo("Config successfully uploaded to Spell, "
                           "please wait a few minutes for DNS to be processed.")
            else:
                click.echo("Config successfully uploaded to Spell!")
    except Exception as e:
        click.echo("ERROR: Uploading config to Spell failed. Error was: {}".format(e), err=True)

    cluster_utils.echo_delimiter()
    click.echo("Cluster setup complete!")


def create_eks_cluster(aws_profile, cluster_name, session,
                       vpc_public_subnets, node_private_networking,
                       nodes_min, nodes_max, node_volume_size):
    """Create the EKS cluster with eksctl"""

    cmd = [
        "eksctl", "create", "cluster",
        "--profile", aws_profile,
        "--cluster", cluster_name,
        "--region", session.region_name,
        "--version", "1.14",
        "--nodegroup-name", "ng",
        "--node-type", "m5.large",
        "--nodes-min", str(nodes_min),
        "--nodes-max", str(nodes_max),
        "--node-volume-size", str(node_volume_size),
        "--asg-access",
    ]
    if vpc_public_subnets:
        cmd.append("--vpc-public-subnets={}".format(",".join(vpc_public_subnets)))
    if node_private_networking:
        cmd.append("--node-private-networking")

    try:
        click.echo("Creating the cluster. This can take a while...")
        subprocess.check_call(cmd)
        click.echo("Cluster created!")
    except subprocess.CalledProcessError:
        raise ExitException("Failed to run `eksctl`. Make sure it's installed correctly and "
                            "your inputs are valid. Error details are above in the `eksctl` output.")


def get_bucket_name(s3, region, cluster_name):
    from botocore.exceptions import ClientError

    cluster_utils.echo_delimiter()

    bucket_name = click.prompt(
        "Please enter a name for the S3 Bucket Spell will create for run outputs",
        default=u"spell-{}".format(cluster_name.replace("_", "-").lower())).strip()
    if not bucket_name.islower():
        click.echo("AWS does not support capital letters in the bucket name")
        return get_bucket_name(s3, region, cluster_name)
    if "_" in bucket_name:
        click.echo("AWS does not allow underscores in the bucket name")
        return get_bucket_name(s3, region, cluster_name)

    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=bucket_name, ACL="private")
        else:
            s3.create_bucket(Bucket=bucket_name,
                             ACL="private",
                             CreateBucketConfiguration={"LocationConstraint": region})
        click.echo("Created your new bucket {}!".format(bucket_name))
        return bucket_name
    except ClientError as e:
        click.echo("ERROR: Unable to create bucket. AWS error: {}".format(e))
        return get_bucket_name(s3, region, cluster_name)


def get_vpc(ec2, cluster_name):
    from botocore.exceptions import BotoCoreError

    cluster_utils.echo_delimiter()
    click.echo("Creating new VPC")

    # Create VPC
    cidr = u"10.0.0.0/16"
    try:
        vpc = ec2.create_vpc(CidrBlock=cidr)
        vpc.wait_until_available()
        vpc.create_tags(Tags=[{"Key": "Name", "Value": "Spell-{}".format(cluster_name)}])
    except BotoCoreError as e:
        raise ExitException("Unable to create VPC. AWS error: {}".format(e))
    click.echo("Created a new VPC with ID {}!".format(vpc.id))

    # Create subnets
    zones = [z[u'ZoneName'] for z in ec2.meta.client.describe_availability_zones()[u'AvailabilityZones']]
    zones = zones[:8]  # Max at 8 since we use at most 3 bits of the cidr range for subnets
    subnet_bits = 3
    if len(zones) <= 4:
        subnet_bits = 2
    if len(zones) <= 2:
        subnet_bits = 1
    cidr_generator = ipaddress.ip_network(cidr).subnets(subnet_bits)
    subnets = []
    for zone in zones:
        subnet_cidr = str(next(cidr_generator))
        try:
            subnet = vpc.create_subnet(AvailabilityZone=zone, CidrBlock=subnet_cidr)
            # By default give instances launched in this subnet a public ip
            resp = subnet.meta.client.modify_subnet_attribute(SubnetId=subnet.id, MapPublicIpOnLaunch={"Value": True})
            if resp[u'ResponseMetadata'][u'HTTPStatusCode'] != 200:
                click.echo("WARNING: Unable to set subnet {} to launch instances with "
                           "public ip address. This is required for Spell.".format(subnet.id))
            subnets.append(subnet.id)
            click.echo("Created a new subnet {} in your new VPC in availability-zone {} ".format(subnet.id, zone))
        except BotoCoreError as e:
            click.echo(e)
    if len(subnets) == 0:
        raise ExitException("Unable to make any subnets in your new VPC. Contact Spell for support")

    # Create internet gateway
    gateway = ec2.create_internet_gateway()
    resp = vpc.attach_internet_gateway(InternetGatewayId=gateway.id)
    if resp[u'ResponseMetadata'][u'HTTPStatusCode'] != 200:
        raise ExitException("Failed to attach internet gateway {} to vpc".format(gateway.id))
    route_tables = list(vpc.route_tables.all())
    if len(route_tables) == 0:
        raise ExitException("No route table found on VPC, unable to set route for internet gateway")
    route_table = route_tables[0]
    route_table.create_route(DestinationCidrBlock=u'0.0.0.0/0', GatewayId=gateway.id)
    click.echo("Created internet gateway {} for new VPC".format(gateway.id))

    return vpc


# Make sure the VPC exists and has subnets
def verify_existing_vpc(ec2, vpc_id):
    vpc = ec2.Vpc(vpc_id)
    if len(list(vpc.subnets.all())) == 0:
        raise ExitException("VPC {} has no subnets. Subnets are required for creating "
                            "spell worker machines".format(vpc_id))
    if not click.confirm("Found vpc {} with subnets {}. Use these?".format(vpc_id, list(vpc.subnets.all()))):
        raise ExitException("Exiting")
    return vpc


def get_security_group(ec2, vpc):
    from botocore.exceptions import BotoCoreError
    try:
        security_group = vpc.create_security_group(
            GroupName="Spell-Ingress",
            Description="Allows the Spell API SSH and Docker access to worker machines",
        )
        for port in INGRESS_PORTS:
            security_group.authorize_ingress(CidrIp="0.0.0.0/0", FromPort=port, ToPort=port, IpProtocol="tcp")
        security_group.authorize_ingress(IpPermissions=[{
            'IpProtocol': '-1',
            'FromPort': 0,
            'ToPort': 65355,
            'UserIdGroupPairs': [{'GroupId': security_group.id, 'VpcId': security_group.vpc_id}],
        }])
        click.echo("Successfully created security group {}".format(security_group.id))
        return security_group
    except BotoCoreError as e:
        raise ExitException("Unable to create new security group in VPC. AWS error: {}".format(e))


# Returns a tuple of
# role_arn: the full ARN of the IAM role
# external_id: the external_id required to assume this role
# read_policy: the name of the s3 policy that allows read access to selected buckets
def get_role_arn(iam, bucket_name):
    from botocore.exceptions import ClientError

    cluster_utils.echo_delimiter()
    click.echo("Creating new IAM role")

    write_bucket_arn = "arn:aws:s3:::{}".format(bucket_name)
    write_bucket_objects_arn = "arn:aws:s3:::{}/*".format(bucket_name)

    suffix = str(random.randint(10**6, 10**7))
    read_policy = "SpellReadS3-{}".format(suffix)
    policies = {
        "SpellEC2-{}".format(suffix): [
            {
                "Sid": "EC2",
                "Effect": "Allow",
                "Action": [
                    "s3:GetAccountPublicAccessBlock",
                    "s3:HeadBucket",
                    "ec2:DescribeInstances",
                    "ec2:DescribeImages",
                    "ec2:DescribeVolumes",
                    "ec2:DescribeSpotInstanceRequests",
                    "ec2:RequestSpotInstances",
                    "ec2:RunInstances",
                    "ec2:CreateKeyPair",
                    "ec2:DeleteKeyPair",
                    "ec2:CreateTags",
                    "ec2:DescribeVolumesModifications",
                    "ec2:ModifyVolume",
                    "ec2:AttachVolume"
                ],
                "Resource": "*"
            },
            {
                "Sid": "EC2Terminate",
                "Effect": "Allow",
                "Action": [
                    "ec2:TerminateInstances",
                    "ec2:DeleteVolume"
                ],
                "Resource": "*",
                "Condition": {
                    "StringEquals": {
                        "ec2:ResourceTag/spell-machine": "true"
                    }
                }
            }
        ],
        read_policy: {
            "Sid": "ReadS3",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketByTags",
                "s3:GetLifecycleConfiguration",
                "s3:GetBucketTagging",
                "s3:GetInventoryConfiguration",
                "s3:GetObjectVersionTagging",
                "s3:ListBucketVersions",
                "s3:GetBucketLogging",
                "s3:ListBucket",
                "s3:GetAccelerateConfiguration",
                "s3:GetBucketPolicy",
                "s3:GetObjectVersionTorrent",
                "s3:GetObjectAcl",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketRequestPayment",
                "s3:GetObjectVersionAcl",
                "s3:GetObjectTagging",
                "s3:GetMetricsConfiguration",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketPolicyStatus",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketWebsite",
                "s3:GetBucketVersioning",
                "s3:GetBucketAcl",
                "s3:GetBucketNotification",
                "s3:GetReplicationConfiguration",
                "s3:ListMultipartUploadParts",
                "s3:GetObject",
                "s3:GetObjectTorrent",
                "s3:GetBucketCORS",
                "s3:GetAnalyticsConfiguration",
                "s3:GetObjectVersionForReplication",
                "s3:GetBucketLocation",
                "s3:GetObjectVersion"
            ],
            "Resource": [write_bucket_arn, write_bucket_objects_arn]
        },
        "SpellWriteS3-{}".format(suffix): {
            "Sid": "WriteS3",
            "Effect": "Allow",
            "Action": [
                "s3:PutAnalyticsConfiguration",
                "s3:PutAccelerateConfiguration",
                "s3:DeleteObjectVersion",
                "s3:ReplicateTags",
                "s3:RestoreObject",
                "s3:ReplicateObject",
                "s3:PutEncryptionConfiguration",
                "s3:DeleteBucketWebsite",
                "s3:AbortMultipartUpload",
                "s3:PutBucketTagging",
                "s3:PutLifecycleConfiguration",
                "s3:PutObjectTagging",
                "s3:DeleteObject",
                "s3:PutBucketVersioning",
                "s3:DeleteObjectTagging",
                "s3:PutMetricsConfiguration",
                "s3:PutReplicationConfiguration",
                "s3:PutObjectVersionTagging",
                "s3:DeleteObjectVersionTagging",
                "s3:PutBucketCORS",
                "s3:PutInventoryConfiguration",
                "s3:PutObject",
                "s3:PutBucketNotification",
                "s3:PutBucketWebsite",
                "s3:PutBucketRequestPayment",
                "s3:PutBucketLogging",
                "s3:ReplicateDelete"
            ],
            "Resource": [write_bucket_arn, write_bucket_objects_arn]
        }
    }

    spell_aws_arn = "arn:aws:iam::002219003547:root"
    external_id = str(random.randint(10**8, 10**9))
    assume_role_policy = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": spell_aws_arn
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "sts:ExternalId": external_id
                    }
                }
            }
        ]
    })

    try:
        role_name = "SpellAccess-{}".format(suffix)
        role = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=assume_role_policy,
            Description="Grants Spell EC2 and S3 access")
    except ClientError as e:
        raise ExitException("Unable to create new IAM role. AWS error: {}".format(e))

    try:
        for name, statement in policies.items():
            iam_policy = iam.create_policy(
                PolicyName=name,
                PolicyDocument=json.dumps({"Version": "2012-10-17", "Statement": statement}))
            role.attach_policy(PolicyArn=iam_policy.arn)
    except ClientError as e:
        raise ExitException("Unable to create and attach IAM policies. AWS error: {}".format(e))

    click.echo("Successfully created IAM role {}".format(role_name))
    return role.arn, external_id, read_policy


def get_session(profile, message=""):
    try:
        import boto3
        import botocore
    except ImportError:
        click.echo("Please pip install boto3 and rerun this command")
        return None
    try:
        session = boto3.session.Session(profile_name=profile)
    except botocore.exceptions.BotoCoreError as e:
        click.echo("Failed to set profile {} with error: {}".format(profile, e))
        return None
    if message:
        click.echo(message)
    if not click.confirm(
        "All of this will be done with your AWS profile '{}' which has "
        "Access Key ID '{}' and region '{}' - continue?".format(
            profile,
            session.get_credentials().access_key,
            session.region_name)):
        return None
    return session


@click.pass_context
def add_s3_bucket(ctx, bucket_name, cluster, profile):
    """
    This command adds a cloud storage bucket to SpellFS, which enables interaction with the bucket objects
    via ls, cp, and mounts. It will also add bucket read permissions to the AWS role associated with the
    cluster.

    NOTE: This command uses your AWS credentials, found in ~/.aws/credentials to create the necessary
    AWS resources for Spell to access the remote storage bucket. Your AWS credentials will
    need permission to setup these resources.
    """
    spell_client = ctx.obj["client"]
    cluster_name = cluster['name']

    message = """This command will
    - List your buckets to generate an options menu of buckets that can be added to Spell
    - Add list and read permissions for that bucket to the IAM role associated with the cluster"""
    session = get_session(profile, message)
    if not session:
        return

    import botocore
    from botocore.exceptions import BotoCoreError
    # Set up clients with the provided profile
    try:
        s3 = session.resource("s3")
        iam = session.resource("iam")
    except BotoCoreError as e:
        click.echo("Failed to get clients with profile {}: {}".format(profile, e))
        return

    # Get all buckets
    all_buckets = [bucket.name for bucket in s3.buckets.all()]

    # Prompt for bucket name
    if bucket_name is None:
        bucket_names = [bucket.name for bucket in s3.buckets.all()]
        for bucket in bucket_names:
            click.echo("- {}".format(bucket))
        bucket_name = click.prompt("Please choose a bucket")

    # Check if bucket is public if the bucket name is not one of the returned
    bucket_is_public = False
    if bucket_name not in all_buckets:
        # Set up an anonymous client
        anon_s3 = session.resource("s3", config=botocore.client.Config(signature_version=botocore.UNSIGNED))
        try:
            list(anon_s3.Bucket(bucket_name).objects.limit(count=1))
        except botocore.exceptions.ClientError:
            click.echo("Bucket {} is not accessible".format(bucket_name))
            return
        bucket_is_public = True

    # Skip IAM role management logic if bucket is public
    if bucket_is_public:
        click.echo("Bucket {} is public, no IAM updates required.".format(bucket_name))
        with api_client_exception_handler():
            spell_client.add_bucket(bucket_name, cluster_name, "s3")
        click.echo("Bucket {} has been added to cluster {}!".format(bucket_name, cluster_name))
        return

    # Add bucket read permissions to policy
    policy_name = cluster["role_credentials"]["aws"]["read_policy"]
    policies = [p for p in iam.policies.all() if p.policy_name == policy_name]
    if len(policies) != 1:
        click.echo("Found {} policies with name {}".format(len(policies), policy_name))
        return
    policy = policies[0]
    current_policy_version = policy.default_version
    policy_document = current_policy_version.document
    statements = policy_document["Statement"]
    if isinstance(statements, list):
        if len(statements) != 1:
            click.echo(
                "Unexpected number of statements in policy document {}, "
                "expecting one. Statements:\n{}".format(policy_name, statements)
            )
            return
        read_resources = statements[0]["Resource"]
    else:
        read_resources = statements["Resource"]
        policy_document["Statement"] = [statements]
    bucket_arn = "arn:aws:s3:::{}".format(bucket_name)
    if read_resources != "*" and bucket_arn not in read_resources:
        policy_document["Statement"][0]["Resource"] += [bucket_arn, bucket_arn+"/*"]
        click.echo("Creating new version of policy {} with read access to {}...".format(policy.arn, bucket_name))
        new_version = policy.create_version(PolicyDocument=json.dumps(policy_document), SetAsDefault=True)
        click.echo("Created new version {} of policy {}.".format(new_version.arn, policy.arn))
        click.echo("Pruning old version {} of policy {}...".format(current_policy_version.arn, policy.arn))
        current_policy_version.delete()
    else:
        click.echo("Policy {} has permissions to access {}".format(policy.arn, bucket_arn))

    # Register new bucket to cluster in API
    with api_client_exception_handler():
        spell_client.add_bucket(bucket_name, cluster_name, "s3")
    click.echo("Bucket {} has been added to cluster {}!".format(bucket_name, cluster_name))


@click.pass_context
def add_ec_registry(ctx, repo_name, cluster, profile):
    """
    This command adds docker repository read permissions to the AWS role associated with the
    cluster.

    NOTE: This command uses your AWS credentials, found in ~/.aws/credentials to give
    Spell access to the docker images in a repository in your container registry.
    Your AWS credentials will need permission to setup these resources.
    """

    message = """This command will
    - Allow Spell to get authorization tokens to access your docker registry
    - If no repository is specified, list your repositories in the registry
    - Add read permissions for that repository to the IAM role associated with the cluster"""
    session = get_session(profile, message)
    if not session:
        return

    import botocore
    # Set up clients with the provided profile
    try:
        iam = session.resource("iam")
        ecr = session.client("ecr")
    except botocore.exceptions.BotoCoreError as e:
        click.echo("Failed to get clients with profile {}: {}".format(profile, e))
        return

    account_id = iam.CurrentUser().arn.split(':')[4]
    # Get all repositories
    all_repo_names = [repo['repositoryName'] for repo in ecr.describe_repositories()['repositories']]
    valid_repo_name = repo_name in all_repo_names
    if repo_name and not valid_repo_name:
        click.echo("No repository named {} found".format(repo_name))
    # Get repos Spell has access to
    read_policy_name = cluster["role_credentials"]["aws"]["read_policy"]
    policy_name = read_policy_name.replace("SpellReadS3", "SpellReadECR")
    policies = [p for p in iam.policies.all() if p.policy_name == policy_name]
    read_resources = []
    repo_arn_prefix = "arn:aws:ecr:*:{}:repository/{}"
    if policies:
        policy = policies[0]
        current_policy_version = policy.default_version
        policy_document = current_policy_version.document
        read_resources = policy_document["Statement"]["Resource"]
        if repo_arn_prefix.format(account_id, repo_name) in read_resources:
            click.echo("Policy {} already has permissions to access {}".format(policy.arn, repo_name))
            return
    repo_names = [n for n in all_repo_names if repo_arn_prefix.format(account_id, n) not in read_resources]
    if not repo_names:
        click.echo("Spell already has access to all repos found in your AWS account")
        return
    # Prompt for repository name
    if not valid_repo_name:
        click.echo("Spell does not yet have access to the following repos found in your AWS account:")
        for repo in repo_names:
            click.echo("- {}".format(repo))
        while not valid_repo_name:
            repo_name = click.prompt("Please choose a repository")
            valid_repo_name = repo_name in repo_names
            if not valid_repo_name:
                if repo_name not in all_repo_names:
                    click.echo("No repository named {} found".format(repo_name))
                else:
                    click.echo("Spell already has permissions to access {}".format(repo_name))

    token_policy_name = read_policy_name.replace("SpellReadS3", "SpellAuthToken")
    roleArn = cluster['role_credentials']['aws']['role_arn']
    role = iam.Role(roleArn.split('/')[-1])
    update_token_authorization_policy(iam, True, token_policy_name, role)

    # Add repository read permissions to policy
    repo_arn = repo_arn_prefix.format(account_id, repo_name)
    if len(policies) == 0:
        statement = {
            "Sid": "ReadECR",
            "Effect": "Allow",
            "Action": [
                    "ecr:Get*",
                    "ecr:List*",
                    "ecr:Describe*",
                    "ecr:BatchGetImage",
                    "ecr:BatchCheckLayerAvailability"
                ],
            "Resource": [repo_arn]
        }
        try:
            policy = iam.create_policy(
                PolicyName=policy_name,
                PolicyDocument=json.dumps({"Version": "2012-10-17", "Statement": statement}))
            role.attach_policy(PolicyArn=policy.arn)
            click.echo("You can now run using images from repository {}".format(repo_name))
        except botocore.exceptions.ClientError as e:
            raise ExitException("Unable to create and attach read policy to repository {}."
                                " AWS error: {}".format(repo_name, e))
    else:
        if read_resources != "*" and repo_arn not in read_resources:
            read_resources.append(repo_arn)
            click.echo("Creating new version of policy {} with read access to {}...".format(policy.arn, repo_name))
            new_version = policy.create_version(PolicyDocument=json.dumps(policy_document), SetAsDefault=True)
            click.echo("Created new version {} of policy {}.".format(new_version.arn, policy.arn))
            click.echo("Pruning old version {} of policy {}...".format(current_policy_version.arn, policy.arn))
            current_policy_version.delete()
            click.echo("Successfully added read permission to {}".format(repo_name))
        else:
            click.echo("Policy {} already has permissions to access {}".format(policy.arn, repo_name))


@click.pass_context
def delete_ec_registry(ctx, repo_name, cluster, profile):
    """
    This command removes docker repository read permissions to the AWS role associated with the
    cluster.

    NOTE: This command uses your AWS credentials, found in ~/.aws/credentials to remove
    Spell access to the docker images in a repository in your container registry.
    Your AWS credentials will need permission to setup these resources.
    """

    message = """This command will
    - Optionally disable Spell from getting authorization tokens to access your registry
    - If no repository is specified, list repositories Spell has access to
    - Remove read permissions for chosen repository from the IAM role associated with the cluster"""
    session = get_session(profile, message)
    if not session:
        return

    import botocore
    # Set up clients with the provided profile
    try:
        iam = session.resource("iam")
    except botocore.exceptions.BotoCoreError as e:
        click.echo("Failed to get clients with profile {}: {}".format(profile, e))
        return

    read_policy_name = cluster["role_credentials"]["aws"]["read_policy"]
    token_policy_name = read_policy_name.replace("SpellReadS3", "SpellAuthToken")
    roleArn = cluster['role_credentials']['aws']['role_arn']
    role = iam.Role(roleArn.split('/')[-1])
    policy_name = read_policy_name.replace("SpellReadS3", "SpellReadECR")
    policies = [p for p in iam.policies.all() if p.policy_name == policy_name]
    if len(policies) == 0:
        click.echo("Spell does not have access to any docker repositories in your registry")
        return

    policy = policies[0]
    current_policy_version = policy.default_version
    policy_document = current_policy_version.document
    read_resources = policy_document["Statement"]["Resource"]
    # Get all repositories Spell has access to
    repo_names = [arn.split('/')[-1] for arn in read_resources]
    valid_repo_name = repo_name in repo_names
    if repo_name and not valid_repo_name:
        click.echo("Spell has no access to repository named {}".format(repo_name))
    # Prompt for repository name
    if not valid_repo_name:
        click.echo("Spell has access to the following repos:")
        for repo in repo_names:
            click.echo("- {}".format(repo))
        while not valid_repo_name:
            repo_name = click.prompt("Please choose a repository")
            valid_repo_name = repo_name in repo_names
            if not valid_repo_name:
                click.echo("Spell has no access to repository named {}".format(repo_name))

    # Remove repository read permissions to policy
    account_id = iam.CurrentUser().arn.split(':')[4]
    repo_arn = "arn:aws:ecr:*:{}:repository/{}".format(account_id, repo_name)
    if repo_arn in read_resources:
        read_resources.remove(repo_arn)
        if read_resources:
            click.echo("Creating new version of policy {} without read access to {}...".format(policy.arn, repo_name))
            new_version = policy.create_version(PolicyDocument=json.dumps(policy_document), SetAsDefault=True)
            click.echo("Created new version {} of policy {}.".format(new_version.arn, policy.arn))
            click.echo("Pruning old version {} of policy {}...".format(current_policy_version.arn, policy.arn))
            current_policy_version.delete()
        else:
            role.detach_policy(PolicyArn=policy.arn)
            click.echo("Removing ECR policy and token generation policy as no remaining ECR repos are accessible.")
            policy.delete()
            update_token_authorization_policy(iam, False, token_policy_name, role)
        click.echo("Access to {} has been removed".format(repo_name))
    else:
        click.echo("Spell does not have permissions to access {}".format(repo_name))


def update_token_authorization_policy(iam, add, policy_name, role):
    from botocore.exceptions import ClientError
    matching_policies = [p for p in iam.policies.all() if p.policy_name == policy_name]
    if len(matching_policies) > 1:
        raise ExitException("Found unexpected number of get authorization tokens policies named "
                            "'{}': {}".format(policy_name, len(matching_policies)))
    if add:
        if len(matching_policies) == 1:
            return
        if not click.confirm("Give Spell permission to get authorization tokens?"
                             " Spell needs both token and read permission to pull private docker images from ECR."):
            raise ExitException("Spell cannot access docker registry without the ability to"
                                " get authorization tokens")
        statement = {
            "Sid": "GetAuthorizationToken",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
        try:
            iam_policy = iam.create_policy(
                PolicyName=policy_name,
                PolicyDocument=json.dumps({"Version": "2012-10-17", "Statement": statement}))
            role.attach_policy(PolicyArn=iam_policy.arn)
        except ClientError as e:
            raise ExitException("Unable to create and attach token authorization policy. AWS error: {}".format(e))
    else:
        if len(matching_policies) == 1:
            policy = matching_policies[0]
            role.detach_policy(PolicyArn=policy.arn)
            policy.delete()


@click.pass_context
def update_aws_cluster(ctx, profile, cluster):
    """
    This command idempotently makes sure that any updates needed since you ran cluster init are available.

    NOTE: This command uses your AWS credentials, found in ~/.aws/credentials to create the necessary
    AWS resources for Spell to access the remote storage bucket. Your AWS credentials will
    need permission to setup these resources.
    """
    try:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError
    except ImportError:
        click.echo("Please pip install boto3 and rerun this command")
        return

    try:
        session = boto3.session.Session(profile_name=profile)
    except BotoCoreError as e:
        click.echo("Failed to set profile {} with error: {}".format(profile, e))
        return

    # Retrieve Spell cluster
    spell_client = ctx.obj["client"]

    click.echo("""This command will
    - Update your security group ingress rules""")
    if not click.confirm(
        "This will be done with your AWS profile '{}' which has "
        "Access Key ID '{}' and region '{}' - continue?".format(
            profile,
            session.get_credentials().access_key,
            session.region_name)):
        return

    # Set up clients with the provided profile
    try:
        ec2 = session.resource("ec2")
    except BotoCoreError as e:
        click.echo("Failed to get clients with profile {}: {}".format(profile, e))
        return

    id = cluster["networking"]["aws"]["security_group_id"]
    security_group = ec2.SecurityGroup(id)
    for port in INGRESS_PORTS:
        try:
            security_group.authorize_ingress(CidrIp="0.0.0.0/0", FromPort=port, ToPort=port, IpProtocol="tcp")
        except ClientError as e:
            if "InvalidPermission.Duplicate" not in e.message:
                click.echo(e.message)
                return
    try:
        security_group.authorize_ingress(IpPermissions=[{
            'IpProtocol': '-1',
            'FromPort': 0,
            'ToPort': 65355,
            'UserIdGroupPairs': [{'GroupId': security_group.id, 'VpcId': security_group.vpc_id}],
        }])
    except ClientError as e:
        if "InvalidPermission.Duplicate" not in e.message:
            click.echo(e.message)
            return

    spell_client.update_cluster_version(cluster["name"], cluster_version)

    click.echo("Congratulations, your cluster {} is up to date".format(cluster["name"]))


def delete_aws_cluster(ctx, cluster, profile, keep_vpc):
    """
    Deletes an AWS cluster, including the Spell Cluster, Machine Types,
    Model Servers, VPC, IAM role, and IAM policies associated with this cluster.
    """

    spell_client = ctx.obj["client"]
    cluster_utils.validate_org_perms(spell_client, ctx.obj["owner"])

    try:
        import boto3
        from botocore.exceptions import BotoCoreError
    except ImportError:
        click.echo("Please pip install boto3 and rerun this command")
        return

    try:
        if not profile:
            profile = click.prompt("Enter the name of the AWS profile you would like to use", default=u"default")
        session = boto3.session.Session(profile_name=profile)
        s3 = session.resource("s3")
        ec2 = session.resource("ec2")
        iam = session.resource("iam")
    except BotoCoreError as e:
        click.echo("Failed to set profile {} with error: {}".format(profile, e))
        return
    click.echo("This command will delete the Spell Cluster, Machine Types, Model Servers, "
               "VPC, IAM role, and IAM policies associated with this cluster. It will also "
               "prompt with the option to delete the output bucket.")
    if not click.confirm("Are you SURE you want to delete the spell cluster {}?".format(cluster["name"])):
        return

    if not click.confirm(
        "The deletion will use AWS profile '{}' which has "
        "Access Key ID '{}' and region '{}' - continue?".format(
            profile,
            session.get_credentials().access_key,
            session.region_name)):
        return

    # Delete Machine Types and Model Servers on cluster first
    with api_client_exception_handler():
        click.echo("Sending message to Spell to remove all Machine Types "
                   "from the cluster {}...".format(cluster["name"]))
        spell_client.delete_cluster_contents(cluster["name"])

    # Delete associated EKS cluster if it exists
    if cluster["has_kube_config"]:
        delete_eks_cluster(profile)

    # Block until cluster is drained. This is necessary because the API will fail to
    # drain if we delete the IAM role before the machine types are marked as drained
    cluster_utils.block_until_cluster_drained(spell_client, cluster["name"])

    # Delete VPC
    if not keep_vpc:
        vpc_id = cluster['networking']['aws']['vpc_id']
        click.echo("Deleting VPC {}".format(vpc_id))
        from botocore.exceptions import ClientError
        try:
            vpc = ec2.Vpc(vpc_id)
            # Delete subnets
            for subnet in vpc.subnets.all():
                subnet.delete()
                click.echo("Deleted subnet {}".format(subnet.id))
            # Delete internet gateway(s)
            for gateway in vpc.internet_gateways.all():
                vpc.detach_internet_gateway(InternetGatewayId=gateway.id)
                gateway.delete()
                click.echo("Deleted gateway {}".format(gateway.id))
            # Delete security group(s)
            for group in vpc.security_groups.all():
                if group.group_name == 'default':
                    continue
                group.delete()
                click.echo("Deleted security group {}".format(group.id))
            # Delete VPC
            vpc.delete()
            click.echo("Deleted VPC {}".format(vpc.id))
        except ClientError as e:
            # If the VPC is already deleted return True for success
            if e.response['Error']['Code'] == 'InvalidVpcID.NotFound':
                click.echo("VPC {} is already deleted!".format(vpc.id))
            else:
                click.echo("Failed to delete VPC {}: {}".format(vpc.id, e))

    # Delete IAM
    def getNameFromArn(arn):
        return arn.split('/')[-1]
    roleArn = cluster['role_credentials']['aws']['role_arn']
    roleName = getNameFromArn(roleArn)
    click.echo("Deleting Role {}".format(roleName))
    from botocore.exceptions import ClientError
    try:
        role = iam.Role(roleName)
        # Delete policies
        for policy in role.attached_policies.all():
            role.detach_policy(PolicyArn=policy.arn)
            policy.delete()
            click.echo("Deleted policy {}".format(getNameFromArn(policy.arn)))
        # Delete role
        role.delete()
        click.echo("Deleted role {}".format(roleName))
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            click.echo("Role {} is already deleted!".format(roleName))
        else:
            click.echo("Failed to delete role {}: {}".format(roleName, e))

    # Optionally delete the output bucket
    bucket = cluster['storage_uri']
    if click.confirm("Delete bucket {}? WARNING: This will delete all the data in the bucket".format(bucket)):
        try:
            bucketObj = s3.Bucket(bucket)
            bucketObj.objects.all().delete()
            bucketObj.delete()
            click.echo("Deleted bucket {}".format(bucket))
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                click.echo("Bucket {} is already deleted!".format(bucket))
            else:
                click.echo("Failed to delete bucket {}: {}".format(bucket, e))

    # Last step is to mark the cluster as deleted
    with api_client_exception_handler():
        spell_client.delete_cluster(cluster["name"])
        click.echo("Successfully deleted cluster on Spell")


def delete_eks_cluster(profile):
    if not is_installed("eksctl"):
        if click.confirm("Detected an associated Model Server EKS Cluster but `eksctl` "
                         "is not installed. This command will not be able to delete the Model Server cluster. "
                         "Would you like to skip this step and continue with deleting this cluster? "
                         "Skipping will mean you must delete the EKS cluster manually."):
            return
        else:
            raise ExitException("`eksctl` is required, please install it before proceeding https://eksctl.io/")
    click.echo("Detected an associated Model Server EKS Cluster. Listing out the known EKS clusters:")
    try:
        cmd = ["eksctl", "get", "clusters", "--profile", profile]
        subprocess.check_call(cmd)
        if click.confirm("Would you like to delete the associated Model Server EKS cluster "
                         "listed above? If you do NOT see it listed above, respond 'n' to skip "
                         "this step."):
            eks_name = click.prompt("What is the name of the EKS cluster? "
                                    "Please choose one of the names listed above. "
                                    "NOTE: This is the name used in EKS, NOT the name in Spell)",
                                    default=u"spell-model-serving").strip()
            click.echo("Deleting EKS cluster {}. This can take a while!".format(eks_name))
            cmd = ["eksctl", "delete", "cluster", "--name", eks_name, "--profile", profile]
            subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        click.echo("Failed to run `eksctl`. Make sure it's installed correctly and "
                   "your inputs are valid. Error details are above in the `eksctl` output. "
                   "You will need to delete your EKS cluster using eksctl manually.")
