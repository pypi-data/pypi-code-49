"""Unipart OpenStack port client tools"""

from netaddr import valid_ipv6
from openstackclient.i18n import _
from osc_lib.command import command
from osc_lib.exceptions import CommandError
from osc_lib.utils import format_list_of_dicts


class CreateRoutingPort(command.ShowOne):
    """Create a subnet routing port"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--network', metavar='<network>',
            help=_("Network (name or ID)"),
        )
        parser.add_argument(
            '--dns-name', metavar='<dns-name>',
            help=_("DNS hostname"),
        )
        parser.add_argument(
            '--prefix-length', metavar='<prefix-length>', type=int, default=60,
            help=_("Prefix length for subnet allocation from subnet pool"),
        )
        parser.add_argument(
            'name', metavar='<name>',
            help=_("Subnet routing port name"),
        )
        return parser

    def take_action(self, parsed_args):
        mgr = self.app.client_manager
        if parsed_args.network is None:
            parsed_args.network = parsed_args.name.split('-', 1)[0]
        if parsed_args.dns_name is None:
            parsed_args.dns_name = parsed_args.name.split('-', 1)[1]
        network = mgr.network.find_network(parsed_args.network,
                                           ignore_missing=False)

        # Create subnet
        if mgr.network.find_subnet(parsed_args.name):
            raise CommandError('Subnet %s already exists' % parsed_args.name)
        subnet = mgr.network.create_subnet(
            name=parsed_args.name,
            project_id=network.project_id,
            network_id=network.id,
            ip_version=6,
            prefixlen=parsed_args.prefix_length,
            use_default_subnet_pool=True,
            enable_dhcp=False,
        )
        mgr.network.update_subnet(
            subnet,
            gateway_ip=None,
            allocation_pools=[],
        )

        # Create port
        if mgr.network.find_port(parsed_args.name):
            raise CommandError('Port %s already exists' % parsed_args.name)
        port = mgr.network.create_port(
            name=parsed_args.name,
            project_id=network.project_id,
            network_id=network.id,
            dns_name=parsed_args.dns_name,
            description="Routing port",
            allowed_address_pairs=[{'ip_address': subnet.cidr}],
        )
        nexthop = next(x['ip_address'] for x in port.fixed_ips
                       if valid_ipv6(x['ip_address']))

        # Create route
        router = mgr.network.find_router('internal-external',
                                         ignore_missing=False)
        routes = [{
            'destination': subnet.cidr,
            'nexthop': nexthop,
        }]
        mgr.network.update_router(
            router,
            routes=(router.routes + routes),
        )

        return zip(*{
            'name': parsed_args.name,
            'network_id': network.id,
            'subnet_id': subnet.id,
            'port_id': port.id,
            'dns_name': parsed_args.dns_name,
            'cidr': subnet.cidr,
            'fixed_ips': format_list_of_dicts(port.fixed_ips),
            'dns_assignment': format_list_of_dicts(port.dns_assignment),
            'routes': format_list_of_dicts(routes),
        }.items())


class DeleteRoutingPort(command.ShowOne):
    """Delete a subnet routing port"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'name', metavar='<name>',
            help=_("Subnet routing port name"),
        )
        return parser

    def take_action(self, parsed_args):
        mgr = self.app.client_manager
        subnet = mgr.network.find_subnet(parsed_args.name)
        port = mgr.network.find_port(parsed_args.name)
        router = mgr.network.find_router('internal-external',
                                         ignore_missing=False)
        routes = [x for x in router.routes
                  if subnet is not None and x['destination'] == subnet.cidr]

        # Delete route, if applicable
        if subnet is not None:
            mgr.network.update_router(
                router,
                routes=[x for x in router.routes if x not in routes],
            )

        # Delete port, if applicable
        if port is not None:
            mgr.network.delete_port(port)

        # Delete subnet, if applicable
        if subnet is not None:
            mgr.network.delete_subnet(subnet)

        return zip(*{
            'name': parsed_args.name,
            'subnet_id': None if subnet is None else subnet.id,
            'port_id': None if port is None else port.id,
            'routes': format_list_of_dicts(routes),
        }.items())
