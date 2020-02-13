import logging

from kaf_pas.kd.models.documents import Documents, DocumentManager, DocumentQuerySet

logger = logging.getLogger(__name__)


class Lotsman_documentsQuerySet(DocumentQuerySet):
    pass


class Lotsman_documentsManager(DocumentManager):
    def get_queryset(self):
        return Lotsman_documentsQuerySet(self.model, using=self._db).filter(attr_type__code='LOTSMAN')


class Lotsman_documents(Documents):
    objects = Lotsman_documentsManager()

    class Meta:
        verbose_name = 'Докумеенты Лоцман'
        proxy = True
