#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: isky
@Email: 19110240019@fudan.edu.cn
@Created: 2020/02/20
------------------------------------------
@Modify: 2020/02/20
------------------------------------------
@Description:
"""
from pathlib import Path
from unittest import TestCase

from sekg.model.word2vec.tune_word2vec import TunedWord2VecTrainer
from test.data.definition import ROOT_DIR
from test.ir.models.doc_sim_test_data import FakeDocumentCollectionData


class TestTuneWord2vec(TestCase):
    def test_tune(self):
        dc = FakeDocumentCollectionData.fake_pre_dc()
        word2vec_path = Path(ROOT_DIR) / "pretrain" / "pretrainwiki.100.w2v.bin"
        model = TunedWord2VecTrainer.tune_from_pre_doc_collection(dc, pretrain_w2v_path=str(word2vec_path))
