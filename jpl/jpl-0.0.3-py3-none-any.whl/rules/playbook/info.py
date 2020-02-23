"""JiggyPlaybook rules."""
from jpl.rules.jiggyrule import JiggyRule


class PlayBookExists(JiggyRule):
    """Validate `JiggyPlaybook` exists."""

    rule = "001"
    description = "Validate `JiggyPlaybook` exists."
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def exists(self, playbook: dict) -> str:
        if not playbook:
            self.mark = "FAILED"
            self.message = "Jiggy Playbook is empty!"

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.exists(playbook)


class PlaybookHasName(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `name`"""

    rule = "I01"
    description = "Validate `JiggyPlaybook` has attribute `name`"
    priority = "high"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_name(self, playbook: dict) -> str:
        if not playbook.get("name", "").strip():
            self.mark = "FAILED"
            self.message = "Playbook `name` has not been declared."

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.has_name(playbook)


class PlaybookHasAuthor(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I02"
    description = "Validate `JiggyPlaybook` has attribute `author`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_author(self, playbook: dict) -> str:
        if not playbook.get("author"):
            self.mark = "WARNING"
            self.message = "Playbook `author` has not been declared."

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.has_author(playbook)


class PlaybookHasDescription(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I03"
    description = "Validate `JiggyPlaybook` has attribute `description`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_desc(self, playbook: dict) -> str:
        if not playbook.get("description"):
            self.mark = "WARNING"
            self.message = "Playbook `description` has not been declared."

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.has_desc(playbook)


class PlaybookHasVersion(JiggyRule):
    """Validate `JiggyPlaybook` has attribute `author`"""

    rule = "I04"
    description = "Validate `JiggyPlaybook` has attribute `version`"
    priority = "medium"
    commands = ["command", "core"]
    mark = "PASSED"
    message = ""
    task = None

    def has_version(self, playbook: dict) -> str:
        if not playbook.get("version"):
            self.mark = "WARNING"
            self.message = "Playbook `version` has not been declared."

        return self.mark

    def run(self, playbook: dict) -> str:
        return self.has_version(playbook)


rules = [PlaybookHasName, PlaybookHasAuthor, PlaybookHasDescription, PlaybookHasVersion]
