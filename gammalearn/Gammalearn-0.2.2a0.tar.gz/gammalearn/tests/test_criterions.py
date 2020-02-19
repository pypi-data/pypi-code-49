import unittest
import torch

from gammalearn.criterions import one_hot


class TestCriterions(unittest.TestCase):

    def setUp(self) -> None:
        self.labels = torch.tensor([0, 1, 1, 0, 1, 0, 0, 1], dtype=torch.long)
        self.onehot = torch.tensor([[1, 0],
                                    [0, 1],
                                    [0, 1],
                                    [1, 0],
                                    [0, 1],
                                    [1, 0],
                                    [1, 0],
                                    [0, 1]], dtype=torch.long)

    def test_onehot(self):
        torch.allclose(self.onehot.float(),
                       one_hot(self.labels, num_classes=2).float())
