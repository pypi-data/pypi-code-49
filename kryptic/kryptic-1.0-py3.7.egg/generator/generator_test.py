import pytest
from .generator import Generator

@pytest.mark.parametrize('minlength,maxlength,minexpected,maxexpected', [(0,0,1,1),(-1,4,1,4),(5,-1,5,5),(10,10,10,10)])
def test_getRandomLength(minlength, maxlength, minexpected, maxexpected):
    assert minexpected <= Generator(minlength,maxlength).getRandomLength(minlength,maxlength) >= maxexpected