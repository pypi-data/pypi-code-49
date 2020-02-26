# coding: utf8

import argparse
import re
import sys
import warnings
import collections
import random

from pathlib import Path
from typing import List

from ehealthkd.submit import Algorithm, Run, handle_args
from ehealthkd.utils import Collection, Keyphrase, Relation, Sentence, tokenize


class DummyBaseline(Algorithm):
    def __init__(self):
        self.model = None

    def train(self, finput: Path):
        collection = Collection().load(finput)

        self.model = keyphrases, relations = {}, {}

        for sentence in collection.sentences:
            for keyphrase in sentence.keyphrases:
                text = keyphrase.text.lower()
                keyphrases[text] = keyphrase.label

        for sentence in collection.sentences:
            for relation in sentence.relations:
                origin = relation.from_phrase
                origin_text = origin.text.lower()
                destination = relation.to_phrase
                destination_text = destination.text.lower()

                relations[
                    origin_text, origin.label, destination_text, destination.label
                ] = relation.label

    def run(self, collection, *args, taskA, taskB, **kargs):
        gold_keyphrases, gold_relations = self.model

        if taskA:
            next_id = 0
            for gold_keyphrase, label in gold_keyphrases.items():
                for sentence in collection.sentences:
                    text = sentence.text.lower()
                    pattern = r"\b" + gold_keyphrase + r"\b"
                    for match in re.finditer(pattern, text):
                        keyphrase = Keyphrase(sentence, label, next_id, [match.span()])
                        keyphrase.split()
                        next_id += 1

                        sentence.keyphrases.append(keyphrase)

        if taskB:
            for sentence in collection.sentences:
                for origin in sentence.keyphrases:
                    origin_text = origin.text.lower()
                    for destination in sentence.keyphrases:
                        destination_text = destination.text.lower()
                        try:
                            label = gold_relations[
                                origin_text,
                                origin.label,
                                destination_text,
                                destination.label,
                            ]
                        except KeyError:
                            continue
                        relation = Relation(sentence, origin.id, destination.id, label)
                        sentence.relations.append(relation)

                sentence.remove_dup_relations()

        return collection


class RandomBaseline(Algorithm):
    def train(self, finput: Path):
        self.keyphrase_classes = collections.Counter()
        self.relation_classes = collections.Counter()

        collection = Collection().load(finput)

        for sentence in collection.sentences:
            for keyphrase in sentence.keyphrases:
                self.keyphrase_classes[keyphrase.label] += 1

            total_tokens = len(tokenize(sentence.text))
            self.keyphrase_classes[""] += total_tokens - len(sentence.keyphrases)

        for sentence in collection.sentences:
            for relation in sentence.relations:
                self.relation_classes[relation.label] += 1

            total_relations = len(sentence.keyphrases) * len(sentence.keyphrases)
            self.relation_classes[""] += total_relations - len(sentence.relations)

    def run(self, collection, *args, taskA, taskB, **kargs):
        if taskA:
            next_id = 0

            for sentence in collection.sentences:
                pos = 0

                for token, spans in tokenize(sentence.text):
                    label = random.choices(
                        list(self.keyphrase_classes),
                        list(self.keyphrase_classes.values()),
                    )[0]

                    if label:
                        keyphrase = Keyphrase(
                            sentence, label, next_id, [spans]
                        )
                        sentence.keyphrases.append(keyphrase)
                        next_id += 1

                    pos += len(token) + 1

        if taskB:
            for sentence in collection.sentences:
                for origin in sentence.keyphrases:
                    for destination in sentence.keyphrases:
                        label = random.choices(
                            list(self.relation_classes),
                            list(self.relation_classes.values()),
                        )[0]

                        if label:
                            relation = Relation(
                                sentence, origin.id, destination.id, label
                            )
                            sentence.relations.append(relation)

                sentence.remove_dup_relations()

        return collection


def main(tasks):
    if not tasks:
        warnings.warn("The run will have no effect since no tasks were given.")
        return

    baseline = DummyBaseline()
    baseline.train(Path("../corpus/training/scenario.txt"))
    Run.submit("baseline", tasks, "dummy", baseline)

    baseline = RandomBaseline()
    baseline.train(Path("../corpus/training/scenario.txt"))
    Run.submit("baseline", tasks, "random", baseline)


if __name__ == "__main__":
    tasks = handle_args()
    main(tasks)
