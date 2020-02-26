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

from sekg.ir.models.tf_idf import TFIDFModel
from test.data.definition import ROOT_DIR
from test.ir.models.doc_sim_test_data import FakeDocumentCollectionData


class TestTFIDFModel(TestCase):
    def test_string2vector(self):
        model_dir = Path(ROOT_DIR) / "models" / "tfidf"
        dc = FakeDocumentCollectionData.fake_pre_dc()
        model: TFIDFModel = TFIDFModel.train(model_dir, dc)
        result = model.search("how to split a string")
        print(result)

        test_pair = [
            ("string", "String s"),
            ("how to split a string", "split string"),
            ("how to split a string", "split Strings"),
            ("how to split a string", "convert Strings"),
            ("how to split a string", "splitting Strings"),
            ("eat apple", "eating banana"),
            ("text", "file"),
            ("thread", "process"),
            ("thread", "process"),
            ("java", "python"),
            ("java code", "python code"),
            ("java program", "python code"),
            ("s1", "s2"),
            ("apple", "banana"),
            ("apples", "apple"),
            ("apple", "apple"),
            ("split apples", "split apple")

        ]
        for s1, s2 in test_pair:
            sim = model.sim_for_doc_pair(s1, s2)
            print(s1, "--VS--", s2, sim)

        to_text = ["how to split a string java", "split text", "contain special character",
                   "text contains", "str", "how to JAVA", "character"]
        sim = model.sim_for_one_to_many_docs("how to split a string java",
                                             to_text)
        print(sim)
        for text, score in zip(to_text, sim):
            print(text, score)
