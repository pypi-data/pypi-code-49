# coding: utf-8
import argparse

import os

import pandas as pd
import json

from sklearn.feature_extraction.text import CountVectorizer

# import sys
# sys.path.insert(0, 'topic_modeling_twitter/preprocessing')
from topic_modeling.preprocessing.text_preprocessing import *


# Functions to filter tweets
def create_tweet_matrix(corpus):
    """Create a doc-term matrix from a given corpus"""
    vectorizer = CountVectorizer(min_df=max(int(len(corpus) * 0.0025), 10), ngram_range=(2, 3),  # 1,3
                                 binary=True)
    doc_term_matrix = vectorizer.fit_transform(corpus)
    return doc_term_matrix


def filter_low_text_tweets(doc_term_matrix, term_no):
    """Return index of tweets that should be involved """
    included_tweet_ids=[]
    for i in range(0, doc_term_matrix.shape[0]):
        # keep sample with size at least 5
        if doc_term_matrix[i].sum() > term_no:
            included_tweet_ids.append(i)
    return included_tweet_ids


def get_rich_text_tweets(text_list, no_terms_per_tweet):
    """Create tweet_term matrix with bi-grams and tri-grams , including vocabulary filtering"""
    doc_term_matrix = create_tweet_matrix(text_list)

    """Filter tweets that does not include the minium number of terms, required for a rich tweet """
    included_indices  = filter_low_text_tweets(doc_term_matrix, no_terms_per_tweet)
    return included_indices


def remove_repeated_tweets(df,text_column,no_repeated_column):
    """Remove repeated tweets from a given data-frame"""
    columns_name = list(df.columns) + [no_repeated_column]
    df_clean = pd.DataFrame(columns=columns_name)

    for index, row in df.iterrows():
        tweet_found = df_clean.loc[df_clean[text_column] == row[text_column]].shape[0]
        if tweet_found >0:
            repeated_num = df_clean.loc[df_clean[text_column] == row[text_column],no_repeated_column]
            df_clean.loc[df_clean[text_column] == row[text_column], no_repeated_column] = repeated_num.iloc[0] + 1
        else:

            df_row = df[df.index == index].copy()
            df_row[no_repeated_column] = 1
            df_clean = df_clean.append(df_row)
    return df_clean


def clean(doc, lemmatization, users_no, hash_no, terms_no, no_filter, no_hash_sign = False, hashtags_weight=1):

    normalized , usr_count, hash_count, words_count = clean_text(doc, lemmatization,no_hash_sign, hashtags_weight)

    if not no_filter:  # filter tweets with too many usernames, hashtags or very short texts, then it return empty text
        if usr_count > users_no or hash_count > hash_no or words_count < terms_no:
            return ""

    return normalized


def read_news_accounts(news_accounts_file_path):
    """return accounts of News organizations"""
    news_accounts_file = open(news_accounts_file_path,'r')
    acc = news_accounts_file.read().split(",")
    news_accounts_file.close()
    accounts = [c.replace("\n","").strip() for c in acc]
    return accounts


def json_reader_generator(fp):
    """JSON lines generator."""
    with open(fp, "r") as f:
        for line in f:
            yield json.loads(line)

if __name__ == '__main__':

    # parse arguments if available
    parser = argparse.ArgumentParser(description='Data preparation')
    parser.add_argument(
        '--input_fp',
        type=str, nargs="*",
        help='source file'
    )
    parser.add_argument(
        '--output_fp',
        type=str,
        default=None,
        help='result file'
    )

    parser.add_argument(
        '--lemmatization',
        type=bool,
        default=False,
        help='spedify if pre-processing should include lemmatization or not'
    )

    parser.add_argument(
        '--no_news',
        type=bool,
        default=False,
        help='spedify if tweets from News organizations should be removed, or not'
    )

    parser.add_argument(
        '--news_acc',
        type=str,
        default="",
        help='file includes news accounts'
    )

    parser.add_argument(
        '--hashtags_weight',
        type=int,
        default=1,
        help='number of times a hashtag should be weighted'
    )

    parser.add_argument(
        '--no_hash_sign',
        type=bool,
        default=False,
        help='indicate whether hashtag sign should be removed'
    )

    parser.add_argument(
        '--no_repeated_tweet',
        type=bool,
        default=False,
        help='repeated tweets are removed'
    )

    parser.add_argument(
        '--no_users_per_tweet',
        type=int,
        default=2,
        help='maximum number of mentioned users that are allowed in tweets, otherwise the tweet is filtered'
    )

    parser.add_argument(
        '--no_hashtags_per_tweet',
        type=int,
        default=2,
        help='maximum number of hashtags that are allowed in tweets, otherwise the tweet is filtered'
    )

    parser.add_argument(
        '--no_terms_per_tweet',
        type=int,
        default=4,
        help='minimum number of terms that are required in tweets, otherwise the tweet is filtered'
    )

    parser.add_argument(
        '--user_subset_fp',
        type=str,
        default=None,
        help='specifies if the tweets from a subset of users, for example main actors should be selected'
    )

    # if false, no filtering on tweets is applicable, only pre-processing on text
    # is applied. This is a preprocessing before applying topic model on a dataset.
    parser.add_argument(
        '--no_filter',
        type=bool,
        default=False,
        help='specifies if short text tweets should be filtered'
    )

    args = parser.parse_args()  # parse all the arguments

    if args.output_fp is not None:
        directory = os.path.dirname(args.output_fp)
        if not os.path.exists(directory):
            os.makedirs(directory)


    result = []
    for fp in args.input_fp:
        print("Processing file {}".format(fp))
        for doc in json_reader_generator(fp):
            if "extended_tweet" in doc:
                result.append(
                    {"id": doc["id"],
                     "created_at": doc["created_at"],
                     'clean_text': clean(doc["extended_tweet"]["full_text"], args.lemmatization, args.no_users_per_tweet,
                                        args.no_hashtags_per_tweet,args.no_terms_per_tweet, args.no_filter,
                                        args.no_hash_sign, args.hashtags_weight),
                     "screen_name": doc["user"]["screen_name"],
                     }
                )
            else:
                result.append(
                    {"id": doc["id"],
                     "created_at": doc["created_at"],
                     'clean_text': clean(doc['text'], args.lemmatization, args.no_users_per_tweet,
                                        args.no_hashtags_per_tweet,args.no_terms_per_tweet, args.no_filter,
                                        args.no_hash_sign, args.hashtags_weight),
                     "screen_name": doc["user"]["screen_name"],
                    }
                )

    clean_data_df = pd.DataFrame(result)
    print(clean_data_df.shape)

    if args.user_subset_fp is not None:  # if tweets of a specific list of users are requiered
        df_user_subset = pd.read_csv(args.user_subset_fp)
        clean_data_df = clean_data_df.merge(df_user_subset, on='screen_name')
        print(clean_data_df.shape)

    if args.no_filter:  # if short tweets should be included, i.e. for dataset to apply topic model
        clean_data_df.to_csv(args.output_fp, index=False)
    else:

        if args.no_news and args.news_acc != "":
            print('in news filtering')
            news = read_news_accounts(args.news_acc)
            clean_data_df = clean_data_df[~clean_data_df['screen_name'].isin(news)]

        included_indices = get_rich_text_tweets(clean_data_df["clean_text"], args.no_terms_per_tweet)

        print(len(included_indices))

        result_df = clean_data_df.iloc[included_indices].copy()

        if args.no_repeated_tweet: # Remove repeated tweets
            result_df = remove_repeated_tweets(result_df, 'clean_text', 'repeated')

        print('number of selected tweets',result_df.shape)
        result_df.to_csv(args.output_fp, index=False)
