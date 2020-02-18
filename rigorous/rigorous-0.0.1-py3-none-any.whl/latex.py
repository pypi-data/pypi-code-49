# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import pathlib

import click

from . import syntax


@click.group()
def main() -> None:
    """
    Auxiliary tool for our POPL20 paper.
    """


_DEFAULT_TARGET = (pathlib.Path(__file__).parent.parent / "generated").absolute()


@main.command()
@click.option(
    "--target",
    type=click.Path(exists=True, file_okay=False),
    default=str(_DEFAULT_TARGET),
)
def dump_syntax(target: str) -> None:
    target_path = pathlib.Path(target).absolute()

    print(f"Generating LaTeX files...")
    print(f"Target Directory: {target_path}")

    (target_path / "full_syntax.tex").write_text(
        r"\begin{align*}" + syntax.LATEX_FULL_SYNTAX + r"\end{align*}", encoding="utf8"
    )
