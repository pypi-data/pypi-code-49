from numbers import Real
from typing import List, TypeVar

import jax.numpy as np
from sklearn.linear_model import Ridge

# Notes
# - May eventually want a time series object, though not clear how to abstract
# - Do we use the most recent observation or not? I.e., does predict need to take an input value?

TimeSeries = TypeVar("TimeSeries", Real, List[Real], np.ndarray)


class BaseMethod(object):
    """
    Questions:
        - Should we have TimeSeries and TimeSeriesValue classes so we can distinguish?
        - For each method, should we operate on TimeSeries, TimeSeriesValues, or both?
        - How to distinguish between training data independent from the TimeSeries we care about and training
          data that *is* the TimeSeries we care about?
          - Fit: if the model predicts the 10th previous step, training data *is* the TimeSeries
          - Fit: if the model is autogressive, the training data may be offline collected earlier
    """

    def __init__(self):
        pass

    def fit(self, data: TimeSeries) -> None:
        """
        Description: catch-all for training step (e.g., offline, pre-train, incremental).
        Questions:
            - Does fit incrementally train a method or retrain from scratch?
        Args:
            data (TimeSeries):
        Returns:
            None
        """
        raise NotImplementedError()

    def predict(self, data: TimeSeries, steps: int = 1) -> TimeSeries:
        """
        Description: make a prediction based on new data.
        Questions:
            - Should we use most recent data in prediction or not?
            - Should predict even take in any value if update handles incorporating new data?
            - Should we predict a single value or a TimeSeries (e.g., number of steps)?
        Args:
            data (TimeSeries):
            steps (int):
        Returns:
            ts (TimeSeriesValue):
        """
        raise NotImplementedError()

    def update(self, data: TimeSeries) -> None:
        """
        Description: updates a model?
        Questions:
            - How does update differ from fit? Possibilities:
                - fit retrains from scratch; update incrementally trains
                - fit trains the model, update incorporates new data
            - Does update touch the model? Should it just call fit as subroutine? or vice versa?
        Args:
            data (TimeSeries):
        Returns:
            None
        """
        raise NotImplementedError()

    def transform(self, data: TimeSeries) -> TimeSeries:
        """
        Description: transforms a TimeSeries a la clustering in sklearn.
        Args:
            data (TimeSeries):
        Returns:
            ts (TimeSeries):
        """
        raise NotImplementedError()


class ConstantMethod(BaseMethod):
    def __init__(self, constant: Real = 0):
        super().__init__()
        self.constant = constant

    def fit(self, data: TimeSeries) -> None:
        pass

    def predict(self, data: TimeSeries, steps: int = 1) -> TimeSeries:
        if np.isscalar(data):
            return self.constant
        elif type(data) == list:
            return [self.constant] * len(data)
        else:
            return np.ones(data.shape) * self.constant

    def update(self, data: TimeSeries) -> None:
        pass


# Predict value n steps ago (pad missing predictions with some constant)
def predict_last(data, offset=1, constant=0):
    test_last = [np.full(x.shape, constant, dtype=x.dtype) for x in data]
    for x, y in zip(test_last, data):
        x[offset:] = y[:-offset]

    return test_last


# Predict perfect
def predict_perfect(data):
    return data


# Predict linear
def predict_linear(data, window_size=5, delay=30, constant=0):
    X, Y = [], []
    for i, shot in enumerate(data):
        x, y = [], []
        for i in range(window_size, len(shot) - delay + 1):
            x.append(shot[i - window_size:i].flatten())
            y.append(shot[i + delay - 1])
        X += x
        Y += y

    lr = Ridge(alpha=1)
    lr.fit(X, Y)

    test_linear = [np.full(x.shape, constant, dtype=x.dtype) for x in data]
    for i, (x, y) in enumerate(zip(X, Y)):
        preds = lr.predict(x)
        test_linear[i][delay + window_size - 1:] = preds

    return test_linear
