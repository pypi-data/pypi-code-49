import logging
import os
from typing import Type

import click

from memfault_cli.authenticator import Authenticator
from memfault_cli.context import MemfaultCliClickContext
from memfault_cli.upload import (
    AndroidAppSymbolsUploader,
    BugreportUploader,
    CoredumpUploader,
    ReleaseArtifactUploader,
    SoftwareArtifactUploader,
    SymbolDirectoryUploader,
    SymbolUploader,
    Uploader,
)

pass_memfault_cli_context = click.make_pass_decorator(MemfaultCliClickContext, ensure=True)


@click.group()
@click.option("--email", help="Account email to authenticate with")
@click.password_option(
    "--password", prompt=False, help="Account password or user API key to authenticate with",
)
@click.option(
    "--project-key", help="Memfault Project Key",
)
@click.option("--org", help="Organization slug")
@click.option("--project", help="Project slug")
@click.option("--url", hidden=True)
@pass_memfault_cli_context
def cli(ctx: MemfaultCliClickContext, **kwargs):
    ctx.obj.update(kwargs)


def _do_upload_or_raise(
    ctx: MemfaultCliClickContext, path: str, uploader_cls: Type[Uploader],
):
    authenticator = Authenticator.create_authenticator_given_context_or_raise(ctx)
    ctx.check_required_cli_args(authenticator=authenticator)

    uploader = uploader_cls(ctx=ctx, file_path=path, authenticator=authenticator)
    if not uploader.can_upload_file():
        raise click.exceptions.UsageError(f"Upload failed!")
    uploader.upload()


@cli.command(name="upload-coredump")
@click.argument("path", type=click.Path(exists=True))
@pass_memfault_cli_context
def upload_coredump(ctx: MemfaultCliClickContext, path: str):
    """Upload a firmware coredump for analysis.

    Coredumps can be added to a firmware platform by integrating the Memfault C SDK:
    https://github.com/memfault/memfault-firmware-sdk
    """
    _do_upload_or_raise(ctx, path, CoredumpUploader)


@cli.command(name="upload-bugreport")
@click.argument("path")
@pass_memfault_cli_context
def upload_bugreport(ctx: MemfaultCliClickContext, path: str):
    """Upload an Android Bug Report for analysis by Memfault."""
    uploader_cls = BugreportUploader
    _do_upload_or_raise(ctx, path, uploader_cls)


@cli.command(name="upload-symbols")
@click.option(
    "--software-type",
    required=False,
    help="Required for firmware builds, see https://mflt.io/34PyNGQ",
)
@click.option(
    "--software-version",
    required=False,
    help="Required for firmware builds, see https://mflt.io/34PyNGQ",
)
@click.argument("path")
@pass_memfault_cli_context
def upload_symbols(ctx: MemfaultCliClickContext, path: str, **kwargs):
    """Upload symbols for a Firmware or Android build."""
    ctx.obj.update(**kwargs)

    if os.path.isdir(path):
        uploader = SymbolDirectoryUploader
    else:
        if ctx.software_info is None:
            uploader = SymbolUploader
        else:
            uploader = SoftwareArtifactUploader

    _do_upload_or_raise(ctx, path, uploader)


@cli.command(name="upload-android-app-symbols")
@click.option(
    "--build-variant",
    required=True,
    help="The build variant for which to upload the Android app symbols",
)
@click.option(
    "--package",
    required=False,
    help="The package identifier of the app. When not specified, it is read from the .apk",
)
@click.option(
    "--version-name",
    required=False,
    help="The version name of the app. When not specified, it is read from the .apk",
)
@click.option(
    "--version-code",
    required=False,
    help="The version code of the app. When not specified, it is read from the .apk",
)
@click.option(
    "--mapping-txt",
    required=False,
    help="The path to the Proguard/R8 mapping.txt file. When not specified, the default locations are searched.",
)
@click.argument("path")
@pass_memfault_cli_context
def upload_android_app_symbols(ctx: MemfaultCliClickContext, path: str, **kwargs):
    """Upload symbols & R8/ProGuard mapping for an Android app build.

    Pass the root 'build' directory of the Android app as argument, for example:

    memfault upload-android-app-symbols --build-variant=release ~/my/app/build

    The command will automatically try to locate the mapping.txt and extract the
    version and package identifier from the .apk file.

    If this automatic behavior does not work in your use case, consider using
    option flags (i.e. --version-code, --version-name, --package, etc.) to specify
    the required information directly.
    """
    ctx.obj.update(**kwargs)
    _do_upload_or_raise(ctx, path, AndroidAppSymbolsUploader)


@cli.command(name="upload-ota-payload")
@click.option("--hardware-version", required=True)
@click.option("--software-type", required=True)
@click.option("--software-version", required=True)
@click.argument("path")
@pass_memfault_cli_context
def upload_ota_payload(ctx: MemfaultCliClickContext, path: str, **kwargs):
    """Upload a binary to be used for a firmware update.

    See https://mflt.io/34PyNGQ for details about 'hardware-version', 'software-type' and
    'software-version' nomenclature.

    When deployed, this is the binary that will be returned from the Memfault /latest endpoint
    which can be used for an Over The Air (OTA) update.
    """
    ctx.obj.update(**kwargs)
    _do_upload_or_raise(ctx, path, ReleaseArtifactUploader)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    cli()


if __name__ == "__main__":
    main()
