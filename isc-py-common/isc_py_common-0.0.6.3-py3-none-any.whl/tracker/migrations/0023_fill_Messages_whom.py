from django.db import migrations

from tracker.models.messages import Messages
from tracker.models.messages_whom import Messages_whom


def fill(apps, schema_editor):
    for message in Messages.objects.all():
        Messages_whom.objects.update_or_create(message=message.message, to_whom=message.to_whom)


class Migration(migrations.Migration):
    dependencies = [
        ('tracker', '0022_auto_20190517_1802'),
    ]
    atomic = True

    operations = [
        # migrations.RunPython(fill),
    ]
