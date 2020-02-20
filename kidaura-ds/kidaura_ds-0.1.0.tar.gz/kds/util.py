import pandas as pd
import numpy as np
import boto3
import seaborn as sns
import datetime
from dateutil.tz import tzutc
import pytz
from itertools import tee
import pickle
import json
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform


def fetch_s3_object(bucket, folder, date):
    date = datetime.datetime.strptime(date, "%d/%m/%Y")
    date = pytz.utc.localize(date)
    client = boto3.client('s3')
    for o in client.list_objects(Bucket=bucket, Prefix=folder)['Contents']:
        o_date = o['LastModified']
        if o['Key'].endswith(".sqlite3") and o_date >= date:
            yield o['Key']


def save_s3_object(bucket, key, path):
    client = boto3.client('s3')
    client.download_file(bucket, key, path)


def pickle_object(obj, path):
    pickle.dump(obj, open(path, "wb"))


def plot_corr_matrix(df, dropDuplicates=True):
    if dropDuplicates:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

    # Set background color / chart style
    sns.set_style(style='white')

    # Set up  matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Add diverging colormap from red to blue
    cmap = sns.diverging_palette(250, 10, as_cmap=True)

    # Draw correlation plot with or without duplicates
    if dropDuplicates:
        sns.heatmap(df,
                    mask=mask,
                    cmap=cmap,
                    square=True,
                    linewidth=.5,
                    cbar_kws={"shrink": 1},
                    ax=ax)
    else:
        sns.heatmap(df,
                    cmap=cmap,
                    square=True,
                    linewidth=.5,
                    cbar_kws={"shrink": 1},
                    ax=ax)
    plt.show()


def distcorr(X, Y):
    """ Compute the distance correlation function """
    X = np.atleast_1d(X)
    Y = np.atleast_1d(Y)
    if np.prod(X.shape) == len(X):
        X = X[:, None]
    if np.prod(Y.shape) == len(Y):
        Y = Y[:, None]
    X = np.atleast_2d(X)
    Y = np.atleast_2d(Y)
    n = X.shape[0]
    if Y.shape[0] != X.shape[0]:
        raise ValueError('Number of samples must match')
    a = squareform(pdist(X))
    b = squareform(pdist(Y))
    A = a - a.mean(axis=0)[None, :] - a.mean(axis=1)[:, None] + a.mean()
    B = b - b.mean(axis=0)[None, :] - b.mean(axis=1)[:, None] + b.mean()

    dcov2_xy = (A * B).sum() / float(n * n)
    dcov2_xx = (A * A).sum() / float(n * n)
    dcov2_yy = (B * B).sum() / float(n * n)
    dcor = np.sqrt(dcov2_xy) / np.sqrt(np.sqrt(dcov2_xx) * np.sqrt(dcov2_yy))
    return dcor


def read_json_s3(bucket, key):
    s3 = boto3.resource('s3')
    content_object = s3.Object(bucket, key)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return json_content


def next_row(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def cluster(p, distance):
    coords = set(p)
    C = []
    while len(coords):
        locus = coords.pop()
        cluster = [x for x in coords if euclidean(locus, x) <= distance]
        C.append(cluster + [locus])
        for x in cluster:
            coords.remove(x)
    return C
