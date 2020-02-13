import os
import json

from alfa_sdk.common.stores import ConfigStore
from alfa_sdk.common.auth import Authentication
from alfa_sdk.common.helpers import AlfaConfigHelper
from alfa_sdk.common.exceptions import AlfaConfigError
from alfa_cli.common.exceptions import RuntimeError
from alfa_cli.lib.runner.python import PythonRunner


class LocalRunner:
    def __init__(self, obj, algorithm_id, environment_name, function_type="invoke"):
        self.config = AlfaConfigHelper.load(os.path.join(".", "alfa.yml"), is_package=False)
        self.user = obj["client"].user
        self.algorithm_environment_id = self.parse_algorithm_environment_id(algorithm_id, environment_name)
        self.set_function_config(function_type)
        self.runner = self.create_runner(function_type)
        self.set_context()

    #

    def set_context(self):
        alfa_environment = ConfigStore.get_value("alfa_env", group="alfa", default="prod")
        auth = Authentication({}, alfa_env=alfa_environment)

        context = {
            "userId": self.user["userId"],
            "teamId": self.user["teamId"],
            "alfaEnvironment": alfa_environment,
            "algorithmEnvironmentId": self.algorithm_environment_id,
            "algorithmRunId": -1,
            "token": auth.token,
            "accessToken": auth.token,
            "auth0Token": auth.token,
        }

        os.environ["ALFA_CONTEXT"] = json.dumps(context)
        return context

    def parse_algorithm_environment_id(self, algorithm_id=None, environment_name=None):
        if not algorithm_id:
            algorithm_id = self.config["id"]
        if not environment_name:
            environment_name = self.config["environment"]
        team_id = self.user["teamId"]
        return f"{team_id}:{algorithm_id}:{environment_name}"

    def create_runner(self, function_type):
        runtime = self.get_runtime()

        if "python" in runtime:
            return PythonRunner(self.function_config, function_type)
        else:
            raise RuntimeError(message=f"Runtime '{runtime}' not supported")

    #

    def set_function_config(self, function_type):
        ERROR_MESSAGE = f"{function_type} function not defined"

        functions = self.config.get("functions")
        if not functions:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        invoke_functions = [func for func in functions if function_type in func.keys()]
        if len(invoke_functions) == 0:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        invoke_function = invoke_functions[0]
        self.function_config = invoke_function[function_type]

    def get_runtime(self):
        ERROR_MESSAGE = "runtime not defined"

        provider = self.function_config.get("provider")
        if not provider:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        runtime = provider.get("runtime")
        if not runtime:
            raise AlfaConfigError(message="Invalid configuration", error=ERROR_MESSAGE)

        return runtime

    #

    def run(self, problem, to_profile=False, profile_sort=None):
        return self.runner.run(problem, to_profile, profile_sort)
