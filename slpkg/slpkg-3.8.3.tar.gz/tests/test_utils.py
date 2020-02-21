from slpkg.utils import Utils


def test_dimensional_list():
    """Testing dimesional list util
    """
    lists = [[1, 2, 3, 4, 5]]
    utils = Utils()
    assert [1, 2, 3, 4, 5] == utils.dimensional_list(lists)


def test_remove_dbs():
    """Testing removing doubles item from list
    """
    lists = [1, 2, 3, 3, 4, 5, 2, 1]
    utils = Utils()
    assert [1, 2, 3, 4, 5] == utils.remove_dbs(lists)