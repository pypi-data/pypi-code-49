# -*- coding: utf-8 -*-

import click
import concurrent.futures
import configparser
import json
import sys
import time
import tuxbuild.build
import tuxbuild.config
import tuxbuild.exceptions
import yaml
import requests
import re
from os.path import expanduser


def is_valid_token(token, config):
    headers = {"Content-type": "application/json", "Authorization": "{}".format(token)}
    kbapi_url = config.get_kbapi_url()
    url = kbapi_url + "/verify"
    for i in range(6):
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return True
        else:
            r.raise_for_status()  # Some unexpected status that's not caught
        time.sleep(2 ** i)  # exponential backoff


def get_config(config_path="~/.config/tuxbuild/config.ini"):
    try:
        return tuxbuild.config.Config(config_path)
    except (
        FileNotFoundError,
        PermissionError,
        configparser.NoSectionError,
        tuxbuild.exceptions.TokenNotFound,
    ) as e:
        raise click.ClickException(e)


def get_auth_token(config):
    token = config.get_auth_token()
    try:
        is_valid_token(token, config)
    except Exception as e:
        print(e)
        raise (click.ClickException("😔 Invalid Token"))
    return token


def get_default_buildset():
    home = expanduser("~")
    return "{}/.config/tuxbuild/builds.yaml".format(home)


def wait_for_object(build_object):
    """ Wait for a build to complete. Return True if the build completed successfully """
    click.echo(click.style("🤔 Queued: ", fg="white", bold=True) + str(build_object))
    build_object.wait_on_status("queued")
    if build_object.tuxbuild_status == "building":
        click.echo(
            click.style("🚀 Building: ", fg="cyan", bold=True) + str(build_object)
        )
        build_object.wait_on_status("building")
    # Check for build result
    status_message = build_object.status_message
    if build_object.tuxbuild_status == "building":
        click.echo(
            click.style("👹 Tuxbuild Timeout: ", fg="bright_red").format(status_message)
            + str(build_object)
        )
        return False
    elif build_object.tuxbuild_status != "complete":
        click.echo(
            click.style("🔧 Tuxbuild Error ({}): ", fg="white").format(status_message)
            + str(build_object)
        )
        return False
    elif build_object.build_status == "fail":
        errors_count = build_object.errors_count
        error_message = ""
        if errors_count != 0:
            error_message = f"({errors_count} errors)"
        if status_message:
            error_message += f" with status message '{status_message}'"
        click.echo(
            click.style("👹 Fail {}: ", fg="bright_red", bold=True).format(error_message)
            + str(build_object)
        )
        return False
    elif build_object.build_status == "pass":
        warnings_count = build_object.warnings_count
        if warnings_count == 0:
            click.echo(
                click.style(
                    "🎉 Pass ({} warnings): ".format(warnings_count),
                    fg="green",
                    bold=True,
                )
                + str(build_object)
            )
        elif warnings_count == 1:
            click.echo(
                click.style(
                    "👾 Pass ({} warning): ".format(warnings_count),
                    fg="yellow",
                    bold=True,
                )
                + str(build_object)
            )
        else:
            click.echo(
                click.style(
                    "👾 Pass ({} warnings): ".format(warnings_count),
                    fg="yellow",
                    bold=True,
                )
                + str(build_object)
            )
        return True
    return False


@click.group()
@click.version_option()  # Implement --version
def cli():
    pass


@cli.command()
@click.option("--git-repo", required=True, help="Git repository")
@click.option("--git-ref", required=True, help="Git reference")
@click.option("--target-arch", required=True, help="Target architecture")
@click.option(
    "--kconfig",
    required=True,
    multiple=True,
    help="Kernel kconfig arguments (may be specified multiple times)",
)
@click.option(
    "--toolchain",
    required=True,
    help="option to choose between gcc-8, gcc-9, clang-8 and clang-9",
)
@click.option(
    "--kconfig-allconfig",
    required=False,
    help=(
        "Argument used only with allyesconfig/allmodconfig/allnoconfig/randconfig."
        "The argument is a path to a file with specific config symbols which you want to override"
    ),
)
@click.option(
    "--json-out",
    required=False,
    help="Write json build status out to a named file path",
    type=click.File("w", encoding="utf-8"),
)
def build(
    git_repo,
    git_ref,
    target_arch,
    kconfig,
    toolchain,
    kconfig_allconfig=None,
    json_out=None,
):
    auth = get_config()
    token = get_auth_token(auth)
    kbapi_url = auth.get_kbapi_url()
    build = tuxbuild.build.Build(
        git_repo,
        git_ref,
        target_arch,
        kconfig,
        toolchain,
        token,
        kbapi_url,
        kconfig_allconfig,
    )
    click.echo("Building Linux Kernel {} at {}".format(git_repo, git_ref))
    try:
        build.build()
    except tuxbuild.exceptions.BadRequest as e:
        raise (click.ClickException(str(e)))
    build_result = wait_for_object(build)
    if json_out:
        json_out.write(json.dumps(build.status, sort_keys=True, indent=4))
    if not build_result:
        sys.exit(1)


def get_tux_config(url, retries=3, sleep=3):
    result = requests.get(url)
    if result.status_code != 200:
        if retries == 0:
            raise tuxbuild.exceptions.TuxbuildError(
                f"Unable to retrieve {url}: {result.reason}"
            )
        time.sleep(sleep)
        return get_tux_config(url, retries - 1, sleep * 2)
    return result.text


@cli.command()
@click.option(
    "--tux-config",
    default=get_default_buildset(),
    help="Path or a web URL to tuxbuild config file",
)
@click.option("--set-name", required=True, help="Set name")
@click.option("--git-repo", required=True, help="Git repository")
@click.option("--git-ref", required=True, help="Git reference")
@click.option("--target-arch", required=False, help="Target architecture")
@click.option(
    "--kconfig",
    required=False,
    multiple=True,
    help="Kernel kconfig arguments (may be specified multiple times)",
)
@click.option(
    "--toolchain",
    required=False,
    help="option to choose between gcc-8, gcc-9, clang-8 and clang-9",
)
@click.option(
    "--kconfig-allconfig",
    required=False,
    help=(
        "Argument used only with allyesconfig/allmodconfig/allnoconfig/randconfig."
        "The argument is a path to a file with specific config symbols which you want to override"
    ),
)
@click.option(
    "--json-out",
    required=False,
    help="Write json build status out to a named file path",
    type=click.File("w", encoding="utf-8"),
)
def build_set(
    tux_config,
    set_name,
    git_repo=None,
    git_ref=None,
    target_arch=None,
    kconfig=(),
    kconfig_allconfig=None,
    toolchain=None,
    json_out=None,
):
    params = {}
    params["git_repo"] = git_repo
    params["git_ref"] = git_ref
    params["target_arch"] = target_arch
    params["kconfig"] = kconfig
    params["kconfig_allconfig"] = kconfig_allconfig
    params["toolchain"] = toolchain
    config = get_config()
    token = get_auth_token(config)
    kbapi_url = config.get_kbapi_url()
    tux_config_regex = re.compile(r"^https?://")
    if tux_config_regex.match(tux_config):
        tux_config_contents = yaml.safe_load(get_tux_config(tux_config))
    else:
        with open(tux_config, "r") as f:
            tux_config_contents = yaml.safe_load(f)

    click.echo("Building Linux Kernel build set {}".format(set_name))
    # Find build named set_name
    build_list = None
    for bs in tux_config_contents.get("sets"):
        if bs.get("name") == set_name:
            build_list = bs.get("builds")
            assert (
                len(build_list) > 0
            ), "build set {} does not contain any builds".format(set_name)
            break

    # Build not found in config
    if not build_list:
        raise click.ClickException(
            "No set named {} found in {}".format(set_name, tux_config)
        )

    # Create build objects. Do this first to take advantage of argument validation
    # before submitting builds
    build_objects = []
    for b in build_list:
        for param in [
            "git_repo",
            "git_ref",
            "target_arch",
            "kconfig",
            "kconfig_allconfig",
            "toolchain",
        ]:
            if params[param]:
                b[param] = params[param]
            elif param not in b:
                raise click.ClickException(
                    "No {} found in command line or in the set {} in {}: {}".format(
                        param, set_name, tux_config, b
                    )
                )

        build_objects.append(
            tuxbuild.build.Build(
                b["git_repo"],
                b["git_ref"],
                b["target_arch"],
                b["kconfig"],
                b["toolchain"],
                token,
                kbapi_url,
                b["kconfig_allconfig"],
            )
        )

    build_set = tuxbuild.build.BuildSet(build_objects, token, kbapi_url)
    build_set.build()

    # Wait for the builds to complete - one watcher thread per build
    # Gather the results in build_results
    build_results = []
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=len(build_objects)
    ) as executor:
        for b in build_objects:
            build_results.append(executor.submit(wait_for_object, b))

    if json_out:
        json_out.write(json.dumps(build_set.status_list, sort_keys=True, indent=4))

    # If any of the builds did not pass, exit with exit code of 1
    if False in [result._result for result in build_results]:
        sys.exit(1)
