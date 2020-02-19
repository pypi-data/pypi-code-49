from collections import deque
import torch
from sklearn.metrics import roc_auc_score
from ignite.metrics import Metric


class BufferMetric(Metric):

    def __init__(self, compute_fn, window=None, output_transform=lambda x: x):

        if not callable(compute_fn):
            raise TypeError("Argument compute_fn should be callable.")
        self.compute_fn = compute_fn
        self.window = window
        self._predictions = deque(maxlen=self.window)
        self._targets = deque(maxlen=self.window)
        super(BufferMetric, self).__init__(output_transform=output_transform)

    def reset(self):
        self._predictions.clear()
        self._targets.clear()

    def update(self, output):
        predictions, targets = output
        self._predictions.append(predictions)
        self._targets.append(targets)

    def compute(self):
        _predictions = torch.cat(list(self._predictions))
        _targets = torch.cat(list(self._targets))
        return self.compute_fn(_predictions, _targets)


class SingleBufferMetric(Metric):

    def __init__(self, compute_fn, window=None, output_transform=lambda x: x):

        if not callable(compute_fn):
            raise TypeError("Argument compute_fn should be callable.")
        self.compute_fn = compute_fn
        self.window = window
        self._output = deque(maxlen=self.window)
        super(SingleBufferMetric, self).__init__(output_transform=output_transform)

    def reset(self):
        self._output.clear()

    def update(self, output):
        self._output.append(output)

    def compute(self):
        _output = torch.cat(list(self._output))
        return self.compute_fn(_output)


def accuracy(predictions, targets):
    assert predictions.shape[0] == targets.shape[0], 'Predictions and targets must have same batch size'
    pred = torch.argmax(predictions, dim=1).float()
    acc = (pred == targets).sum().float() / targets.size(0)
    return acc


def auc_score(predictions, targets):
    assert predictions.shape[1] == 2, 'AUC can only be computed for 2 classes but got {}'.format(predictions.shape[1])
    # Positive class is 1
    score = predictions[:, 1]
    auc = roc_auc_score(targets, score)
    return auc

