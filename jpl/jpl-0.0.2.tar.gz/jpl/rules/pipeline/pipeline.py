"""JiggyPlaybook Pipeline rules."""
from enum import Enum

from jpl.rules.jiggyrule import JiggyRule

from jpl.utils.path import file_exists


class ExtendedEnum(Enum):  # pragma no cover
    """Enum for Jiggy.Runner types."""

    @classmethod
    def list(cls):  # pragma no cover
        """List ExtendedEnum for runner types."""
        return list(map(lambda c: c.value, cls))


class Runner(ExtendedEnum):  # pragma no cover
    """Runner types supported by Jiggy."""

    PARALLEL_RUNNER = "parallel"
    SEQUENTIAL_RUNNER = "sequential"


class PipelineHasRunner(JiggyRule):
    """Validate `JiggyPlaybook.pipeline` declared `runner` exists"""

    rule = "P01"
    description = "Validate `pipeline` declares `runner`"
    priority = "medium"  # NOTE this will get defaulted otherwise
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def validate_runner(self, playbook: dict) -> str:
        pipeline = playbook.get("pipeline", {})

        if not pipeline.get("runner"):
            self.mark = "WARNING"
            self.message = "Pipeline Runner set to `sequential`"

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.validate_runner(playbook)


class RunnerIsSupported(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.runner` is supported"""

    rule = "P02"
    description = "Validate `runner` is supported by Jiggy"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def validate_runner_supported(self, playbook: dict) -> str:
        pipeline = playbook.get("pipeline", {})
        runner = pipeline.get("runner", "")

        if not runner.lower() in [jr.value for jr in Runner]:
            self.mark = "FAILED"
            self.message = "Declared Runner: `{}` is not supported.".format(runner)

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.validate_runner_supported(playbook)


class SecretsHasMetadata(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.secrets` has relevant metadata"""

    rule = "P03"
    description = "Validate `secrets` has mandatory metadata."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def validate_secrets(self, playbook: dict) -> str:
        """Check `secrets` metadata if exists for mandatory fields."""
        pipeline = playbook.get("pipeline", {})
        secrets = pipeline.get("secrets")

        if secrets:
            if not isinstance(secrets, dict):
                self.mark = "FAILED"
                self.message = "Invalid `secrets` declaration."
            elif "location" not in secrets.keys():
                self.mark = "FAILED"
                self.message = "Secrets requires attribute `location`."
            elif "source" not in secrets.keys():
                self.mark = "FAILED"
                self.message = "Secrets requires attribute `source`."

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.validate_secrets(playbook)


class SecretsLocationExists(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.secrets.location` exists."""

    rule = "P04"
    description = "Validate `secrets.location` exists."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def validate_secrets_exists(self, playbook: dict) -> str:
        """Check `secrets.location` exists."""
        pipeline = playbook.get("pipeline", {})
        secrets = pipeline.get("secrets", {})
        secrets_loc = secrets.get("location")

        if secrets_loc:
            _exists = file_exists(secrets_loc)
            if not _exists:
                self.mark = "FAILED"
                self.message = "Declared path to secrets: `{}` does not exist.".format(
                    secrets_loc
                )

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.validate_secrets_exists(playbook)


class PipelineHasTasks(JiggyRule):
    """Validate `JiggyPlaybook.pipeline.tasks` exists"""

    rule = "P05"
    description = "Validate `tasks` exists."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def validate_pipeline_has_tasks(self, playbook: dict) -> str:
        """Check `JiggyPlaybook.pipeline.tasks` exists."""
        pipeline = playbook.get("pipeline", {})
        tasks = pipeline.get("tasks")

        if not tasks:
            self.message = "No tasks declared in pipeline."
            self.mark = "FAILED"

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.validate_pipeline_has_tasks(playbook)


rules = [
    PipelineHasRunner,
    RunnerIsSupported,
    SecretsHasMetadata,
    SecretsLocationExists,
    PipelineHasTasks,
]
