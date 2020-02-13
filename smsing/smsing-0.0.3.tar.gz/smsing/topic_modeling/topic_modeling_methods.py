import csv
import itertools
import math
import os
import pickle
import platform
import re
import sys
from datetime import datetime
from pprint import pprint
from typing import Dict, List, Tuple

import gensim
import gensim.corpora as corpora
import numpy as np
import pandas as pd
import spacy
from gensim.matutils import Sparse2Corpus
from gensim.models import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.models.ldamulticore import LdaMulticore
from nltk.corpus import stopwords
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV

import smsing.preprocessing as prep
from smsing.errors import CorpusNotLoadedException


def build_corpus(
    model_id: int,
    path:str,
    data: List[str] = None,
    custom_dictionary: List[str] = None,
    min_count: int = 3,
    threshold: int = 10,
    tokenize: str = "tokenize",
    frequency: str = "tf",
) -> None:

    data = data or []
    custom_dictionary = custom_dictionary or []

    model_path = f"{path}/topic_modeling_models/{model_id}"


    if tokenize != None:
        tokenize_method = getattr(prep, tokenize)
        data = [tokenize_method(sent) for sent in data]

    bigram = gensim.models.Phrases(
        data, min_count=min_count, threshold=threshold, delimiter=b" "
    )
    trigram = gensim.models.Phrases(
        bigram[data], min_count=min_count, threshold=threshold, delimiter=b" "
    )
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    data_words = [bigram_mod[doc] for doc in data]

    del data

    data_words = [trigram_mod[bigram_mod[doc]] for doc in data_words]

    if custom_dictionary:
        id2word = corpora.Dictionary([custom_dictionary])
    else:
        id2word = corpora.Dictionary(data_words)

    corpus = [id2word.doc2bow(text) for text in data_words]

    if frequency == "tf-idf":
        tfidf = gensim.models.TfidfModel(corpus)
        corpus = tfidf[corpus]

    store_lda_data(model_path, corpus, id2word, data_words)

def append_corpus(
    model_id: int,
    data: List[str] = None,
    custom_dictionary: List[str] = None,
    min_count: int = 3,
    threshold: int = 10,
    tokenize: str = "tokenize",
    frequency: str = "tf",
) -> int:

    data = data or []
    custom_dictionary = custom_dictionary or []

    model_path = "./topic_modeling_models/{}".format(model_id)

    prev_corpus, id2word, _ = get_lda_data(model_path)

    if tokenize != None:
        tokenize_method = getattr(prep, tokenize)
        data = [tokenize_method(sent) for sent in data]

    bigram = gensim.models.Phrases(
        data, min_count=min_count, threshold=threshold, delimiter=b" "
    )
    trigram = gensim.models.Phrases(
        bigram[data], min_count=min_count, threshold=threshold, delimiter=b" "
    )
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    data = [bigram_mod[doc] for doc in data]
    data = [trigram_mod[bigram_mod[doc]] for doc in data]

    if custom_dictionary:
        id2word.add_documents([custom_dictionary])
    else:
        id2word.add_documents(data)

    corpus = [id2word.doc2bow(text) for text in data]
    corpus = prev_corpus.corpus + corpus

    if frequency == "tf-idf":
        tfidf = gensim.models.TfidfModel(corpus)
        corpus = tfidf[corpus]

    store_lda_data(model_path, corpus, id2word, data)
    return model_id


def join_corpus(merged_id: int, models: List[int]) -> int:
    """Almacena un nuevo corpus y un nuevo diccionario a partir de varios más pequeños

    Parameters
    ------------
    merged_id : int
        Id del directorio en el que se almacenan el diccionario y corpus resultante
    models : list
        Lista con los id de los modelos que queremos unir

    Returns
    ------------
    merged_id
        Id del directorio en el que se almacenan el diccionario y corpus resultante
    """
    corpus_list = []
    dictionaries = []
    for model_id in models:
        model_path = "./topic_modeling_models/{}".format(model_id)

        corpus, id2word = get_lda_data(model_path)
        corpus_list.append(corpus)
        dictionaries.append(id2word)

    previous_dict = dictionaries[0]
    previous_corpus = corpus_list[0]

    for i, corpus in enumerate(corpus_list[1:]):
        previous_dict = previous_dict.merge_with(dictionaries[i + 1])
        previous_corpus = itertools.chain(
            previous_corpus, previous_dict[corpus_list[i + 1]]
        )

    model_path = "./topic_modeling_models/{}".format(merged_id)

    store_lda_data(model_path, previous_corpus, previous_dict, None)

    return merged_id


def get_lda(
    model_id: int,
    num_topics: int,
    passes: int,
    update_every: int,
    alpha,
    beta,
    iterations: int,
    per_word_topics: bool,
    chunksize: int,
) -> int:
    model_path = "./topic_modeling_models/{}".format(model_id)

    corpus, id2word, data_words = get_lda_data(model_path)

    if platform.system() == "Windows" or alpha == "auto":
        lda_model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            num_topics=num_topics,
            passes=passes,
            update_every=update_every,
            alpha=alpha,
            eta=beta,
            # iterations=iterations,
            # per_word_topics=per_word_topics,
            random_state=100,
            # chunksize=chunksize,
        )
    else:
        lda_model = LdaMulticore(
            corpus=corpus,
            id2word=id2word,
            num_topics=num_topics,
            passes=passes,
            alpha=alpha,
            eta=beta,
            # iterations=iterations,
            # per_word_topics=per_word_topics,
            random_state=100,
            # chunksize=chunksize,
        )

    lda_model.save(model_path + "/lda_model")

    c_model = CoherenceModel(
        model=lda_model, texts=data_words, dictionary=id2word, coherence="c_v"
    )

    coherence = c_model.get_coherence()
    perplexity = lda_model.log_perplexity(corpus)
    print(
        f"[{datetime.now()}] Num topics:{num_topics}, Coherence(c_v):{coherence}, Perplexity:{perplexity}\n"
    )

    return model_id


def corpus_to_csv(model_id: int):
    model_path = "./topic_modeling_models/{}".format(model_id)

    lda_model = LdaModel.load(model_path + "/lda_model")

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    tokens = lda_model.id2word.id2token
    pressent_keys = corpus.obj.dfs.keys()
    pressent_tokens = {
        key: value for key, value in tokens.items() if key in pressent_keys
    }

    df = pd.DataFrame(columns=pressent_tokens.values())
    for doc in corpus:
        # Por cada documento se mete una fila de 0s
        df.loc[df.shape[0]] = [0] * df.shape[1]
        for token in doc:
            # Por cada aparición se aumenta el peso
            df.iloc[df.shape[0] - 1][pressent_tokens[token[0]]] += 1

    df.to_csv(model_path + "/corpus.csv")


def store_lda_data(model_path: str, corpus, id2word, texts):
    if not os.path.exists(model_path):
        os.makedirs(model_path)

    with open(model_path + "/corpus.pkl", "wb") as f:
        pickle.dump(corpus, f)

    with open(model_path + "/id2word.pkl", "wb") as f:
        pickle.dump(id2word, f)

    with open(model_path + "/processed_texts.pkl", "wb") as f:
        pickle.dump(texts, f)


def get_lda_data(model_path: str) -> Tuple:
    if not os.path.exists(model_path + "/corpus.pkl"):
        raise CorpusNotLoadedException(
            "No existe un corpus almacenado para el id de modelo indicado"
        )

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    with open(model_path + "/id2word.pkl", "rb") as f:
        id2word = pickle.load(f)

    with open(model_path + "/processed_texts.pkl", "rb") as f:
        processed_texts = pickle.load(f)

    return corpus, id2word, processed_texts


def get_results(model_id: int) -> Tuple[Dict, float, float, float, int]:
    model_path = "./topic_modeling_models/{}".format(model_id)

    lda_model = LdaModel.load(model_path + "/lda_model")

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)
    with open(model_path + "/id2word.pkl", "rb") as f:
        dictionary = pickle.load(f)
    with open(model_path + "/processed_texts.pkl", "rb") as f:
        processed_texts = pickle.load(f)
    raw_topics = lda_model.print_topics(num_topics=lda_model.num_topics)
    topics = {}
    for topic in raw_topics:
        topics[int(topic[0])] = {}

        for topic_weight in topic[1].split("+"):
            weight, term = topic_weight.split("*")
            weight = float(weight)
            term = term.replace('"', "").strip()
            topics[int(topic[0])][term] = weight

    """
    perplexity = lda_model.log_perplexity(corpus)
    u_mass = CoherenceModel(model=lda_model, corpus=corpus, coherence="u_mass")
    u_mass_coherence = u_mass.get_coherence()
    c_v = CoherenceModel(
        model=lda_model, texts=processed_texts, dictionary=dictionary, coherence="c_v"
    )
    c_v_coherence = c_v.get_coherence()
    """
    num_topics = lda_model.num_topics
    return topics, 0, 0, 0, num_topics


def get_num_documents(model_id: int) -> int:
    model_path = "./topic_modeling_models/{}".format(model_id)

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    return corpus.obj.num_docs


def get_topics_from_docs(docs: dict, model_id: int):
    model_path = "./topic_modeling_models/{}".format(model_id)

    lda_model = LdaModel.load(model_path + "/lda_model")
    _, id2word, _ = get_lda_data(model_path)

    data = []

    for key, elem in docs.items():
        bow = id2word.doc2bow(elem["text"])
        topic_distribution = dict(lda_model.get_document_topics(bow))
        num_topic = max(topic_distribution, key=topic_distribution.get)
        data.append(
            (
                int(key),
                float("{0:.4f}".format(topic_distribution[num_topic])),
                num_topic,
            )
        )

    return data


def print_results(lda_model, corpus):
    pprint(lda_model.print_topics())

    print(
        "\nPerplexity: ", lda_model.log_perplexity(corpus)
    )  # a measure of how good the model is. lower the better.

    # Compute Coherence Score. more the better.
    coherence_model_lda = CoherenceModel(
        model=lda_model, corpus=corpus, coherence="u_mass"
    )
    coherence_lda = coherence_model_lda.get_coherence()
    print("\nCoherence Score: ", coherence_lda)

    print("\nNumber of topics: {}\n".format(lda_model.num_topics))


def compute_coherence_values(
    model_id,
    custom_dictionary,
    tokenize,
    frequency,
    texts,
    topics_limit: int,
    topics_start: int,
    topics_step: int,
    min_count_limit: int,
    min_count_start: int,
    min_count_step: int,
    threshold_limit: int,
    threshold_start: int,
    threshold_step: int,
):
    stats = pd.DataFrame(
        columns=["num_topics", "min_count", "threshold", "coherence", "perplexity"]
    )
    for threshold in range(threshold_start, threshold_limit, threshold_step):
        for min_count in range(min_count_start, min_count_limit, min_count_step):
            print(f"[{datetime.now()}] threshold: {threshold}, min_count: {min_count}")

            try:
                build_corpus(
                    model_id,
                    texts,
                    custom_dictionary,
                    min_count,
                    threshold,
                    tokenize,
                    frequency,
                )

                print(f"[{datetime.now()}] Corpus loaded")

                for num_topics in range(topics_start, topics_limit, topics_step):

                    print(f"[{datetime.now()}] num_topics: {num_topics}")

                    model_path = "./topic_modeling_models/{}".format(model_id)
                    corpus, id2word, data_words = get_lda_data(model_path)

                    get_lda(
                        model_id, num_topics, 1, 1, "symmetric", None, 100, True, 2000
                    )

                    model = LdaModel.load(model_path + "/lda_model")

                    c_model = CoherenceModel(
                        model=model,
                        texts=data_words,
                        dictionary=id2word,
                        coherence="c_v",
                    )

                    coherence = c_model.get_coherence()
                    perplexity = model.log_perplexity(corpus)
                    print(
                        f"[{datetime.now()}] Num topics:{num_topics}, Coherence(c_v):{coherence}, Perplexity:{perplexity}\n"
                    )

                    if math.isnan(coherence):
                        break

                    stats = stats.append(
                        {
                            "num_topics": num_topics,
                            "min_count": min_count,
                            "threshold": threshold,
                            "coherence": coherence,
                            "perplexity": perplexity,
                        },
                        ignore_index=True,
                    )

                    stats.to_csv("{}/stats_coherence.csv".format(model_path))
            except Exception as e:
                print(f"[{datetime.now()}] {e}")


def refine_coherence_values(
    model_id,
    custom_dictionary,
    tokenize,
    frequency,
    texts,
    threshold: int,
    num_topics: int,
    min_count: int,
    limit: float,
    start: float,
    step: float,
):
    stats = pd.DataFrame(
        columns=["num_topics", "min_count", "threshold", "coherence", "perplexity"]
    )
    try:
        alphas = list(np.arange(start, limit, step)) + [
            "symmetric",
            "asymmetric",
            "auto",
        ]
        betas = list(np.arange(start, limit, step)) + ["symmetric"]
        model_path = ".topic_modeling_models/{}".format(model_id)
        corpus, id2word, data_words = get_lda_data(model_path)

        for alpha in alphas:
            for eta in betas:
                print(f"alpha: {alpha}, beta: {eta}")

                get_lda(model_id, num_topics, 1, 1, alpha, eta, 100, True, 2000)

                model = LdaModel.load(model_path + "/lda_model")

                c_model = CoherenceModel(
                    model=model, texts=data_words, dictionary=id2word, coherence="c_v"
                )

                coherence = c_model.get_coherence()
                perplexity = model.log_perplexity(corpus)
                print(
                    f"Num topics:{num_topics}, Coherence(c_v):{coherence}, Perplexity:{perplexity}\n"
                )

                if math.isnan(coherence):
                    break

                stats = stats.append(
                    {
                        "num_topics": num_topics,
                        "min_count": min_count,
                        "threshold": threshold,
                        "alpha": alpha,
                        "beta": eta,
                        "coherence": coherence,
                        "perplexity": perplexity,
                    },
                    ignore_index=True,
                )

                stats.to_csv("{}/stats_coherence_refined.csv".format(model_path))
    except Exception as e:
        print(e)
