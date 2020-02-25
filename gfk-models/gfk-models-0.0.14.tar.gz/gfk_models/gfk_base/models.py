from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist


class GFKQuerySet(models.QuerySet):

    def filter(self, *args, **kwargs):
        if '_target' in kwargs:
            kwargs['target_id'] = kwargs['_target'].id
            kwargs['target_content_type'] = ContentType.objects.get_for_model(kwargs['_target']).id
            kwargs.pop("_target", None)

        # print('GFKQuerySet -> filter', self, args, kwargs)

        return super(GFKQuerySet, self).filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        if '_target' in kwargs:
            kwargs['target_id'] = kwargs['_target'].id
            kwargs['target_content_type'] = ContentType.objects.get_for_model(kwargs['_target']).id
            kwargs.pop("_target", None)

        # print('GFKQuerySet -> get', self, args, kwargs)

        return super(GFKQuerySet, self).get(*args, **kwargs)


class GFKManger(models.Manager):
    def get_queryset(self):
        return GFKQuerySet(self.model, using=self._db)

    def filter(self, *args, **kwargs):
        if '_target' in kwargs:
            kwargs['target_id'] = kwargs['_target'].id,
            kwargs['target_content_type'] = ContentType.objects.get_for_model(kwargs['_target']).id
            kwargs.pop("_target", None)

        # print('GFKManger -> filter',self, args, kwargs)
        new_qs = super(GFKManger, self).get_queryset().filter(*args, **kwargs)
        new_gfk_qs = new_qs._clone()
        return super(GFKManger, self).get_queryset().filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        if '_target' in kwargs:
            kwargs['target_id'] = kwargs['_target'].id
            kwargs['target_content_type'] = ContentType.objects.get_for_model(kwargs['_target']).id
            kwargs.pop("_target", None)

        # print(self, args, kwargs)

        return super(GFKManger, self).get_queryset().get(*args, **kwargs)


class GFKModel(models.Model):
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_id')
    # placeholder для GFKManger.filter чтобы можно было получать данные по target автоматом
    # нужно использовать objects.filter(_target=target), в GFKManager _target будет
    # преобразован в target_content_type и target_id
    _target = models.BooleanField(default=True, blank=True)

    objects = GFKQuerySet.as_manager() # GFKManger()

    class Meta:
        abstract = True

    def get_target(self):
        # print('self.target_id', self.target_id)
        # content_type = ContentType.objects.get(id=self.target_content_type)
        return self.target_content_type.model_class().objects.get(id=self.target_id)

    @staticmethod
    def get_target_static(target):
        content_type = ContentType.objects.get(id=target.target_content_type)
        return content_type.model_class().objects.get(id=target.target_id)

    @staticmethod
    def get_ct_model_static(target_ct_id):
        return ContentType.objects.get(id=target_ct_id).model_class()


    @staticmethod
    def get_content_type(target):
        return ContentType.objects.get_for_model(target).id

    @classmethod
    def filter_by_target(cls, target):

        return cls.objects.filter(
            target_id=target.id,
            target_content_type=ContentType.objects.get_for_model(target).id
        )


from django.db.models import signals


class GFKStats(GFKModel):
    # Model to count stats
    item_model = None

    recount_attr_list = ['count']

    count = models.IntegerField(default=0)

    class Meta:
        unique_together = ['target_content_type', 'target_id']
        abstract = True

    def recount_count(self):
        return self.get_recount_queryset().count()

    def recount_stats(self):
        '''
        This method invokes by signal each time when model instance has been updated
        :return:
        '''
        for attr in self.recount_attr_list:
            recount_attr = getattr(self, 'recount_%s' % attr)
            setattr(self, attr, recount_attr())

        self.save()

    def get_recount_queryset(self):
        # We count statistics for same target as GFKStats target
        kwargs = {
            'target_content_type': self.target_content_type,
            'target_id': self.target_id
        }
        return self.item_model.objects.filter(**kwargs)

    @classmethod
    def setup_relation(cls, model):
        '''
        Set up relation with GFK model which statics we should count.
        '''
        cls.item_model = model
        signals.post_save.connect(cls.signal_callback, sender=model)

    @classmethod
    def signal_callback(cls, **kwargs):
        inst = kwargs['instance']

        kwargs = {
            'target_content_type': inst.target_content_type,
            'target_id': inst.target_id
        }

        try:
            stats_object = cls.objects.get(**kwargs)
        except ObjectDoesNotExist:
            stats_object = cls(**kwargs)
            stats_object.save()

        stats_object.recount_stats()