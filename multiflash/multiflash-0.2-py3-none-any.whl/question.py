# Copyright 2020 John Reese
# Licensed under the MIT License

import random
from typing import List

from attr import dataclass

from multiflash.dataset import Fact


@dataclass
class Question:
    correct: Fact
    incorrect: List[Fact]
    full_answer: bool = False

    def ask(self) -> str:
        raise NotImplementedError

    def choices(self) -> List[str]:
        raise NotImplementedError

    def answer(self) -> str:
        raise NotImplementedError


@dataclass
class GuessKeyword(Question):
    full_answer: bool = True

    def ask(self) -> str:
        value = random.choice(self.correct.value_list)
        return f"________ means {value!r}"

    def choices(self) -> List[str]:
        tpl = "{keyword} ({description})"
        values = [
            tpl.format(
                keyword=self.correct.keyword, description=self.correct.description,
            )
        ]
        for fact in self.incorrect:
            values.append(
                tpl.format(keyword=fact.keyword, description=fact.description)
            )
        return values

    def answer(self) -> str:
        return self.correct.keyword


@dataclass
class GuessValue(Question):
    full_answer: bool = False
    value: str = ""

    def ask(self) -> str:
        return f"{self.correct.keyword!r} ({self.correct.description}) means"

    def choices(self) -> List[str]:
        self.value = random.choice(self.correct.value_list)
        values = [self.value] + [
            random.choice(fact.value_list) for fact in self.incorrect
        ]
        return values

    def answer(self) -> str:
        return self.value
