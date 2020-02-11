import PyInquirer
import argparse
from git import Repo


try:
    repo = Repo('.')
    is_issue = str(repo.active_branch)[0].isdigit()

    if is_issue:
        id_issue = str(repo.active_branch)[0]
    else:
        id_issue = 'nt'

except Exception as ignored:
    id_issue = 'nt'


TEMPLATE = '{action}({topic}): {message} #{issue} [!{tag}]'


class Issue(PyInquirer.Validator):
    def validate(self, document):
        if not document.text == 'nt':
            try:
                int(document.text)
            except ValueError:
                raise PyInquirer.ValidationError(
                    message='Please enter a number or #nt',
                    cursor_position=len(document.text)
                )


class NoEmpty(PyInquirer.Validator):
    def validate(self, document):
        if len(document.text.split(' ')) < 2:
            raise PyInquirer.ValidationError(
                message='Commit message must have grant 2 words',
                cursor_position=len(document.text)
            )


def get_commit_message():
    global id_issue

    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': '>>> Select ACTION:    ',
            'choices': [
                {'name': 'feat:        new features, big improvement'},
                {'name': 'fix:         bug fixes'},
                {'name': 'refactor:    code refactoring, without any visual user change'},
                {'name': 'chore:       any else but the app'},
                {'name': 'test:        any kind of tests (functionnal, unitary...)'},
                {'name': 'style:       cosmetic changes (spaces vs tab...)'},
                {'name': 'docs:        documentation'}
            ],
            'filter': lambda v: v.split(':')[0]
        },
        {
            'type': 'list',
            'name': 'topic',
            'message': '>>> Select TOPIC:     ',
            'choices': [
                {'name': 'dev:         developpers (API changes, refactors...)'},
                {'name': 'usr:         final users (UI changes)'},
                {'name': 'pkg:         packagers   (packaging changes)'},
                {'name': 'test:        testers     (test only related changes)'}
            ],
            'filter': lambda v: v.split(':')[0]
        },
        {
            'type': 'input',
            'name': 'message',
            'message': '>>> Type Commit message: ',
            'validate': NoEmpty,
        },
        {
            'type': 'input',
            'name': 'issue',
            'message': '>>> Select ID-ISSUE:',
            'default': id_issue,
            'validate': Issue
        },
        {
            'type': 'list',
            'name': 'tag',
            'message': '>>> Select TOPIC:     ',
            'choices': [
                {'name': 'refactor:    obviously for refactoring code only'},
                {'name': 'minor:       a very meaningless change (a typo, adding a comment)'},
                {'name': 'cosmetic:    cosmetic driven change (re-indentation, 80-col...)'},
                {'name': 'wip:         partial functionality but complete subfunctionality.'}
            ],
            'filter': lambda v: v.split(':')[0]
        }
    ]

    answers = PyInquirer.prompt(questions)

    return TEMPLATE.format_map(answers)


def main():
    print('Created By Carlos Neto | https://github.com/augustoliks')
    commit_message = get_commit_message()
    print('\n\n' + commit_message + '\n\n')


if __name__ == '__main__':
    main()