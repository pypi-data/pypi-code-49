import hashlib

import boto3
import dill
import numpy as np


def hash_file(filename):
    hash_ = hashlib.sha256()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash_.update(chunk)

    return hash_.hexdigest()


def explain_transaction(model_set, version, features, aws_credentials):
    """
    Downloads trained model and respective explainers from s3.
    Then calculates explanation for a given transaction.

    Args:
        model_set: A UUID string for the monitaur model set.
        version: Monitaur model version.
        aws_credentials: S3 credentials
            {
                "aws_access_key": "123",
                "aws_secret_key": "456",
                "aws_region": "us-east-1",
                "aws_bucket_name": "bucket name"
            }

    Returns:
        foo
    """

    explain_threshold = 0.95

    # connect to s3
    client = boto3.client(
        "s3",
        aws_access_key_id=aws_credentials["aws_access_key"],
        aws_secret_access_key=aws_credentials["aws_secret_key"],
        region_name=aws_credentials["aws_region"],
    )

    # download explainers for the model
    anchors_filename = f"{model_set}.anchors"
    with open(anchors_filename, "wb") as f:
        client.download_fileobj(
            aws_credentials["aws_bucket_name"],
            f"{model_set}/{version}/{anchors_filename}",
            f,
        )

    # load explainer from s3 download
    with open(anchors_filename, "rb") as f:
        explainer = dill.load(f)

    # determine explanation for transaction
    inputs = list(features.values())
    reshaped_inputs = np.asarray(inputs).reshape(1, len(inputs))
    explanation = explainer.explain(reshaped_inputs, threshold=explain_threshold)

    return explanation["names"]
