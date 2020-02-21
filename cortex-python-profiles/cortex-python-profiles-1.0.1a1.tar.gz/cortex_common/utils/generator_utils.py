"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import itertools
import re
from typing import Callable, Any, List, Optional, Generator

from .object_utils import assign_to_dict
from .string_utils import split_string_into_parts

ToYeild = Any

__all__ = [
    "get_until",
    "get_unique_cortex_objects",
    "label_generator",
    "chunk_iterable"
]


def chunk_iterable(iterable, size) -> Generator[List, None, None]:
    """
    From: https://alexwlchan.net/2018/12/iterating-in-fixed-size-chunks/
    :param iterable:
    :param size:
    :return:
    """
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


def get_until(
        yielder:Callable[[], Any],
        appender:Callable[[Any, ToYeild], Any],
        ignore_condition:Callable[[Any, ToYeild], bool],
        stop_condition:Callable[[ToYeild], bool],
        to_yield:ToYeild) -> ToYeild:
    """
    Keep on yeilding items from a generator until certain conditions are met, optionally ignoring some generated items
    too ...
    :param yielder:
    :param appender:
    :param ignore_condition:
    :param stop_condition:
    :param to_yield:
    :return:
    """
    ignored = 0
    returnVal = to_yield
    while not stop_condition(returnVal):
        next_item = yielder()
        if ignore_condition(next_item, returnVal):
            ignored += 1
        else:
            returnVal = appender(next_item, returnVal)
    # print(ignored, len(returnVal))
    return returnVal


def get_unique_cortex_objects(yielder, limit:int) -> List:
    """
    Generate unique concepts similar to the Cortex Concept Synthesizor / Provider
    :param yielder:
    :param limit:
    :return:
    """
    return list(
        get_until(
            yielder,
            appender=lambda obj, dictionary: assign_to_dict(dictionary, obj["id"], obj),
            ignore_condition=lambda obj, dictionary: obj["id"] in dictionary,
            stop_condition=lambda dictionary: len(dictionary) >= limit,
            to_yield={}
        ).values()
    )


def label_generator(word:str, used_labels:List[str], label_length:int=3) -> Optional[str]:
    """
    Right now, labels are only three letters long!
    :param word:
    :param used_labels:
    :return:
    """
    words = re.split(r'[^a-zA-Z0-9]', word)
    if len(words) != label_length:
        word = "".join(words)
        words = split_string_into_parts(word, label_length)
    try:
        return "".join(next(filter(lambda x: "".join(x).upper() not in used_labels, itertools.product(*words)))).upper()
    except StopIteration as e:
        print("Failed to generate label")
        return None

    # longest_word = max(map(len, words))
    # extended_words = [
    #     list(word) + ['']*(longest_word-len(word)) for word in words
    # ]
    # list(itertools.combinations((itertools.chain(*list(zip(*extended_words)))), 3))

