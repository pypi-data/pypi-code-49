import requests

from halo import Halo

from .requests import request_token


class Services(object):
    def __init__(self, ctx):
        """
        TODO: put correct endpoints to check if online
        extractor: '/'
        vat_validator: https://github.com/hypatos/vat-validator/pull/36
        """
        endpoint_env = ctx.obj.get("env")
        config = ctx.obj["config"]
        endpoints = config["endpoints"]

        username = config.get("username", None)
        password = config.get("password", None)
        ctx.obj["token"] = None

        self.are_up(endpoints)

        if endpoint_env != "localhost":
            ctx.obj["token"] = request_token(
                endpoints["authentication"], username, password
            )

    def are_up(self, endpoints):
        """ Return True if all endpoints are up. """
        for name, endpoint in endpoints.items():
            endpoint_spinner = Halo(spinner="dots")
            try:
                req = requests.get(endpoint)

            # On connection error.
            except requests.exceptions.ConnectionError:
                endpoint_spinner.fail(
                    f"{name.capitalize()} on endpoint {endpoint} is offline\n"
                )
                endpoints[name] = None
                if name == "extractor":
                    quit(
                        f"Expecting extraction service on {endpoint}, this service is mandatory."
                    )

            # Connection was successful on 401 and 405.
            else:
                if req.status_code == 401 or req.status_code == 405:
                    endpoint_spinner.succeed(
                        f"{name.capitalize()} endpoint is online\n"
                    )
                else:
                    endpoint_spinner.fail(
                        f"{name.capitalize()} endpoint returns {req.status_code}\n"
                    )
                    endpoints[name] = None
