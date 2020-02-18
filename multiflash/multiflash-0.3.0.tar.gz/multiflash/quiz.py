# Copyright 2020 John Reese
# Licensed under the MIT License

import random
from typing import List, Set, Type, Optional

import click

from multiflash.dataset import Fact, Facts, connect
from multiflash.question import GuessKeyword, GuessValue, Question

DEFAULT_QUESTION_TYPES = (GuessKeyword, GuessValue)


class Quiz:
    def __init__(
        self,
        class_name: str,
        num_choices: int = 4,
        question_limit: Optional[int] = None,
        question_types: List[Type[Question]] = None,
    ):
        self.class_name = class_name
        self.num_choices = num_choices
        self.question_limit = question_limit
        self.question_types = question_types or DEFAULT_QUESTION_TYPES

        self.counter: int = 0
        self.questions: List[Question] = []

        self._facts: Set[Fact] = set()

    @property
    def facts(self) -> Set[Fact]:
        if not self._facts:
            db, engine = connect()
            query = Facts.select().where(Facts.class_name == self.class_name)
            cursor = db.execute(*engine.prepare(query))
            rows = cursor.fetchall()
            self._facts.update(Fact(**row) for row in rows)
        return self._facts

    def generate(self) -> List[Question]:
        questions: List[Question] = []

        all_facts = self.facts
        num_incorrect = self.num_choices - 1

        for guess_type in self.question_types:
            for fact in all_facts:
                incorrect = random.sample(all_facts - {fact}, num_incorrect)
                q = guess_type(fact, incorrect)
                questions.append(q)

        if self.question_limit:
            questions = questions[: self.question_limit]

        return questions

    def ask(self, question: Question) -> bool:
        click.echo(f"\nQuestion {self.counter}: {question.ask()}\n")

        letter = ord("a")
        choices = question.choices()
        answer = question.answer()

        for choice in random.sample(choices, len(choices)):
            if question.full_answer:
                click.echo(f"  • {choice}")
            else:
                if choice == answer:
                    answer = chr(letter)
                click.echo(f"  {chr(letter)}) {choice}")
                letter += 1

        response = click.prompt("\nAnswer: ", prompt_suffix="").strip()

        if response.lower() == answer.lower():
            click.echo("Correct!")
            return True

        click.echo(f"Incorrect. Correct answer was {answer!r}")
        return False

    def start(self):
        questions = self.generate()
        random.shuffle(questions)

        self.counter = 0
        score = 0
        for question in questions:
            self.counter += 1
            correct = self.ask(question)
            if correct:
                score += 1

        click.echo(f"\nQuiz complete. You scored {score} / {len(questions)} correct!")
