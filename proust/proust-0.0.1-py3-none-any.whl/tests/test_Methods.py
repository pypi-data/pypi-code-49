import numpy as np

from proust import ConstantMethod


def test_predict_zero():
    predict_zero = ConstantMethod(constant=0)
    assert predict_zero.predict(0) == 0
    assert predict_zero.predict([0]) == [0]
    assert predict_zero.predict([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0] * 10
    assert np.array_equal(predict_zero.predict(np.random.rand(2, 2)), np.zeros((2, 2)))
    assert np.array_equal(predict_zero.predict(np.random.rand(2, 3, 4, 1)), np.zeros((2, 3, 4, 1)))


def test_predict_one():
    predict_one = ConstantMethod(constant=1)
    assert predict_one.predict(0) == 1
    assert predict_one.predict([0]) == [1]
    assert predict_one.predict([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1] * 10
    assert np.array_equal(predict_one.predict(np.random.rand(2, 2)), np.ones((2, 2)))
    assert np.array_equal(predict_one.predict(np.random.rand(2, 3, 4, 1)), np.ones((2, 3, 4, 1)))
