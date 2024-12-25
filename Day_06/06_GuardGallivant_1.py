import fileinput
from enum import Enum


class OffGridException(Exception):
    pass


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Gallivant:
    def __init__(self, input: list[str]):
        self.grid: list[list[bool]] = []

        for r, row in enumerate(input):
            if "^" in row:
                self.guard_r: int = r
                self.guard_c: int = row.index("^")
                self.guard_dir: Direction = Direction.NORTH

            self.grid.append([x == "#" for x in row])
        self.positions: set[tuple[int, int]] = {(self.guard_r, self.guard_c)}

    def move(self):
        match self.guard_dir:
            case Direction.NORTH:
                target_r = self.guard_r - 1
                target_c = self.guard_c
            case Direction.EAST:
                target_r = self.guard_r
                target_c = self.guard_c + 1
            case Direction.SOUTH:
                target_r = self.guard_r + 1
                target_c = self.guard_c
            case Direction.WEST:
                target_r = self.guard_r
                target_c = self.guard_c - 1

        if self.on_grid(target_r, target_c):
            if self.grid[target_r][target_c]:  # Obstructed
                self.turn_right()
            else:
                self.guard_r = target_r
                self.guard_c = target_c
                self.positions.add((self.guard_r, self.guard_c))
        else:
            raise OffGridException  # Left grid

    def turn_right(self):
        self.guard_dir = Direction((self.guard_dir.value + 1) % len(Direction))

    def on_grid(self, r: int, c: int) -> bool:
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])

    def left_grid(self):
        return not self.on_grid(self.guard_r, self.guard_c)


grid = Gallivant(list(map(str.strip, fileinput.input())))

while True:
    try:
        grid.move()
    except OffGridException:
        break
print(len(grid.positions))
