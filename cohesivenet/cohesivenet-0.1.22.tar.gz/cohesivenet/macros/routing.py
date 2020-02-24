from functools import partial as bind

from cohesivenet import data_types, network_math, Logger, util, VNS3Client
from cohesivenet.macros import api_operations, state


def create_local_gateway_route(client, local_cidr, **route_kwargs):
    """[summary]

    Arguments:
        client {[type]} -- [description]
        local_cidr {[type]} -- [description]

    Keyword Arguments:
        gateway {[type]} -- [description] (default: {None})

    Returns:
        OperationResult
    """
    route = dict(
        **{
            "cidr": local_cidr,
            "description": "Local Underlay Network Routing",
            "interface": "eth0",
            "gateway": network_math.get_default_gateway(local_cidr),
            "advertise": "False",
            "metric": 0,
        },
        **route_kwargs
    )
    return api_operations.try_api_call(
        client.routing.post_create_route, route, should_raise=True
    )


def create_route_advertisements(
    clients, local_subnets
) -> data_types.BulkOperationResult:
    """create_route_advertisements Create a route advertisement for controllers network

    Arguments:
        clients {List[VNS3Client]}
        local_subnets {List[str]} - order should correspond with clients list

    Returns:
        data_types.BulkOperationResult
    """
    assert len(clients) == len(
        local_subnets
    ), "clients list length must equal local_subnets list length"

    invalid = []
    for index, client in enumerate(clients):
        private_ip = state.get_primary_private_ip(client)
        if not network_math.subnet_contains_ipv4(private_ip, local_subnets[index]):
            invalid.append("%s not in %s" % (private_ip, local_subnets[index]))

    if len(invalid):
        raise AssertionError(
            "Invalid subnets provided for clients: %s." % ",".join(invalid)
        )

    def _create_route(_client, subnet):
        return _client.routing.post_create_route(
            {
                "cidr": subnet,
                "description": "Local subnet advertisement",
                "advertise": True,
                "gateway": "",
            }
        )

    bound_api_calls = [
        bind(_create_route, client, local_subnets[index])
        for index, client in enumerate(clients)
    ]

    return api_operations.__bulk_call_api(bound_api_calls)


def create_route_table(client: VNS3Client, routes, state={}):
    """Create routing policy

    Arguments:
        client {VNS3Client}
        routes {List[Route]} - [{
            "cidr": "str",
            "description": "str",
            "interface": "str",
            "gateway": "str",
            "tunnel": "int",
            "advertise": "bool",
            "metric": "int",
        }, ...]

    Keyword Arguments:
        state {dict} - State to format routes with. (can call client.controller_state)

    Returns:
        Tuple[List[str], List[str]] - success, errors
    """
    successes = []
    errors = []
    Logger.debug(
        "Setting controller route table.",
        host=client.host_uri,
        route_count=len(routes),
    )
    for i, route_kwargs in enumerate(routes):
        skip = False
        for key, value in route_kwargs.items():
            _value, err = util.format_string(value, state)
            if err:
                errors.append("Route key %s not formattable." % key)
                skip = True
            else:
                route_kwargs.update(**{key: _value})

        if skip:
            continue

        client.routing.post_create_route_if_not_exists(route_kwargs)
        successes.append("Route exists: route=%s" % str(route_kwargs))
    return successes, errors
