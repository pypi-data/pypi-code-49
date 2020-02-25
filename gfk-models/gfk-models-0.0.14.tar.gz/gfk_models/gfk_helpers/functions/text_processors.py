from django.contrib import auth
from .translitirate import transliterate

from django.contrib.contenttypes.models import ContentType
import bleach
import re


class TextProcessors:
    text_allowed_tags = ['a', 'img', 'div', 'p', 'h2', 'h3', 'h4', 'em', 'b', 'strong', 'ul', 'ol', 'li', 'blockquote']
    text_allowed_attrs = ['alt', 'rel', 'href']

    @classmethod
    def text_sanitize(cls, text, text_allowed_tags=None, text_allowed_attrs=None):

        if text_allowed_tags is None:
            text_allowed_tags = cls.text_allowed_tags

        if text_allowed_attrs is None:
            text_allowed_attrs = cls.text_allowed_attrs

        text = bleach.clean(text,
                            tags=text_allowed_tags,
                            attributes=text_allowed_attrs,
                            strip=True
                        )
        text = cls.__clean_blank_tags(text, text_allowed_tags)
        text = cls.__clean_line_breaks(text)
        callbacks = [
            cls.__add__a_rel_nofollow,
            cls.__add__a_target,
            cls.__add__a_href_protocol
        ]
        text = bleach.linkify(text, callbacks=callbacks)

        return text

    @staticmethod
    def __clean_blank_tags(text, tags):
        for tag in tags:
            pattern = "<%s>\s</%s>" % (tag, tag)
            # print(pattern)
            regex = re.compile(pattern, re.IGNORECASE)
            text = regex.sub('', text)

        return text

    @staticmethod
    def __clean_line_breaks(text):
        pattern = "\r"
        regex = re.compile(pattern, re.IGNORECASE)
        text = regex.sub('', text)

        pattern = "\n"
        regex = re.compile(pattern, re.IGNORECASE)
        text = regex.sub('', text)

        return text

    @staticmethod
    def __add__a_rel_nofollow(attrs, new=False):
        attrs['rel'] = 'nofollow'
        return attrs

    @staticmethod
    def __add__a_href_protocol(attrs, new=False):
        # print(attrs)
        # if not attrs['href'].startswith("http://") and \
        #    not attrs['href'].startswith("https://"):
        #     attrs['href'] = "http://%s" % attrs['href']

        return attrs

    @staticmethod
    def __add__a_target(attrs, new=False):
        attrs['target'] = '_blank'
        return attrs

    @staticmethod
    def text_linkify(text):
        return bleach.linkify(text)

    @staticmethod
    def get_content_type(target):
        return ContentType.objects.get_for_model(target)

    @staticmethod
    def get_content_type_by_id(ct):
        return ContentType.objects.get(id=ct)

    @classmethod
    def get_target(cls, target_ct, target_id):
        # print('get_target', target_ct, target_id)
        return cls.get_content_type_by_id(target_ct).model_class().objects.get(id=target_id)

    @staticmethod
    def get_attr_list(arr, attr_name):
        '''
        :param arr: list of objects
        :param attr_name: object attribute
        :return: new list of 'arr' item object 'attr_name' attributes
        '''
        attr_arr = []
        for elem in arr:
            attr_arr.append(getattr(elem, attr_name))

        return attr_arr

    @staticmethod
    def list_sort__by_another_list_items_attr(list_to_sort, attr_name, list_sorted_by):
        '''
        Сортировка списка объектов по списку параметров этих объектов,
        например сортровка [Taxonomy] по списку id этих Taxonomy.

        Выдает ошибку если хотя бы в одном элементе 'list_to_sort' нет атрибута 'attr_name'
        :param list_to_sort:
        :param attr_name:
        :param list_sorted_by:
        :return: [typeof(list_to_sort[0]]
        '''
        list_sorted = []
        for item in list_sorted_by:
            try:
                list_sorted.append([s_item for s_item in list_to_sort if getattr(s_item, attr_name) == item][0])
            except:
                pass

        return list_sorted