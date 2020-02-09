from pathlib import Path

from .note import Note


def test_note():

    note = Note(Path('data/3.md'))

    assert repr(note) == 'Note(data/3.md)'
    assert note['Title'] == 'C'
