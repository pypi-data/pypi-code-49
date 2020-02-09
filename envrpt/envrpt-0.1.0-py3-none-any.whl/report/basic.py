
from copy import deepcopy

from .._vendor.ashes import AshesEnv


class BasicReport:
    templates = {}

    def __init__(self):
        self.ashes = AshesEnv(
            filters={
                'len': len,
                'date': lambda d: d.strftime('%Y-%m-%d'),
                'time': lambda t: t.strftime('%H:%M:%S'),
            },
        )
        for name, tmpl in self.templates.items():
            self.ashes.register_source(name, tmpl)

    def create_template_args(self, environment, options):  # noqa: no-self-use
        args = deepcopy(environment)
        args.update(options)

        issues = [
            (package, issue)
            for package in environment['packages'].values()
            for issue in package['issues']
        ]
        args['outdated'] = sorted({
            pkg['key']
            for pkg, issue in issues
            if issue['type'] == 'OUTDATED'
        })
        args['missing'] = sorted({
            issue['key']
            for pkg, issue in issues
            if issue['type'] == 'REQ_MISSING'
        })
        args['invalid'] = sorted({
            issue['key']
            for pkg, issue in issues
            if issue['type'] == 'REQ_INVALID'
        })
        args['vulnerable'] = sorted({
            pkg['key']
            for pkg, issue in issues
            if issue['type'] == 'VULNERABLE'
        })

        args['packages'] = sorted(
            environment['packages'].values(),
            key=lambda p: p['name'].lower(),
        )
        for pkg in args['packages']:
            pkg['dependencies'] = sorted(
                [
                    {
                        'key': key,
                        'spec': val,
                        'installed': key in environment['packages'],
                    }
                    for key, val in pkg['requirements'].items()
                ],
                key=lambda d: d['key'],
            )
            pkg['dependents'] = sorted(
                [
                    {
                        'key': key,
                    }
                    for key, val in environment['packages'].items()
                    if pkg['key'] in val['requirements']
                ],
                key=lambda d: d['key'],
            )
        args['problem_packages'] = [
            package
            for package in args['packages']
            if package['issues'] or package['key'] in args['invalid']
        ]

        if 'envrpt' in environment['packages']:
            args['envrpt_home_page'] = \
                environment['packages']['envrpt']['home_page']

        return args

    def create(self, environment, options):
        args = self.create_template_args(environment, options)
        return self.ashes.render('MAIN', args).strip()

