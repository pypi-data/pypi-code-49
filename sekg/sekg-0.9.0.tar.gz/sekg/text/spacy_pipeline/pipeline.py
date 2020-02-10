#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: isky
@Email: 19110240019@fudan.edu.cn
@Created: 2019/12/13
------------------------------------------
@Modify: 2019/12/13
------------------------------------------
@Description:
"""
import neuralcoref
import spacy

from sekg.text.spacy_pipeline.tokenizer import CustomizeSpacy
from sekg.text.spacy_pipeline.sentenceHandler import SentenceHandler
from sekg.util.spacy_fixer import SoftwareTextPOSFixer


class PipeLineFactory:
    @staticmethod
    def custom_pipeline(**config):
        """
        create a new custom pipeline with fixing some tokenization problem.
        """
        nlp = spacy.load('en_core_web_sm')
        CustomizeSpacy.customize_tokenizer_split_single_lowcase_letter_and_period(nlp)
        CustomizeSpacy.customize_tokenizer_merge_hyphen(nlp)
        CustomizeSpacy.customize_tokenizer_api_name_recognition(nlp)
        nlp.add_pipe(SentenceHandler.hyphen_handler, name='sh', after='tagger')
        return nlp

    @staticmethod
    def full_pipeline():
        nlp = spacy.load('en', disable=["ner"])
        CustomizeSpacy.customize_tokenizer_split_single_lowcase_letter_and_period(nlp)
        CustomizeSpacy.customize_tokenizer_merge_hyphen(nlp)
        CustomizeSpacy.customize_tokenizer_api_name_recognition(nlp)
        nlp.add_pipe(SentenceHandler.hyphen_handler, name='sh', after='tagger')
        # 将核心动词与紧挨着的head是这个动词的介词合并
        # nlp.add_pipe(SentenceHandler.merge_verb_prep, name='merge_verb_prep', after='parser')
        nlp.add_pipe(SoftwareTextPOSFixer.fixer_for_pos, name="pos_fixer", after="tagger")
        nlp.add_pipe(SentenceHandler.tag_fixer_after_parser, name='pos_fixer_after_parser', after='parser')
        return nlp

    @staticmethod
    def full_pipeline_for_xss():
        nlp = spacy.load('en', disable=["ner"])
        CustomizeSpacy.customize_tokenizer_split_single_lowcase_letter_and_period(nlp)
        CustomizeSpacy.customize_tokenizer_merge_hyphen(nlp)
        CustomizeSpacy.customize_tokenizer_merge_dot_upper_letter(nlp)
        CustomizeSpacy.customize_tokenizer_api_name_recognition(nlp)
        nlp.add_pipe(CustomizeSpacy.customize_sentencizer_merge_colon, before="tagger")
        nlp.add_pipe(CustomizeSpacy.pipeline_merge_bracket, name='pipeline_merge_bracket', after='tagger')
        return nlp

    @staticmethod
    def full_pipeline_for_coreference_resolution():
        nlp = spacy.load('en', disable=["ner"])

        nlp.add_pipe(SentenceHandler.hyphen_handler, name='sh', before='tagger')
        nlp.add_pipe(SoftwareTextPOSFixer.fixer_for_pos, name="pos_fixer", after="tagger")
        neuralcoref.add_to_pipe(nlp, greedyness=0.5)
        return nlp
