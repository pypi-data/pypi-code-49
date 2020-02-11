import os
import click
from indico_install.config import merge_dicts
from indico_install.utils import run_cmd
from indico_install.infra.init import init

DEFAULT_NODE_CONFIGS = {
    "image-type": "UBUNTU",
    "disk-type": "pd-standard",
    "scopes": '"https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append"',
    "no-enable-autorepair": None,
    "min-nodes": 1,
    "max-nodes": 3,
}

NODE_POOL_TYPES = {
    "default-gpu-pool": {
        "machine-type": "n1-standard-8",
        "accelerator": "type=nvidia-tesla-p4,count=1",
    },
    # N2s do not support GPU and are not supported in us-east4-c
    "default-cpu-pool": {"machine-type": "n1-standard-2"},
    "default-mem-pool": {"machine-type": "n1-standard-8"},
    "default-pool": {"machine-type": "n1-standard-16"},
    "finetune": {
        "machine-type": "n1-standard-8",
        "accelerator": "type=nvidia-tesla-p4,count=1",
    },
}


def nodegroup_args(ng_type, **kwargs):
    args = merge_dicts(DEFAULT_NODE_CONFIGS, NODE_POOL_TYPES[ng_type])
    args.update(kwargs)
    if "accelerator" not in args:
        args["enable-autoscaling"] = None
    return " ".join([f"--{k}" if v is None else f"--{k}={v}" for k, v in args.items()])


@click.group("gke")
@click.pass_context
def gke(ctx):
    """
    Managing a kubernetes cluster on Google Kubernetes Engine
    """
    pass


gke.command("init")(init(__name__))
environment_abbrev = {"production": "prod", "development": "dev"}


@gke.command("create-nodepools")
@click.pass_context
@click.option(
    "--cluster-name", required=True, help="Name of cluster to attach nodepools to"
)
@click.option(
    "--node-pool",
    help=f"additional pools and counts. EX: --node-pool gpu=3 --node-pool finetune=1. Types are {list(NODE_POOL_TYPES.keys())}",
    multiple=True,
)
def create_nodepools(ctx, cluster_name, node_pool=None):
    """
    Creates additional nodepools for existing cluster
    """
    node_pools = {}
    for np in node_pool or []:
        np_type, np_size = np.split("=", 1)
        assert (
            np_type in NODE_POOL_TYPES
        ), f"node_pool type {np_type} is not valid. Please select from {NODE_POOL_TYPES}"
        assert (
            int(np_size) > 0
        ), f"node_pool size {np_size} is not valid. Please specify an int > 0"
        node_pools[np_type] = np_size

    if not node_pools:
        return

    for np, count in node_pools.items():
        run_cmd(
            f"gcloud container node-pools create {np} "
            f"--num-nodes={count} --cluster={cluster_name} " + nodegroup_args(np)
        )


@gke.command("create")
@click.pass_context
@click.argument("environment")
@click.argument("name")
@click.argument("size", type=int)
@click.option("--subnetwork", help="Network to be used")
@click.option(
    "--version", help="GKE Cluster Version", default="1.14.8-gke.33", show_default=True
)
@click.option(
    "--project", help="GKE Project Name", default="new-indico", show_default=True
)
@click.option("--zone", help="GKE zone", default="us-east4-c", show_default=True)
@click.option(
    "-d",
    "--deployment-root",
    default=os.getcwd(),
    show_default=True,
    help="Root directory for installation files",
)
@click.option(
    "--node-pool",
    help=f"additional pools. EX: --node-pool gpu=3 --node-pool finetune=1. Types are {list(NODE_POOL_TYPES.keys())}",
    multiple=True,
)
def create_cluster(
    ctx,
    environment,
    name,
    size,
    subnetwork=None,
    version=None,
    project=None,
    zone=None,
    deployment_root=None,
    node_pool=None,
):
    """
    Creates a GKE cluster through gcloud.

    Don't change the kubernetes version unless absolutely necessary for
        security invulnerabilities/necessary feature

    The network used is default to indico-{environment},
        this will need to be created ahead of time with custom subnets (not auto)

    The subnetwork specified needs to be created in the network
        created in the zone desired.

    Use specific node pools by specifying the nodeSelector in the service
        using indico_pool: <type>. The default pool is default.

    Prod scaling is indico_pool: default = 2, gpu = 1, cpu = 1
    """
    environment = next(
        iter(env for env in {"production", "development"} if environment in env)
    )

    name = name.lower()
    assert environment_abbrev[environment] in name

    size = int(size)
    assert size > 0

    subnetwork = subnetwork or f"{environment}-default"
    network = f"indico-{environment}"

    click.secho(
        f"Creating cluster {name} in {environment} with {size} nodes...",
        fg="red" if environment == "production" else "green",
    )
    # TODO: Check if we need the python2.7 aliasing.
    # If we do, figure out how to install gcloud for python3

    # TODO: this will probably require components installation and will cause the
    # command to fail since its non-interactive.
    run_cmd(
        f"""
        gcloud beta container clusters create {name} \
            --project "{project}" \
            --zone {zone} \
            --username "admin" \
            --cluster-version "{version}" \
            --num-nodes "{size}" \
            --max-nodes "{size + 1}" \
            --min-nodes "{max(1, size - 1)}" \
            --enable-cloud-logging \
            --enable-cloud-monitoring \
            --addons HorizontalPodAutoscaling,HttpLoadBalancing \
            --no-enable-autoupgrade \
            --enable-ip-alias \
            --network "projects/new-indico/global/networks/{network}" \
            --subnetwork "{subnetwork}" \
        """
        + nodegroup_args("default-pool")
    )

    # TODO: Refactor rbac & switch
    # TODO: ensure this actually persists in current session
    run_cmd(
        f"""
        gcloud config set compute/zone {zone}
        gcloud container clusters get-credentials {name} \
            --zone {zone} \
            --project {project}
        """
    )

    email = run_cmd(
        f"""
        cat {deployment_root}/.config/gcloud/configurations/config_default \
            | grep account \
            | awk -F "=" '{{print $2}}'
        """
    )

    user = email.split("@")[0]

    run_cmd(
        f"""kubectl create clusterrolebinding cluster-admin-binding-{user} \
            --clusterrole cluster-admin \
            --user {email}"""
    )
    if node_pool:
        ctx.invoke(create_nodepools, cluster_name=name, node_pool=node_pool)

    # TODO: Wait for nodes to be ready - then run Nvidia-scripts
    # TODO: Nvidia Script
