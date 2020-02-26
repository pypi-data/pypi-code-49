from prettytable import PrettyTable
from django.core.management.base import BaseCommand
import six
from ...models import InputSettingsField


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        table = PrettyTable()
        table.field_names = ["settings", "input_name", "output_name", "date_format", "default_value", "omit_empty", "omit"]
        for field in InputSettingsField.objects.order_by('settings', 'field_position'):
            table.add_row([field.settings, field.input_name, field.output_name, 
                field.date_format, field.default_value, field.exclude_if_empty, field.omit])
        six.print_(table)
