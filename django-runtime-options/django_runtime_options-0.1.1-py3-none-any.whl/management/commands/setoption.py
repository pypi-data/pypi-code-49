from django.core.management.base import BaseCommand

from options.models import Option


class Command(BaseCommand):
    help = "Create or update a runtime option."

    def add_arguments(self, parser):
        types = f"Available types are {Option.TYPE_TXT}, {Option.TYPE_INT}, and {Option.TYPE_BOOL}"
        parser.add_argument("key", type=str, help="Key to use")
        parser.add_argument("value", type=str, help="Value to set")
        parser.add_argument("--type", type=str, help=f"Type of value being set. {types}")

    def handle(self, *args, **kwargs):
        key = kwargs["key"]
        value = kwargs["value"]
        if kwargs["type"]:  # A manual type was provided
            value_type = kwargs["type"]
            option, created = Option.objects.update_or_create(
                key=key, defaults={"value": value, "value_type": value_type}
            )
        else:  # Create new Option with default type or don't change existing type
            option, created = Option.objects.update_or_create(key=key, defaults={"value": value})

        YELLOW = "\033[33m"
        verb = f"Created" if created else f"Updated"
        verb = f"{YELLOW}{verb}"
        self.stdout.write(f"{verb} option '{option}' with type '{option.value_type}'")
