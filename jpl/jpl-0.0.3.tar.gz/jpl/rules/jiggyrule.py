"""
A base class for JiggyRule.

ETYMOLOGY:
Playbook Info - Top level information for JiggyPlaybook

JiggyRule - JiggyRule.rule consists of 3 characters (i.e.) X01

X: (char) - letter describes corresponding ruleset
0: (digit) - incrementing based on third digit
0: (digit) - incrementing

(i.e.) Playbook INFO Ruleset

Rule 1. PlaybookHasName
rule.rule = I (info) 0 (base 10) 1 (rule number 1)

Rule 2. PipelineHasDescription
rule.rule = P (pipeline) 0 (base 10) 1 (rule number 1)
"""


class JiggyRule(object):  # pragma no cover
    """Base class for JiggyRule."""

    rule = ""
    description = ""
    priority = ""
    commands = []
    mark = ""
    message = ""

    def __repr__(self):
        return "<JiggyRule: {}>".format(self.rule)

    def __verbose__(self):
        return "<JiggyRule: {} - {}>".format(self.rule, self.description)

    def run(self, playbook):
        """Base class runner."""
        raise NotImplementedError()
