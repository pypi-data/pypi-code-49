from django.utils.translation import ugettext_lazy as _

import logging

from isc_common.models.base_ref import BaseRef

logger = logging.getLogger(__name__)


class Messages_state(BaseRef):
    def __str__(self):
        return f"{self.code}: {self.name}"

    class Meta:
        verbose_name = 'Состояние сообщений'
        