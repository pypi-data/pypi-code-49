"""Jiggy Rule."""
import yaml

from jpl.rules import PlayBookExists, rules, task_rules


class JiggyPlaybookLint(object):  # pragma no cover
    """Runner for jpl."""

    def __init__(self, path: str, allow_warning=False):
        self.playbook = self._read(path)
        self.aw = allow_warning
        self.exe = ["PASSED"]

    def run(self):
        """Runner for JiggyPlaybookLinter."""
        playbook_exists = PlayBookExists()
        playbook_exists.run(self.playbook)
        if playbook_exists.mark == "FAILED":
            return [playbook_exists]

        jiggy_response = []
        for rule in rules:
            init_rule = rule()
            init_rule.run(playbook=self.playbook)

            jiggy_response.append(init_rule)

        for task in self.playbook.get("pipeline", {}).get("tasks"):
            for rule in task_rules:
                init_rule = rule()
                init_rule.run(playbook=task)

                jiggy_response.append(init_rule)

        return jiggy_response

    def validate(self) -> tuple:
        """
        Executor for in runtime JiggyPlaybookLint validation and response structure

        Returns:
            (tuple) - (is_valid, failures)
                is_valid = bool
                failures = list [JiggyRule] with mark FAILED
        """
        response = self.run()

        if self.aw:
            self.exe = self.exe.append("WARNING")

        prevent = list(filter(lambda rule: rule.mark not in self.exe, response))

        return bool(not prevent), prevent

    @staticmethod
    def _read(path: str):  # pragma no cover
        """Reader of .yml file."""
        with open(path, "r") as f:
            return yaml.full_load(f)
