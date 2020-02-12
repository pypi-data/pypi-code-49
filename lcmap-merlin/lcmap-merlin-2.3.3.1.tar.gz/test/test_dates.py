from merlin import dates
import pytest

def test_to_ordinal():
    assert dates.to_ordinal('1999-01-01') == 729755
    assert dates.to_ordinal('1999/11/01') == 730059


def test_startdate():
    assert dates.startdate('1980-01-01/1982-01-01') == '1980-01-01'


def test_enddate():
    assert dates.enddate('1980-01-01/1982-01-01') == '1982-01-01'


def test_is_acquired():
    assert dates.is_acquired('1980-01-01/1982-01-01') is True
    assert dates.is_acquired('1980-01-011982-01-01') is False


def test_minmax():
    datestrs = ['1980', '1979', '1990']

    assert '1979/1990' == dates.minmax(datestrs)

    
def test_symmetric():
    datemap = {'a': [1, 2, 3],
               'b': [2, 1, 3],
               'c': [3, 2, 1]}

    assert set([1, 2, 3]) == set(dates.symmetric(datemap))

    with pytest.raises(Exception):

        datemap = {'a': [1, 2, 3],
                   'b': [2, 1, 3],
                   'c': [3]}

        dates.symmetric(datemap)


def test_single():

    # single date from each key-value should pass
    datemap = {'a': [1,],
               'b': [2,],
               'c': [3,]}

    assert set([1, 2, 3]) == set(dates.single(datemap))

    # zero dates from each is also acceptable
    datemap = {'a': [],
               'b': [],
               'c': []}

    assert set([]) == set(dates.single(datemap))

    # more than 1 date is an error
    with pytest.raises(Exception):

        datemap = {'a': [1, 2, 3],
                   'b': [2, 1, 3],
                   'c': [3, 2, 1]}

        dates.single(datemap)

    # more than 1, misshappen is an Exception
    with pytest.raises(Exception):

        datemap = {'a': [1, 2, 3],
                   'b': [2, 1, 3],
                   'c': [3]}

        dates.single(datemap)

        
    # assymetric dates are an Exception
    with pytest.raises(Exception):

        datemap = {'a': [1,],
                   'b': [2,],
                   'c': []}

        dates.single(datemap)

    
def test_rsort():
    assert [3, 2, 1] == dates.rsort([3, 1, 2])
 
