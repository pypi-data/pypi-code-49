#!/usr/bin/env python3
# coding: utf8

# Author: Lenz Furrer, 2020


"""
Test bconv.load() and bconv.loads().
"""


import json
from pathlib import Path

import pytest

import bconv


DATA = Path(__file__).parent / 'data'

COLL_LOADERS = [fmt for fmt, loader in bconv.LOADERS.items()
                if hasattr(loader, 'iter_documents')]
DOC_LOADERS = [fmt for fmt, loader in bconv.LOADERS.items()
               if hasattr(loader, 'document')]
COLL_FETCHERS = [fmt for fmt, loader in bconv.FETCHERS.items()
                 if hasattr(loader, 'iter_documents')]

TEXT_ONLY = {'txt', 'txt_json', 'pxml', 'pxml.gz', 'nxml', 'pubmed', 'pmc'}


@pytest.fixture(scope="module")
def expected():
    """Read the expected outputs from JSON dumps."""
    exp = {}
    for p in Path(DATA, 'internal').glob('*.json'):
        with open(p, 'r', encoding='utf8') as f:
            exp[p.stem] = json.load(f)
    return exp


@pytest.mark.parametrize('fmt', COLL_LOADERS)
def test_load_collection(fmt, expected):
    """Test the load function with multi-doc formats."""
    path = None  # marker for empty iteration
    for path in Path(DATA, fmt).glob('*'):
        exp = expected[path.stem]
        coll = bconv.load(fmt, path)

        assert _get_text(coll) == exp['text']
        if fmt not in TEXT_ONLY:
            assert _get_entities(coll) == exp['entities']
    assert path is not None, 'no test files found'


def _get_text(content):
    return [[[sent.text
              for sent in sec]
             for sec in doc]
            for doc in content.units('document')]


def _get_entities(content):
    return [[getattr(entity, att) for att in entity.__slots__]
            for entity in content.iter_entities()]
