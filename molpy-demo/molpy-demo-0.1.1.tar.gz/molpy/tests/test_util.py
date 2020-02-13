import pytest
import molpy

@pytest.mark.parametrize("point1, point2, bench",[
    ([0,1],[0,0],1),
    ([0,2],[0,0],2),
    ([0,3],[0,0],3),
    ([2.236, -2.236],[0,0],3.162),
    ])

def test_distance(point1,point2,bench):

    assert molpy.util.distance(point1,point2) == pytest.approx(bench, abs=1.e-3)

def test_distance_failure():
    assert molpy.util.distance([0],[3]) != 5
    

def test_get_molecule_missing():
    
    with pytest.raises(FileNotFoundError):
        mol = molpy.data.get_molecule('non-existant')
        
