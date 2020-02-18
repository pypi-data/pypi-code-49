#! /usr/bin/env python

from typing import List, Tuple, Dict, Union, TypeVar, Type

from easylabel.document import Annotation, Document  # type: ignore

# abstract type, use to annotate classmethod
C = TypeVar("C", bound="Corpus")


class Corpus:
    patterns: Dict[str, str]
    documents: List[Document]

    def __init__(self) -> None:
        self.patterns = {}
        self.documents = []

    def add(self, doc: Union[str, Document]) -> None:
        if doc:
            if isinstance(doc, str):
                doc = Document(doc)
            doc.corpus = self
            self.documents.append(doc)

    def add_patterns(self, patterns: Dict[str, str]) -> None:
        """Update self.patterns with the key/value pairs from patterns, overwriting existing keys. Return None."""
        self.patterns.update(patterns)

    def update_pattern(self, old_pat: str, new_pat: str) -> None:
        """Replace old_pat with new_pat, keeping the label in place. Raises KeyError."""
        self.patterns[new_pat] = self.patterns.pop(old_pat)

    def __len__(self) -> int:
        return len(self.documents)

    def annotate(self) -> None:
        for d in self.documents:
            d.annotate()

    def annotations(self) -> List[Document]:
        # Return documents with annotations
        return [d for d in self.documents if len(d) >= 1]

    def as_dict(self) -> Dict[str, Union[Dict, List]]:
        return {
            "patterns": self.patterns,
            "documents": [d.as_tuple() for d in self.documents],
        }

    @classmethod
    def from_json(
        cls: Type[C],
        corp_d: Dict[
            str, Union[Dict[str, str], List[Tuple[str, Tuple[int, int, str]]]]
        ],
    ) -> C:
        corp = cls()
        corp.patterns = corp_d["patterns"]  # type: ignore
        corp.documents = [Document.from_values(d) for d in corp_d["documents"]]  # type: ignore
        return corp

    def __eq__(self, other):
        if not isinstance(other, Corpus):
            raise TypeError(f"Can't compare Corpus to {type(other)}")
        return all(
            [
                all(a == b for a, b in zip(self.patterns, other.patterns)),
                all(a == b for a, b in zip(self.documents, other.documents)),
            ]
        )

    def __repr__(self):
        return f'Corpus("patterns": {self.patterns}, {self.documents})'
