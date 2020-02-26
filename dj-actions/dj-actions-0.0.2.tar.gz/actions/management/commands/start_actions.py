from django.core.management.base import BaseCommand
import os
from .helpers import template_to_out

class Command(BaseCommand):

    help = 'Configure defaul actions setup inside a module'

    def handle(self, *args, **options):

        # create directory structure
        base_path = '/code/actions/actions/'

        context = {
            "resource": "ActionEvent",
            "code_path": base_path,
            "resource_path": '/dj-actions/actionevents/',
            "appname": "actions"
        }

        try:
            os.makedirs(base_path)
        except FileExistsError:
            print ('actions folder already exists')
        except OSError as e:
            raise CommandError(e)

        # create registry:
        template_to_out(
            'djactions/action_registry.py',
            context,
            '{}action_registry.py'.format(base_path)
        )

        # print instructions
        instructions = template_to_out('djactions/instructions.txt', context)
        print(instructions)
