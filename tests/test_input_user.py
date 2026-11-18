

# check input user (shoot parameter) is not length >= 4
# same, length < 2

# check first character is not a a special char.
# check first character is a letter (from A to Z).

# check char 2 (and more is number char from 0 to 9)
# check number is valid (1 ~ 10).


from bataille_naval.classes import *

import pytest


def test_input_user():

    bs = BattleShip()

    bs.shoot('A1')  # valid.
    bs.shoot('B2')  # valid.
    bs.shoot('c9')  # valid.
    bs.shoot('C10')  # valid.


    with pytest.raises(Exception, match='already shooted'):
        bs.shoot('A1')  # already shooted.


    with pytest.raises(Exception, match='length'):
        bs.shoot('1')  # length to short.
    with pytest.raises(Exception, match='length'):
        bs.shoot('A')
    with pytest.raises(Exception, match='length'):
        bs.shoot('')
    with pytest.raises(Exception):
        bs.shoot(None)  # invalid type.
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('AA')  # invalid format.
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('11')
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('A02')
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('Z1')  # out of range.
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('C11')
    with pytest.raises(Exception, match='length'):
        bs.shoot('C010')  # to long (+ invalid format).
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('^2')  # unexpected char.
    with pytest.raises(Exception, match='invalid format'):
        bs.shoot('A+')