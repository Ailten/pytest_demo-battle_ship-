
from bataille_naval.classes.BattleShip import input_user
from bataille_naval.classes.BattleShip import divide

import pytest


#@pytest.mark.skip
#@pytest.mark.xfail

class TestDefault():

    def test_input_user(self):

        assert input_user() == "F8"


    def test_divide(self):

        assert divide(5, 5) == 1
        assert divide(5, 1) == 5
        assert divide(10, 2) == 5

        assert divide(1, 3) == pytest.approx(0.333, abs=0.005)
        assert 0.2 == pytest.approx(0.3, abs=0.1)

        with pytest.raises(ZeroDivisionError):
            assert divide(5, 0)
    
        with pytest.raises(TypeError):
            assert divide(None, 2)

        with pytest.raises(Exception, match="user log"):
            raise Exception("fail to user log during connection")


# execute a test (specify file test, class, function).
# uv run pytest -v tests/test_input_user.py::TestDefault::test_input_user

# for test only functions who contains "divide".
# uv run pytest -v -k divide