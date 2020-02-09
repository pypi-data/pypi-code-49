
from .basic import BasicReport


class ConsoleReport(BasicReport):
    templates = {
        'MAIN': '''
Python: {python_version}
Runtime: {runtime} {runtime_version}
Platform: {platform}
Pip: {pip_version}
Location: {base_directory}
Total: {packages|len}
Outdated: {?outdated}{c_yellow}{outdated|len}{c_norm}{#outdated}
  {.}{/outdated}{:else}0{/outdated}
Vulnerable: {?vulnerable}{c_red}{vulnerable|len}{c_norm}{#vulnerable}
  {.}{/vulnerable}{:else}0{/vulnerable}
Missing: {?missing}{c_red}{missing|len}{c_norm}{#missing}
  {.}{/missing}{:else}0{/missing}
Invalid: {?invalid}{c_red}{invalid|len}{c_norm}{#invalid}
  {.}{/invalid}{:else}0{/invalid}

{?summary_only}{:else}{?problems_only}{#problem_packages}{>PACKAGE/}{/problem_packages}{:else}{#packages}{>PACKAGE/}{/packages}{/problems_only}{/summary_only}
''',

        'PACKAGE': '''{c_bold}{name}=={version}{c_reset}{?license} ({license}){:else}{/license}
{#issues}  {@eq key=type value="OUTDATED"}{c_yellow}!! Package is outdated; {c_bold}{latest_version}{c_unbold} is available{/eq}{@eq key=type value="REQ_MISSING"}{c_red}!! Dependency {c_bold}{key}{c_unbold} is missing{/eq}{@eq key=type value="REQ_INVALID"}{c_red}!! Dependency {c_bold}{key}{c_unbold} is invalid; require {c_bold}{requirement|s}{c_unbold} but {c_bold}{installed}{c_unbold} is installed{/eq}{@eq key=type value="VULNERABLE"}{c_red}!! Package has a known vulnerability: {id}: {description|s}{/eq}{c_reset}{~n}{/issues}{?dependencies}{#dependencies}  {key}{?spec} ({spec|s}){/spec}{~n}{/dependencies}{/dependencies}
''',  # noqa
    }

    def create_template_args(self, environment, options):
        args = super().create_template_args(environment, options)
        if options.get('tty'):
            args['c_bold'] = '\x1b[1m'
            args['c_unbold'] = '\x1b[22m'
            args['c_red'] = '\x1b[31m'
            args['c_yellow'] = '\x1b[33m'
            args['c_norm'] = '\x1b[39m'
            args['c_reset'] = '\x1b[0m'
        return args


def create(environment, options):
    return ConsoleReport().create(environment, options)

