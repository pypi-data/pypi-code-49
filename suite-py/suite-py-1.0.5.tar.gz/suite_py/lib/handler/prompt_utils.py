# -*- encoding: utf-8 -*-
import sys

from PyInquirer import prompt


def ask_confirm(text, default=True):
    questions = [
        {"type": "confirm", "message": text, "name": "continue", "default": default}
    ]
    answer = prompt(questions)
    return bool(answer["continue"])


def ask_questions_input(question_text, default_text=""):
    questions = [
        {
            "type": "input",
            "name": "value",
            "message": question_text,
            "default": default_text,
        }
    ]

    answer = prompt(questions)
    return answer["value"]


def ask_questions_editor(question_text, default_text=""):
    questions = [
        {
            "type": "editor",
            "name": "value",
            "message": question_text,
            "default": default_text,
            "eargs": {"editor": "default"},
        }
    ]

    answer = prompt(questions)
    return answer["value"]


def ask_choices(question_text, choices, default_text=""):
    questions = [
        {
            "type": "list",
            "name": "value",
            "message": question_text,
            "choices": choices,
            "default": default_text,
        }
    ]

    answer = prompt(questions)
    return answer["value"]


def project_confirmation(project):
    if not ask_confirm(f"Vuoi continuare sul progetto {project}?"):
        sys.exit(-1)
