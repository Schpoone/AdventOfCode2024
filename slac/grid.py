class Vec2:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Grid:
    data: dict[Vec2, str]
