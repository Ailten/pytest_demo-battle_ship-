

from bataille_naval.classes.Ship import Ship

import pytest


def test_ship_length():

    with pytest.raises(Exception, match="length"):
        Ship(0, 0, True, 0)
    with pytest.raises(Exception, match="length"):
        Ship(0, 0, True, -10)
    with pytest.raises(Exception, match="length"):
        Ship(0, 0, True, 12)
    with pytest.raises(Exception, match="length"):
        Ship(0, 0, True, 999)
    
def test_ship_pos():

    with pytest.raises(Exception, match="pos"):
        Ship(-1, 0, True, 3)
    with pytest.raises(Exception, match="pos"):
        Ship(0, -1, True, 3)
    with pytest.raises(Exception, match="pos"):
        Ship(0, -32, True, 3)
    with pytest.raises(Exception, match="pos"):
        Ship(-12, -32, True, 3)

    with pytest.raises(TypeError):
        Ship(None, 2, True, 3)
    with pytest.raises(TypeError):
        Ship(2, None, True, 3)

def test_valid_ship():

    # valide length.
    Ship(0, 0, True, 2)
    Ship(0, 0, True, 3)
    Ship(0, 0, True, 4)
    Ship(0, 0, True, 5)


