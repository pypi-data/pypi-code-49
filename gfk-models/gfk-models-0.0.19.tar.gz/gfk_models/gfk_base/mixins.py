from django.core.exceptions import ObjectDoesNotExist
from django.forms.forms import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class GFKBaseManager(object):
    item_model = None
    # Item model form - used for adding new Item's to ItemList
    item_form = None

    base_create_or_update_fields = ['target_id', 'target_content_type']
    create_or_update_fields = []

    def set_kwargs(self, kwargs):
        return kwargs

    # def all(self, *args, **kwargs):
    #     self.set_kwargs(kwargs)
    #     return self.item_model.objects.filter(*args, **kwargs)
    #
    # def get(self, *args, **kwargs):
    #     self.set_kwargs(kwargs)
    #     return self.item_model.objects.get(*args, **kwargs)
    #
    # def filter(self, *args, **kwargs):
    #     self.set_kwargs(kwargs)
    #     return self.item_model.objects.filter(*args, **kwargs)

    def get__create_or_update_fields(self):
        return self.create_or_update_fields + self.base_create_or_update_fields

    def get_queryset__by_create_or_update_fields(self, data):
        '''
        Build filter to retrieve Item instance
            * base_create_or_update_fields
            * create_or_update_fields

            * - reuired fields
        :param data:
        :return: queryset.get
        '''
        kwargs = {}
        for field in self.get__create_or_update_fields():
            kwargs[field] = data[field]

        return self.item_model.objects.get(**kwargs)

    def add(self, review_dict):
        self.set_kwargs(review_dict)

        # try:
        #     item = self.get_queryset__by_create_or_update_fields(review_dict)
        # except ObjectDoesNotExist:
        item = self.item_model()

        form = self.item_form(review_dict, instance=item)

        if form.is_valid():
            return form.save()
        else:
            raise ValidationError(_('Form is invalid'), form)


class GFKItemsManager(GFKBaseManager):
    '''
    Use for GFKModel's appended directly to target
    '''

    def __init__(self, target):
        self.target = target

    def set_kwargs(self, kwargs):
        kwargs['target_id'] = self.target.id
        kwargs['target_content_type'] = self.item_model.get_content_type(self.target)
        return kwargs


class GFKItemsStatsManager(GFKItemsManager):
    # stats model
    stats_model = None
    '''
    Use for GFKModel's Items appended to targets thru lists (f.e. likes or reviews)
    '''
    def stats(self):
        try:
            stats = self.stats_model.objects.get(_target=self.target)
        except ObjectDoesNotExist:
            stats = self.stats_model(target=self.target)
            stats.save()

        return stats


class GFKBaseMixin(models.Model):
    class Meta:
        abstract = True
    # def __init__(self, relation_name, relation_model, manager_model, *args, **kwargs):
    #     '''
    #     :param relation_name: name of relation for target model
    #     :param args:
    #     :param kwargs:
    #     '''
    #
    #     print('GFKBaseMixin __init__ ->')
    #
    #     self.__relation_name = relation_name
    #     self.__relation_model = relation_model
    #     self.__manager_model = manager_model
    #
    #     setattr(self, relation_name, GenericRelation(relation_model))
    #     setattr(self, relation_name + "_manager", self.__get_manager)
    #
    #     super(GFKBaseMixin, self).__init__(*args, **kwargs)
    #
    # def __get_manager(self):
    #     return self.__manager_model(self)


# class GFKBaseStatsMixin(GFKBaseMixin):
#     def __init__(self, *args, **kwargs):
#         '''
#         :param relation_name: name of relation for target model
#         :param args:
#         :param kwargs:
#         '''
#         super(GFKBaseMixin, self).__init__(*args, **kwargs)
