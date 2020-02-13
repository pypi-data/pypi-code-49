import pytest
import molpy
#import numpy as np

@pytest.mark.parametrize("molecule, symbols, coords",[
    ('water',
     ['H', 'H', 'O'],
     [9.818333333333333, 7.603666666666666, 12.673])
    ])


def test_read_xyz_files(molecule, symbols, coords):

    assert molpy.data.open_xyz(molecule)[0] == symbols
    
    for i in range(0,3):
        assert molpy.data.open_xyz(molecule)[1][i] \
            == pytest.approx(coords[i], abs=1.e-3)
    
    

