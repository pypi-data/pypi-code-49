"""Callbacks which integrate with and/or modify the behavior of model optimizers."""

from typing import Mapping

from torch.optim.lr_scheduler import _LRScheduler, ReduceLROnPlateau

from forecast.callbacks import Callback


class LRScheduleCallback(Callback):
    """Wraps a generic learning rate schedule in a callback."""

    def __init__(self, sched: _LRScheduler):
        """Wraps a generic learning rate schedule in a callback.

        Parameters
        ----------
        sched: _LRScheduler
            A learning rate scheduler which only requires the current epoch to step

        """
        super().__init__()
        self._sched = sched

    def on_train_val_epoch_end(self, epoch: int) -> None:
        """Steps the learning rate scheduler.

        Parameters
        ----------
        epoch: int
            The current epoch

        Returns
        -------
        None

        """
        self._sched.step(epoch)


class ReduceLROnPlateauCallback(Callback):
    """Wraps a ReduceLROnPlateau schedule in a callback."""

    def __init__(self, sched: ReduceLROnPlateau, metric_name: str):
        """Wraps a ReduceLROnPlateau schedule in a callback.

        Parameters
        ----------
        sched: ReduceLROnPlateau
            The learning rate schedule
        metric_name: str
            The name of the metric to be examined for plateau (or 'loss' if the loss function should be monitored)

        """
        super().__init__()
        self._sched = sched
        self._metric_name = metric_name

    def on_val_end(self, epoch: int, loss: float, metrics: Mapping[str, float]) -> None:
        """Examines whether the specified metric has plateaued.

        Parameters
        ----------
        epoch: int
            The current epoch
        loss: float
            The current value of the loss
        metrics: Mapping[str, float]
            The model's performance on the validation set during the current epoch

        Returns
        -------
        None

        """
        if self._metric_name == 'loss':
            m = loss
        else:
            m = metrics[self._metric_name]
        self._sched.step(m, epoch)
