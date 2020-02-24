from django.db import models
from django.utils.functional import Promise
from django.utils.itercompat import is_iterable


class DynamicLazyChoices:
    GROUP_INDEX = 0
    GROUP_CHOICES_INDEX = 1

    def __init__(self):
        self._choices = list()

    def __str__(self):
        return str(i for i in self)

    def __iter__(self):
        choices = self._pre_iter()
        for choice in choices:
            if self.is_group_choice(choice):
                choice = self._wrap_with_tuple_group_choice(choice)
            else:
                choice = tuple(choice)
            yield choice

    def __eq__(self, other):
        if not is_iterable(other):
            return False
        self_ = tuple(sorted(self))
        other_ = tuple(sorted(other))
        return len(self_) == len(other_) and self_ == other_

    def register(self, *args, **kwargs):
        self._register(*args)

    def raise_check_error(self, error_code):  # pragma: no cover
        # TODO: integrar corretamente com o framework de system check do django
        print("CHECK ERROR", error_code)

    def get_group(self, name):
        for choice in self._choices:
            if not self.is_group_choice(choice):
                continue
            if choice[self.GROUP_INDEX] == name:
                return self._wrap_with_tuple_group_choice(choice)

    def is_group_choice(self, choice):
        cls = type(self)
        value, label = choice
        return not (cls._is_value(value) and cls._is_value(label))

    def _register(self, *choice):
        cls = type(self)
        # Expect [group_name, [value, display]]
        try:
            group_name, group_choices = choice
        except (TypeError, ValueError):
            return self.raise_check_error('fields.E005-1')
        try:
            invalid = not all(
                cls._is_value(value) and cls._is_value(label)
                for value, label in group_choices
            )
            if invalid:
                return self.raise_check_error('fields.E005-2')
        except (TypeError, ValueError):
            value, label = group_name, group_choices
            invalid = not cls._is_value(value) or not cls._is_value(label)
            if invalid:
                return self.raise_check_error('fields.E005-3')

        _choices = self._choices.copy()
        self._add_choice(choice)
        if cls._is_value(self._choices, accept_promise=False):
            # TODO: volta o estado do choices ao que era antes de adicionar a
            # nova choice isso está sendo necessário pq o system check
            # (impede do sistema iniciar se algum check falha) não foi
            # implementado ainda
            self._choices = _choices
            return self.raise_check_error('fields.E004')

    @classmethod
    def _is_value(cls, value, accept_promise=True):
        bases = (str, Promise) if accept_promise else (str,)
        is_instance_of_bases = isinstance(value, bases)
        return is_instance_of_bases or not is_iterable(value)

    def _pre_iter(self):
        choices = self._choices.copy()
        return choices

    def _wrap_with_tuple_group_choice(self, choice):
        group_name, group_choices = choice
        group_choices = tuple(tuple(c) for c in group_choices)
        return (group_name, group_choices)

    def _add_choice(self, choice):
        choice = list(choice)
        if self.is_group_choice(choice):
            self._add_group_choice(choice)
        else:
            self._choices.append(choice)

    def _add_group_choice(self, group_choice):
        for i, existing_choice in enumerate(self._choices):
            if not self.is_group_choice(existing_choice):
                continue
            choices_group_name = group_choice[self.GROUP_INDEX]
            choices_group = group_choice[self.GROUP_CHOICES_INDEX]
            if existing_choice[self.GROUP_INDEX] == choices_group_name:
                existing_choice[self.GROUP_CHOICES_INDEX] += choices_group
                break
        else:
            self._choices.append(group_choice)


class ModelLazyChoices(DynamicLazyChoices):
    def __init__(
            self, value_attr='_choice_value', label_attr='_choice_label',
            group_attr='_choice_group'):
        super().__init__()
        self._models = {}
        self._displays_to_models = {}
        self.value_attr = value_attr
        self.label_attr = label_attr
        self.group_attr = group_attr

    def __call__(self, model_class=None, *args, **kwargs):
        def register_decorator(model_class):
            self.register(model_class, *args, **kwargs)
            return model_class

        if model_class:
            return register_decorator(model_class)
        return register_decorator

    def register(self, model: models.Model, *args, **kwargs):
        value_attr = kwargs.get('value_attr', self.value_attr)
        label_attr = kwargs.get('label_attr', self.label_attr)
        group_attr = kwargs.get('group_attr', self.group_attr)

        value = getattr(model, value_attr, model.__name__)
        label = getattr(model, label_attr, model._meta.verbose_name)
        group = getattr(model, group_attr, None)
        self._models[value] = model
        choice = [value, label]
        if group:
            choice = [group, [choice]]
        return super().register(*choice)

    def get_model(self, choice_value):
        return self._models.get(choice_value, None)

