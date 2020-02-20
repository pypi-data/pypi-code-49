"""Unipart OpenStack network client tools"""

import time
from openstack.exceptions import ConflictException
from openstackclient.i18n import _
from openstackclient.identity.common import find_project
from osc_lib.command import command
from osc_lib.utils import format_list


class CreateNetwork(command.ShowOne):
    """Create a network and associated default resources"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--project', metavar='<project>',
            help=_("Project (name or ID)"),
        )
        parser.add_argument(
            '--zone', metavar='<zone>',
            help=_("DNS zone"),
        )
        parser.add_argument(
            '--ttl', metavar='<ttl>', type=int, default=60,
            help=_("DNS default TTL"),
        )
        parser.add_argument(
            'name', metavar='<name>',
            help=_("Network name"),
        )
        return parser

    def take_action(self, parsed_args):
        mgr = self.app.client_manager
        if parsed_args.project is None:
            parsed_args.project = parsed_args.name
        if parsed_args.zone is None:
            parsed_args.zone = '%s.devonly.net.' % parsed_args.name

        # Identify project
        project = find_project(mgr.identity, parsed_args.project)

        # Update default security group to allow ICMP echo
        secgroup = next(mgr.network.security_groups(
            project_id=project.id,
            name='default',
        ))
        try:
            mgr.network.create_security_group_rule(
                security_group_id=secgroup.id,
                project_id=project.id,
                direction='ingress',
                ethertype='IPv4',
                remote_ip_prefix='0.0.0.0/0',
                protocol='icmp',
                port_range_min=8,  # ICMP type
            )
        except ConflictException:
            pass
        try:
            mgr.network.create_security_group_rule(
                security_group_id=secgroup.id,
                project_id=project.id,
                direction='ingress',
                ethertype='IPv6',
                remote_ip_prefix='::/0',
                protocol='icmp',
                port_range_min=128,  # ICMP type
            )
        except ConflictException:
            pass

        # Find or create DNS zone
        mgr.dns.session.sudo_project_id = project.id
        zone = next(iter(mgr.dns.zones.list({
            'name': parsed_args.zone,
        })), None) or mgr.dns.zones.create(
            parsed_args.zone,
            'PRIMARY',
            email='sysadmins@unipart.io',
            ttl=parsed_args.ttl,
        )

        # Create network and subnets
        network = mgr.network.create_network(
            name=parsed_args.name,
            project_id=project.id,
            dns_domain=parsed_args.zone,
        )
        subnetv6 = mgr.network.create_subnet(
            name='%s-ipv6' % parsed_args.name,
            project_id=project.id,
            network_id=network.id,
            ip_version=6,
            ipv6_ra_mode='dhcpv6-stateful',
            ipv6_address_mode='dhcpv6-stateful',
            use_default_subnet_pool=True,
        )
        subnetv4 = mgr.network.create_subnet(
            name='%s-ipv4' % parsed_args.name,
            project_id=project.id,
            network_id=network.id,
            ip_version=4,
            use_default_subnet_pool=True,
        )

        # Delay to allow DHCP port to be created
        time.sleep(2)

        # Set DHCP port name
        dhcp = next(mgr.network.ports(
            network_id=network.id,
            device_owner='network:dhcp',
        ))
        mgr.network.update_port(
            dhcp,
            name='%s-dhcp' % parsed_args.name,
            dns_name='%s-dhcp' % parsed_args.name,
            description="DHCP agent",
        )

        # Create gateway port
        gateway = mgr.network.create_port(
            name='%s-gateway' % parsed_args.name,
            project_id=project.id,
            network_id=network.id,
            dns_name='%s-gateway' % parsed_args.name,
            description="Default gateway",
            device_owner='network:router_interface',
            fixed_ips=[
                {'subnet': subnetv6.id, 'ip_address': subnetv6.gateway_ip},
                {'subnet': subnetv4.id, 'ip_address': subnetv4.gateway_ip},
            ],
            port_security_enabled=False,
        )

        # Add gateway port to router
        mgr.network.add_interface_to_router(
            mgr.network.find_router('internal-external', ignore_missing=False),
            port_id=gateway.id,
        )

        return zip(*{
            'name': parsed_args.name,
            'network_id': network.id,
            'v6_subnet_id': subnetv6.id,
            'v4_subnet_id': subnetv4.id,
            'dhcp_port_id': dhcp.id,
            'gateway_port_id': gateway.id,
            'zone_id': zone['id'],
            'dns_domain': network.dns_domain,
            'cidr': format_list([subnetv6.cidr, subnetv4.cidr]),
        }.items())


class DeleteNetwork(command.ShowOne):
    """Delete a network and associated default resources"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--no-delete-zone', action='store_true',
            help=_("Do not delete associated DNS zone"),
        )
        parser.add_argument(
            'name', metavar='<name>',
            help=_("Network name"),
        )
        return parser

    def take_action(self, parsed_args):
        mgr = self.app.client_manager

        # Identify network
        network = mgr.network.find_network(parsed_args.name)

        # Identify gateway, if applicable
        if network is not None:
            gateway = next(mgr.network.ports(
                network_id=network.id,
                name='%s-gateway' % parsed_args.name,
            ), None)
        else:
            gateway = None

        # Identify DNS zone
        if network is not None:
            zone = next(iter(mgr.dns.zones.list({
                'name': network.dns_domain,
            })), None)
        else:
            zone = None

        # Remove gateway port from router, if applicable
        if gateway is not None:
            mgr.network.remove_interface_from_router(
                mgr.network.find_router('internal-external',
                                        ignore_missing=False),
                port_id=gateway.id,
            )

        # Delete gateway port, if applicable
        if gateway is not None:
            mgr.network.delete_port(gateway)

        # Delete zone, if applicable
        if zone is not None and not parsed_args.no_delete_zone:
            mgr.dns.zones.delete(zone['id'])

        # Delete network, if applicable
        if network is not None:
            mgr.network.delete_network(network)

        return zip(*{
            'name': parsed_args.name,
            'network_id': None if network is None else network.id,
            'gateway_port_id': None if gateway is None else gateway.id,
            'zone_id': None if zone is None else zone['id'],
        }.items())
