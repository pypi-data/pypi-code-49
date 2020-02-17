#!/usr/bin/env python3

import sys
import shutil
import tempfile

from random import randint
from urllib.parse import urlparse
from subprocess import check_output, Popen, PIPE
from graphqlclient import GraphQLClient
from .graphql_requests import delete_deployment, \
                              delete_workspace, \
                              create_deployment, \
                              create_workspace, \
                              add_card


def get_client_interactive():
    base_domain = input(
        "Base domain? example - astro.airflow.run (do not include 'app'): "
    ).strip()
    houston_v1 = "https://houston." + base_domain + "/v1"

    token = input(
        "Go to https://app." +
        base_domain +
        "/token and paste the token here: "
    ).strip()
    print(
        "Enter the emails you want to be admins one at a time by typing below,"
        " then pressing enter one time. "
        "Press enter on the new line when you are done"
    )
    client = GraphQLClient(houston_v1)
    client.inject_token(token)
    return client


def check_for_cli_tools():
    required_tools = ["git", "astro", "docker"]
    for tool in required_tools:
        if not shutil.which(tool):
            raise Exception(
                "Please make sure the following tools "
                f"are in your path: {required_tools}"
            )


def astro_deploy(client, workspace_id, release_name):
    endpoint_parsed = urlparse(client.endpoint)
    hostname = endpoint_parsed.hostname.replace("houston.", "")
    print(f"astro auth login {hostname}")
    process = Popen(
        ["astro", "auth", "login", hostname],
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    stream = ""
    while True:
        character = process.stdout.read(1).decode("utf-8")
        sys.stdout.write(character)
        stream += character
        if character == ":":
            if "leave blank for oAuth" in stream:
                process.stdin.write("\n".encode())
            break
    result, err = process.communicate(f"{client.token}\n\n".encode())
    result = result.decode("utf-8")
    err = err.decode("utf-8")
    print(result)
    print(err)
    assert "Successfully authenticated" in result
    with tempfile.TemporaryDirectory() as tmpdirname:
        print("astro airflow init")
        check_output("astro airflow init", shell=True, cwd=tmpdirname)
        print("astro workspace switch")
        print(
            check_output(
                ["astro", "workspace", "switch", workspace_id], cwd=tmpdirname
            ).decode("utf-8")
        )
        print("astro deploy")
        process = Popen(["astro", "deploy", release_name],
                        cwd=tmpdirname, stdout=PIPE)
        for c in iter(lambda: process.stdout.read(1), b""):
            sys.stdout.write(c.decode("utf-8"))


def test(client, workspaces):
    workspace_count = 1
    deployment_count = 1

    for i in range(0, workspace_count):
        workspace_name = f"e2etest-{randint(0,1000000)}"
        response = create_workspace(client, workspace_name)
        workspace_id = response["data"]["createWorkspace"]["id"]
        workspaces[workspace_id] = []
        add_card(client, workspace_id)

    for i in range(0, deployment_count):
        if i % 3 == 0:
            executor = "KubernetesExecutor"
        elif i % 3 == 1:
            executor = "LocalExecutor"
        else:
            executor = "CeleryExecutor"
        deployment_name = f"e2etest-{randint(0,1000000)}"
        workspace_id = list(workspaces.keys())[i % len(workspaces)]
        response = create_deployment(
            client, deployment_name, workspace_id, executor=executor
        )
        deployment_id = response["data"]["createDeployment"]["id"]
        deployment_release_name = \
            response["data"]["createDeployment"]["releaseName"]
        workspaces[workspace_id].append(
            (deployment_id, deployment_release_name))

    for workspace_id, deployments in workspaces.items():
        for deployment_id, release_name in deployments:
            astro_deploy(client, workspace_id, release_name)


def cleanup(client, workspaces):
    for workspace_id, deployments in workspaces.items():
        for deployment_id, release_name in deployments:
            print(f"Deleting deployment {release_name}")
            delete_deployment(client, workspace_id, deployment_id)
        print(f"Deleting workspace {workspace_id}")
        delete_workspace(client, workspace_id)


def main():

    check_for_cli_tools()
    # query user interactively to provide an auth token
    client = get_client_interactive()

    # key = workspace_id, value = list(deployment_id)
    workspaces = {}
    try:
        test(client, workspaces)
    finally:
        cleanup(client, workspaces)


if __name__ == "__main__":
    main()
