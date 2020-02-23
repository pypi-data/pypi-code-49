"""JiggyPlaybook.pipeline.tasks rules."""
from jpl.rules.jiggyrule import JiggyRule


class TaskHasName(JiggyRule):
    """Validate task has attribute `name`"""

    rule = "T01"
    description = "Validate `JiggyPlaybook.pipeline.task` has attribute `name`"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_name(self, task):
        self.task = task.get("name")
        if not task.get("name"):
            self.mark = "FAILED"
            self.message = "Task `name` has not been declared."

        return self.mark

    def run(self, playbook):
        return self.has_name(playbook)


class TaskHasDescription(JiggyRule):
    """Validate task has attribute `name`"""

    rule = "T02"
    description = "Validate `JiggyPlaybook.pipeline.task` has attribute `description`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_desc(self, task):
        self.task = task.get("name")
        if not task.get("description"):
            self.mark = "WARNING"
            self.message = "Task `description` has not been declared."

        return self.mark

    def run(self, playbook):
        return self.has_desc(playbook)


class TaskHasFunction(JiggyRule):
    """Validate task has attribute `name`"""

    rule = "T03"
    description = "Validate `JiggyPlaybook.pipeline.task` has attribute `function`"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_function(self, task):
        self.task = task.get("name")
        if not task.get("function"):
            self.mark = "FAILED"
            self.message = "Task `function` has not been declared."

        return self.mark

    def run(self, playbook):
        return self.has_function(playbook)


rules = [TaskHasName, TaskHasDescription, TaskHasFunction]
