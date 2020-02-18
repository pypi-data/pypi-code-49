# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines the Explanation dashboard class."""

from interpret_community.widget import ExplanationDashboard as NewExplanationDashboard
from warnings import warn


class ExplanationDashboard(object):
    """The dashboard class, wraps the dashboard component."""

    def __init__(self, explanationObject, learner, dataset, trueY=None):
        """Initialize the Explanation Dashboard.

        :param explanationObject: An object that represents an explanation. It is assumed that it
            has a local_importance_values property that is a 2d array in teh case of regression,
            and 3d array in the case of classification. Dimensions are either samples x features, or
            classes x samples x features. Optionally, it may have a features array that is the string name
            of the features, and a classes array that is the string name of the classes.
        :type explanationObject: object
        :param learner: An object that represents a model. It is assumed that for the classification case
            it has a method of predict_proba() returning the prediction probabilities for each
            class and for the regression case a method of predict() returning the prediction value.
        :type learner: object
        :param dataset:  A matrix of feature vector examples (# examples x # features), the same sampels
            used to build the explanationObject.
        :type dataset: numpy.array or list[][]
        :param trueY: The true labels for the provided dataset
        :tpye trueY: numpy.array or list[]
        """
        msg = 'Please use the explanation dashboard from interpret-community package, this one will be deprecated'
        warn(msg, UserWarning)
        NewExplanationDashboard(explanationObject, learner, datasetX=dataset, trueY=trueY)
