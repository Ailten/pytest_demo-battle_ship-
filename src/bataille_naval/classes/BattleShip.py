from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Ship import Ship

import re


class BattleShip:
    def __init__(self):
        # is cel aleady targeted.
        self.board: list[list[bool]] = [ [False for _ in range(10) ] for _ in range(10) ]
        # ships.
        self.ships: list["Ship"] = []

    def __str__(self) -> str:
        """
        render the board.
        """

        # write the head line (with letters).
        sea_chars = (" "*3) + ''.join([chr(i) for i in range(65,75)]) + '\n'

        # render the sea.
        for y in range(len(self.board)):

            # whrite the line index (number at left of eatch line).
            sea_line = str(y + 1).rjust(2) + ' '

            # render a line (of the sea).
            for x in range(len(self.board[y])):
                
                # mask every cel who's not already shooted.
                if not self.board[y][x]:
                    sea_line += "~"
                    continue

                # search a ship matching the cel currently rendering.
                is_ship_found = False
                for ship in self.ships:

                    # check if boat is crossing 
                    if ship.is_pos_into_ship(x, y):
                        sea_line += "x"
                        is_ship_found = True
                        break

                # if cel shooted and no shil on it, render a dot.
                if not is_ship_found:
                    sea_line += "."

            sea_chars += sea_line + "\n"

        return sea_chars
    

    def add_ship(self, ship: 'Ship'):
        """
        add a ship in list.
        """

        # check overange.
        if ship.is_horizontal:
            if ship.pos[0] + ship.length >= len(self.board[0]):
                raise Exception('ship position overrange')
            if ship.pos[1] >= len(self.board):
                raise Exception('ship position overrange')
        else:
            if ship.pos[1] + ship.length >= len(self.board):
                raise Exception('ship position overrange')
            if ship.pos[0] >= len(self.board[0]):
                raise Exception('ship position overrange')


        #if [0] >= len(self.board[0]):
        #    raise Exception('ship position overrange horizontaly')
        #if ship.pos[1] >= len(self.board):
        #    raise Exception('ship position overrange verticaly')
        #
        #if ship.pos[0] >= len(self.board[0]):
        #    raise Exception('ship position overrange')
        #if ship.pos[1] >= len(self.board):
        #    raise Exception('ship position overrange')

        # check if ships are overlaping.
        for ship_already_present in self.ships:
            for cel_present in ship_already_present:
                if ship.is_pos_into_ship(cel_present[0], cel_present[1]):
                    raise Exception('ships is overlaping')

        self.ships.append(ship)

    def shoot(self, pos_ask: str):
        """
        take user input str, and insert edit board.
        """
        # pos_ask = 'B5'
        # pos_ask = 'I10'

        pos_ask = pos_ask.lower()

        # tests.
        length = len(pos_ask)
        if length < 2 or length > 3:
            raise Exception('input length invalid')
        
        # regex match patern.
        match = re.match(f'^[a-j]([1-9]|10)$', pos_ask)
        if match == None:
            raise Exception('invalid format')

        # eval x index.
        x = ord(pos_ask[0]) - 97

        # eval y index.
        y = int(pos_ask[1:]) - 1

        # already shoot.
        if self.board[y][x]:
            raise Exception('position already shooted')

        # check the position in board (as shooted).
        self.board[y][x] = True


    def is_every_ship_shooted(self) -> bool:
        """
        return True if every ship are fully shooted.
        """
        for ship in self.ships:
            for pos in ship:
                x, y = pos
                if not self.board[y][x]:
                    return False
        return True




# for demo test.
def input_user() -> str:
    return "F8"

def divide(a: int, b: int) -> float:
    return a / b