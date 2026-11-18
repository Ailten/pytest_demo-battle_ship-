
# verify raise error if append a ship overlapping.

# if ship overange pos
# and overange length


from bataille_naval.classes import *

import pytest


def test_add_ship():

    # case work successfully.
    bs = BattleShip()
    s = Ship(0,0,is_horizontal=True, length=3)
    bs.add_ship(s)

    # is same position start.
    s = Ship(0,0,is_horizontal=True, length=3)
    with pytest.raises(Exception, match="overlaping"):
        bs.add_ship(s)


    bs = BattleShip()
    s = Ship(2,1,is_horizontal=False, length=3)
    bs.add_ship(s)

    # is overlaping in center.
    s = Ship(1,2,is_horizontal=True, length=3)
    with pytest.raises(Exception, match="overlaping"):
        bs.add_ship(s)


    # check overange from board.
    bs = BattleShip()
    s = Ship(10,1,is_horizontal=True, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

    s = Ship(1,10,is_horizontal=True, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

    s = Ship(10,1,is_horizontal=False, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

    s = Ship(1,10,is_horizontal=False, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

    s = Ship(8,1,is_horizontal=True, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

    s = Ship(1,8,is_horizontal=False, length=3)
    with pytest.raises(Exception, match="overrange"):
        bs.add_ship(s)

