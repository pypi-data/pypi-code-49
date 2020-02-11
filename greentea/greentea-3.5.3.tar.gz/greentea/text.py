"""Implement a wrapper for `str`."""
import os
from dataclasses import dataclass
import re
from typing import Sequence
import collections.abc as collections


@dataclass
class Text:
    """Represent a text.

    Attributes
    ----------
    text: str

    """

    text: str

    def concat(self, text, separator='. '):
        """Concatenation of itself and `text`.

        Parameters
        ----------
        text: Text
            a text to be concatenated.

        """
        if text.is_empty():
            return self
        return Text(f'{self.text}{separator}{text.text}')

    def is_empty(self) -> bool:
        """Return `True` iff empty."""
        return len(self.text) == 0

    def strip(self):
        """Return the Stripped text.

        Returns
        -------
        Text

        """
        text = self.text.strip()
        return Text(text)

    def empty():
        """Return an emtpy :py:class:`Text`."""
        return Text('')

    def end_with_linesep(self):
        """Append a line separator if `self` does not end with it.

        Return
        ------
        Text

        """
        if self.text.endswith(os.linesep):
            return self
        return Text(f'{self.text}{os.linesep}')

    def tokenize(self, tokenizer):
        """Tokenize `self` to Texts.

        Parameters
        ----------
        tokenizer: function
            Take a `str`, and tokenize it
            to a sequence of :py:class:`Text`.

        Returns
        -------
        Texts

        """
        return Texts(tokenizer(self.text))

    def remove_consec_linesep(self):
        """Convert the consecutive line separators to a line separator."""
        pattern = re.compile(f"{os.linesep}+")
        return Text(re.sub(pattern, os.linesep, self.text))

    def join(self, texts):
        """Return a :py:class:`Text` which is the concatenation of `texts`.

        The separator between items is the the text providing this method.

        Parameters
        ----------
        texts: Texts

        Returns
        -------
        Text

        """
        return Text(self.text.join((txt.text for txt in texts)))

    def contains_only_whitespaces(self) -> bool:
        """Return `True` iff :py:attr:`text` contains only whitespace chars."""
        return re.match(r'^\s*$', self.text)


@dataclass
class Texts(collections.Sequence):
    """A sequence of :py:class:`Text`."""

    texts: Sequence[Text]

    def __len__(self):
        """Return the size of :py:attr:`texts`."""
        return len(self.texts)

    def __getitem__(self, s):
        """Access a subset of: py: attr: `texts`."""
        found = self.texts.__getitem__(s)
        if isinstance(found, Text):
            return found
        return Texts(found)

    def remove_whitespaces(self):
        """Return the :py:class:`Texts` with no whitespace characters.

        Returns
        -------
        Texts
        :py:attr:`texts` gets list.

        """
        return Texts([text
                      for text in self.texts
                      if not text.contains_only_whitespaces()])

