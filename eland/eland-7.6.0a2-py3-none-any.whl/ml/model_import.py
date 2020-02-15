#  Copyright 2019 Elasticsearch BV
#
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
from typing import Union, List

from eland import Client
from eland.ml._optional import import_optional_dependency

sklearn = import_optional_dependency("sklearn")
xgboost = import_optional_dependency("xgboost")

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from xgboost import XGBRegressor, XGBClassifier


def put_model(es_client,
              model_id: str,
              model: Union[DecisionTreeClassifier,
                           DecisionTreeRegressor,
                           RandomForestRegressor,
                           RandomForestClassifier,
                           XGBClassifier,
                           XGBRegressor],
              feature_names: List[str],
              classification_labels: List[str] = None,
              classification_weights: List[float] = None):
    """
    Add a trained machine learning model to Elasticsearch.
    (See https://www.elastic.co/guide/en/elasticsearch/reference/master/put-inference.html)
    
    Parameters
    ----------
    es_client: Elasticsearch client argument(s)
        - elasticsearch-py parameters or
        - elasticsearch-py instance or
        - eland.Client instance

    model_id: str
        - The unique identifier of the trained inference model Elasticsearch.

    model: An instance of a supported python model. We support the following model types:
        - sklearn.tree.DecisionTreeClassifier
        - sklearn.tree.DecisionTreeRegressor
        - sklearn.ensemble.RandomForestRegressor
        - sklearn.ensemble.RandomForestClassifier
        - xgboost.XGBClassifier
        - xgboost.XGBRegressor

    feature_names: List[str]
        - Names of the features (required)

    classification_labels: List[str]
        - Labels of the classification targets

    classification_weights: List[str]
        - Weights of the classification targets
    """
    client = Client(es_client)

    # Transform model

    m = str(model.serialize_and_compress_model())[2:-1]  # remove `b` and str quotes
    response = client.perform_request(
        "PUT", "/_ml/inference/" + model_id,
        body={
            "input": {
                "field_names": model.feature_names
            },
            "compressed_definition": m
        }
    )

    return response
