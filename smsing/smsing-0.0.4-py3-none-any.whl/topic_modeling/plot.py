import math
import os
import pickle
import re
import warnings
import webbrowser
from collections import Counter
from pprint import pprint
import matplotlib
import gensim
import gensim.corpora as corpora
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import pyLDAvis
import pyLDAvis.gensim
import seaborn as sns
import spacy
from bokeh.models import Label
from bokeh.plotting import figure, output_file, show
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import FuncFormatter
from nltk.corpus import stopwords
from sklearn.manifold import TSNE
from wordcloud import STOPWORDS, WordCloud

import app.preprocessing as prep


def get_pyldavis(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)

    if os.path.exists(model_path + "/pyldavis.html"):
        webbrowser.open("file://" + os.path.realpath(model_path + "/pyldavis.html"))

    else:
        lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")

        with open(model_path + "/corpus.pkl", "rb") as f:
            corpus = pickle.load(f)

        # Visualize the topics
        vis = pyLDAvis.gensim.prepare(lda_model, corpus, lda_model.id2word)
        pyLDAvis.save_html(vis, model_path + "/pyldavis.html")

        webbrowser.open("file://" + os.path.realpath(model_path + "/pyldavis.html"))


def format_topics_sentences(ldamodel, corpus, texts) -> pd.DataFrame:
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for row_list in ldamodel[corpus]:
        row = row_list[0] if ldamodel.per_word_topics else row_list
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(
                    pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]),
                    ignore_index=True,
                )
            else:
                break
    sent_topics_df.columns = ["Dominant_Topic", "Perc_Contribution", "Topic_Keywords"]

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return sent_topics_df


def get_frequency_word_counts(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/frequency_word_counts.html")

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    with open(model_path + "/processed_texts.pkl", "rb") as f:
        texts = pickle.load(f)

    df_topic_sents_keywords = format_topics_sentences(
        ldamodel=lda_model, corpus=corpus, texts=texts
    )

    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = [
        "Document_No",
        "Dominant_Topic",
        "Topic_Perc_Contrib",
        "Keywords",
        "Text",
    ]
    df_dominant_topic.head(10)

    pd.options.display.max_colwidth = 100

    sent_topics_sorteddf_mallet = pd.DataFrame()
    sent_topics_outdf_grpd = df_topic_sents_keywords.groupby("Dominant_Topic")

    for i, grp in sent_topics_outdf_grpd:
        sent_topics_sorteddf_mallet = pd.concat(
            [
                sent_topics_sorteddf_mallet,
                grp.sort_values(["Perc_Contribution"], ascending=False).head(1),
            ],
            axis=0,
        )

    sent_topics_sorteddf_mallet.reset_index(drop=True, inplace=True)

    sent_topics_sorteddf_mallet.columns = [
        "Topic_Num",
        "Topic_Perc_Contrib",
        "Keywords",
        "Representative Text",
    ]

    sent_topics_sorteddf_mallet.head(10)

    doc_lens = [len(d) for d in df_dominant_topic.Text]

    plt.figure(figsize=(16, 7), dpi=160)
    plt.hist(doc_lens, bins=np.amax(doc_lens), color="navy")
    plt.text(750, 100, "Mean   : " + str(round(np.mean(doc_lens))))
    plt.text(750, 90, "Median : " + str(round(np.median(doc_lens))))
    plt.text(750, 80, "Stdev   : " + str(round(np.std(doc_lens))))
    plt.text(750, 70, "1%ile    : " + str(round(np.quantile(doc_lens, q=0.01))))
    plt.text(750, 60, "99%ile  : " + str(round(np.quantile(doc_lens, q=0.99))))

    plt.gca().set(
        xlim=(0, np.amax(doc_lens)),
        ylabel="Number of Documents",
        xlabel="Document Word Count",
    )
    plt.tick_params(size=16)
    plt.xticks(np.linspace(0, np.amax(doc_lens), 9))
    plt.title("Distribution of Document Word Counts", fontdict=dict(size=22))
    plt.show()

    cols = [color for name, color in mcolors.XKCD_COLORS.items()]

    fig, axes = plt.subplots(
        2,
        math.ceil(lda_model.num_topics / 2.0),
        figsize=(16, 14),
        dpi=160,
        sharex=True,
        sharey=True,
    )
    max_num_bins = 0

    for i, ax in enumerate(axes.flatten()):
        if lda_model.num_topics > i:
            df_dominant_topic_sub = df_dominant_topic.loc[
                df_dominant_topic.Dominant_Topic == i, :
            ]
            doc_lens = [len(d) for d in df_dominant_topic_sub.Text]
            if doc_lens != []:
                num_bins = np.amax(doc_lens)
            else:
                num_bins = 100

            if num_bins > max_num_bins:
                max_num_bins = num_bins
            ax.hist(doc_lens, bins=num_bins, color=cols[i])
            ax.tick_params(axis="y", labelcolor=cols[i], color=cols[i])
            sns.kdeplot(doc_lens, color="black", shade=False, ax=ax.twinx())
            ax.set(xlim=(0, num_bins), xlabel="Document Word Count")
            ax.set_ylabel("Number of Documents", color=cols[i])
            ax.set_title("Topic: " + str(i), fontdict=dict(size=16, color=cols[i]))
        else:
            fig.delaxes(axes[-1, -1])

    fig.tight_layout()
    fig.subplots_adjust(top=0.90)
    plt.xticks(np.linspace(0, max_num_bins, 9))
    fig.suptitle("Distribution of Document Word Counts by Dominant Topic", fontsize=22)
    plt.show()


def get_word_map(model_id: int, language: str):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/word_map.html")

    cols = [color for name, color in mcolors.XKCD_COLORS.items()]

    cloud = WordCloud(
        stopwords=stopwords.words(language),
        background_color="white",
        width=2500,
        height=1800,
        max_words=10,
        colormap="tab10",
        color_func=lambda *args, **kwargs: cols[i],
        prefer_horizontal=1.0,
    )

    topics = lda_model.show_topics(formatted=False)

    fig, axes = plt.subplots(
        2,
        math.ceil(lda_model.num_topics / 2.0),
        figsize=(10, 10),
        sharex=True,
        sharey=True,
    )

    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        if len(topics) > i:
            topic_words = dict(topics[i][1])
            cloud.generate_from_frequencies(topic_words, max_font_size=300)
            plt.gca().imshow(cloud)
            plt.gca().set_title("Topic " + str(i), fontdict=dict(size=16))
            plt.gca().axis("off")

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()


# TODO: Método adaptado para representación en el paper de Java
def get_word_counts_of_corpus(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    doc_sizes = [len(elem) for elem in corpus.corpus]

    doc_sizes = [elem for elem in doc_sizes if elem <= 100]
    # doc_sizes = [elem for elem in doc_sizes if elem <= 10]

    del corpus
    plt.figure(figsize=(12, 8), dpi=160)
    plt.rcParams.update({"font.size": 18})

    plt.hist(doc_sizes, bins=10, label="Word Count")
    # plt.hist(doc_sizes, bins=9, label="Word Count")

    plt.text(80, 700000, f"Mean:     {round(np.mean(doc_sizes))}")
    plt.text(80, 650000, f"Median:  {round(np.median(doc_sizes))}")
    plt.text(80, 600000, f"Stdev:    {round(np.std(doc_sizes))}")
    # plt.text(8, 700000, f"Mean:     {round(np.mean(doc_sizes))}")
    # plt.text(8, 650000, f"Median:  {round(np.median(doc_sizes))}")
    # plt.text(8, 600000, f"Stdev:    {round(np.std(doc_sizes))}")
    plt.gca().set(ylabel="Number of titles", xlabel="Number of words")
    plt.tick_params(size=12)
    plt.xticks(np.linspace(0, 100, 11))
    # plt.xticks(np.linspace(0, 10, 11))
    plt.yticks(np.linspace(0, 800000, 9))
    plt.savefig(f"{model_path}/words_in_titles.png", dpi=160)
    plt.show()


def get_word_counts_of_topic_keywords(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/word_counts_of_topic_keywords.html")

    with open(model_path + "/processed_texts.pkl", "rb") as f:
        texts = pickle.load(f)

    topics = lda_model.show_topics(formatted=False)
    data_flat = [w for w_list in texts for w in w_list]
    counter = Counter(data_flat)

    out = []
    for i, topic in topics:
        for word, weight in topic:
            out.append([word, i, weight, counter[word]])

    df = pd.DataFrame(out, columns=["word", "topic_id", "importance", "word_count"])
    max_importance = df.importance.max()
    max_word_count = df.word_count.max()

    # Plot Word Count and Weights of Topic Keywords
    fig, axes = plt.subplots(
        2, math.ceil(lda_model.num_topics / 2.0), figsize=(16, 10), sharey=True, dpi=160
    )
    cols = [color for name, color in mcolors.XKCD_COLORS.items()]
    for i, ax in enumerate(axes.flatten()):
        if lda_model.num_topics > i:
            ax.bar(
                x="word",
                height="word_count",
                data=df.loc[df.topic_id == i, :],
                color=cols[i],
                width=0.5,
                alpha=0.3,
                label="Word Count",
            )
            ax_twin = ax.twinx()
            ax_twin.bar(
                x="word",
                height="importance",
                data=df.loc[df.topic_id == i, :],
                color=cols[i],
                width=0.2,
                label="Weights",
            )
            ax.set_ylabel("Word Count", color=cols[i])
            # Ponemos la altura máxima a un 5% más para que se note donde acaba
            ax_twin.set_ylim(0, max_importance * 1.05)
            ax.set_ylim(0, max_word_count * 1.05)
            ax.set_title("Topic: " + str(i), color=cols[i], fontsize=16)
            ax.tick_params(axis="y", left=False)
            ax.set_xticklabels(
                df.loc[df.topic_id == i, "word"],
                rotation=30,
                horizontalalignment="right",
            )
        else:
            fig.delaxes(axes[-1, -1])

    fig.tight_layout(w_pad=2)
    fig.suptitle("Word Count and Importance of Topic Keywords", fontsize=22, y=1.05)
    plt.show()


def get_word_counts_of_topic_keywords_store_each(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/word_counts_of_topic_keywords.html")

    with open(model_path + "/processed_texts.pkl", "rb") as f:
        texts = pickle.load(f)

    topics = lda_model.show_topics(num_topics=lda_model.num_topics, formatted=False)
    data_flat = [w for w_list in texts for w in w_list]
    counter = Counter(data_flat)

    out = []
    for i, topic in topics:
        for word, weight in topic:
            out.append([word, i, weight, counter[word]])

    df = pd.DataFrame(out, columns=["word", "topic_id", "importance", "word_count"])
    max_importance = df.importance.max()
    max_word_count = df.word_count.max()

    cols = [color for name, color in mcolors.XKCD_COLORS.items()]
    """ TODO: Colores coherentes con pyldavis
    cols = [
        "#e9d1a4",
        "#ffc6c6",
        "#b4bbf4",
        "#cbd3aa",
        "#a8a8a8",
        "#f7ac7f",
        "#f0f2b3",
        "#c7a8d6",
        "#b9e9bc",
        "#eac3de",
    ]"""
    for i in range(lda_model.num_topics):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.bar(
            x="word",
            height="word_count",
            data=df.loc[df.topic_id == i, :],
            color=cols[i],
            width=0.5,
            alpha=0.3,
            label="Word Count",
        )
        ax_twin = ax.twinx()
        ax_twin.bar(
            x="word",
            height="importance",
            data=df.loc[df.topic_id == i, :],
            color=cols[i],
            width=0.2,
            label="Weights",
        )
        ax.set_ylabel("Word Count", color=cols[i])
        # Ponemos la altura máxima a un 5% más para que se note donde acaba
        ax_twin.set_ylim(0, max_importance * 1.05)
        ax.set_ylim(0, max_word_count * 1.05)
        ax.set_title("Topic: " + str(i), color=cols[i], fontsize=16)
        ax.tick_params(axis="y", left=False)
        ax.set_xticklabels(
            df.loc[df.topic_id == i, "word"], rotation=30, horizontalalignment="right"
        )
        fig.savefig(f"{model_path}/ax{i}_figure.png", dpi=160)


def get_sentences_chart(model_id: int, start: int = 0, end: int = 13):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/sentences_chart.html")

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    corp = corpus[start:end]
    mycolors = [color for name, color in mcolors.XKCD_COLORS.items()]
    mycolors = mycolors + mycolors

    fig, axes = plt.subplots(
        end - start, 1, figsize=(20, (end - start) * 0.95), dpi=160
    )
    axes[0].axis("off")
    for i, ax in enumerate(axes):
        if i > 0:
            corp_cur = corp[i - 1]
            topic_percs, wordid_topics, wordid_phivalues = lda_model[corp_cur]
            word_dominanttopic = []
            for wd, topic in wordid_topics:
                if len(topic) > 0:
                    word_dominanttopic.append((lda_model.id2word[wd], topic[0]))
                else:
                    word_dominanttopic.append((lda_model.id2word[wd], 10))
            # word_dominanttopic = [(lda_model.id2word[wd], topic[0]) for wd, topic in wordid_topics]
            ax.text(
                0.01,
                0.5,
                "Doc " + str(i - 1) + ": ",
                verticalalignment="center",
                fontsize=12,
                color="black",
                transform=ax.transAxes,
                fontweight=500,
            )

            # Draw Rectange
            ax.add_patch(Rectangle((0.0, 0.05), 0.99, 0.90, fill=False, alpha=1.0))

            word_pos = 0.06
            for j, (word, topics) in enumerate(word_dominanttopic):
                if j < 14:
                    ax.text(
                        word_pos,
                        0.5,
                        word,
                        horizontalalignment="left",
                        verticalalignment="center",
                        fontsize=12,
                        color=mycolors[topics],
                        transform=ax.transAxes,
                        fontweight=500,
                    )
                    word_pos += 0.009 * len(word)  # to move the word for the next iter
                    ax.axis("off")
            ax.text(
                word_pos,
                0.5,
                ". . .",
                horizontalalignment="left",
                verticalalignment="center",
                fontsize=12,
                color="black",
                transform=ax.transAxes,
            )

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.suptitle(
        "Sentence Topic Coloring for Documents: " + str(start) + " to " + str(end - 2),
        fontsize=22,
        y=0.95,
        fontweight=700,
    )
    plt.tight_layout()
    plt.show()


def get_most_discussed_topics(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")
    output_file(model_path + "/most_discussed_topics.html")

    with open(model_path + "/corpus.pkl", "rb") as f:
        corpus = pickle.load(f)

    corpus_sel = corpus[0 : len(corpus)]
    dominant_topics = []
    topic_percentages = []
    for i, corp in enumerate(corpus_sel):
        topic_percs, wordid_topics, wordid_phivalues = lda_model[corp]
        dominant_topic = sorted(topic_percs, key=lambda x: x[1], reverse=True)[0][0]
        dominant_topics.append((i, dominant_topic))
        topic_percentages.append(topic_percs)

    # Distribution of Dominant Topics in Each Document
    df = pd.DataFrame(dominant_topics, columns=["Document_Id", "Dominant_Topic"])
    dominant_topic_in_each_doc = df.groupby("Dominant_Topic").size()
    df_dominant_topic_in_each_doc = dominant_topic_in_each_doc.to_frame(
        name="count"
    ).reset_index()

    # Total Topic Distribution by actual weight
    topic_weightage_by_doc = pd.DataFrame([dict(t) for t in topic_percentages])
    df_topic_weightage_by_doc = (
        topic_weightage_by_doc.sum().to_frame(name="count").reset_index()
    )
    del df_topic_weightage_by_doc["index"]

    print(df_dominant_topic_in_each_doc)
    print(df_topic_weightage_by_doc)

    # Top 3 Keywords for each Topic
    topic_top3words = [
        (i, topic)
        for i, topics in lda_model.show_topics(formatted=False)
        for j, (topic, wt) in enumerate(topics)
        if j < 3
    ]

    df_top3words_stacked = pd.DataFrame(topic_top3words, columns=["topic_id", "words"])
    df_top3words = df_top3words_stacked.groupby("topic_id").agg(", \n".join)
    df_top3words.reset_index(level=0, inplace=True)
    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), dpi=120, sharey=True)

    # Topic Distribution by Dominant Topics
    ax1.bar(
        x="Dominant_Topic",
        height="count",
        data=df_dominant_topic_in_each_doc,
        width=0.5,
        color="firebrick",
    )
    ax1.set_xticks(
        range(df_dominant_topic_in_each_doc.Dominant_Topic.unique().__len__())
    )
    tick_formatter = FuncFormatter(
        lambda x, pos: "Topic "
        + str(x)
        + "\n"
        + df_top3words.loc[df_top3words.topic_id == x, "words"].values[0]
    )
    ax1.xaxis.set_major_formatter(tick_formatter)
    ax1.set_title("Number of Documents by Dominant Topic", fontdict=dict(size=10))
    ax1.set_ylabel("Number of Documents")
    ax1.set_ylim(0, df_dominant_topic_in_each_doc["count"].max())

    # Topic Distribution by Topic Weights
    ax2.bar(
        x="index",
        height="count",
        data=df_topic_weightage_by_doc,
        width=0.5,
        color="steelblue",
    )
    ax2.set_xticks(range(df_topic_weightage_by_doc.index.unique().__len__()))
    ax2.xaxis.set_major_formatter(tick_formatter)
    ax2.set_title("Number of Documents by Topic Weightage", fontdict=dict(size=10))

    plt.show()


def get_tsne_clustering_chart(model_id: int):
    model_path = "./app/topic_modeling_models/{}".format(model_id)
    if os.path.exists(model_path + "/cluster.html"):
        webbrowser.open("file://" + os.path.realpath(model_path + "/cluster.html"))
    else:
        lda_model = gensim.models.ldamodel.LdaModel.load(model_path + "/lda_model")

        with open(model_path + "/corpus.pkl", "rb") as f:
            corpus = pickle.load(f)
        # Get topic weights
        topic_weights = []
        for i, row_list in enumerate(lda_model[corpus]):
            topic_weights.append([w for i, w in row_list[0]])

        # Array of topic weights
        arr = pd.DataFrame(topic_weights).fillna(0).values

        # Keep the well separated points (optional)
        arr = arr[np.amax(arr, axis=1) > 0.35]

        # Dominant topic number in each doc
        topic_num = np.argmax(arr, axis=1)

        # tSNE Dimension Reduction
        tsne_model = TSNE(
            n_components=2,
            verbose=1,
            random_state=0,
            angle=0.99,
            init="pca",
            metric="cosine",
        )
        tsne_lda = tsne_model.fit_transform(arr)

        # Plot the Topic Clusters using Bokeh
        output_file(model_path + "/cluster.html")
        mycolors = np.array([color for name, color in mcolors.XKCD_COLORS.items()])
        plot = figure(
            title="t-SNE Clustering of {} LDA Topics".format(lda_model.num_topics),
            plot_width=900,
            plot_height=700,
        )
        plot.scatter(x=tsne_lda[:, 0], y=tsne_lda[:, 1], color=mycolors[topic_num])
        show(plot)
