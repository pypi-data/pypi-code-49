#! /usr/bin/env python

from dataclasses import dataclass, astuple
import re
from typing import List, Tuple, Dict, Optional, TypeVar, Type


# abstract type, use to annotate classmethod
D = TypeVar("D", bound="Document")


@dataclass(eq=True, frozen=True)
class Annotation:
    __slots__ = ["start", "end", "label"]
    start: int
    end: int
    label: str

    def span(self) -> Tuple:
        return (self.start, self.end)

    def overlaps(self, other):
        """Check if ranges overlap"""
        if set(range(*self.span())) & set(range(*other.span())):
            return True
        else:
            return False

    def __len__(self) -> int:
        return self.end - self.start

    def as_tuple(self):
        return astuple(self)


class Document:
    text: str
    corpus: Optional["Corpus"]  # type: ignore
    annotations: List[Annotation]

    def __init__(self, text: str) -> None:
        self.text = text
        self.annotations = []
        self.corpus = None

    def annotate(self, pats: Dict[str, str] = {}) -> None:
        if pats:
            patterns = pats
        else:
            patterns = self.corpus.patterns if self.corpus else {}

        # TODO: think of a way to indicate priority, other than length. (E.g. custom > spacy)
        # NB: spaCy labels are not in the patterns dict!
        for pat, lab in patterns.items():
            for m in re.finditer(rf"{pat}", self.text):
                A = Annotation(m.start(), m.end(), lab)
                # find overlapping annotations -- NB: this is expensive for documents with lots of annotations
                substrings = [b for b in self.annotations if A.overlaps(b)]
                if substrings:
                    # Remove the substrings from the list of annotations for this document
                    for s in substrings:
                        self.annotations.remove(s)
                    substrings.append(A)
                    # Append the annotation with the longest substring to the list of annotations
                    self.annotations.append(max(substrings, key=lambda x: len(x)))
                else:
                    self.annotations.append(A)

    def add_annotation(self, annotation: Annotation) -> None:
        if annotation not in self.annotations:
            self.annotations.append(annotation)

    def as_tuple(self) -> Tuple:
        return (self.text, [a.as_tuple() for a in self.annotations])

    def show(self) -> List[Tuple[Annotation, str]]:
        return [(a, self.text[a.start:a.end]) for a in self.annotations]

    @classmethod
    def from_values(cls: Type[D], tup: Tuple[str, List[Tuple[int, int, str]]]) -> D:
        txt, anns = tup
        doc = cls(txt)
        doc.annotations = [Annotation(*a) for a in anns]
        return doc

    def __repr__(self) -> str:
        return f'Document("{self.text}", {self.annotations})'

    def __eq__(self, other):
        if not isinstance(other, Document):
            raise TypeError(f"Can't compare Document to {type(other)}")
        return all(
            [
                self.text == other.text,
                all(a == b for a, b in zip(self.annotations, other.annotations)),
            ]
        )

    def __len__(self):
        """Use to check if Document has any annotations."""
        return len(self.annotations)
