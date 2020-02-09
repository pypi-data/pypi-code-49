from typing import Optional, Callable, Union, Iterable

from torch import Tensor
from torch.optim.optimizer import Optimizer


OptClosure = Optional[Callable[[], float]]
_params_t = Union[Iterable[Tensor], Iterable[dict]]


class SGD(Optimizer):
    def __init__(self, params: _params_t, lr: float = 0.001) -> None:
        defaults = dict(lr=lr)
        super(SGD, self).__init__(params, defaults)

    def __setstate__(self, state: dict) -> None:
        super(SGD, self).__setstate__(state)

    def step(self, closure: OptClosure = None) -> Optional[float]:
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                d_p = p.grad.data
                p.data.add_(-group['lr'], d_p)
        return loss
