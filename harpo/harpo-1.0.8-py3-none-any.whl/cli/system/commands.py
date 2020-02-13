import click

from harpo.cli.domain.commands import complete_domain_name
from harpo.cli.util import _find_ctx_root_parent, with_harpo_context
from harpo.cli.util import handle_harpo_exceptions
from harpo.exporter import Exporter
from harpo.main import Harpo


@click.group()
def system():
    """Manage Harpo"""
    pass


@system.command()
@click.pass_context
@handle_harpo_exceptions
def init(ctx):
    """Initialize Harpo repository"""
    common_parameters = _find_ctx_root_parent(ctx).params
    base_dir = common_parameters.get("base_dir") or ".harpo"
    Harpo(base_dir, None).initialize()


@system.command()
@click.argument("domain_name", default="ALL", autocompletion=complete_domain_name)
@with_harpo_context
def reencrypt(harpo, common_parameters, domain_name):
    """Re-encrypt the whole Harpo repository or specific domains"""
    if domain_name == "ALL":
        for domain in harpo.domain_list():
            domain.reencrypt(recurse=False)
    else:
        harpo.domains[domain_name].reencrypt()


@system.command()
@click.option("--recurse/-r", is_flag=True, default=True)
@click.argument("destination", type=click.Path(resolve_path=True))
@click.argument("domain_name", autocompletion=complete_domain_name)
@with_harpo_context
def export(harpo, common_parameters, recurse, destination, domain_name):
    """Export domain(s) to another Harpo instance"""
    exporter = Exporter(src_base_dir=harpo.base_dir, gpg_home=harpo.gpg_home, dst_base_dir=destination)
    exporter.export(domain_name, recurse=recurse)
