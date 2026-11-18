
from bataille_naval.classes import *

def main():

    # create battle ship.
    battle_ship = BattleShip()

    # add ships.
    battle_ship.ships.append(Ship(1, 1, is_horizontal=True, length=2))
    battle_ship.ships.append(Ship(1, 3, is_horizontal=True, length=3))
    battle_ship.ships.append(Ship(3, 5, is_horizontal=True, length=3))
    battle_ship.ships.append(Ship(1, 7, is_horizontal=True, length=4))
    battle_ship.ships.append(Ship(9, 1, is_horizontal=False, length=5))


    print('--- START ---')

    # loop play.
    while True:

        # take input user.
        print('enter a position [ex: a1] :')
        input_user = input()

        try:
            battle_ship.shoot(input_user)
        except Exception as e:
            print('input invalid')
            continue

        # render the battle_ship.
        print(battle_ship)

        # exit loop when every ship is dead.
        if battle_ship.is_every_ship_shooted():
            break

    print('--- END ---')


# cmd :
# uv run bataille-naval                      # run the project.
# uv run pytest -v                           # run tests (all).
# uv run pytest -v tests/test_ship.py        # run tests (only one file).
