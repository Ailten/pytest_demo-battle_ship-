class Ship:
    def __init__(self, x: int, y: int, is_horizontal: bool, length: int):

        if x < 0:
            raise Exception('pos x is negative')
        if y < 0:
            raise Exception('pos y is negative')

        self.pos: tuple[int, int] = (x, y)
        self.is_horizontal = is_horizontal

        if length < 2:
            raise Exception('length is to short')
        if length > 5:
            raise Exception('length is to big')

        self.length = length

    def is_pos_into_ship(self, x: int, y: int) -> bool:
        """
        return true if the position is into the shit body.
        """
        is_match_horizontaly = (
            self.is_horizontal and
            y == self.pos[1] and 
            x >= self.pos[0] and x < self.pos[0] + self.length 
        )
        is_match_verticaly = (
            not self.is_horizontal and
            x == self.pos[0] and
            y >= self.pos[1] and y < self.pos[1] + self.length
        )
        return is_match_horizontaly or is_match_verticaly
    
    def __iter__(self):
        """
        iter on every pos of the ship.
        """
        for i in range(self.length):
            pos_cel: tuple[int, int]|None = None

            if self.is_horizontal:
                pos_cel = (self.pos[0] + i, self.pos[1])
            else:
                pos_cel = (self.pos[0], self.pos[1] + i)

            yield pos_cel

