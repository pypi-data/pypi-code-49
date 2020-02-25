from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.filter
def get_item_credentials(item):
    item_id = str(item.id)
    item_ct = str(ContentType.objects.get_for_model(item).id)
    return '%s-%s' % (item_id, item_ct)
