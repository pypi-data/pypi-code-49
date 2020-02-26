#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

import gensim
import numpy as np
from gensim.models.keyedvectors import Word2VecKeyedVectors

from sekg.ir.doc.wrapper import PreprocessMultiFieldDocumentCollection
from sekg.ir.models.base import DocumentSimModel
from sekg.util.file import DirUtil
from bert_serving.client import BertClient


class AVGBertLModel(DocumentSimModel):
    __corpus_name__ = 'corpus.mm'
    __w2v_model_name__ = "bervec.model"
    __avg_w2v_model_name__ = "bert.avg.model"
    __dictionary_name__ = 'dictionary.dict'
    __sim_index__ = "avgbert.sim.index"

    __entity_collection_name__ = "doc.pre.collection"

    DEFAULT_EMBEDDING_SIZE = 768

    def __init__(self, name, model_dir_path, **config):

        """
        init the lsi model with
        :param model_dir_path:
        """
        super().__init__(name, model_dir_path, **config)
        self.bert_model = BertClient(ip="10.141.221.87")
        self.avg_w2v_model = None

        # self.avg_w2v_model_field_map = {}
        self.field_set = {}

        self.corpus = None
        self.dict = None
        self.similarity_index = None
        self.__init_sub_model_path__()
        self.preprocessor = None
        self.preprocess_doc_collection = None

        self.NP_VECTOR_NOT_EXIST = None
        self.embedding_size = 0
        self.__init_embedding_size(AVGBertLModel.DEFAULT_EMBEDDING_SIZE)

    def __init_sub_model_path__(self):
        if self.model_dir_path is None:
            return
        # init the paths of models
        self.corpus_path = os.path.join(self.model_dir_path, self.__corpus_name__)
        self.dictionary_path = os.path.join(self.model_dir_path, self.__dictionary_name__)
        self.w2v_model_path = os.path.join(self.model_dir_path, self.__w2v_model_name__)
        self.avg_w2v_model_path = os.path.join(self.model_dir_path, self.__avg_w2v_model_name__)

        # todo: fix the path name
        self.entity_collection_path = os.path.join(self.model_dir_path, self.__entity_collection_name__)

        self.sim_index_dir = os.path.join(self.model_dir_path, "index")

        self.sim_index_path = os.path.join(self.sim_index_dir, self.__sim_index__)

        DirUtil.create_file_dir(self.model_dir_path)
        DirUtil.create_file_dir(self.sim_index_dir)

    def __init_document_collection(self, preprocess_doc_collection):
        self.preprocess_doc_collection = preprocess_doc_collection
        self.preprocessor = preprocess_doc_collection.get_preprocessor()
        self.field_set = preprocess_doc_collection.get_field_set()

    def __init_embedding_size(self, embedding_size):
        self.embedding_size = embedding_size
        self.NP_VECTOR_NOT_EXIST = np.zeros(embedding_size)
        self.NP_VECTOR_NOT_EXIST[0] = 1e-07

    def init_model_as_submodel(self):
        print("init_sub_model_path")
        self.__init_sub_model_path__()

        print("loading doc_collection")
        preprocess_doc_collection = PreprocessMultiFieldDocumentCollection.load(self.entity_collection_path)
        self.preprocessor = preprocess_doc_collection.get_preprocessor()
        self.field_set = preprocess_doc_collection.get_field_set()

        self.avg_w2v_model = gensim.models.keyedvectors.Word2VecKeyedVectors.load(self.avg_w2v_model_path)

    def init_model(self):
        """
        init the model
        :return:
        """
        print("init_sub_model_path")
        self.__init_sub_model_path__()

        print("loading doc_collection")
        preprocess_doc_collection = PreprocessMultiFieldDocumentCollection.load(self.entity_collection_path)
        self.__init_document_collection(preprocess_doc_collection)

        self.avg_w2v_model = gensim.models.keyedvectors.Word2VecKeyedVectors.load(self.avg_w2v_model_path)

        # todo: load the index
        self.corpus = gensim.corpora.MmCorpus(self.corpus_path)
        self.dict = gensim.corpora.Dictionary.load(self.dictionary_path)
        print("All document number: ", self.dict.num_docs)
        print("All words number: ", self.dict.num_pos)

    def get_full_doc_score_vec(self, query):
        full_entity_score_vec = self.get_cache_score_vector(query)
        if full_entity_score_vec is not None:
            return full_entity_score_vec

        query_vec = self.string2vector(query)
        sim_score_vec = self.avg_w2v_model.similar_by_vector(query_vec, topn=None)
        full_entity_score_vec = (sim_score_vec + 1) / 2

        self.cache_entity_score_vector(query, full_entity_score_vec)

        return full_entity_score_vec

    def train_from_document_collection(self, preprocess_document_collection, embedding_size=100,
                                       ):
        print("start training")
        self.__init_embedding_size(embedding_size)
        self.__init_document_collection(preprocess_document_collection)

        corpus_clean_text = []
        preprocess_multi_field_doc_list = preprocess_document_collection.get_all_preprocess_document_list()
        for docno, multi_field_doc in enumerate(preprocess_multi_field_doc_list):
            corpus_clean_text.append(multi_field_doc.get_document_text_words())

        print("corpus len=%d" % len(corpus_clean_text))

        print("Dictionary init...")
        self.dict = gensim.corpora.Dictionary(corpus_clean_text)
        print(" Dictionary init complete ")

        print("parse to bow corpus")
        self.corpus = [self.dict.doc2bow(text) for text in corpus_clean_text]
        print("parse to bow corpus complete")

        self.compute_avgw2v_for_docs(preprocess_document_collection)

    def compute_avgw2v_for_docs(self, preprocess_document_collection):
        avg_w2v_model = gensim.models.keyedvectors.Word2VecKeyedVectors(vector_size=self.embedding_size)
        corpus_clean_text = preprocess_document_collection.get_all_preprocess_documents_text_words()

        avg_vector_list = []
        avg_index_str_list = []
        for index, doc_clean_text in enumerate(corpus_clean_text):
            avg_vector = self.get_avg_bert_vec(doc_clean_text)
            avg_vector_list.append(avg_vector)
            avg_index_str_list.append(str(index))
            if index % 1000 == 0:
                print("index=%d avg_vec" % index)
        print("avg_index_str_list len=%d avg_vector_list=%d" % (len(avg_index_str_list), len(avg_vector_list)))

        avg_w2v_model.add(entities=avg_index_str_list, weights=avg_vector_list, replace=True)
        self.avg_w2v_model = avg_w2v_model

    def get_avg_bert_vec(self, word_str_list):
        """
        get the average word2vec for list of str
        :param word_str_list:  list of str
        :return: np.array()
        """
        # todo: add a empty zero vectors result.
        if len(word_str_list) == 0:
            return self.NP_VECTOR_NOT_EXIST

        valid_word_str_list = []

        for word in word_str_list:
            valid_word_str_list.append(word)

        if len(valid_word_str_list) == 0:
            return self.NP_VECTOR_NOT_EXIST

        doc_word_vectors = self.bert_model.encode([valid_word_str_list], is_tokenized=True)
        avg_vector = np.mean(doc_word_vectors, axis=0)
        return avg_vector

    def train_from_doc_collection_with_preprocessor(self, doc_collection, **config):
        embedding_size = self.DEFAULT_EMBEDDING_SIZE

        if "embedding_size" in config.keys():
            embedding_size = config["embedding_size"]

        print("start training")

        if isinstance(doc_collection, PreprocessMultiFieldDocumentCollection):
            self.train_from_document_collection(preprocess_document_collection=doc_collection,
                                                embedding_size=embedding_size,
                                                )

    def save(self, model_dir_path):
        """
        save model to the model_dir_path
        :param model_dir_path: the dir to save the model
        :return:
        """
        super().save(model_dir_path)

        self.__init_sub_model_path__()

        self.dict.save(self.dictionary_path)

        print("build dictionary in %s" % self.dictionary_path)

        gensim.corpora.MmCorpus.serialize(self.corpus_path, self.corpus)
        print("save the corpus to %s" % self.corpus_path)

        self.avg_w2v_model.save(self.avg_w2v_model_path)
        print("AVGWord2vec Training finish , save to %s" % self.avg_w2v_model_path)

        print("entity collection saving...")
        self.preprocess_doc_collection.save(self.entity_collection_path)
        print(
            "entity collection finish saving , save to %s, %r" % (
                self.entity_collection_path, self.preprocess_doc_collection))

    def support_text2vector(self):
        return True

    def string2vector(self, doc):
        query_words = self.preprocessor.clean(doc)
        avg_vector = self.get_avg_bert_vec(query_words)
        return avg_vector

    def words2vector(self, words):
        avg_vector = self.get_avg_bert_vec([w.lower() for w in words])
        return avg_vector
